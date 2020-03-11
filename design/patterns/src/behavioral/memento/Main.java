package behavioral.memento;

public class Main {
    // The Main class is acting as a Caretaker which creates and restores the memento objects
    public static void main(String[] args) {

        Article article = new Article(1, "My Article");
        article.setContent("ABC");      // original content
        System.out.println(article);

        ArticleMemento memento = article.createMemento();    // created immutable memento

        article.setContent("123");  // changed content
        System.out.println(article);

        article.restore(memento);   // undo change
        System.out.println(article);    // original content

    }
}