# How Harness, Loop & Graph Engineering Actually Work (Every AI failure is one of these three things)

source_url: https://www.youtube.com/watch?v=Np8UTsHnUV0
author: Johnny Nel | AI for Founders

---

# How Harness, Loop & Graph Engineering Actually Work (Every AI failure is one of these three things)

Most people building with AI agents have never once counted what their setup can actually reach — and the control room on my own machine proved it by reading a copy of itself out of the trash. Nobody's tooling warned me. Nothing you're running right now will tell you either.

## The Control Room That Read Itself Out of the Trash [00:00:00]

**Johnny Nel:** A control room on this machine was telling me what my agents were doing. And the run history in it was real, all the way down to the token counts. It was reading a copy of itself that I had dragged into the trash. And nothing you're running right now will tell you where it is reading from.

That control room is one of ours, and this machine runs agents against real work most weeks.

## What Actually Went Wrong [00:00:20]

**Johnny Nel:** What had gone wrong in there? The model was doing its job, and there was nothing wrong with the words I had typed at it, and the whole problem was where the thing was standing. And when I tell you something broke, that happened on this machine. And I will tell you which of the two you're getting.

Where the thing is standing is one of exactly three things that get decided every time an AI does a real job for you. And it is the one you can change today with no code and nobody's help.

## The Sentence That Tells You Which One Is Broken [00:00:42]

**Johnny Nel:** Can you tell which of the three has gone wrong on your setup right now? There is a sentence you can say out loud that tells you which of the three is broken. And for most people watching, the answer is —

## Meet Johnny Nel [00:00:52]

**Johnny Nel:** Hey, I'm Johnny Nel. I spent years building businesses the old hard way, managing teams, scaling operations, and doing everything manually. Today, everything I built, from automations and no-code infrastructures to fully AI SaaS products, has AI helping in one way or another.

First of all, let me quickly show you this. In South Africa, we call this a braai. I built with AI tools that in my opinion anyone can learn to use. My mission is simple: to help creators, entrepreneurs, and business owners get clarity with AI. Let's build smarter together and enjoy this video.

## The Editing Tool That Had No Field for What I Needed [00:01:27]

**Johnny Nel:** The editing tool I use every week publishes an interface where the only thing you're allowed to hand it is a sentence in plain English, and there is no field for a frame or a track anywhere in the whole thing. So, I sat down and wrote better sentences. What I wanted was a graphic laid over the footage holding for said number of seconds, and I described that to it, what it should say and exactly where on the picture it had to go. And every time I got back something close and wrong in a slightly different way.

So, was I wording it badly? For a stretch of that week, that is exactly what I thought. And some of you are going to say this is just prompting with extra steps. There was one job in there where the wording genuinely was the problem. And once I described it the way the tool expected, it did the job properly.

But the graphic over the footage was never that kind of problem because what I was asking for had nowhere in the software to land. That field does not exist. And a field that does not exist cannot be talked into existing however carefully you word the request. So the whole visual layer came off that tool and onto something we build ourselves to draw the picture.

## What LangChain Calls "The Harness" [00:02:32]

**Johnny Nel:** That whole business has a name and I only ran into it afterwards. LangChain published a piece on the 10th of March 2026 written up by Vivek Trivedi. And their line is that a harness is every piece of code, configuration, and execution logic that isn't the model itself. Or as he puts it earlier on, if you're not the model, you're the harness.

## Count Your Doors [00:02:55]

**Johnny Nel:** So essentially, everything that is not the brain is the working conditions. And your working conditions decide what it can actually open and touch. Whatever you are running right now, take the model out of the picture and look hard at what is left around it. Because every one of those things is a choice somebody made once and never went back to.

And everything still connected to the model is a set of keys. And the question is which doors those keys open. Most people have never counted their doors and the permissions you handed over on day one are still hanging on the ring. And you might be thinking you would just use a different tool. That is a reasonable answer and it changes something real because a different tool can reach different things. So what you are changing is this first decision, which is the point.

