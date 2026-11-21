---
source_url: https://forklightning.substack.com/p/the-education-of-an-ai-skeptic
author: David Deming
date: 2026-11-16
---

# The education of an AI skeptic

*How reading 75 experiments on AI in education gave me some cause for optimism*

Hello Forked Lightning readers! It’s been a while, but I’ve been busy recording podcasts, including a three-part series (part one, part two, part three) that I just completed about AI in education.

To prepare for that series I read more than 75 studies (mostly randomized controlled trials) and distilled them into a small number of lessons about the good and bad uses of AI to learn, to get feedback, and to write. Today I want to tell you what I’ve learned.


I also assembled the studies into a massive table, which you can find at the end of this post. The table is organized according to the major themes I’ll mention, and each row includes a brief description and a link to the paper if you want to learn more. I will try to update it periodically as new evidence becomes available.

The antecedent of this effort was an essay I published nearly a year ago called “Using Generative AI to learn is like Odysseus untying himself from the mast.” I argued that while AI can provide personalized learning at scale, it also removes all the friction. You can get the exact answer you want, right away, with little or no effort. And that makes it awfully tempting to take the easy way out. Like Odysseus, the right answer is not to plug our ears and foreswear unlimited knowledge, but to restrain ourselves strategically so we can benefit from access to AI without giving in to temptation.

When I published the essay in early January 2026 I could find only a small number of high-quality studies on AI in education. And they showed very clearly that AI without guidelines or guardrails was harmful for learning. Many professors and tech leaders have been critical about the impact of AI on education and concerned that it will lead to cognitive offloading and learning loss, including Bill Gates, Andrew Ng, Noam Chomsky, Jonathan Haidt, and others. I was in good company with my pessimism about AI in the classroom.

But since January, dozens of RCTs and other studies with good research designs have been published. And that means it’s time for some belief updating. After reading all the studies and synthesizing the evidence, I’ve updated positively on the possibility that AI really can improve learning.

49 of the 75 studies I reviewed showed broadly positive impacts, 16 were mixed or null results, and 10 were negative. There were some clear patterns in the positive and negative results, which I’ll describe in more detail below. Of course, I can only read the studies that exist and that were publicly released. With research on controversial topics like AI people sometimes worry about publication bias - or more colloquially the “file drawer” problem, meaning unfavorable results get buried in a file drawer.

A useful antidote for publication bias is pre-registration, where researchers write up a full analysis plan before starting data collection and submit it to a website like the AEA RCT registry. Pre-analysis plans solve the file drawer problem because the study gets publicly posted before the results are known.

I could verify that 14 of the studies I reviewed were pre-registered, and another 6 may have been pre-registered.1 9 of the 14 studies with pre-analysis plans showed broadly positive impacts, 3 were mixed or null, and 2 were negative. Those proportions are almost exactly the same in the full study sample (9/14 = 64%; 49/75 = 65%), which suggests that we don’t have a serious problem with publication bias.

If anything, publication bias on the topic of AI in education is likely to go in the other direction, because the negative studies have gotten most of the media attention. That’s mainly because negative news headlines causally increase readership - if it bleeds it leads. There are bad vibes about AI and big tech in general, and not without reason. For example, when people balked at Google rolling their Gemini chatbot out to grade school classrooms around the country, they responded by disabling the entire Google suite because they claimed that AI was too integrated into Google search to fully separate them. Bernie Sanders called this “extortion”, and Zohran Mamdani accused Google of using its “monopoly power to force AI into our public schools.”

It’s hard to feel good about AI under the circumstances! But it doesn’t change the fact that a randomized trial of Gemini’s Guided Learning AI tool in Sierra Leone found huge learning gains in math relative to a control group that got business-as-usual instruction, and that students and teachers reportedly loved the tool and engaged actively with it.

