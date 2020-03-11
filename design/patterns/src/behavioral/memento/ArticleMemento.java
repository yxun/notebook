package behavioral.memento;

public final class ArticleMemento {
    private final long id;
    private final String title;
    private final String content;

    public ArticleMemento(long id, String title, String content) {
        super();
        this.id = id;
        this.title = title;
        this.content = content;
    }

    public long getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }
}

/** Challenges of memento pattern
 * A high number of mementos require more storage. At the same time, they put additional burdens on a caretaker.
 * It also increases maintenance costs in parallel because code efforts needs to be made to manage memento classes.
 * The additional time to save the states decreases the overall performance of the system.
 */