## Why a Crowded Toolset Hurts You [00:03:41]

**Johnny Nel:** So guys, the way I look at it, you can fix a surprising amount of this in an afternoon. And it starts with counting what is switched on. The connectors, the integrations you added in March and forgot about. And then switching off everything you did not deliberately turn on for the job in front of you.

Why does that matter more than it sounds? A crowded tool set most probably makes it reach for the wrong tool. And the descriptions of the tools you never use get sent along on every single turn. Meaning every back and forth between you and the thing, whether you call them or not. And by the end of that afternoon, the list of what your setup can reach is a lot shorter. And everything still on it is there because you put it there on purpose.

## The Background Paragraph You Retype Every Morning [00:04:12]

**Johnny Nel:** Every morning, I opened the same chat and typed out the same few paragraphs of background before the thing could do anything useful for me. And guys, I know how that sounds. A grown man retyping the same paragraph before breakfast. But that is what the setup gave me. Because the conversation was the only memory in the building, and the conversation ended every night. Does any of that sound like your own Monday morning?

On a building site, the scaffolding you leave standing is still there when you come back. And whatever went into the van at 5:00 went home with the van. Your chat window is the van, and nothing you put in it is standing on site tomorrow. And I know a few of you have already made this exact fix and called it memory. And there's a whole video of mine on that one. So yes, it is the same problem. And I put the fix in that video and then went on retyping my background every morning anyway.

## What Anthropic Found When They Tried Compaction [00:04:32]

**Johnny Nel:** Anthropic wrote up what happened when they tried this internally on the 26th of November, 2025. They were building a clone of their own product with over 200 features in it, session after session. And what did they try first? They tried squeezing the conversation smaller, which is the obvious move and the one you would reach for. And I'll give you their sentence about it word for word. However, compaction isn't sufficient. That is the sentence printed on their own page.

## The Text File That Fixed It [00:05:20]

**Johnny Nel:** What worked instead was basically a text file. The first session writes down what it did and what is still open. And every session after that reads the file before it starts and updates it before it stops. Mine has a heading for what got done and a heading for what is still left. And then blocked sits on its own line underneath. And blocked is the one that saves you the most time because it stops tomorrow's run from walking into the wall you hit today.

Now, that is one internal experiment on one demo build and the write-up says the demo was tuned for one kind of work. So, I'm not handing it to you as a law. In my opinion, writing that file is the best hour you will spend on any of this and it is not a hole you are plugging. It is the first piece of your setup that belongs to you rather than to whatever window you happen to open that morning.

## Write Four Lines Tonight [00:05:54]

**Johnny Nel:** So, write four lines in it tonight and tomorrow point the thing at the file instead of typing your background out from scratch. And the morning after that, you're opening something that already knows where you got to, which means you start your day on the work rather than on the briefing.

## Your Laptop Has Been Doing This for Decades [00:06:26]

**Johnny Nel:** There is a part of the laptop in front of you whose entire job is deciding which programs are allowed to open which files and it has been doing that job for decades without anybody calling it a harness. So, most of what I have described to you is that same job with new words on it. And that is a reason to be less nervous about it. The shape of the problem is one your own machine has been handling since before you bought it.

## The Part Made of Language Is the New Bit [00:07:00]

**Johnny Nel:** Which part of this is genuinely new? The part made of language is the new bit because nothing inside your laptop ever had to write the instructions a thing reads before it starts.

## Where the Lines Between the Three Sit [00:07:20]

**Johnny Nel:** The people publishing on this do not agree where the lines between these three sit and one of them folds the ordering work into the first decision entirely. So, the way I see it, the split I'm handing you is mine and it is not anybody's standard. I've put most of my time here on that first decision because that is where most of what goes wrong for you happens. And which one of these three has no older version of itself anywhere?

## The Vault Audit: Count What Your Setup Can Reach [00:07:41]

