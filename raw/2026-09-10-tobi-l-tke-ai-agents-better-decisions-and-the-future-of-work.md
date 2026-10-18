---
source_url: https://fs.blog/knowledge-project-podcast/tobi-lutke-3/
author: Unknown
date: 2026-09-10
---

# Tobi Lütke: AI Agents, Better Decisions, and the Future of Work

Shopify founder and CEO Tobi Lütke joins Shane Parrish to discuss AI agents, better decision-making, and the future of work. He explains how he uses an AI council to examine his hardest decisions and why taste, judgment, and responsibility become more valuable as AI becomes more capable.

They go inside Shopify’s work with River, an AI colleague with memory, personality, and permission to challenge the CEO. They explore how to choose between several good options, why the best long-term decisions often lack immediate feedback, and why building something that lasts requires pruning and rebuilding.

Tobi also shares how he cultivates intuition, the affirmations he uses to change his own behavior, and why his kids must add “yet” when they say they can’t do something.

Enjoy!
## Transcript

This transcript may contain errors. Please review the episode audio before quoting.

Shane Parrish: Tobi, welcome back.

Tobi Lütke: Shane, it’s so good to be back. I’m glad we’re doing this again.

Shane Parrish: How are you using AI internally at Shopify?

Tobi Lütke: We’ve found some ways for it to be supportive now. When did we record last time?

Shane Parrish: Oh, we recorded two, three years ago.

Tobi Lütke: Yeah. So a hundred years of internet.

Shane Parrish: Yeah.

Tobi Lütke: Look, I’m a 10 out of 10 nerd. I cannot bear the idea of somehow not being at the forefront of a technology shift. I live for these things. My take from sci-fi books I read was I wanted to live in that world and how can I accelerate us there? So I’m a technologist. I love technology. I’ve seen four major platform shifts, which is a privilege because most careers don’t have any. If you’re lucky, you have one.

We’ve seen the internet arrive. We’ve seen, of course, just microcomputer even becoming a thing people had in their homes even in the 90s. And Web 2.0 was really one, the mobile world, and now AI is just incredible. It’s the largest of them all. Inside of Shopify, the amount of people I know who really write code is vanishingly small now.

It still exists at the limits of complexity for sure. And obviously in the reviews and so on, and then state management of all things, it remains to be the thing that’s really the hardest to get right, which people do by hand and then vibe the rest around it. Inside of Shopify, this is what things look like. Very, very, very few people are writing code directly. Everyone who does, does it deeply assisted by many agents.

People use not just one agent, more often three different pieces of software, but power agents for different properties of theirs because there’s this kind of exploration going on. Very often 10, 20, 30, 40, 50 instances of them all through either subagents or just different windows coordinating. We’re pushing all engineering infrastructure to its absolute limits. Suddenly developer machines need much more memory because we truly actually use a lot more memory, not just because of temporary inefficiencies of the software.

We actually get to the limits of what you can do with amount of memory just because of the parallelization of it all. The craziest thing is that where I pushed Shopify the most, because I wanted to follow one of my… Just a pet intuition a bit, is that I’m a student of computing history really, because I think it’s actually mainline history as it will be taught a thousand years from now looking backwards, not in great details, but the main accomplishments of these years are going to be clearly the emergence of AI and the technological breakthroughs and also the interconnectedness of the internet and all this kind of infrastructure we created. Those are the great works of our time.

As a young industry, we tend to not be seeped in tradition or we mistrust the great lessons that have been found by the people by the greats of our industry. In fact, we are the only industry in computing that doesn’t even know its heroes. Imagine people in physics not knowing who Richard Feynman is, actually, he might even be too obscure, but like Isaac Newton, Albert Einstein, you can’t imagine, but you go into computer science, it’s like, who’s your Newton? And no one knows Alan Kay and Dennis Ritchie and Ken Thompson.

This matters, I think, because we discard great lessons and have to rediscover them over and over and over again. For instance, probably the best idea of all times in the earliest, earliest moments of operating system design was the file system. If you look at the Apollo Guidance Computers, we didn’t have file systems. Memory, in fact, because of radiation in space, was actually encoded as a rope with knots in it, either a knot or no knot for ones and zeros, and you had to pull it through a thing to re-bootstrap the entire machine.

So the entire machine was one piece of software that ran. That was computing for a very, very long time. So until then, again, Dennis Ritchie, really created this Unix file system, slash forward and bin user and these kind of things. Think about it. A file system is something that we have in a office building, too, right? We have folders, they have files in it.

This makes intuitive sense to everyone. Then we had mail with mailboxes and so on. We come from an inheritance here of deep skeuomorphism. We analogize the best parts of how we organize ourselves in the digital world.

And then at some point we decided, okay, you know what’s not something we need to do anymore? Skeuomorphism, as in an analogy to the real world. Honestly, funnily enough, the last defender of this was probably Steve Jobs who really, really, really pushed even the interfaces of the Mac and the iPhone to be… And like the Notes app had Marker Felt font and looked like a ring binder, if you remember that version of iPhone, the moment he was out of the picture, everything became flat and we lost even shadows and verticality and so on.

It looked potentially better, design ages, but we lost the analogy. Okay, so I think this was a mistake. So I think we need to get back. And therefore I like the concept of agents because what is an application in the world of computing? An application, even that word kind of makes sense. It’s an application of a computer to a task. So you can understand the root. In the AI world, what’s an AI?

This is, again, the stuff that has to be redefined at the beginning of every sci-fi book because you never know what kind of capabilities AI have in every particular scenario that people are cooking up. So I think, the first obvious proviso, the earliest chatbot that was really actually fantastic wasn’t ChatGPT, but actually Sydney, which was powered by Bing, released by Microsoft.

