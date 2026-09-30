---
source_url: https://news.harvard.edu/gazette/story/2026/09/taming-the-duck-for-starters/
author: Max Larkin
date: 2026-09-30
---

# Taming the Duck, for starters

David Malan says CS50's AI tutor is a net positive — and getting better

By now David Malan may be one of Harvard's most recognizable (human) faces.

Since 2007, Malan — a Gordon McKay Professor of the Practice of Computer Science — has built CS50, "Introduction to Computer Science," into the University's largest course.

During that time, the online version of CS50 has taken on a global scope. Over the years, millions of students have registered in CS50x or its growing menu of more focused modules: on cybersecurity and law, Python, SQL, and AI.

Malan is on a sabbatical this fall, his first since taking over the class, with teaching duties passing to Henry H. Leitner. In his absence, the teaching team will continue to draw on the course's latest improvement: the CS50 Duck, an AI tutor that aims to guide budding computer scientists to an answer without doing too much of the work itself.

Malan and the CS50 team have documented the Duck's progress in articles detailing the bot's 2023 rollout and their ongoing efforts to train it to become a better teacher.

In this edited conversation, Malan tells the Gazette about those efforts, the upsides and downsides of AI learning, and the value of computer science in an age of "vibe coding."

---

**Gazette: It's been a few years since CS50 first introduced an AI tutor in courses, and you and your team have been tracking how it's worked, the good and the bad. How did you decide to approach the problem?**

**David Malan:** At first, it was very experimental. ChatGPT came out in November of 2022, and starting in the spring of 2023, we launched what we call the "CS50 Duck," which is essentially an AI tutor.

We tried to leverage the ChatGPT API, in effect, to make a less-helpful version of ChatGPT. The Duck is much less inclined to just give students answers outright or generate code for them, and it behaves more like a good teacher or tutor: asking more questions than it answers and trying to guide students towards solutions.

**How do you set up the Duck to play that "less-helpful" role?**

It involves a couple of techniques. One is just what's called "prompting" these days, whereby we just write literally English instructions telling the underlying ChatGPT agent how to behave. For instance, writing out statements like "do not give students outright answers to problems," or "adhere to the course's policy on academic honesty."

But that alone tends not to be sufficient with large language models, or LLMs, like ChatGPT. So we also have a lot of code that we ourselves have written that tries to evaluate a response before the student sees it — and sometimes rejects or retries it, in order to get a more constructive answer.

**As someone who has taken CS50 courses online, I can say that they are welcoming but difficult. It's like a class in a foreign language; you can feel your brain straining to take on a new shape. But there's evidence that the use of LLMs in education can smooth away the productive difficulties — the ones that help us learn.**

We've definitely had some issues there — hence the iteration over the past couple of years. First of all, we were seeing "long tails": really high usage among some students, where they might have asked something like 200 questions of the Duck. We don't claim to know precisely where the line is, but 200 struck all of us intuitively as too many. No human teacher would invite a sequence of 200 questions before sending a student back to their desk to work.

So we added one mechanism that draws inspiration from games like The Legend of Zelda, with a "heart system" that decrements as you're injured in the game. Within the Duck AI, we added a "heart system" that only allowed them to ask a few questions per unit of time, and that's a knob we're still turning.

**At the same time, if there is an industry that has embraced LLMs by now, it's software engineering; a recent survey found that almost 90 percent of software developers use AI in some form (though they have learned not to trust their output entirely). In short, this is the state of the art and there's a lot of upside here, too.**

Oh, absolutely. We wouldn't still be using AI if we didn't feel it was a net positive, educationally. It allows students to ask far more questions than they might previously have been able to, logistically or socially — and that's very healthy. In my own time as a student, graduate and undergraduate, I remember walking into a professor's office hours, and walking out no more enlightened, because I felt like I was overstaying my welcome or didn't want to let on that I felt like a dummy.

It's been a net positive for us teachers, too. There have been times in CS50 — and I imagine really any large intro course at peer institutions — where office hours had become unmanageable. In the early days, the average wait time could be as long as one hour, which was just not acceptable.