**Johnny Nel:** Now, everything I have just handed you is written down properly inside the AI Founder's Vault. There's a 20-minute audit waiting in there that you can run this afternoon and you come out of it holding a written count of what your setup can actually reach. The community's in there running the same audit on their own setups, and the link is down in the description below.

## The Second Decision: How It Knows It's Finished [00:07:52]

**Johnny Nel:** All right, so let's get into the second of these three, which is how anything you set running is supposed to know that it is finished. When a render finishes on this machine, the program that did it hands back a number. It tells you whether the job worked without a single person having to look at it. That number was computed by the thing doing the work, which is why you can act on it while you are asleep.

An AI job stops when the AI says it is done. And the fair pushback is that you asked it and it told you it was done, which is true. What you did was asked the same source for a second opinion on itself. So, the AI is now the thing that decides its own ending, and the AI is the part that can be wrong, which is why this is the only one of the three with nothing older behind it.

## Why No Operating System Ever Had This Problem [00:08:20]

**Johnny Nel:** No operating system has ever had to decide whether a piece of work is good enough to be called finished, because that is a judgment somebody has to make. Everything before this computed its own ending out of the work it had just done. And an AI hands you a claim instead, which is a different kind of thing to trust.

What does that cost you in practice? Your finish line is now something you build from the outside. It has to be cheap enough for you to check, and plain enough that somebody else could check it without asking you what you meant.

So, what does the piece of software that runs the job do when nobody can tell whether it is finished? OpenAI's own agent runner does not sit there waiting for a real ending. It ships with a cap on how many turns a single run gets. And when a run goes past that cap, the runner raises an error and stops. The runner stops at 10. That is the default in their own source code, and a cap like that is what you end up with when the ending cannot be worked out from the inside.

## The Done Test [00:08:55]

**Johnny Nel:** So, essentially, what I write now before a run starts is what I call a done test. It's a short written list of conditions that have to be true when the thing comes back. I'd say the rule that makes it work sounds like a technicality at first, but it is the part that matters. Every condition on it has to be checkable by somebody who is not in the conversation.

## A Test vs. a Wish [00:09:32]

**Johnny Nel:** And how do you tell a test from a wish? Say your condition is that it should read professionally. That is a wish because the only thing that can grade it is the thing that wrote it. Now, say your condition is that every figure in the draft appears on the source sheet. That is a test because you can settle it in a minute.

When I was mixing tracks a mix was never finished when I thought it was finished. It was finished when somebody who had not been in the room could play it through once and not stop me. Your done test is the same thing with different equipment.

The standing rule on this machine now is that anything which starts a render sets a check running in the same turn. And that check has to report back when the job dies, not only when it finishes.

## The Check That Waits Forever [00:10:12]

**Johnny Nel:** Because a check that only ever looks for finished will wait forever on a job that already failed. That is why the rule exists at all. The run had stopped, the check was still open, and there was nothing on the screen that would have told me the difference. You have lived this. You set the thing running and went to lunch, and you came back with no way of telling whether it was working or stuck.

## Stop Retrying — Look at Decision #1 [00:10:52]

**Johnny Nel:** Now, some of you guys will have been told to keep trying until it works, and I would look hard at what that is costing you. Every retry is another run you are paying for and another hour you do not get back. A retry only ever helps you when the failure was random. And if two attempts come back failing the same way, what that tells you is the problem lives in the first decision. So, you go and look at what it could reach.

So, before your next run, write those conditions down first, three lines on a sticky note. Each one has to be something a stranger could settle, not something only the thing that did the work could grade. Then let it go.

## The Third Decision: What Has to Happen Before What [00:11:12]

**Johnny Nel:** Microsoft's own documentation has a page about fixing the order your steps run in, and they call that feature graph. The wording is use graph when you need strict control over the order in which agents act or when different outcomes must lead to different next steps. And the same page marks that feature experimental, with its behavior subject to change. So, the warning is printed next to what they recommend. Strict is their word, not mine.

So, this last one is about what has to happen before what, and where I have drawn it, that ordering work falls inside the first decision, and stops mattering the moment nothing later in your run reads what came before it. That is the error test I walked you through last week. And it's linked underneath.

