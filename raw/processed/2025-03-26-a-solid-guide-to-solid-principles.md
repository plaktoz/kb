# A Solid Guide to SOLID Principles

source_url: https://www.baeldung.com/solid-principles

---

By Sam Millington | Last updated: March 26, 2025

## 1. Overview

SOLID is a mnemonic acronym for five object-oriented design principles introduced by Robert C. Martin in his 2000 paper "Design Principles and Design Patterns," later popularized by Michael Feathers. These principles help create more maintainable, understandable, and flexible software.

## 2. Why SOLID?

As applications grow in size, SOLID principles help reduce complexity and prevent the accumulation of technical debt.

## 3. Single Responsibility Principle (SRP)

**A class should only have one responsibility and one reason to change.**

Benefits: fewer test cases, lower coupling, better organization.

```java
// BAD: Book prints itself
public class BadBook {
    void printTextToConsole() { ... }
}

// GOOD: Separate concern
public class BookPrinter {
    void printTextToConsole(String text) { ... }
    void printTextToAnotherMedium(String text) { ... }
}
```

## 4. Open/Closed Principle (OCP)

**Classes should be open for extension but closed for modification.**

Avoid modifying existing working classes; extend them instead.

```java
// Extend rather than modify
public class SuperCoolGuitarWithFlames extends Guitar {
    private String flameColor;
}
```

## 5. Liskov Substitution Principle (LSP)

**Every subclass should be substitutable for its parent class without disrupting behavior.**

Violation example: `ElectricCar implements Car` but throws exception on `turnOnEngine()`, breaking the contract. Solution: rework the interface to reflect the engine-less state.

## 6. Interface Segregation Principle (ISP)

**Split large interfaces into smaller, focused ones so implementing classes only need to concern themselves with relevant methods.**

```java
// BAD: Forces petting dangerous bears
public interface BearKeeper {
    void washTheBear();
    void feedTheBear();
    void petTheBear();
}

// GOOD: Separate interfaces
public interface BearCleaner { void washTheBear(); }
public interface BearFeeder { void feedTheBear(); }
public interface BearPetter { void petTheBear(); }
```

## 7. Dependency Inversion Principle (DIP)

**High-level modules and low-level modules should both depend on abstractions, not concrete implementations.**

```java
// BAD: Tightly coupled
public class Windows98Machine {
    private final StandardKeyboard keyboard;
    private final Monitor monitor;
    public Windows98Machine() {
        keyboard = new StandardKeyboard();
        monitor = new Monitor();
    }
}

// GOOD: Depends on abstractions, injected via constructor
public interface Keyboard { }
public class Windows98Machine {
    private final Keyboard keyboard;
    private final Monitor monitor;
    public Windows98Machine(Keyboard keyboard, Monitor monitor) {
        this.keyboard = keyboard;
        this.monitor = monitor;
    }
}
```

## 8. Conclusion

SOLID principles guide us toward more testable, maintainable, and extensible object-oriented software. Apply them contextually — the benefit scales with codebase size and complexity.
