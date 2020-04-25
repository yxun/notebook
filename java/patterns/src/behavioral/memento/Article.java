package behavioral.memento;

/**
 * also known as snapshot pattern
 * The intent of memento is to capture the internal state of an object
 * without violating encapsulation and thus providing a mean for
 * restoring the object into initial state when needed.
 */

/** Design participants
 * Originator - is the object that knows how to create and save it's state for future.
 * It provides methods createMemento() and restore(memento)
 * 
 * Caretaker - performs an operation on Originator while having the possibility to rollback.
 * It keeps track of multiple mementos.
 * 
 * Memento - the lock box that is written and read by the Originator, and shepherded by the Caretaker.
 * In principle, a memento must be in immutable object.
 */


public class Article {
    private long id;
    private String title;
    private String content;

    public Article(long id, String title) {
        super();
        this.id = id;
        this.title = title;
    }

    // Setters and getters
    public void setContent(String content) {
        this.content = content;
    }

    public ArticleMemento createMemento() {
        ArticleMemento m = new ArticleMemento(id, title, content);
        return m;
    }

    public void restore(ArticleMemento m) {
        this.id = m.getId();
        this.title = m.getTitle();
        this.content = m.getContent();
    }

    @Override
    public String toString() {
        return "Article [id=" + id + ", title=" + title + ", content=" + content + "]";
    }
}

