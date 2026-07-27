# Best Practices for Unit Testing in Java

source_url: https://www.baeldung.com/java-unit-testing-best-practices

---

By Anshul Bansal | Last updated: May 11, 2024

## 1. Overview

Unit Testing is a methodology of testing source code for its fitness for production. The complete test suite executes to catch regressions in the implementation phase or during deployment builds.

## 2. Best Practices

### 2.1 Source Code Separation
Keep test classes separate from main source code to avoid running test code in production. Follow Maven/Gradle convention: `src/main/test` for test implementations.

### 2.2 Package Naming Convention
The package of a test class should match the package of the source class it tests. (`com.baeldung.math.Circle` → `com.baeldung.math.CircleTest`).

### 2.3 Test Case Naming Convention
Names should be insightful. Use the `given_when_then` format:
```java
@Test
public void givenRadius_whenCalculateArea_thenReturnArea() { ... }

@Test
public void givenDoubleMaxValueAsRadius_whenCalculateArea_thenReturnAreaAsInfinity() { ... }
```
Structure test bodies in Given (setup), When (action), Then (assertion) blocks.

### 2.4 Expected vs Actual
Always assert expected vs. actual values. Prefix variables with `expected` and `actual` for clarity:
```java
Assert.assertEquals(expectedArea, actualArea);
```

### 2.5 Prefer Simple Test Cases
Use hard-coded expected values. Do not recompute expected values using the same logic as the production code — that provides no value.

### 2.6 Use Appropriate Assertions
Use the full range of JUnit/AssertJ methods: `assertEquals`, `assertNotEquals`, `assertNotNull`, `assertTrue`, `assertNotSame`.

### 2.7 One Scenario Per Test
Write one unit test per specific scenario. Multiple assertions in one test make failure analysis harder.

### 2.8 Test Production Scenarios
Write tests based on real use cases to make them relatable and meaningful in production context.

### 2.9 Mock External Services
Mock dependencies like databases and external APIs using Mockito, EasyMock, or JMockit. Test your logic, not the external system.

### 2.10 Avoid Code Redundancy
Create helper functions for generating commonly used test objects and mock data.

### 2.11 Use Annotations
Use lifecycle annotations (`@Before`, `@BeforeClass`, `@After`) to set up and tear down test state, keeping tests isolated.

### 2.12 Aim for 80% Test Coverage
80% code coverage is a useful rule of thumb. Use JaCoCo or Cobertura with Maven/Gradle for coverage reports.

### 2.13 TDD Approach
Test-Driven Development: write failing tests first, then implement. Benefits include testable code from the start and fewer regressions.

### 2.14 Automate Test Execution
Integrate unit test execution into CI/CD pipelines. Automated execution ensures rapid feedback before broken code reaches production.
