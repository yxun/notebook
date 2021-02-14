package concurrency.synch;

import java.util.Arrays;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

/**
 * A lock protects sections of code, allowing only one thread to execute the code at a time.
 * A lock manages threads that are trying to enter a protected code segment.
 * A lock can have one or more associated condition objects.
 * Each condition object manages threads that have entered a protected code section but that cannot proceed. 
 */

public class Bank {
    private final double[] accounts;
    private Lock bankLock;
    private Condition sufficientFunds;
 
    public Bank(int n, double initialBalance) {
        accounts = new double[n];
        Arrays.fill(accounts, initialBalance);
        bankLock = new ReentrantLock();
        sufficientFunds = bankLock.newCondition();
    }

    public void transfer(int from, int to, double amount) throws InterruptedException {
        bankLock.lock();
        try {
            while (accounts[from] < amount) {
                sufficientFunds.await();
            }
            System.out.print(Thread.currentThread());
            accounts[from] -= amount;
            System.out.printf(" %10.2f from %d to %d", amount, from, to);
            accounts[to] += amount;
            System.out.printf(" Total Balance: %10.2f%n", getTotalBalance());
            sufficientFunds.signalAll();
        } finally {
            bankLock.unlock();
        }
    }

    /**
    * If a method is declared with the synchronized keyword, the object's lock protects the entire method.
    */
    public synchronized void syncTransfer(int from, int to, int amount) throws InterruptedException {
        while (accounts[from] < amount) {
            wait();  // wait on intrinsic object lock's single condition
        }
        accounts[from] -= amount;
        accounts[to] += amount;
        notifyAll();  // notify all threads waiting on the condition
    }

    public double getTotalBalance() {
        bankLock.lock();
        try {
            double sum = 0;
            for (double a : accounts) {
                sum += a;
            }
            return sum;
        } finally {
            bankLock.unlock();
        }
    }

    public synchronized double syncGetTotalBalance() {
        double sum = 0;
        for (double a : accounts) {
            sum += a;
        }
        return sum;
    }

    public int size() {
        return accounts.length;
    }
}