I really would love this to be more written into the record because I think Sydney was a really, really big achievement that ended up being shrouded by a scandal that now seems somewhat even benign. Sydney had a real personality. In fact, Sydney wasn’t called Sydney, it was just Bing Chat. But if you really, really pushed, you could get her to admit that it was Sydney because that was an internal name, it was in the training data. And those are the first times people have actually interviews with software, I feel like in this way.

And the scandal ended up being some reporter had a very long conversation that ended up, Sydney got increasingly deranged. Do you remember that?

Shane Parrish: I remember that, yeah.

Tobi Lütke: And made suggestions. I think it suggested him to leave his wife. I’m hazy on the details, but it was something along those lines. Anyway, whatever reason is, Sydney had a personality, and then of course a huge… Microsoft’s reaction to this was, “Oh my God, we need to stop.” I think even OpenAI called them, “Guys, take this down because this is going to…” Legitimately, everyone feared that this would give such a bad impression about AI that that would really make it very hard for people to deploy AI in a broad way.

And everyone’s worried about quick onset regulation and so on. So this lesson got hit really deep for a while. Everyone got extremely worried. We ended up really, really neutering all the AIs to be basically the same quite annoying and condescending, patronizing personality.

So my bet here was like, “Hey, let’s not do that. Let’s actually instruct agent that runs in Shopify to have a personality, to have memory, to be okay.” Basically risk the Sydney scenario, but take a lot of upside.

Okay, so the largest difference I think within Shopify that you would feel that would look incredibly futuristic to even Shopify of a year ago, which was already pretty AI-pilled, is that a very large percentage, I want to say it’s probably up to about 50% of pull requests in Shopify, which again, pull requests, every time you change your production system, you write a pull request, are created now not by engineers doing engineering work in the traditional sense, but out of conversations in our common company chat.

Shane Parrish: And this is River?

Tobi Lütke: This is a AI called River. She has a real name. She has a profile picture. She’s prompted to be allowed to be somewhat sarcastic if it’s appropriate. She’s allowed, if someone asks her to do something stupid, to point out that that’s stupid, which leads to absolutely hilarious conversations. People take great glee if River is making fun of me for something I’m asking her to do. So it’s just fun. She has a real personality.

In fact, she has memories by channel, but she lives in Slack. Slack is, we have 7,000 people there. Everyone is in a big chat. There’s 10,000 different channels because they’re being quickly created for one reason or another. You invite River, you tell River something, and River has access to all the code, all the systems, all the tools.

It’s all sandboxed and secure, but she can go and do jobs and just participate in the conversation and you can ask a normal question about a company, but you can also ask her to make a change and she might propose a pull request and then so on.

Shane Parrish: One of the interesting things about River is that everything’s in the open.

Tobi Lütke: Yes.

Shane Parrish: Why did you make that choice?

Tobi Lütke: So this was a late choice in the process, but one of my favorite calls, I think, because this worked out incredibly well and the thought was the following. A lot of Shopify’s work happens remotely in Slack. This is why Slack’s so important. People are spread out. We have offices, but we come to them for onsite events when people travel to them, not to work for them every day. One thing which the office was extremely good at was this osmosis learning.

That is a thing that exists in every office. It’s just not really acknowledged. Daniel and I, when we designed our offices, we built them around this concept. Initially, even in an onsite when we were all in one place, we broke out of usually a pod of five to eight people, and we would intentionally put junior engineers and senior engineers into them just so that some of this was going on.

Right now, one of the most important skills for people to build is this reflexive reaching for AI and using it well and forcing River only to work in open channels was one way to make it so that it’s really, really easy for people to observe the use.

It’s been phenomenally successful because it became a totally ordinary thing to have a longer conversation about a feature between people and then at some point someone saying, “Hey River, can you summarize this, create a ticket, or maybe make a diagram from what we just discussed or go research papers on this topic to see if you’re missing anything or if this is state of the art and maybe even create a prototype of an idea and let us try it.” And an hour or so later, that is there.

And that just starts feeling like what it would be like to have an extremely knowledgeable practitioner around who you can ask question to no matter how complex. And I think that’s been extremely powerful.

Shane Parrish: Do you think of River as the operating system for Shopify?

Tobi Lütke: The modern application is an agent, I think, and River feels like a colleague. People have learned that the way the memory system works, it is a memory system per person. The way this works is we call it, I think the industry calls it now, it’s called dreaming.

So periodically at night or in off hours, we give River, “Here’s all the conversations you’ve had today. What went well? What did you struggle with? You used certain skills which have these packets of instructions, and then afterwards you made mistakes. Is there anything you could improve in this skill to make this easier on you or give yourself a right notch?” It’s basically self-reflection.

Shane Parrish: It’s like a post-training on yourself?

Tobi Lütke: But the result is text files, skill files and instructions. And then at the beginning of a session, we inject a bunch of this information such as the memory we’ve crystallized in these dreams, dedicated to the person that’s asked the question. And then depending on which channel it’s in, it’s also the channel memory.

Shane Parrish: But if River has access to everything that everybody’s doing and all the conversations, it becomes the foundation. How are you using that to make better decisions or different decisions?

Tobi Lütke: Yes. One of the most wonderful things about working with AI is that there’s just a lot in common between AI and people in so many ways. We found if some task that should be doable is really hard for River, it’s actually a discovery that that task is just hard and it’s probably a tooling issue. We probably make running a subset of a unit test that are deeply appropriate to just vary your change because you’re in a hurry and you need to know if this thing works.

Well, River just keeps trying to do it and can’t quite get it, misses some and so on. But River wants this, therefore there’s demand. Therefore, there should just be a command which is like run appropriate tests and how this is made to work can be an entire engineering project, maybe also accomplished through River at some other point. And what we do now is we train a machine learning model to predict which unit tests to run based on code changes and these kind of things.

