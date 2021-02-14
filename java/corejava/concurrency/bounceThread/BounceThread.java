package concurrency.bounceThread;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Container;
import concurrency.bounce.BallComponent;
import concurrency.bounce.Ball;
import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionListener;


/**
 * Shows animated bouncing balls
 * procedure for running a task in a separate thread:
 * 1. Place the code for the task into the run method of a class that implements the Runnable interface.
 * Since Runnable is a functional interface, you can make an instance with a lambda expression:
 * Runnable r = () -> { task code };
 * 2. Construct a Thread object from the Runnable:
 * Thread t = new Thread(r);
 * 3. Start the thread:
 * t.start() 
 */

public class BounceThread {
    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            JFrame frame = new BounceFrame();
            frame.setTitle("BounceThread");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        });
    }
}

class BounceFrame extends JFrame {
    private BallComponent comp;
    public static final int STEPS = 1000;
    public static final int DELAY = 5;

    public BounceFrame() {
        comp = new BallComponent();
        add(comp, BorderLayout.CENTER);
        JPanel buttonPanel = new JPanel();
        addButton(buttonPanel, "Start", event -> addBall());
        addButton(buttonPanel, "Close", event -> System.exit(0));
        add(buttonPanel, BorderLayout.SOUTH);
        pack();
    }

    public void addButton(Container c, String title, ActionListener listener) {
        JButton button = new JButton(title);
        c.add(button);
        button.addActionListener(listener);
    }

    public void addBall() {
        Ball ball = new Ball();
        comp.add(ball);
        Runnable r = () -> {
            try {
                for (int i = 1; i <= STEPS; i ++) {
                    ball.move(comp.getBounds());
                    comp.repaint();
                    Thread.sleep(DELAY);
                }
            } catch (InterruptedException e) {}
        };
        Thread t = new Thread(r);
        t.start();
    }
}