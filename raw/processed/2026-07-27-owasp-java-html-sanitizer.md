# OWASP Java HTML Sanitizer

source_url: https://owasp.org/www-project-java-html-sanitizer/

---

OWASP Foundation

## What Is It?

The OWASP HTML Sanitizer is a fast, easy-to-configure Java HTML sanitizer that lets you include third-party HTML in your web application while protecting against XSS. It is dual-licensed under Apache 2 and New BSD licenses. Code was written with security best practices in mind, has an extensive test suite, and has undergone adversarial security review.

Dependencies: Guava and JSR 305 (compile-only).

## How to Use

Available on [Maven Central](https://search.maven.org/#search%7Cga%7C1%7Cowasp%20html%20sanitizer).

### 1. Use Prepackaged Policies
```java
PolicyFactory policy = Sanitizers.FORMATTING.and(Sanitizers.LINKS);
String safeHTML = policy.sanitize(untrustedHTML);
```

### 2. Configure Custom Policy
```java
PolicyFactory policy = new HtmlPolicyBuilder()
    .allowElements("a")
    .allowUrlProtocols("https")
    .allowAttributes("href").onElements("a")
    .requireRelNofollowOnLinks()
    .build();
String safeHTML = policy.sanitize(untrustedHTML);
```

### 3. Define Custom Element Policies
```java
PolicyFactory policy = new HtmlPolicyBuilder()
    .allowElements("p")
    .allowElements(
        new ElementPolicy() {
            public String apply(String elementName, List<String> attrs) {
                attrs.add("class");
                attrs.add("header-" + elementName);
                return "div";
            }
        }, "h1", "h2", "h3", "h4", "h5", "h6")
    .build();
```

### 4. Predefined Policies
- **eBay policy**: Allows common formatting.
- **Slashdot policy**: Allows `a`, `p`, `div`, `i`, `b`, `em`, `blockquote`, `tt`, `strong`, `br`, `ul`, `ol`, `li` with restricted attributes.

## CSS Sanitization Notes
- `position:sticky` and `position:fixed` are disallowed to prevent overlay attacks.
- Embedders must use `position:relative; overflow:hidden` to contain sanitized content.
- Unproxied image URLs can be used for tracking; use URL rewriting if allowing background styling.
- CSS has a large attack surface — not allowing CSS at all is the safest option.

## Inline/Embedded Images
Allow inline images (data URIs) by:
1. Adding `"data"` to the URL protocol allowlist.
2. Adding a matcher on `src` attribute of `img` elements to restrict to data URIs only.
3. Adding a matcher on `href` of `a` elements to reject any URL containing a colon that doesn't start with `http:`, `https:`, or `mailto:`.