I believe the other reason that people are so negative about AI in education is that the status quo is the worst way to use AI. In most classrooms around the world, AI is either uncritically accepted without clear guidelines, or banned without a realistic enforcement mechanism. This leads to situations like a recent “cheating scandal” at Brown where students scored an average of 96% on a take-home midterm exam in a course where AI was supposedly banned, and in response the professor announced that the final would be proctored and in-person. The average final exam score fell to 49%, and many students dropped the class rather than take the in-person assessment. To be clear, this could have easily happened at Harvard or anywhere else, so we’re all on notice.

There were probably some students in the course who knew it was wrong but decided to use AI anyway, because they knew their classmates would use it and they didn’t want to fall behind. It’s hard to score 96% on a midterm exam without help, and the ChatGPT window was just sitting there, like a devil on their shoulder, sweetly whispering “everybody’s doing it.” Unenforceable AI bans make it hard to the right thing, and easy to do the wrong thing. It’s not fair to students.

My point is that there are good and bad uses of AI, and it is our job to help students distinguish between them. It’s bad to let AI think and write for you, because it creates the illusion of mastery and can lead to laziness and cognitive offloading. And yet, if you do your own thinking first, AI can be an exceptional tutor, feedback partner, and critic. Some students have the self-control and motivation to work this out on their own. But many more do not, and it’s our job as educators to help them. When we ignore, or ban and shame, we lose the opportunity to teach and guide students toward good uses of a powerful new technology.

And that is why the research mostly shows positive impacts. Almost all the studies I reviewed put some scaffolding around the use of AI, whether it was forcing students to write first before receiving AI feedback, developing a Socratic tutor that doesn’t just give away the answers, adaptively sequencing follow-up material, or some other clever design. All these scaffolding choices are better than how AI is being used in classrooms today – in the shadows, with little guidance or oversight. Students deserve better. And if we want to teach them how to think for themselves, we should lead by example.

With that preamble, I’ve organized my review into seven sections below.

## Think first, ChatGPT later

This was the main lesson from my January essay, but several studies published since then have backed up the basic conclusion that you should do the work yourself before asking AI for help.2

An experiment in a large Turkish high school gave some students access to out-of-the-box ChatGPT, gave others a “tutor” mode version of ChatGPT that didn’t give away answers, and a “no AI” control group. The study found that both forms of AI helped students in the practice sessions, but neither improved performance on an unaided final exam, and out-of-the-box ChatGPT made students do worse than the control group. Another study found that AI helped management consultants complete a data science task, but when AI was taken away they retained none of the knowledge.

A third study in an afterschool tutoring company in China found that an AI tutor designed to activate only after a student submitted an unassisted answer helped students do many more practice problems in much less time. A fourth study in a similar setting found that students using an AI tutor got the biggest learning benefits when getting an answer only after they had attempted the problem without help.

Two other recent studies validated “think first, ChatGPT later” in different settings. One was a creativity experiment where participants were given a stuffed bunny and asked to propose ideas to make it better. One group got unlimited access to ChatGPT, another came up with their own ideas first before getting ChatGPT, and a third got no AI help. After each group finished, they were given another creative task to complete where none of them got AI. The “think first, ChatGPT later” group was much better on the final unassisted task than the other two groups, and the researchers found that this was because it encouraged participants to use AI to build on their ideas and make them more practical, which apparently translated over to a new task. A second study found that students in an English as a foreign language (EFL) got the highest scores on an unassisted final exam when their access to an AI tutor activated only after they completed the reading independently.

## Personalize productive struggle

Learning requires what psychologists and educational experts often call “productive struggle”, which is the level of difficulty where you feel a little confused and overwhelmed but can still make consistent progress. The problem is that a teacher with 30 students can’t possibly tailor material to everyone’s needs at the same time.

That is where AI can help. I found four randomized controlled trials, all released in 2026, that show the benefits of using AI to personalize productive struggle.

