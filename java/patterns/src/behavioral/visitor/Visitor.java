package behavioral.visitor;

public interface Visitor {
    void visit(Customer cusotmer);
    void visit(Order order);
    void visit(Item item);
}
