---
title: "Lesson 7: Effective prompting techniques (Deep Dive) | AI Fluency: Framework & Foundations Course"
channel: Anthropic
date: 2025-06-12
url: "https://www.youtube.com/watch?v=2YCaBqP8muw"
cover: imgs/cover.jpg
description: "This video is part of Deep Dive 2 of AI Fluency: Framework & Foundations, a course developed by Anthropic, Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). It explores practical skills for crafting effective prompts when working with AI assista"
language: en
---

# Lesson 7: Effective prompting techniques (Deep Dive) | AI Fluency: Framework & Foundations Course

This video is part of Deep Dive 2 of AI Fluency: Framework & Foundations, a course developed by Anthropic, Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). It explores practical skills for crafting effective prompts when working with AI assistants like Claude. View the full free course, including all videos, exercises, and resources, at https://www.anthropic.com/ai-fluency.

## Table of Contents
* [00:00:12] Introduction: What Is Prompting?
* [00:02:15] Tip 1: Give Claude Context
* [00:03:34] Tip 2: Show Examples of What Good Looks Like
* [00:04:53] Tip 3: Specify Output Constraints
* [00:05:36] Tip 4: Break Complex Tasks Into Steps
* [00:06:51] Tip 5: Ask Claude to Think First
* [00:07:56] Tip 6: Define Claude's Role, Style, or Tone
* [00:08:45] Bonus Tip: Ask Claude to Improve Your Prompt
* [00:09:17] Iterative Practice and Recap

![cover](imgs/cover.jpg)


## Introduction: What Is Prompting? [00:00:12]

[Music] [00:00:09]

**Narrator:** Let's explore one of the most practical skills when working with AI. Crafting effective prompts. This might sound technical or complicated, and some guides certainly make it seem that way, but at its heart, it's surprisingly straightforward. [00:00:12 → 00:00:26]

Prompting is simply how we apply this course's description competency in practice. Clearly communicating what we want, how we want it done, and how we want to interact with our AI assistant throughout the entire process. Think of prompting like explaining a task to a helpful new colleague who's eager to assist, but needs clear directions and expectation setting to do their best work. [00:00:26 → 00:00:45]

We'll be using Claude throughout this section, but these tips can be carried over to many other AI systems. You might have heard the term prompt engineering tossed around. Prompt engineering is simply the practice of designing effective instructions for AI systems like Claude. It's about crafting your questions and providing context in ways that help AI assistants understand exactly what you want. [00:00:45 → 00:01:09]

What's fascinating is that effective prompting blends familiar human communication skills with a few considerations specific to AI. Many principles that make for good human conversation, such as being clear, providing relevant context, and giving concrete examples, also apply when working with AI. Yet, there are differences, such as being more explicit about things humans could naturally infer, and accommodating the AI's limited context window, and sometimes, depending on the AI you're working with, using specific formatting that machines can easily process. [00:01:09 → 00:01:40]

As AI assistants continue to evolve, prompting best practices evolve, too. What works with today's AI systems may be different from what works with tomorrow's. Experimentation is key to discovering what works best for your specific needs. [00:01:40 → 00:01:52]

In this video, we'll mainly explore six foundational prompting tips that will go a long way toward helping you effectively communicate and collaborate with Claude and other AI systems. They are give Claude context, show examples of what good looks like, specify output constraints, break complex tasks into steps, ask Claude to think first, and define Claude's role, style, or tone. [00:01:52 → 00:02:15]


## Tip 1: Give Claude Context [00:02:15]

**Narrator:** The first principle is simple but powerful. Be specific and clear about what you want, why you want it, and perhaps most surprisingly, who you are. [00:02:15 → 00:02:24]

Let's take a simple prompt. Tell me about climate change. How can we improve this by giving Claude more context? A more specific, context-rich version could look like, explain three major impacts of climate change on agriculture in tropical regions with examples from the past decade. [00:02:24 → 00:02:43]

Our baseline prompt was vague and leaves Claude guessing about our interests, level of knowledge, and the depth of detail we're looking for, such as geography and time span. We can even add more context by providing information not just about what we're looking for, but why we're asking and how we'll be using that information that Claude gives us. [00:02:43 → 00:03:00]