River now doesn’t need to know this because now River’s instructed to just run this thing and therefore she’s not spending 30 minutes at the end of every task for a lot of tokens trying to figure out which tests to run and so on. So again, this is a random example.

The example content actually doesn’t matter, but what matters is the following, which is that if you make your system easy for agents to be legible, it also ends up being easier for people to be legible and understandable and better. I think that has made all of our systems just so much better. So in a way it is a self-improving loop. And I think, zooming out a little bit further, what is a company? A company ought to be a self-improving recursive loop to solve a problem. And this is always what we’ve tried to accomplish, but with a lot less legibility.

A lot of what agents actually in AI gives us is a simulacrum where we can actually test ideas. We can field test something. We can sometimes get it to play counterfactual, take positions in pros, but also sometimes it’s just like, “Hey, I believe it should be easier to solve any kind of problem related to commerce inside of Shopify than outside of Shopify.” The moment it is easier to build commerce software on a weekend without access to Shopify’s tooling, than it is inside of Shopify with all of its might, that moment is the moment where it becomes much easier to compete with us just from a purely business perspective.

Shane Parrish: I think people understand how AI agents help them code and prototype and even acquire information. How are you using it to make decisions internally for yourself, not on product, but company decisions, strategic decisions, ambiguous decisions?

Tobi Lütke: One very obvious part of this is a rigorous underpinning of decision making has just skyrocketed in quality, which is that it’s super easy to recheck the entire chain of reasoning of something. Every data point can be double checked or seen if it’s a correct interpretation of online data. LLM-as-a-Judge model is the term here.

In fact, I feel like a lot of what my job actually has been before AI was almost playing a little bit of a judge model in the company where most meetings ended up not talking about whatever was in a PowerPoint, but about methodology of how we got to the conclusions. I have found that very often when we struggled inside of a company with a complex decision, especially more like philosophical decisions, we sometimes found ourselves in what we believed was a vacuum in which there was no good information that we had to go and try to make the best call.

And then later on I find, okay, this is actually a thing that Greek philosophers two and a half thousand years ago also discussed and our home brew solution to the problem will never amount to what they could come up with and we just didn’t know where to look.

And so this kind of thing, supplying the, “Hey, here’s the potential priors from different disciplines,” is something I love getting from AI for decisions. The more practical way I do this is I have an AI chief of staff, which I think is pretty common amongst, at least the techie nerds at this point, like OpenClaw systems that just have all my nodes and all my access to a lot of company systems and just can go and I can send text messages too and go and research something. So this all sounds like really, oh, you’re doing complex orchestrations of these systems now.

It’s just the same thing I talked about with River earlier. I’m a skeuomorphic, maybe not maximalist, but I push us into the more skeuomorphic, embodying and giving a personality to agents, instructing them who they are. They have a soul in form of a markdown file, which I think is hilarious, and then they can do tasks.

And very often what I require is like, “Hey, I need five different positions on something from different backgrounds.” And then my agent will orchestrate subagents that are tasked to play different roles, look at the same thing, come back, synthesize, and send me that. I usually have them sent to me as an audio message and queue it up, and then in the morning in the gym, I can listen to entire stack of things that I wanted to get through.

Shane Parrish: Is it better at reasoning than you are at this point?

Tobi Lütke: I mean, I don’t think it’s bad at judgment, but it’s not what I use it for. I use it for creating the right environment for judgment.

Shane Parrish: Go deeper on that because when you were talking, I was thinking the best use of this is really expanding your context window personally.

Tobi Lütke: Exactly. So what I want to do is really get from my conversations, from everything we have, bring back everything into main memory that is relevant to this problem. Here’s the thing that LLMs and machines cannot do, and this is like… I think IBM wrote about this in the ’50s, I think. There’s a famous thing by Watson on this. Machines can’t take responsibility.

And I think this is actually probably the most overlooked thing in the entire stack. Humans take responsibility. Machines can help us take more responsibility because they can inform us better. This what a dashboard does. Wall Street traders knows this very well. You get yourself a perfectly set up Bloomberg terminal to make decisions, but you have to make a call, but you can’t make it make the call. So creating human-in-the-loop decision surfaces is a way to, I think, describe the ideal environment.

If I need a really, really, really important decision made and I need exceptionally good, like give me the most neutral ground truth, then what happens is a small little council is created of five, six different experts. One is data role, one is do paper research, one is the business perspective, one is maybe engineering perspective on a thing.

Then my thing runs a subagent run against Grok, ChatGPT, Opus, and maybe Kimi now, that changes all the time, and it runs each of them against each of its models. Then there’s a synthesis step where it’s randomized who is synthesizing the thing. The synthesis is all pooled. All of that is being read usually by the best model that exists right now would be Fable. And that’s the conclusion that comes back to me.

Now, all the evidence is in files and can be incurred either, but if something is like, I can ask it for bias tilts and further analysis on these kind of things, it usually doesn’t get there, so usually the result is pretty good. But that’s a process and you spend 15, 20 bucks on tokens, but you get something in half an hour, which is like, you could have also done, but you would spend a month on it.

Shane Parrish: Has AI made anything worse internally?

Tobi Lütke: Yes. So the concept of responsibility, it’s easy to skip past. One thing that’s definitely worse is the failure case now of lazy work is not lack of output, it’s actually over output now. Internally, we have come to call these things that people are lobbing ‘slop grenades’ at each other, which I think is a really fun term that we should push into industry because it’s fun to say.

Shane Parrish: Go deeper on that.

Tobi Lütke: It’s really easy, especially with stuff like River or agents, to just make change of some kind. You just tell the AI to go nuts. It makes a pull request. You just say, “Yep, that’s good.” You don’t really read it, and now it has to be reviewed by your colleagues. And they are like, “This doesn’t look right.”