I mentioned the first one already. A large RCT with more than 1,700 students in 48 classrooms and 12 middle schools in Sierra Leone found that Google Gemini’s Guided Learning – which acts like a patient Socratic tutor that guides students through problems – improved unassisted math test scores by 0.26 standard deviations after eight weeks, relative to a no-AI control group. Students reported that Gemini met their individual learning needs and helped them understand concepts step-by-step. A second study of more than 1,000 high school students learning Python compared a standard AI tutor to an augmented version that used RL techniques to adaptively sequence practice problems for students based on their previous answers. This personalized productive struggle improved students’ scores by 0.15 standard deviations on an unaided pencil-and-paper test relative to standard AI.

A third study gave chess students access to automatic AI tips to help them learn important concepts. One group was tips only, and another group had the option to request help any time just by pushing a button. The first group actually learned more, because the ability to ask for help on-demand meant that students didn’t engage in enough productive struggle. The fourth study was a large randomized trial in Tennessee middle schools of Khanmigo, an AI-assisted Socratic tutor developed by Khan Academy. They found that Khanmigo’s personalized AI tutoring platform increased math scores by 0.14 standard deviations per school year of participation, relative to a control group that had access to alternative coursework including other other online tutoring programs.

All four studies used AI to tailor practice problems to students’ individual needs and guided them through the material steadily while providing feedback.

## The importance of scaffolding

Even though personalized 1:1 tutoring speeds up learning, it is hard to scale purely with technology, because students need to be intrinsically motivated to take advantage of it. Consider Alpha School, a fast-growing network of private schools that promises to use AI to double students’ annual learning gains in half the time. Alpha School currently serves about 1500 students across 50 campuses, but it has announced ambitions to serve a billion students worldwide. A recent New York Times article threw cold water on their claims, although the framing was laughably negative (“about half of K-8 students enrolled in Alpha private schools last year did not meet their promise that they would learn math twice as fast, according to Alpha data reviewed by The New York Times” – which means that half did, that’s pretty good!)

Still, the core issue with scaling Alpha school is that most kids are not self-motivated enough to speed run a curriculum for 2-3 hours on an iPad every day, with no teachers or books. Self-paced, technology-assisted learning probably works best for students who are already highly motivated. The implication is that scaffolding is important – you can’t just drop AI on students and expect learning to happen.

I found four high-quality research studies that provide good evidence on scaffolding and motivation.

The first paper is a staggered event study across Chinese schools where students adopted AI tools on their own at different times. This measures the impact of unsupervised AI use, meaning no scaffolding at all. The paper found that AI adoption increased homework scores but decreased final exam scores, and was the source of some viral charts that traveled all around social media and the internet. In my opinion, this paper gets closest to measuring the impact of the status quo in most American grade schools and colleges.

A second study evaluated the impact of an AI study assistant in online college courses in Maryland. The AI assistant mostly gave direct answers to student questions, and it was pitched as a replacement for online discussion with peers and office hours with faculty. The AI treatment group spent less time on the course website, participated less in instructor-designed activities, asked fewer questions, and did worse on the exam. In this case, the design of the AI assistance discouraged productive struggle and engagement, because students could get the answers without having to show up.

Two other studies show how good scaffolding of AI assistance can improve learning. The first randomly assigns an AI tutor to nearly 200 Harvard students in an introductory physics class. The AI tutor was carefully integrated into the course, and students were given guidance on how to use it, which led to huge learning gains. The second study gives a course-specific AI tutor to students in a large economics class in a Chilean university. The instructors initially gave no guidance about how to use it, and it had no impact on midterm scores. But after the midterm they explained to students how to use it to work out concepts step-by-step, generate practice problems, receive feedback, and other tips, and this greatly improved final exam performance (the students were re-randomized after the midterm, and I believe the staging of feedback was part of the design.) That’s an unusually direct demonstration of the importance of scaffolding.

## AI improves writing quality, especially for weaker writers

Lots of studies show that using AI to complete a writing task makes the writing better as judged by blind human graders. A paper published in Science randomized ChatGPT access to ~450 college-educated professionals and asked them to complete a realistic professional writing task. ChatGPT reduced completion time of the writing assignment by 40 percent, and blind human evaluators rated the AI-assisted essays as 18 percent better. The gains were larger for weaker writers.

