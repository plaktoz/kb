---
title: Herdr Gives You Full Control Over Multiple AI Agents
channel: Owain Lewis
date: 2026-07-09
url: "https://www.youtube.com/watch?v=ZMehQM2sEjI"
cover: imgs/cover.jpg
description: "💬 Community: https://aiengineer.co 🔗 Free resources / skills: https://owainlewis.com/youtube"
language: en
---

# Herdr Gives You Full Control Over Multiple AI Agents

In this video Owain Lewis walks through Herdr, a terminal multiplexer built for AI developers, and shows the exact setup he uses to keep multiple coding agents organized instead of losing track of them across terminal tabs. He covers basic setup and key bindings, then gets into the real value: using AI agents to control Herdr itself, running a coordinator pattern where a single slash command spins up a new tab, branch, and worktree per ticket, and pushing that pattern further with milestones.

## Table of Contents
* [00:00:00] Intro
* [00:00:43] Connecting to Herdr and the UI
* [00:01:41] Key bindings: splitting and navigating panes
* [00:03:41] Herdr's agent skill and guide
* [00:04:14] Using AI agents to control Herdr's config
* [00:04:50] Coordinator pattern: /ticket workflow (first ticket)
* [00:05:49] Running a second ticket in parallel
* [00:07:00] Pull request opened
* [00:07:31] Bigger task demo: adding Gemini support with Neo
* [00:08:43] Milestones: pushing the coordinator pattern further
* [00:09:20] Where to get the ticket command
* [00:10:09] Neo finishes, reviewing the Gemini provider PR
* [00:10:46] Why Herdr fits this workflow
* [00:11:23] Outro

![cover](imgs/cover.jpg)


## Intro [00:00:00]

**Owain Lewis:** Herder is a new terminal multiplexer that AI developers can use to stay organized when working with AI coding agents. If you're anything like me, you probably struggle to stay organized when you have many different tasks and agents running on different things at the same time, potentially over long-running sessions. [00:00:00 → 00:00:13]

A terminal multiplexer is one solution to this problem. There are a bunch of different options available to you, like T-Max, which has been around forever, and also CMUX. But Herder is the tool that I enjoy using most in my day-to-day workflow. [00:00:13 → 00:00:25]

In this video, I'm going to show you how to get Herder installed and set up. But more importantly, I'm going to show you some advanced techniques where you can use AI agents to control Herder itself. And these are really, really powerful ideas. I think you'll find this really valuable. All of the resources and the prompts that you need are going to be linked for free in the description below. So, let's get into it. [00:00:25 → 00:00:43]


## Connecting to Herdr and the UI [00:00:43]

**Owain Lewis:** Okay, so the first thing we're going to do is connect to Herder. So, you can type her and then you open up your previous session. If you want to escape back to the terminal, you can press the prefix key, which is control and b. And then if you press Q, you can go back to the main menu. And then when you type that again, you'll start back in your session, which is really useful. [00:00:43 → 00:01:02]

What you'll see in terms of the UI, you have different sections. You have the spaces over here. You have agents down here. You have your terminals here. And then the tabs at the top. So the way I use workspaces is just like each workspace is a project. So you can see here this is my first project, second project, third project I'm working on. [00:01:02 → 00:01:21]

And what's really nice about this terminal multiplexer in particular is you can use your mouse. This is kind of very unusual. You can just literally click around. Obviously, you can use key bindings as well. So, if you type the prefix key and then question mark, you can bring up all of the different key bindings that you have available to you. [00:01:21 → 00:01:38]


## Key bindings: splitting and navigating panes [00:01:41]

**Owain Lewis:** So, I'll quickly go through a couple of the useful key bindings that are worth knowing. So, the first one is splitting the window. So, you might want to have a — let's say we want to start a coding agent here. So, this is my own coding agent right now. And then I can split the window again. If I press prefix and v, we will split the window like this. And then if I want to split it again, I can type prefix and minus will split it this way. [00:01:39 → 00:01:59]

When you start up a different coding agent in one of these tabs, what you'll see here is that we get this agent registered here. You'll notice that this one didn't register cuz this is my own coding agent. It's not registered with her. But if you use something like claud code or even pi and you start those up, you'll see that it will be registered down here as an agent and then you can toggle between your agents. [00:01:59 → 00:02:24]

What's really nice about this is you can see when your agents are doing work and when they're stopped. So review the code. We can run a code review down here. And you can see here on the left we can see that the agent is now working. And once the agent has finished working, it should give you a notification. You'll hear like a bell sound in the terminal which tells you that the agent is done. And I can do the same thing over here. And I can do the same thing over here. So we've got three different agents reviewing the code. [00:02:24 → 00:02:49]