Now, our prompt looks like this. Explain three major impacts of climate change on agriculture in tropical regions with examples from the past decade. I'm preparing for a job interview at an agricultural research lab in Indonesia. I have a degree in ecology, but no specific knowledge on climate change. Write a summary of key concepts that would help me speak intelligently in the interview. [00:03:00 → 00:03:21]

All this added context helps tailor Claude's response to your specific situation and knowledge level. This kind of background information is something we naturally provide in human conversations, but might forget to include when talking with Claude. [00:03:21 → 00:03:34]


## Tip 2: Show Examples of What Good Looks Like [00:03:34]

**Narrator:** Sometimes showing is better than telling. Providing examples of the kind of output you're looking for can be incredibly effective. This is sometimes called few-shot prompting or n-shot prompting in technical circles where n is the number of examples given, but it's really just about showing the AI examples for it to emulate. [00:03:34 → 00:03:50]

For instance, take the following prompt. Please convert this technical statement to plain language. The platform implements end-to-end encryption protocols to safeguard data integrity. [00:03:50 → 00:04:00]

Claude may already be able to do this to your satisfaction. So we definitely recommend you just try first without examples and see where it leads you. But let's say you have a very specific style you want Claude to follow, and it's harder to explain than to give examples. [00:04:00 → 00:04:15]

Your refreshed prompt could look something like this. Here are two examples of how to convert technical jargon into plain language. Original, the quantum algorithm exhibits quadratic speed up. Plain, the new method solves problems roughly twice as fast as previous methods. Original, the interface leverages intuitive design paradigms. Plain, the design is easy to understand and use. Now, please convert this complex technical manual to plain language. [00:04:15 → 00:04:43]

When providing examples, aim to cover the full diversity of possible prompts, such as examples that cover different cases or styles. This helps Claude better understand the broad range of the pattern you want it to follow. [00:04:43 → 00:04:53]


## Tip 3: Specify Output Constraints [00:04:53]

**Narrator:** Being clear about output constraints, such as the desired format and length of Claude's response, or the language you want Claude to code in, or the color of the buttons on the web page you want Claude to design, also helps ensure you get exactly what you need. [00:04:53 → 00:05:08]

Here's an example of clear and detailed description to ensure Claude delivers exactly what you're looking for. Create a clean, modern, single page art portfolio website. Include these main sections: hero, about me, skills, portfolio, projects, experience, and contact. Make the navigation menu sticky and responsive with hamburger menu on mobile. Use a sunset color palette and add a dark light mode toggle in the navigation. [00:05:08 → 00:05:32]

Guidance like this helps Claude structure its response to match your expectations. [00:05:32 → 00:05:36]


## Tip 4: Break Complex Tasks Into Steps [00:05:36]

**Narrator:** When you have a complicated request, breaking it down into smaller steps helps Claude follow your thinking and deliver better results. Think about it this way. If you ask a friend to do something for you without specifying how, there's a chance that they may not do it the way you intended them to. We've all been there. [00:05:36 → 00:05:54]

Listing out task steps ensures that Claude follows the process you want to in order to accomplish its task. This is sometimes called chain of thought prompting. [00:05:54 → 00:06:02]

For example, instead of asking Claude to analyze this quarterly sales data, you might say, "I'd like to analyze this quarterly sales data. Please approach this by looking through our sales records to identify the top performing products, comparing current quarter results to the previous quarter, highlighting any unusual trends or patterns, and then suggesting possible reasons for these trends." [00:06:02 → 00:06:21]

By default, you may not need to do this, especially for tasks that are relatively straightforward. Furthermore, modern reasoning models or extended thinking models are increasingly capable of performing step-by-step reasoning on their own, but you can still guide this process to ensure it aligns with your needs. The more variance there is in ways to execute the task well, or the more that proper task execution relies on experience and knowledge you've gained as a domain expert, the more you should consider taking the time to translate that knowledge into Claude. [00:06:21 → 00:06:51]


## Tip 5: Ask Claude to Think First [00:06:51]

**Narrator:** Relatedly, sometimes it can be helpful to explicitly give AI assistants like Claude space to work through its process first before executing its task. This approach helps Claude produce more thorough and well-considered responses. [00:06:51 → 00:07:04]

For example, you can add this to your prompt. Before answering, please think through this problem carefully. Consider the different factors involved, potential constraints, and various approaches before recommending the best solution. [00:07:04 → 00:07:18]