Another study found a similar result for creative writing. Participants were randomly assigned to one of three conditions – write a short story without any AI assistance, call on the AI to give you a three-sentence starting idea, or ask the AI to give you up to five different three-sentence ideas. The essays of writers given AI-generated story ideas were rated as more creative, better written, and more enjoyable, five AI ideas worked better than one, and again the benefits were greater for initially less-creative writers. A third study asked people to write one essay with ChatGPT and another without it. Human judges strongly preferred the ChatGPT-assisted writing overall, but again the gains were bigger for weaker writers. Finally, a review of 39 studies found that AI improves English writing for people who are non-native English speakers, again with the largest gains for low proficiency students.

AI helps you produce good quality conventional prose. If you’re already a good writer, AI might make your prose worse, even if it speeds you up.

## Outsourcing writing to AI can make later unaided writing worse

AI can improve writing. Does it make you a better writer? In other words, does using AI make you a better or worse writer over time, and do the impacts of AI persist when you don’t have access to it anymore?

Two studies suggest that the answer is no, and that AI may even make your subsequent writing worse. The first is a very well-known study called “Your Brain on ChatGPT: Accumulation of Cognitive Debt when using an AI assistant for an essay writing task.”

They asked people to write three short, SAT-style critical essays under three conditions – no assistance, access to standard Google search, and access to ChatGPT. They also asked 18 of the initial participants to complete a follow-up session a month later where the no assistance group got ChatGPT and vice versa.

They didn’t just grade the essays. They monitored people’s brain activity with an EEG machine and found that the unassisted group showed the greatest brain activity, followed by Google search and then ChatGPT use. This study went completely viral and generated media headlines like “ChatGPT May Be Eroding Critical Thinking Skills” and “A.I. is Homogenizing our Thoughts”.

These are breathless headlines, but in reality the study participants were doing different things. Unassisted users were writing their own text from scratch, which is much more taxing than using AI to write and/or edit for you. If you asked some people to multiply two two-digit numbers in their heads and others to use a calculator, the first group would show more brain activity. That could mean that calculators rot your brain, but we still use calculators because we sometimes want to offload rote computation and save bandwidth for higher-order thinking.

A second study asked 900 participants to write an argumentative essay under three conditions 1) first write a thesis and an outline yourself, then use AI to improve it; 2) unrestricted access to AI, and 3) no AI at all. All three groups were asked to write a 2nd essay on a different topic right afterward, with no AI access. The unrestricted AI group scored much worse than the no AI group, while the “think first, ChatGPT later” group did better. The main caveat is that the final unaided assessment happened only 15-20 minutes later, so it doesn’t really test the concern about long-run cognitive offloading.

## AI feedback improves writing, even on later unaided assessments

What about doing the writing yourself and then asking AI to give you feedback? I found six randomized controlled trials showing that AI feedback improves writing.

The first two studies ask whether AI feedback is better than no feedback. One asks 459 high school EFL students to write an argumentative essay, while the second asks 144 university students to use AI to help revise research abstracts. Both find large positive impacts of AI feedback relative to no feedback.

Two other studies compare AI feedback to teacher feedback. The first randomized students in an introductory economics course to receive either handwritten feedback from teaching assistants, the same feedback plus access to an AI system that read student work and provided suggestions, and a control group. The group whose TAs had access to AI feedback did much better on their revised essays, and the improvements were larger when the TAs adopted more AI revisions. The second study randomized students to teacher feedback, AI feedback, or no feedback. Both teacher and AI feedback improved revision quality by the same amount, although teacher feedback produced higher intrinsic motivation.

