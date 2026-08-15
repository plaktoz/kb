# Introduction to the Dependency Mechanism – Maven

source_url: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html

---

Apache Maven Documentation

## Transitive Dependencies

Maven automatically includes transitive dependencies (dependencies of your dependencies) by reading remote project files. There is no limit on dependency depth, except that cyclic dependencies are detected and rejected.

### Dependency Mediation (Nearest Definition)
When multiple versions of the same dependency exist in the tree, Maven picks the **nearest** one (shortest path from your project). Example:

```
A → B → C → D 2.0
A → E → D 1.0
```

D 1.0 is used (shorter path via E). To force D 2.0, explicitly declare it in A's POM.

**Best practice**: Explicitly declare all dependencies your source code uses directly, even if they're transitively available. This makes the POM self-documenting and avoids build failures if a transitive dependency is removed upstream. Use `mvn dependency:tree` and `mvn dependency:analyze` to audit.

## Dependency Scope

6 scopes control classpath visibility and transitivity:

| Scope | Description |
|---|---|
| `compile` | Default; available in all classpaths; transitive |
| `provided` | Expected at runtime by JDK or container; not transitive |
| `runtime` | Not needed for compilation; needed at runtime |
| `test` | Only for test compilation and execution |
| `system` | Like `provided` but requires explicit `systemPath`; not recommended |
| `import` | Only for `<dependencyManagement>`; imports managed dependencies from another POM |

### Scope Transitivity Matrix

| Scope of A / Scope of B | compile | provided | runtime | test |
|---|---|---|---|---|
| compile | compile | — | runtime | — |
| provided | provided | — | provided | — |
| runtime | runtime | — | runtime | — |
| test | test | — | test | — |

## Dependency Management

Centralizes version and configuration information for dependencies in a parent POM's `<dependencyManagement>` section. Child POMs can then declare dependencies without specifying versions.

Key identity for matching: `{groupId, artifactId, type, classifier}` (shorthand to `{groupId, artifactId}` when type is `jar` and classifier is null).

`<dependencyManagement>` also controls versions of **transitive** dependencies.

## Importing Dependencies

For multi-module projects where single-parent inheritance is insufficient, use `scope=import` to import managed dependencies from another POM:

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>maven</groupId>
      <artifactId>A</artifactId>
      <version>1.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

Import order matters: if multiple imported BOMs define the same artifact, the **first declaration wins**.

## Bill of Materials (BOM) POMs

A BOM POM defines versions of all artifacts in a library. Other projects import it to keep versions consistent without specifying them individually.

```xml
<!-- BOM POM -->
<packaging>pom</packaging>
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.test</groupId>
      <artifactId>project1</artifactId>
      <version>${project1Version}</version>
    </dependency>
  </dependencies>
</dependencyManagement>
```

Maven 4.0 introduces a dedicated `bom` packaging type that is compatible with Maven 3.x consumers.

## System Dependencies

`system` scope uses a `systemPath` to reference a local JAR not in any repository. **Not recommended** — binds the build to a specific machine. Preferred alternative: publish to a private hosted repository.

Note: Java EE (`javax`) packages that historically used `system` scope are now available on Maven Central; never add explicit JDK class dependencies.