The other thing you can do is create a new tab. So the way you do that is press prefix and then C, which will create a new tab. And I'll show you how I'm using tabs in a second. In terms of navigation, you could obviously just click around like this. If you want to jump between these different windows, you can click on them. You can also use keyboard shortcuts as well. So you can type prefix and then you've got the H and the L keys. So, I can switch between these two different uh panes if I want to. [00:02:49 → 00:03:13]

If I don't want to use the mouse, you can also reorder stuff as well, which is useful to know. If you type prefix, shift, and then L, you can swap these around. If you want to just reorganize your windows on the fly using the keyboard, you can do that. The documentation is really good here, so I'm not going to spend a huge amount of time on other key bindings, but anything you want to figure out, you can just check out the documentation. It's really, really good. [00:03:13 → 00:03:36]


## Herdr's agent skill and guide [00:03:41]

**Owain Lewis:** And the other thing to know is that there's an agent skill file. So, I think this is something you might want to check out as well. So, one of the things I really love doing with this particular multiplexer is to use agents to control it. Either use this guide. So, you can give your agents this guide. So, if you open up this link, it will show you like this is a full guide that you could give to a coding agent on how to basically manage her itself. [00:03:36 → 00:04:01]

But you could also install this skill as well. So, let's go ahead and do that. Let's install this skill. and we're going to proceed and then get this installed. [00:04:01 → 00:04:10]


## Using AI agents to control Herdr's config [00:04:14]

**Owain Lewis:** This is going to be useful especially for some of the advanced stuff we're going to show in a sec. So, one of the interesting things you can do with Herder, which I really enjoy doing, is to use AI to control it. So, as I mentioned, there's a guide on using Herder. So we can ask our agent to say we can say read this guide and then we can say update my her configuration to use the rose pine theme and reload it. [00:04:10 → 00:04:36]

So we can actually use our AI agents to manage our configuration because we like to use agents. We might as well get them to do everything right. So this is going to read the herder guidance. Then it's going to read and update my configuration. And then finally it's going to reload her. [00:04:36 → 00:04:51]


## Coordinator pattern: /ticket workflow (first ticket) [00:04:50]

**Owain Lewis:** So what I'm going to show you now is my favorite use case for herder and my favorite pattern in general for working with coding agents. So we're going to start up claud code and I have a custom slash command called ticket. So if I type / I'm going to paste in a ticket number. This is a GitHub issue and then when I run this what's going to happen is claude code is going to orchestrate herder. We're going to create a new tab at the top for this ticket. We're going to create a new get branch, a new get work tree, and then this allows us to work on multiple different tasks at the same time in a really clean and organized way. [00:04:51 → 00:05:23]

So claude code is now going to basically use her. So it's creating a tab in her. And you can see here now we have this /166. So this is the issue number. And if we switch over into this tab, you should see that the now that the orchestrator is spinning up claude code. And what it should do is paste in the prompt that we need to run. So this is the orchestrator is creating all of this. And you can see here it's pasted in this text. [00:05:23 → 00:05:50]


## Running a second ticket in parallel [00:05:49]

**Owain Lewis:** So let's find another task to work on. We're going to work on this bug fix over here. So again, we're just going to jump back into the terminal. And what I'm going to do now, sorry, this is a bit difficult to do on camera. I'm going to go back to the coordinator. I'm going to run exactly the same workflow again. So just ticket number. [00:05:50 → 00:06:07]

What I love about this is it's really consistent. So you're basically systemizing your development process in a really repeatable way, which I think is a really powerful concept when you work with agents. You don't want to be prompting ad hoc or manually doing different things every time. You want to have a repeatable workflow wherever possible. [00:06:07 → 00:06:26]

So now we're going to be orchestrating another ticket. So what you should see is that 163 should be open as a new tab. So you can see here now we've created 163 and again it's started up claude code and it's pasted in the prompt. So now we can work on this second task at the same time. So you can see here we have different agents. We have an agent working on 166 and we have an agent working on 163. [00:06:26 → 00:06:48]

Again, this is really powerful. This just keeps scaling. You could work on five or six different tasks at the same time if you really wanted to. [00:06:48 → 00:06:55]


## Pull request opened [00:07:00]

**Owain Lewis:** So now you can see here we've opened a pull request. Again, all we did here was just paste in the ticket number. What I really love about this kind of approach to agentic coding is you're being really systematic. So, what you can see here now in the browser is that we just created this pull request to fix a bug in the documentation. You can see how easy and how clean and organized this all is. We have the pull requests. Now, we're running a bunch of checks. [00:06:55 → 00:07:18]