Two more studies show how to use AI to give feedback. The first one demonstrates that AI feedback on structural issues like clarity of the claim, reasoning quality, and use of evidence was better than feedback on grammar, vocabulary, and sentence construction. The second study was a large RCT of the impact of feedback on scientific writing and argumentation in a semester-long course of either biology, chemistry, or physics. All students wrote an initial draft and then were randomly assigned to four different groups – 1) peer feedback only; 2) direct AI feedback; 3) self-evaluation first, then reflective feedback from AI; and 4) a combination of self-evaluation, peer critique, and AI critique. All students took a test of understanding after revising their paper, and they also completed a new writing assignment with no AI assistance in the last week of the course. The fourth group did the best on the final assignment, followed by group 3. Group 2 was no better on the final assignment than the control group. The authors show evidence that the more structured feedback in groups 3 and 4 led to greater engagement in the revision process, which boosted learning.

## Learn to write, and write to learn

Finally, I want to talk about two fascinating studies that address important questions about AI and writing. First, can AI go beyond just improving your writing, and actually help you learn how to write? Second, how does AI writing assistance affect later learning, and does it lead to cognitive atrophy?

The first study conducts 3 large-scale RCTs that ask whether AI can help people write and improve cover letters. In all three experiments, people were given a poorly written cover letter, asked to revise it under different conditions, and then given a new cover letter task without any AI help.

The first experiment compares three groups – practice with AI help, practice without AI, and no practice. Practicing with AI improved later unaided cover letter writing skill much more than practicing without AI, which was equivalent to no practice at all. The second experiment compared practice with AI to personalized feedback from professional human editors. AI was substantially better than professional human editors, even though the human editors gave writers customized rewritten examples. The third experiment compares AI assistance to another group that was only allowed to view an example AI-written cover letter (they couldn’t edit it). This third group did just as well as the AI assistance group, and both did much better than the no AI practice group.

The lesson is that AI can speed up learning by providing a high-quality, relevant example to emulate. This is especially valuable for a task like cover letter writing where there is a clear template and more ways to go wrong than right. Speeding up learning could easily look like cognitive offloading. Suppose you hooked two people’s brains up to an EEG. One spends lots of time rewriting their cover letter, beating their head against the wall. The second is given a single high-quality, relevant example and emulates it. The first person would show much more brain activity, but they will have learned less and probably written a worse cover letter.

Learning does require struggle, but it has to be productive struggle, not low-quality trial-and-error.

The second study, called “Experimental Evidence on the Learning Impact of Generative AI”, was designed specifically to test how using AI during the writing process affects later learning. It’s the closest thing we have to a true test of whether AI use leads to cognitive atrophy.

More than 200 Middlebury College students were randomly assigned to complete a writing assignment about an unfamiliar technical topic with or without access to generative AI. All students got access to a printed introductory reading and an internet browser with Google Search, Wikipedia, and the College library site open. Half of the group randomly got access to ChatGPT in addition to these other resources.

Both groups took an unaided knowledge test right after completing the writing assignment. The researchers also brought all participants back a week later and gave them another knowledge test and asked them to write a new essay on the same subject without AI or any other resources.

The results were shocking. The AI group performed significantly better on the immediate unaided knowledge test. A week later, the AI group also performed better on the new unaided knowledge test and the new writing assignment.

The authors show convincingly that AI changed how students allocated their writing time. Students in the AI group spent more time doing research and less time writing, probably because they used AI to help. Give a fixed time budget, AI freed up more time for reading, searching for information, and thinking, because students knew that AI would help them write their essay faster. The students who used AI didn’t offload, they substituted away from the mechanics of the writing process and toward conceptualization and higher-level understanding, which stuck with them a week later. The caveat is that it’s only one study. I’d love to see this result and others replicated in new settings.

I’ve produced a table below with links to all the studies I mention above, plus many more that I didn’t have time to cover, all organized by section heading. I surely left some good research out, so let me know if you find new research and I’ll add it as we go! I hope this can be a resource for people who are trying to understand the changing landscape of AI in education.

## Footnotes

1. In 6 cases, I was unable to confirm that the registry entry was filed prior to data collection.

2. One of the studies in the section deserves credit for the clever phrase “Think first, ChatGPT later.”