As I mentioned, modern reasoning or extended thinking models by default think before acting. But if you're working with an AI assistant that does not think first by default, you can still prompt the AI to do so. [00:07:18 → 00:07:28]

I want to note the importance of giving the AI assistant space to think before doing its task, not after. If you want that thinking to increase the quality of the AI's work, just like how having space to think before you act is different than acting first, then being asked to explain your thinking afterwards. As a side benefit, this also allows you to better see where the AI assistant might be going astray and thus where you could hone your description competency further by providing more guidance. [00:07:28 → 00:07:56]


## Tip 6: Define Claude's Role, Style, or Tone [00:07:56]

**Narrator:** Specifying how you want Claude to communicate and behave can significantly change how it approaches a task. By specifying the level of expected expertise, the perspective you want it to take, or its communication style, you can guide both Claude's interaction with you and the final result of what it produces. Simply put, who do you want the AI to act as? [00:07:56 → 00:08:15]

For example, take this prompt. Please explain how rainbows form from the perspective of an experienced science teacher speaking to a bright 10-year-old who's interested in science. [00:08:15 → 00:08:25]

This is also a good way to brainstorm or get feedback. You can specify a general role or even ask Claude to take on the persona of a specific figure, such as Richard Feynman, when asking for physics explanations. Here's another example. As a UX design expert, review this website wireframe and suggest three improvements focusing on user navigation and accessibility. [00:08:25 → 00:08:45]


## Bonus Tip: Ask Claude to Improve Your Prompt [00:08:45]

**Narrator:** Perhaps the most powerful technique is asking Claude to help improve your prompt. When you're not sure how to ask for something or how to improve your prompt, describe to Claude your issue or situation and ask it to make your prompt better or write your prompt for you. [00:08:45 → 00:08:59]

I'm trying to get you, Claude, to help me with goal. I'm not sure how to phrase my request to get the best results. Can you help me craft an effective prompt for this? [00:08:59 → 00:09:08]

Here's where Claude and other AI assistants may vary most in terms of performance. So, we suggest you experiment with different models as part of practicing delegation. [00:09:08 → 00:09:17]


## Iterative Practice and Recap [00:09:17]

**Narrator:** Effective prompting is iterative and experimental. AI systems and best practices are constantly evolving. So, what works today may change tomorrow. Your first attempt won't always yield the perfect result, and that's expected. [00:09:17 → 00:09:29]

When a response isn't quite what you need, try refining your approach by playing around with any of the techniques we mentioned, such as add more specificity or context. Provide examples of your desired output. Break the task into smaller steps and try a different technique or combination of techniques. [00:09:29 → 00:09:49]

You can also ask for variations such as, "Can you give me three different versions of this?" You can request different formats such as, "Instead of a paragraph, could you present this in an interactive artifact?" Note that artifacts are a unique way that Claude can create outputs that may be easier to understand or more interesting to digest. [00:09:49 → 00:10:07]

You can also check confidence, such as for factual questions, you can ask, "How confident are you about this answer?" You can also reset the conversation entirely. Sometimes starting a fresh conversation gives better results than trying to correct the conversation that's gone off track. [00:10:07 → 00:10:21]

Use each interaction as feedback to improve your next prompt. Over time, you'll develop an intuition for how to communicate effectively with all AI systems. [00:10:21 → 00:10:30]

As you apply these techniques in practice, here's some guidance to recap. Some patterns consistently work well: starting with a clear task overview statement, including format specifications and examples, setting explicit constraints or requirements, providing rich and relevant background information. [00:10:30 → 00:10:47]

And common mistakes to avoid are assuming that Claude can read your mind, or overloading a single prompt or conversation with multiple unrelated tasks, being too vague about what success looks like, and not providing feedback on previous responses. [00:10:47 → 00:11:01]

To recap, effective communication with AI systems like Claude combines timeless human communication principles with AI-specific techniques. The approaches we've covered will serve you well across different AI systems. These six principles together with the secret weapon of asking Claude for help form a solid toolkit for applying the description competence to your AI interactions. [00:11:01 → 00:11:19]

Iteration and practice here is the key to swift improvement and mastery. Remember that prompt engineering is an evolving practice. As models improve, some specific techniques become less necessary. However, these principles of good communication are still relevant even if the way we apply them changes. Maintain a spirit of experimentation and adapt your approach based on your results. [00:11:21 → 00:11:45]
