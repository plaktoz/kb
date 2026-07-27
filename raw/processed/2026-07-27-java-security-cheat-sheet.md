# Java Security Cheat Sheet

source_url: https://cheatsheetseries.owasp.org/cheatsheets/Java_Security_Cheat_Sheet.html

---

OWASP Cheat Sheet Series

## Injection Prevention

### SQL Injection
Use `PreparedStatement` with parameterized queries. Never build SQL by string concatenation with user input.

```java
String query = "select * from color where friendly_name = ?";
try (PreparedStatement pStatement = con.prepareStatement(query)) {
    pStatement.setString(1, "yellow");
    ResultSet rSet = pStatement.executeQuery();
}
```

### JPA Injection
Use named parameters in JPQL:
```java
String queryPrototype = "select c from Color c where c.friendlyName = :colorName";
Query queryObject = entityManager.createQuery(queryPrototype);
Color c = (Color) queryObject.setParameter("colorName", "yellow").getSingleResult();
```

### OS Command Injection
Use Java API methods instead of building shell commands with user input:
```java
// Use InetAddress.isReachable() instead of building a ping command string
InetAddress host = InetAddress.getByName("localhost");
var reachable = host.isReachable(5000);
```

### XPath Injection
Use `XPathVariableResolver` to parameterize XPath queries rather than string concatenation.

### HTML/JavaScript/CSS Injection (XSS)
- **Input**: Use strict allowlist validation (`Pattern.matches("[a-zA-Z0-9\\s\\-]{1,50}", input)`).
- **Output**: Use OWASP Java HTML Sanitizer + OWASP Java Encoder to sanitize and escape output.

```java
PolicyFactory policy = new HtmlPolicyBuilder().allowElements("p", "strong").toFactory();
String safeOutput = policy.sanitize(outputToUser);
safeOutput = Encode.forHtml(safeOutput);
```

### NoSQL Injection (MongoDB)
Validate input for special characters (`'`, `"`, `\`, `;`, `{`, `}`, `$`). Use the MongoDB API's query builder rather than string expressions.

### Log Injection
Use parameterized logging. Never use string concatenation with user data in log calls:
```java
// GOOD
logger.warn("Login failed for user {}.", username);

// BAD
logger.warn("Failure for user " + username);
```

Configure structured JSON logging (Log4j `JsonTemplateLayout`, Logback `JsonEncoder`) with `maxStringLength` limits in production.

## Cryptography

### Encryption for Storage
Follow [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) algorithm guidance.

**Recommended**: Use Google Tink library for symmetric encryption (AES-128-GCM or AES-256-GCM).

**If using JCA/JCE directly**: Use AES/GCM/NoPadding with a 256-bit key and a unique 96-bit nonce for every operation. Have a cryptography expert review the implementation.

```java
KeyGenerator keyGen = KeyGenerator.getInstance("AES");
keyGen.init(256, new SecureRandom());
SecretKey secretKey = keyGen.generateKey();

byte[] nonce = new byte[12]; // 96 bits
new SecureRandom().nextBytes(nonce);

Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
cipher.init(Cipher.ENCRYPT_MODE, secretKey, new GCMParameterSpec(128, nonce));
byte[] cipherText = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
```

### Encryption for Transmission
**Recommended**: Use Google Tink for hybrid encryption (ECDH + AES-GCM) between parties.

**If using JCA/JCE directly**: Use ECDH (secp256r1 curve) to derive a shared secret, then use AES-GCM for symmetric encryption. Regenerate key pairs periodically to avoid long-lived shared secrets.
