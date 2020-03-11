package creational.builder.hero;

/**
 * Imagine a character generator for a role playing game. 
 * The easiest option is to let computer create the character for you. 
 * But if you want to select the character details like profession, gender, hair color etc. 
 * the character generation becomes a step-by-step process that completes 
 * when all the selections are ready.
 */

public final class Hero {
    private final Profession profession;
    private final String name;
    private final HairType hairType;
    private final HairColor hairColor;
    private final Armor armor;
    private final Weapon weapon;

    private Hero(Builder builder) {
        this.profession = builder.profession;
        this.name = builder.name;
        this.hairColor = builder.hairColor;
        this.hairType = builder.hairType;
        this.weapon = builder.weapon;
        this.armor = builder.armor;
    }


    public static class Builder {
        private final Profession profession;
        private final String name;
        private HairType hairType;
        private HairColor hairColor;
        private Armor armor;
        private Weapon weapon;

        public Builder(Profession profession, String name) {
            if (profession == null || name == null) {
                throw new IllegalArgumentException("profession and name can not be null");
            }
            this.profession = profession;
            this.name = name;
        }

        public Builder withHairType(HairType hairType) {
            this.hairType = hairType;
            return this;
        }

        public Builder withHairColor(HairColor hairColor) {
            this.hairColor = hairColor;
            return this;
        }

        public Builder withArmor(Armor armor) {
            this.armor = armor;
            return this;
        }

        public Builder withWeapon(Weapon weapon) {
            this.weapon = weapon;
            return this;
        }

        public Hero build() {
            return new Hero(this);
        }
    }

    public static void main(String[] args) {
        Hero mage = new Hero.Builder(Profession.MAGE, "Riobard")
            .withHairColor(HairColor.BLACK)
            .withWeapon(Weapon.DAGGER)
            .build();

        System.out.println(mage.profession);
        System.out.println(mage.name);
        System.out.println(mage.hairType);
        System.out.println(mage.hairColor);
        System.out.println(mage.armor);
        System.out.println(mage.weapon);
    }


    /** Reference
     * https://java-design-patterns.com/patterns/builder/
     * Design Patterns: Elements of Reusable Object-Oriented Software
     * Effective Java (2nd Edition)
     */  
}