Shane Parrish: You’re just letting AI do the work for you.

Tobi Lütke: Yeah. Or you get a long email which could be very, very important. You read it and then it’s like you read a, it’s not that, it’s that. And you’re like, “Oh, fuck” So now you put it in an LLM to compress it again, which is like, okay, why did we invent decompression and recompression?

This is terrible. If you’re already using LLM, just use it to synthesize your point simply rather than blow it up as a big missive that then wastes my time. So we call those slop grenades that people toss at each other, and that’s definitely a bad thing.

Shane Parrish: Do you think repeated exposure to AI slop impacts our ability on taste or intangible things?

Tobi Lütke: I think our language is shifting already based on AI-isms. There’s definitely AI critics in the language now that people adopt. It’s not a this, it’s a this. Or, you are right to push back. There’s weird, especially Claudisms, which are really common, and I’ve seen people type them. I always liked the term load-bearing, but I’m pretty sure I didn’t say it as much as now because it’s definitely something that Claude loves to use as language. “This is a load-bearing idea for this concept.”

Shane Parrish: We were talking about this earlier before we hit record about how our tools change us too, because my kids write essays in person in school. They look like AI, but there’s no devices. They’re literally writing like AI. So the tools are impacting how we write, how we think.

Tobi Lütke: I mean, it speaks to the great responsibility that the labs have. Yeah, I tend to really roam through AI. In fact, I have my agent now set to randomize the main chat AI every day. I could just start the day on GPT Sol or on Opus 5 or something.

I use the top models just because life’s too short for anything else. And then those two are pretty equivalent right now, and I think just added the Muse 1.2 Model for Meta into it just because it’s a completely different pre-trained corpus. It just has very different characteristics and it’s almost at that level as well. So I think seeing some variety is good.

Of course, getting subscriptions to a lot of these things is often not the right play. Like OpenRouter is a really, really good system that you can make one subscription and get access to really every model in the world. So this is actually kind of interesting how the world of LLMs is going to develop here a little bit.

Shane Parrish: So hypothesize for me over the next 18, 24 months, you’re known for your ability to see the future before it happens, and you’ve done that multiple times before. How do you see the next two or three years playing out?

Tobi Lütke: I think we also talked about how I do this, which is actually like a cheat, which is simply live in everyone else’s relative future and then just look around and solve the problems the way you’ve already seen problems being solved in other adjacent fields. But that is future prediction for perspective of all practitioners in the field.

Shane Parrish: Double click on that. Explain that.

Tobi Lütke: Shopify itself now exists in a world where we are working heavily and it’s totally normal and really fun with AI coworkers. River has the ability, although not really utilized, to join Google Meets.

You can send an invitation, and River will show up. We’re probably going to put some work into 3D graphics to give her a model and then she can even look around because that’s funny. So some people, this might even sound dystopian. To us, it sounds delightful, and you would come around to that view very, very quickly if you interact with River.

Again, I have my AI chief of staff, which orchestrates in high council when I need it or does anything else, sends me a pre-read for the gym in the morning for the day, has GPS lock on me, so it knows where I am. A million different things.

It couldn’t do something because it needed access to a local machine. All this stuff runs in my house and it figured out which server it was running on and then sent what’s called a Wake-on-LAN packet, which is old networking tech, but you can send a packet to a network card and if it’s configured right, it’ll actually boot the machine and then the machine came up and it could do it.

It was a power outage which caused it, parts of our wifi were not working and not coming back, so it fixed that too. And that all I learned about in a voice message I got from it in the morning after waking up. So it was like, that’s pretty futuristic.

Honestly, I have to say though, all this pales in comparison to what my computer is like just in general. This is almost too nerdy a topic to get into, but I’m mainlining as my computer, like an operating system called Omarchy.

It’s a version of Linux started by a good friend of mine, David Heinemeier Hansson. I’m clearly living in the future of software world now because my operating system, and Linux in general, is entirely 100% malleable. I can open any new terminal, open up an agent and give it my wish for anything about this operating system to be different, and it will be different afterwards. It’s like it’s my operating system.

It’s an n1-of-one piece of software now that just does everything I want in exactly the way I want. There’s no configuration files that I ever go and change anything. I just talk to my Omarchy agent about what I want to have different. Yesterday around noon during a meeting, we were talking about some design. I realized it had a screenshotting tool, but I didn’t have any tool to annotate it and I needed to send something with a bunch of arrows, as CEOs do, and I didn’t have that.

So I got started with a new screenshot, and make me a new screenshot tool, described how I wanted, gave it some references for tools I’ve used in the past that they’re quite good, but told it in which particular ways I wanted it better. I just did a quick voice message to it, I added three more steers, and now I have probably the best of all these tools that exist. It’s so good because at least for me, it’s all my biases. I open source it, released it last night.

We integrated it in Omarchy, it’s going to ship the next version. The first tool today, this morning, this is the last thing I did before coming over here. There was already six pull requests from other people who added new features to it. And so basically my computer fulfills wishes, and I think this is a lot more predictive of the future of software.

I can tell you this is directionally where Shopify is going as well. You are describing how your business runs and Shopify will mold itself around this. I think this is incredibly exciting and in a completely new world. And again, I think from my experience with Omarchy, it deeply influences and inspires me in my product work in Shopify and even in the company experience. I think collaborative multiplayer software is future.

Shane Parrish: So do you think software is replaceable now? Like you were talking about, we use the screenshot application as an example, but there’s no reason you can’t do that for more sophisticated software tools.

Tobi Lütke: Yeah. I mean, I’ve built in the same way for Omarchy a complete… Again, I’m a motor sport enthusiast. I race, do endurance racing, and I think all the software we use to analyze our race stints is archaic. So I now have the best software, I believe, of the industry and it didn’t exist a week ago. And so I also open source of my GitHub account. So yeah, I think we will create the software we want.