## When Not to Build a Graph [00:11:42]

**Johnny Nel:** When is it worth drawing one of these? If your process still changes every couple of weeks, I would highly advise you build nothing this week, because a diagram freezes a process you are still learning, and that process will most probably have changed before the month is out.

## The Green Tick That Checked Nothing [00:12:15]

**Johnny Nel:** There is a green tick somewhere in your week that you have looked at and gone straight past, and I have one of my own. From a small program on this machine, whose only job is to check that the promises I made to myself landed in the finished writing. One of them was that every date I give you comes off the company's own page. So, one afternoon, I pointed it at a page of those promises, and the report came back saying nothing was missing, which is exactly the sentence you want to see.

So, why did it say nothing was missing? Nothing was checked. The promises were laid out on that page in a shape the program could not read, and it printed a clean report off the back of zero checks. And a tick on your own screen tells you a check ran, and it does not tell you whether the check read your list.

And did it only fail in the one direction? No. It also reported a failure that was not real, because it took a rule that governs the middle of a piece of writing and applied it to the opening line.

Now, plenty of you have a checklist that does most of this, and I'm not going to pretend otherwise, but a checklist has never once told me it was ticked when nobody read it. And you can catch the one thing my program never will, which is the promise that never made it onto the list, because you're the one reading the draft, and you notice what is missing.

Has it happened to you yet? Where you told the thing to check its own work against a list and it came back saying everything checks out.

So, where does that afternoon land against the three decisions and where would yours land? The program could reach both the draft and the list and the list was in the one shape it could not read. What counted as finished should have been every promise traced back to a line in the draft and what came back was nothing missing. And the ordering answer was the easy one because a check that has read nothing has to stop your run before anybody even reads the results.

## Twenty-Eight Specifics Instead of a Tick [00:12:52]

**Johnny Nel:** Both of those are fixed now and the fix is the boring kind. It reads that page whichever way it is written and if it ever comes back having read nothing, it stops the whole run instead of printing a tick. So, the next time I pointed it at a finished draft, it read down 28 specifics and told me all 28 of them had survived into the writing. And 28 is the number I read now instead of the tick.

Take that control room from the start, the one reading itself out of the trash, and put it through with the first question. Could a competent person have done that job with what the thing was given? The answer is no because what it was given was a copy of itself in the wrong folder. So, you stop there and you do not carry on down the list. I personally believe most of what goes wrong for you stops right at that question.

And what happens when it does not? If the thing had everything it needed and still went wrong, the next thing you look at is whether anybody outside the conversation could have told it was finished. And only when both of those come back clean, does the order of the steps become worth changing.

## The Diagnostic Order: Cheapest and Most Common First [00:14:20]

**Johnny Nel:** Because the lines between these three are contested, what holds up is the order you go through them in. Cheapest and most common first.

## Pick One Thing This Week [00:15:00]

**Johnny Nel:** Now, maybe you are thinking you will sort all three of these out at once. Pick the one thing that annoyed you most this week and change only that because most probably the other two will still be waiting in a fortnight. Your context is your context guys, so none of this is a promise about your outcome.

The big takeaway for me was that I stopped guessing which part had gone wrong and started going through them in a fixed order. And the guessing was what used to eat my whole afternoon. For the build I'm running here, that order has done more for me than anything else I changed this month.

I can't say too much as of yet, but the next one is me pointing this at a job that touches a customer. An inquiry coming in and a quote going back out. And I'll tell you at the top of it which of these three the fix came out of. So, what is the one thing your AI still can't reach? Drop it down in the comments below and I'll be reading through them.

If you feel called to it, hit subscribe so you don't miss what's coming next. And if you want all of this written down, the working conditions kit is inside the AI Founder's Vault. The piece I would open first is the symptom router where you find the sentence you would say out loud about your own setup and it hands you back which of the three to look at. The link is down in the description below.

See you in the next one.