But again, all we're doing is orchestrating the work. We're just deciding what tickets and tasks to work on, handing them off to the coordinator, and then the coordinator is spinning up all of these different terminals, different tabs, managing the work, and it keeps you very clean and organized. [00:07:18 → 00:07:32]


## Bigger task demo: adding Gemini support with Neo [00:07:31]

**Owain Lewis:** I just want to try one more thing which I've never done before but I think this would be interesting to demo. So I've got a more complex task here which is to add Google Gemini support to my coding agent. So what I'm going to do or attempt to do which is going to be super interesting is see if we can use a different coding agent to implement this task. Use the Neo coding agent not claude code. Let's see if we can do this. I don't know if this will work. [00:07:32 → 00:07:56]

So we're going to say ticket paste in the ticket number and then we're saying to use the neocoding agent. What's really nice about Neo is it makes a plan. So you can see here this is a really complex task. So this is my coding agent. And what I like to do is basically break this work down. So this is a bigger task. So we're going to read the developer docs, implement the provider, add tests, run the various check commands, self-review the diff, commit the changes, and then push a branch for review. So this is a very systematic organized workflow, which is why I really like this coding agent myself. [00:07:56 → 00:08:26]


## Milestones: pushing the coordinator pattern further [00:08:43]

**Owain Lewis:** One technique I use a lot which is worth mentioning is to take the idea we just saw to an extreme. So we have instead of working on one task at a time what I found myself doing more and more for personal projects at least to kind of experiment with how far we can push things is to use uh essentially milestones and a milestone is a bunch of tasks or tickets that are related. [00:08:26 → 00:08:46]

So for example maybe this phase 2 is a good example where we have a bunch of different features. So we have three separate tasks or tickets. And what we could do with a coordinator pattern is taking it even further. You can literally just give the entire milestone to the coordinator and ask the coordinator to implement all of the tasks in separate tabs. Once it's done, it will do a check. It will merge all of the work and it will basically implement the entire milestone. [00:08:46 → 00:09:12]

This is taking things to an extreme and I don't necessarily recommend this for everything, but it's kind of interesting to see how far you can push these workflows. [00:09:12 → 00:09:21]


## Where to get the ticket command [00:09:20]

**Owain Lewis:** So, if you do want to get access to the commands that I was using for the demo, it's over here and you can get it for free. I'll link it in the description. If you scroll down to the hurder agent workflow project, all of the resources are here. So, inside the resources section, you'll find this command. And essentially, this is really simple. All we're doing here is basically saying take a GitHub issue end to end, create a work tree, implement test, open a pull request using its own herder tab. And we're just explaining the workflow to the agent. [00:09:21 → 00:09:51]

We're just saying to create the work tree, use the herder pain create. So we're just telling it how to use the herder CLI basically to implement this. So you're welcome to borrow this. I really like this pattern. This is one thing that would taken me away from codeex is being able to do this in the terminal. So definitely something that's worth trying out. [00:09:51 → 00:10:11]


## Neo finishes, reviewing the Gemini provider PR [00:10:09]

**Owain Lewis:** All right, looks like Neo is still going. This is a big task. This is implementing full Gemini provider support. So obviously this is a much bigger task than the previous ones which were just smaller bug fixes and uh documentation updates. So this is going to take a lot longer. All right. So Neo is now done. We've committed the change. We have the pull request. So we can go and check this one out as well. [00:10:09 → 00:10:31]

Okay. So the Gemini provider is now done. So in theory we have Google support with inside this coding agent. I would want to be testing this. I would do a lot more review because this is obviously a much bigger task. And so typically with tasks this big, I would probably want to stay more in the loop than I would with a bug fix or something like that. [00:10:31 → 00:10:47]


## Why Herdr fits this workflow [00:10:46]

**Owain Lewis:** Herder is a really great tool. It's designed agent first. It looks incredible, very easy to use, very easy to set up, and it will just make you more productive as a developer. Most of my day-to-day workflow right now is using codec, the application, because I find that's just a better interface to working on more complex software projects. [00:10:47 → 00:11:04]

I really moved away from using clawed code in the terminal because it was very difficult to stay organized. But with a tool like Herder, you can get a similar effect. If you want to use different coding agents, I definitely recommend trying out Herder. It was a really great tool and it's something I'm using all of the time in my own workflow. This has become my default way to work inside the terminal. [00:11:04 → 00:11:24]


## Outro [00:11:23]

**Owain Lewis:** Hope you enjoyed the video. If you did, please remember to like and subscribe. It massively helps out the channel. If you have any requests for content or video ideas, leave them in the comments below and I'd be happy to take a look. Thank you again for watching and I'll see you in the next one. Take care. [00:11:24 → 00:11:38]