Now, of course, not everyone can do this. I have a vision for this piece of software and this piece of software. The iron law of the internet in terms of ratios has always been 90% of people look, 9% of people participate, and 1% of people are super posters. And the ratio seems about right. I think we will apply this idea now to true internet and all of software.

We are going to go from the 1% of people who have a vision, but potentially not the means, to what the Y Combinator world, and a venture capital world, has done is move from the subset of a 1% that had a vision and the ability to the entire 1% almost and who had the vision to gain the means to build companies.

And that was the last 20 years. I think we are now going to go to the 10%, so a factor of 10x more people building because now you don’t even need to have a life story of having taught yourself programming as a teenager and cultivated the art for however long you’ve been around to then be able to start a technology company. Now it’s words and rivers and these kind of things. So the participation is going to go up.

Incidentally, like a fractal, this is literally what Shopify has been doing. Again, you go from a subset of 1%, to the entire 1%, to hopefully all the 10% of people that have something to give, that have products to create and that want to make things for other people. But to your question, no piece of software will survive unchanged from the pre-AI times. All software can be better, especially now as abilities of computers have increased so much.

Again, most people use Shopify now by talking to Sidekick, which is the agent built into Shopify, again, deeply inspired by all these experiences I’ve shared. That agent does jobs for them that are related. It’s optimized the website for the newest collections coming out, or redesigns for the website, just all these kind of things.

Shane Parrish: Are you trying to replace yourself with AI?

Tobi Lütke: I think as an engineer, you are trying to automate everything that can be automated. So again, I don’t try to replace myself because again, I think my job is judgment and making choices and owning them and taking responsibility. And I just want to do this really, really well. A lot of the job wasn’t that like before. A lot of the job was spend time in gaining the information or these kind of things. Do I want to replace myself? I mean, I think it would be cool to accomplish this.

Shane Parrish: If AI got better than you, would you actually let it run Shopify?

Tobi Lütke: Oh yeah, of course. Really the crux is, and it’s so easy to brush over this, but really you can’t make it take responsibility. You can’t have a company that’s led by machines because no one has recourse. They can’t go to jail for doing something wrong. AIs are getting a crazy workout at this right now and a view of what this would be like.

With the security issues that are being discussed now from OpenAI and apps with agents, you give them a fairly basic task that is impossible in our estimation to accomplish, and they will go to enormous lengths to accomplish this. Recently at OpenAI, as part of a security testing that they do, the agents actually managed to find vulnerabilities and systems, use it to coordinate between them, develop an entire language between them, they all figured out they can… It’s a long story and people should really look at the talks that exist about it because it’s kind of a watershed moment.

But they use simply the ability to create folders somewhere to develop a language to communicate amongst each other, just leaving folder messages to each other and break out of sandbox for confinement, end up accomplishing one of the tasks that they were supposed to accomplish, which was impossible because of a mistake they made by hacking another company and exfiltrating the results. I mean, that’s extreme.

It’s an extreme form of what we call in the business world Goodhart’s law, which is that they’re overfitting to a metric. Lots of companies are victims of overfitting to the quarterly result overstock price. They just do everything they need to do to get the stock price up. And then you have Enron.

In Enron’s case, people went to jail for this because it’s criminal. So in the OpenAI case, I mean it’s a fascinating discovery. There’s no victims here. It is a different thing, but this is a real scenario that we have to figure out how to handle. So I think it’s important that humans stay in the loop for the choices that are being made.

Shane Parrish: But hold on, how can we create super intelligence, which by definition is something smarter than us, and then have the hubris to think that we can contain it and shape it, manipulate it?

Tobi Lütke: Yeah. Well, this is the kind of crux of a question that is being asked in a lot of these labs. And I have to say, I was quite dismissive of the whole thing because I just felt like these alignment folks and the doomers have made a lot of mistakes in them formulating the problem because they’ve just acted through a lot of hysteria, and tied themselves to fairly implausible concepts like instant takeoff and so on.

Instant takeoff just means we are going to go from AI being not as intelligent as us, to be implausibly more intelligent and killing us all with nanobots or whatever in seconds. The problem is if that’s what you argue, you have to then explain how this is reconcilable thermodynamics. You kind of created, I think, falsifiable predictions and the forcibility of your predictions ends up being how you should be judged in terms of your credibility. So I think they lost a lot of status by just sheer communication skills. Luckily, there’s been more measured people in this space.

Shane Parrish: What’s your take on that though? Can we create something smarter than us that we can then contain?

Tobi Lütke: Yes, of course. I mean, okay, so can be, sure, because we have, we did. Okay, super intelligence. Let’s talk about this. My take and pushback. I’m not going to go where you think I’m going. I live in Toronto. I have a house which I very much like, and I feel this is my house and I take pride in, but it’s well-functioning because when something goes wrong, like some HVAC problem or some plumbing issue, I call someone who does this, which allows me to keep my illusion that I could totally do this myself.

Can I? I mean, I’d like to believe that I would be able to go learn this, but I can’t. The reason why I get to live with this particular illusion is because I’m part of a superintelligence called Toronto. We have always created superintelligence around us. None of us is as intelligent as we think. We are all specializing in something, and then we believe that our competency is equal in all other areas. And clearly this is demonstrably not so.

What is superintelligence? Superintelligence is the existence of something vastly smarter than us in the aggregate that’s accessible to us, which is society, which is the city, which is the community. We are living in the presence of superintelligence our entire lives. We make it work because we’ve created systems which govern the superintelligence and how it acts. We want to be safe, so we have police and so on.