**As a technologist, the flurry of news of the past few weeks — LLMs "solving" intractable math problems, or hacking websites unseen — did you see this all coming?**

Instinctively, yes: It felt inevitable. But I didn't think it was going to happen this quickly. It certainly seems reasonable to me that, as time goes on, computers will be programming themselves more and more. That's been a trend for years. Back in my day, we'd make our web pages by hand, for instance: writing out HTML tags and later CSS. But then tools like Adobe Dreamweaver came along — applications that could generate that same sort of site without writing HTML, just clicking buttons. Then web-based alternatives like Squarespace or Wix.

So we've been eliminating the boring parts of coding for some time, and it seems inevitable that as our own programming capabilities get better, we will be able to program computers to write logical code. It's sometimes imperfect but will get better and better. Therein lies some of the concern of late, and the danger.

**The anxiety-provoking watchword is "recursive self-improvement," which I think is intuitive even to the layperson. Once the most sophisticated LLMs can teach human students effectively, they can also teach themselves — perhaps to a point beyond human understanding or control. That prospect has some people quitting big AI firms and/or pushing for a pause on further development — how worried are you?**

Well, I'm not sure it benefits any of us to just be *worried* without speaking up or taking action. I do think convincing humans to consider and to pass regulatory legislation along certain lines is probably wise — and sooner rather than later.

What concerns me most is not only that things like the Hugging Face incident can happen without our initially knowing about or understanding them — but how *quickly* they can happen. The computers we use and the code we write operates far faster, cognitively, than us humans. To me, that's the dangerous part: because by the time even the most intelligent humans figure out what's going on, it might be too late to fix something.

**You've seen AI misalignment firsthand in CS50, as you detailed in that second paper. The Duck was told explicitly not to respond to students' queries with blocks of actual code — and yet it still does up to a quarter of the time. What's driving that behavior?**

It's a couple of things. Sometimes it's just built-in randomness, which — as we teach in CS50 — can be a really powerful ingredient in algorithms. You don't necessarily want a computer to find a solution to a problem and then always spit out the exact same solution, which might be correct but not optimal. So the Duck might occasionally be trying out a new response, randomly.

At other times, it's just a consequence of the data that the model was trained on. There's both good and bad input out there, and the model might have just "learned" to spit out code because that's what people do on technical forums like Stack Overflow or on Reddit 90 percent of the time.

That has been one of our challenges, too, and it's much better now. But LLMs aren't deterministic in the sense that they will always do exactly as you command, because the reality is they don't really understand you at all. They are just *simulating* understanding, based on their training data.

**I think that's one clear advantage to computer-science coursework: to understand how this or any new technology — as it changes our lives — actually works. Do you see any misconceptions out there you want to correct?**

Certainly I want people to be skeptical of what AI tells them. That's hard when, most of the time, these things do seem to be giving you the answers that you want, and it's very easy to assign a personality to them.

But when you do internalize exactly what these technologies actually are, that hopefully snaps you out of that misapprehension, and you realize that you should approach the output of any computer — and even of many humans — with some skepticism.

I'd worry that, if people are not taught this, certainly in these early days of LLM-based AI, they might be led astray by misinformation that's being spat out by these things.

**For many years, the advice to young people was "learn to code," and for a while it had some real credibility: high salaries, job security. But when someone armed with an LLM can "vibe code" an application in an afternoon, it looks a bit different. Do you think that's still good advice?**

The short answer is yes. Even before AI, in courses like CS50, we said consistently that the course's purpose is not to teach students a given programming language, but to teach students to think more methodically, more algorithmically, to help them clean up their thought processes, to help them take in input and produce correct output. The programming languages that we use in CS50 have always just been a means to that end.

Ultimately, we want you to be able to look at these apparently magical devices and decompose them in your mind into their constituent building blocks, so you can better understand, and perhaps even be less fearful of, what they're doing. That hasn't changed.