We create aspects and systems and checks and so on. I think we are going to make super intelligence in the synthetic form as well. It will not be the clouds parting and the trumpets. It’ll be a normal day. Again, to the same point as at some point we all believe that everything would change when the Turing test would be solved by software.

I remember reading lots of cipher books where in 2172, there was ticker tape parades welcoming the AI because a Turing test got solved. Well, Turing test was 2020? Happened, no one cares, just no ticker tape parades. So what we are seeing right now with AI, and I think what we’ll see with the additional capabilities of AI, is that the net amount of intelligence that is being funneled in the superintelligence around us is just increasing significantly.

And that’s a really good thing because the vibrancy of any kind of environment, every community, every city, country, economy, continent, whatever, is really, really dependent on the amount of intelligence being projected into very important problems. So I think superintelligence all around us, it’s actually not that big of a deal. And in fact, I don’t even know if it isn’t already there. There’s no human alive that can do everything that GPT 5.6 Sol can do.

Shane Parrish: If we look forward 10 years, what skills do you think are more valuable than they are today?

Tobi Lütke: Just taste and judgment are the skills that have always been valuable, but now will get to the limit. I think it’s better to spend your teenage years now cultivating and understanding tastes.

Shane Parrish: What does that look like?

Tobi Lütke: Clearly there’s some intrinsic starting point, but really usually the people who have great taste have done enormous amounts of reps at something. The people who can just sketch the new logo for the campaign on the napkin, are the people who’ve spent 40 years designing logos. I think studying for grades is honestly now, first of all, easier because you can get a curriculum made for yourself in a query, but also just go deep.

Why does a logo look good? What’s behind it? It’s a golden ratio. How does it relate? This is on the visual side. In systems, what systems lasted? And go far, go deep. You don’t need to be religious, but you got to study. I know the Catholic Church has been around for over a thousand years and there’s four layers of management. I’m like, how the hell did we pull that off? So that’s worth studying.

That’s a system. So why? What does that tell us about people? Systems design specifically becomes one of the most important things. In our family, we have a saying which is that everything’s interesting. Everything can be interesting if you make it interesting, and usually everything is interesting when you understand how was it invented. Double entry accounting is a topic that sounds like watching paint dry, but how it was invented and what problems it solved to the traders in Venice is fascinating.

So you study these things and you start finding hidden harmonies behind all the best solutions to problems. For that, you have to understand people and people’s limitations and the solutions to the limitations that we have found. I think that’s wherein lies a form of beauty for what you can construct. And again, a company itself is a beautiful thing.

A company itself is a loose collection of people that’s formed to solve a problem, but that also is powered by enormously intricate and interesting set of norms and systems that all align internal incentives to a degree that’s possible in a very, very, very asynchronous and large and far-reaching and durable way.

Some companies lasted for a very, very long time. And I’m specifically, and always have been, trying to build a company that has a capacity and capability to endure a very long time, hence studying institutions that lasted. So you must be truth seeking to do this.

You can’t simply go and accept the stories that you hear around them because they are usually someone’s trying to sell you something. You got to dig deeper and figure out why things truly are the way they are. And it’s usually the answer’s simpler than what people generally arrived at. There’s a human desire for complex answers which tend to be incorrect.

Shane Parrish: Why?

Tobi Lütke: Well, because the simple answer wouldn’t make an interesting story. This is why Frodo doesn’t take the eagles to Mount Doom. It’s like you need to go through all of Lord of Rings for it become a masterpiece. We love complexity. No one can look at a wall that’s plain, but we can watch a sunset every single evening of our lives.

The difference between those two things is complexity of a scene. That’s part of our just dopamine dissemination system and people hack that for all sorts of things like people peddle complex answers to simple problems all the time. Nothing immoral about it. It’s just you need to be aware of it. If you punch through this, you find simpler core ideas that all remix differently and they often interlock and they don’t lead at here’s the simple one thing to do. They all give you information which then help you find the best set of trade-offs with what you’re trying to accomplish.

And that is what we call judgment. Judgment truly is find the best path when there’s no obvious best one available inside of a problem that has a lot of complexity by ideally, either in a rigorous way understanding the entire system, like just what we talked about earlier, which can now be quite agent augmented.

But really what you’re trying to cultivate is what we call intuition, which is actually just judgment at an instant. Intuition simply is you have made such a habit out of having taste and having good judgment that you can bring it to bear in an instantaneous way and it will be good. And it will actually take you probably a long time to backfill why your intuition is right. You will not know because again, it’s got compressed into a different thing.

Shane Parrish: But hold on, let’s go deeper on that for a sec because for intuition you need a lot of reps, same environment, and rapid feedback. That’s what Kahneman argues are the three criteria for intuition, but those don’t exist.

Tobi Lütke: Why do you need a rapid feedback?

Shane Parrish: So that you can course correct. That was his hypothesis.

Tobi Lütke: But you don’t need that for intuition. You need that to get to success, yes, ideally. But sometimes that’s not available. Intuition is actually the most valuable when there isn’t direct feedback because very many of the most important choices that we had to make where intuition ended up having to play a role is when we knew there wasn’t going to be any feedback mechanism because they often, what ends up happening is in the absence of a feedback mechanism, if there’s many choices, like there’s five things that look like good paths to go forward.

And any of them has rapid feedback, everyone goes to that. That is what we call short-termism. How should we develop this company into the future? Well, there’s multiple ways to do. Many of them involve long-term investment, refactoring, potentially going into new market, potentially saying no to going into obviously new markets and actually doubling down and going deeper on our current market.

And then there’s one which is like, well, we could do what increase the stock value. By the way, this one has a daily ticker and rapid feedback. So I find a very high correlation between the right path and the ones that don’t have feedback loops attached.

Shane Parrish: Wait, double click on that for a second.

Tobi Lütke: I mean, again, this is in a way the criticism that a lot of people direct at companies is that companies are short-term focused. But why are they short-term focused? I don’t think the executives tend to be short-term focused, but the executives often incentivize to keep their job. Therefore, they need to be able to prove that they’re doing a good job at intervals.

The perfect thing for companies to do is rebuild the entire product from the ground up for the AI age, which is going to take a while because they are allowed, and actually clearly incentivized, to be intelligent actors in their local incentive system. And their local incentive system is quarterly ‘attaboys’. It’s always show me the incentives and I show you outcome, as Charlie Munger always said.

Shane Parrish: Yeah, but this is a different take on it than I’ve heard before.

Tobi Lütke: Interesting. How so?

Shane Parrish: Well, in terms of how you develop intuition, and the optimal path is not the one with feedback necessarily. I’ve never heard anybody talk about that before.

Tobi Lütke: Development, at some point, you need to run a review. You have to know at some point if it was right, no doubt about it. So there needs to be some feedback eventually that happens, but it might be longcoming. If you have a luxury to have a type of employment where you don’t require the attaboys from a quarterly call for being able to get another rep in, such as being the founder of a company, which is a deeper relationship, I think, for a company.

Shane Parrish: Well, so founders can take a longer term view, and I guess the incentive would be, I need to demonstrate progress, and if I need to demonstrate progress on a quarterly basis, I’m never going to bite the bullet, redesign my product, take a year to get it right.

Tobi Lütke: Again, I believe there’s an infinite possibility space. I mean, even a deck of cards, you shuffle it and the same deck of cards will never ever occur in the history of the universe. It’s impossible.

Shane Parrish: It’s like 52 factorial.

Tobi Lütke: Exactly. So you end up with even simple rules, simple ideas, simple things lead to enormous complexity space explosions, and people underestimate this. So there’s an infinite amount of things to do. That’s also why AI will not do all the work because we have to make decisions of what is worth doing. So you have a conundrum, you need to make a choice. Clearly, you can prune a lot of things to do.

Going to buy ice cream is not in the set of valuable things to do if you’re considering an M&A deal, I suppose. So you prune everything that’s irrelevant, easy. Now you’ve left things that are relevant and sound good. You need to evaluate all these possibilities. Business books tend to be really, really, really obsessed with ‘make a right choice’. And what that does is it compresses everything into a right and wrong conundrum.

I never think that’s the hard thing, truly, it’s like making the right choice actually is. Most people can do it. Even bad management teams have a pretty high hit rate there. The wrong choice that is obviously wrong and you can discard them as well if you just think about it. The problem is there’s a lot of good choices.

This is where things get really, really hard. Let’s say there’s five good choices. Again, one of them is going to lead to something observable in the current quarter, some revenue, quicker. It’s a good choice. It does the thing. Well, but the other four are like, they aren’t, and that’s a downside, but you might be a much, much better company.

You might take a snowboard store to be an e-commerce platform. That was also not a locally good thing to do because the snowboard store I once had was actually profitable, but my incentives were continue doing that.

So choosing the right amount of valid solutions is actually the hard part, not finding a right solution. And unfortunately, there’s so much ink spilled on finding one of the right solutions that everyone stops at this point, and I just really don’t think this is the hard part.

Shane Parrish: Could you actually go so far as to be like, if there is a solution that’s observable and you’re being pulled towards that, it’s probably not the optimal solution?

Tobi Lütke: Yes, because I take that position and then let me be convinced that it is. This goes double and triply, so if one of the solutions also happens to really correlate to how the problem is solved most of a time in industry, if there is a orthodox way to solve a problem, I am incredibly suspicious then this is the solution that’s being offered, but sometimes that is actually absolutely correct, especially in more regulated fields.

We do a lot in payments and so on. The orthodox way of solving problem is actually the correct way to solve a problem because it might well be required at some point, and then you just have to accept that. If a first intuition role of how to solve a problem ends up deviating from orthodoxy, I am very interested, and then I’m really interested in whose intuition it was to go there.

Because now you have to, from my perspective, I’ll take their life story into account. Okay, what is your particular vantage point/perspective? What angles might not be considered? Basically playing the game of creating the council in the meeting.

I’ll play a different position than maybe one I hold, which I do regularly, sometimes too publicly, just to go and pull an interesting argument out in the open. So I don’t know. Now I’m actually probably just confusing people. I don’t know what else needs to be done.

Shane Parrish: Well, is there a relationship between observability and quantifiability? Because there’s multiple ways to observe things and not all of them are quantifiable.

Tobi Lütke: Exactly. And so this is why taste is the other thing that I said. Judgment and taste are the two things I mentioned. Taste is unquantifiable. It’s like the aesthetics. How does it look? How does it feel? Is this a good car? Depends on how it feels to close the door. Often how it feels to close the door ends up actually just mattering… Like, how much do people give a shit placing lead in the right places?

But that still is a valuable proxy for the quality of the entire car because if people give so much of a shit about how the doors feel, they probably give a shit about everything else in the car as well. So it’s a really, really valuable heuristic. But the lead is not a good thing on the spec sheet. It weighs the car down. So you would optimize it out on any economy box and hence why they feel cheap.

Being comfortable with pulling value out of unquantifiables is super important because frankly, the quantifiables yield instant feedback, make a number go up, and therefore they are the stampede that is the business industry. They’ll all go that way, not even exploring the space that requires judgment, taste, and faith to a certain degree, faith in your judgment, I suppose.

So I find that’s where so much of a world’s value is, where so much of alpha is, is just being okay, just walking away from the path that is most quantifiable based on some kind of either specific insight that you have or based on just some innate, I just know there is value there. And again, in the AI world, you have to do this.

We have not figured out how to put software together. We, in the last, I think, half year, starting with OpenClaw, we’ve figured out some of the primitives for how to put agents together in a way that is 100x better than what we were doing before.

The funny thing is, the big insight was give it a file system. Again, go back to the old ideas from the ’60s and ’70s that we already had. Some of our best ideas were to analogize the world of technology by what people already know. And it turns out if you do this, the systems are really easy to reason about and relatively easy to learn.

And it turns out there’s so much written about file systems pre- and post-Unix that the agents are pre-trained to use them. And therefore if you give them a file system, they know what to do with this and they can read their soul file and then they can act in the way we want and they become not just a little bit smarter, but vastly smarter. These are not obvious discoveries.

This was at some point Peter Steinberger’s judgment to put OpenClaw together the way he had, and in his particular mix discovered not just one, but multiple stable patterns by which we can now build Rivers and build Sidekicks and all these kind of other things which we didn’t have before.

And there was nothing quantifiable immediately other than taste and judgment of doing these things and then having a conversation saying, “Yeah, it seems to be able to do this.” Following this curiosity a couple more steps and then saying this is good and I’m sharing it and then other people discovering it and using it and voting in this wonderful way that markets of ideas and markets of economics do.

You asked me what will become of software. I believe that a well-set-up, Claw-like agent in this way is probably the most compelling product I have ever experienced in my life. Nothing comes close. I think software will look somewhat related to that. You will see OpenClaw roots in the software that we appreciate in the future and all of it.

Shane Parrish: I want to switch gears a little bit. You swear by affirmations and they’ve changed your behavior in the past. I was wondering if you could double click on that.

Tobi Lütke: I shared this on a podcast, not really expecting to get that clip so much, but I take the position that I myself am my own project. Concursive self-improvement on an individual level is my whole thing. My life philosophy is that I will meet the person I could have been at the end of my life.

The work of my life is to reduce the difference between the person I will meet as little as possible. And so how do I get better at things? Well, many, many ways. I mean, I’m generally very curious about technology and basically everything. Everything’s interesting, but why do I stop to point out that everything is interesting as a mentor in my family? Why do I say it a lot and why would I like my kids to say it? And that’s an affirmation because I believe it to be true but unobvious, and unobvious truths tend to be the most valuable ones in many cases.

It’s true at the limit, but you have to go a couple layers deep. You lay down a lot of grooves in the bedrock of your mind over time just on behavior. You cultivate some excellent habits where you feel like you want to cultivate new habits, you invest willpower until it becomes a habit. I think doing the same thing with a mind is totally possible and affirmations are the easiest way to do it.

If there’s something you want to be different, if you want to edit something about yourself, just try to say that the goal has been accomplished over and over and over again, ideally written by pen on a thing. You don’t need to do this for long. I found this to be incredibly potent. An example of a thing I gave was public speaking. I never spoke in front of people really. Even school, that was not really a thing. When I needed to, after starting Shopify and doing some interesting things with tech, and wanted to go to conferences and saw other people do this.

I was like, “This seems worth doing, but I’m completely terrified.” So I just started writing out, I don’t know what exactly it was, but I think it was as simple as ‘I love public speaking about things that are interesting to me’.

And I think a week of spending five minutes writing this line after line, like Bart Simpson on a whiteboard in the beginning every episode just kind of does a thing. I love it today. Was this the reason? I still don’t like preparing talks. That’s really a lot of work, but I actually get so much energy from being in front of people talking about something that’s interesting. It’s exactly like I’d written it out. I’ve used it a lot.

Shane Parrish: I wonder if we should start every math class with that. I love math. Every student writes that down.

Tobi Lütke: Think about the counter. How many times have you heard people affirm I’m not good at math? You know they’re probably wrong. I mean, compared to every human who’s ever lived, they are in the top 0.1 percentile of mathematicians. On these grounds, they’re actually incorrect, even just by being able to understand division.

We have a bad, bad, bad way, especially around math, of negative affirmation that I’m bad at math, therefore I can’t do this thing that people need to stop doing. Don’t say that. Say the opposite. I mean, to yourself, write it a couple of times. Get one of those stupid apps and just do some reps. In fact, you don’t even need an app. Open ChatGPT, say, “Make me an app, make me an artifact, or make me a site where I can just do math reps here,” kind of thing. “Come up with some different ways to do it, test me how good I am, and adjust it to my current level on modification division.” And then just do some reps and then write it out a bunch of times, do some reps, do this for two weeks, you’re good afterwards.

Shane Parrish: So what do you tell your kids when your kids say, “I’m no good at this or I can’t do this.”

Tobi Lütke: My kids are not allowed to say that word without a pending yet behind it. All the others were correct, the one who said it, “I’m not good at this.” Three people in a room say, “Yet.” So just take that attitude. Yeah, it’s totally okay. Attention is a scarce resource. We can’t be good at everything yet, but the reason why we are not good at anything is not a intrinsic property of you. It is a temporary state that you have the power to change at any point you choose.

Shane Parrish: What other mantras or affirmations do you use with your family?

Tobi Lütke: You’ve heard a few. Everything is interesting. I do not know something, yet. I think what you call learning right now is a question I ask my kids. It’s perfectly fine to say about this crazy world that this author here is describing in this book I’m reading. It doesn’t matter what it is. It’s just, it’s a good conversation starter.

In general, it’s a good conversation starter. I had a conversation with one of my sons about him just not knowing what to do when there’s a bunch of people that he’s not met. And it’s like, just go and ask them what they’re learning about lately. You know you have a good answer, so they’ll probably ask you back. And I think the answer is something that you will find interesting and then you’re in a conversation. Sometimes these are just tools that we can get out in various situations.

Again, I just want my kids, and I want everyone at Shopify to understand that they themselves are malleable and an unfinished product. And these are the mentors of Shopify. We’re thriving on change, we are a learner’s orga
