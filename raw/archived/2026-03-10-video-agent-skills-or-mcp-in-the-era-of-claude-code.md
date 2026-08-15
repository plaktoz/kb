# Agent Skills or MCP in the era of Claude Code?
source_url: https://www.youtube.com/watch?v=pvxNcQTcIy4
author: Confluent Developer
---


Agentic AI and Claude Code are having a moment, thanks in no small part to agent skills. What does this mean for MCP? In his newest lightboard, Tim Berglund sorts it out. Along the way, he recaps what's new in the MCP spec (streamable HTTP, OAuth 2.1, and the quiet decline of the Resource API), and he breaks down what skills are and where they overlap with MCP. The short answer: local coding agents can lean on skills, but agentic microservices still very much need MCP.




## Introduction [00:00:00]

**Tim Berglund:** Skills are everywhere right now, and that's led some people to say that they spell the end of MCP. Are they right? Well, maybe. But first, let's give MCP a fair shake and take a look at what's developed in the world of MCP since the time of my last video, which you can watch here if you're interested.


## What is MCP? (quick overview) [00:00:17]

**Tim Berglund:** All right, a quick refresher on what MCP is. The idea is that you have an agent, and this could be running on someone's laptop, this could be a microservice running somewhere in the cloud, and your users, whoever they are, are going to submit prompts to that agent.

That agent is then going to call the model of your choice, a large language model, to figure out what to do with that prompt. Now, two problems. First of all, this poor LLM, as we know, only knows what it's read on the internet. Doesn't know anything about your support tickets, your wiki pages, your Google Docs, everything inside your company. How could it? That wouldn't make any sense. Also, it can't do anything. All it can do is give you text back.

But we would like that agent to be able to take action, to cause effects out there in the world. So we call those things tools and resources, whatever those documents are inside the company. The ways that you might get at those things, who knows what those APIs are, right? They could be just about anything.

So MCP, the MCP server, is a piece of infrastructure that stands in the way here, implements the API to call the tools, knows how to get at those resources, and provides a standardized interface to the agent, and even advertises its capabilities to the agent. So it's this pluggable thing. You point the agent at the MCP server, and it just learns how to do all these things. Very, very powerful. And it's working very well.


## What has changed in MCP recently [00:01:45]

**Tim Berglund:** What has changed in, say, the last nine or 12 months? Hardly anyone is using resources. And take a look around. Go find some MCP servers out in the wild, whether they're cloud resources or open source things. You can run locally, whatever they are. Look at the documentation, and tell me if you see a lot of actual use of the resource API.

What people have discovered is you can get this job done with the tools API. A resource query can be a tool call, can be like a method call, right? You pass in some parameters, you get some stuff back. Really no consequence to this. It's just kind of an interesting observation about how hard it is to create APIs. Things don't always work out the way you think, and the community has just taken the solution that it likes. So that's a thing.

There's also support for streamable HTTP. At the time of my last video, we just had support for server sent events, and that was a little frustrating to some people, a little bit harder to work out from a networking perspective if this MCP server isn't running locally and is running in the cloud, that can be a pain. So streamable HTTP, just from an infrastructure and networking standpoint, a little cleaner, easier to deploy, big win there.

There is also support for OAuth 2.1. Now, authentication was an early sore spot in the first version of the spec, for sure. So if you had some kind of secrets in here that the MCP server needed to know, those needed to be secrets that the server knew, right? They needed to be in an environment variable or however else you might wanna do secret management here to be able to authenticate itself to these backend resources.

Might be okay, depending on what you're doing, but like, what if this is trying to get you access to GitHub, you'd rather just the user on the front end be able to have the normal OAuth experience with the pop-up that says, this is trying to get at your GitHub account and it can see your profile and file issues and authorize and you go from there, right?

So this is designed around that experience where this agent is running locally. And now I can have one server in the cloud that lets me OAuth against whatever it is on the backend. So great solution for that use case with the locally running agent. And that's been the majority report by far. Certainly if you're a developer, you probably have experience running Claude Code on your laptop, you get that pop-up, it's great.

If this is an agentic microservice running headlessly somewhere, that OAuth solution doesn't work so well. So there's promise of better solutions down the road here to support the microservice case that I think we're gonna be seeing more of. But in any case, these are some of the updates we've seen in the last, say, nine months that are great things.


## What are skills? (quick overview) [00:04:22]

**Tim Berglund:** Now, do skills replace MCP? Ultimately, no, but there is some overlap. People aren't crazy for asking this question. And to be able to see what that tension is, first, if you're new to skills, I wanna give you some idea of what they're all about.

So fundamentally, a skill is a markdown file. It's a text file that lives in a directory somewhere where your agent can see it. And that markdown file contains instructions for the model. It's just like an extended prompt that contains specialized procedures and advice and conditions for doing something, like helping me find a job, helping me landscape my house, editing an Excel file, something that maybe natively the LLM might be able to take a crack at, but wouldn't be as good at as we like it to be, we get to encode that as good at stuff in the skill.

And there are other things, there can be just arbitrary directories under the skill that the root skill.md file references. So I could have a directory of resources. I could have a directory of scripts. Those can be bash scripts, they can be Python scripts. They can be some sort of executable script to go do something out in the world.

These resources are gonna tend to be static reference data. For my landscaping skill, they might be just a little bit more detail on climate and plant information, maybe some 3D models of plants so I can create a rendering. Things, some of that might've been in the LLM's weights back there lurking in the back, but we're just kind of bringing it to the front.

The scripts might be things like, I mentioned editing Excel file. I could have some Python script uses an API to go access particular rows and cells and make changes in ways that would be tough for the model to do itself. So these are enhancements and these are just examples. I can have anything under there that I want.

And skills came to life as plugins for Claude Desktop and Claude Code. They are files, it's a directory tree. So I could distribute that on GitHub, we can put it in a repository, but I don't put a skill in the cloud to host it. That's just not a thing. It's files that go somewhere in the file system where the agent can see them.


## Where Skills and MCP overlap and diverge [00:06:35]

**Tim Berglund:** So how are skills and MCP not the same? They both can represent resources, but they're really very different things. Like I said, this tends to be static reference information. It might be stuff that's somewhere in the model weights, but we're really explicitly saying, look, this is important, we need you to know this.

Here over an MCP, resources tend to be more real-time data. It's customer data, it's tickets in my ticket tracking system. It's something coming in from a Kafka topic right now. It is in a sense more live and fresh, typically that you're gonna be able to access through an MCP resource, or as we said before, maybe a tool call that gets us at the resource, but it's all the same thing.

Scripts and tools, conceptually similar. And again, I understand why people are thinking these are the same thing, but this again, it has very much a focus on what's going on in my local file system on my laptop. That's tremendously important when we look at the kind of things Claude Code is capable of now and coding agents in general can do in a local environment, really, really big stuff.

But for changing states of affairs out there in the world, deploying a resource into the cloud, opening a GitHub issue, those are things more out there that require authentication to some network resource in the cloud, less local stuff on my machine. So there's that kind of difference in orientation.

Now, another point here, and this, I think where it gets really interesting, where you see actual overlap between these things, we might say we'll have a nice command line interface and a script that can call a CLI, and that CLI can deploy things to the cloud. And these CLIs have authentication solutions that work just fine. I can log-in to a cloud account, and then the CLI has a token, and it just does what it wants.

And so a script that calls a CLI can really start to look like the same kind of thing that you might use an MCP server for. So in the case of the local coding agent use case, which again is by far the most commonly encountered scenario that we're dealing with at the time of this recording, that substitution makes a lot of sense. I see why people are saying this.


## Why agentic microservices still need MCP [00:08:43]

**Tim Berglund:** But when we take our attention over here, not to a coding agent that I got from the foundation lab, but an agentic microservice that I wrote that needs to access tools, that needs to access resources, suddenly that script, that CLI, those skills, none of that stuff makes sense over here, right? I really still do need this standard interface that MCP provides for those agents I'm writing myself.

And even this is an evolving thing. There is at the time of this recording, a Python API that I can bring in as a dependency and use it to execute, access, implement skills in my own agent. So this kind of thing is gonna come from the coding agents into the agents we write, but I haven't seen a lot of that in the wild yet.

And I'm not sure where that's gonna go. It's another thing to keep your eye on.


## Looking ahead [00:09:35]

**Tim Berglund:** For now though, you definitely do need to know and use MCP. You definitely do need to know and use skills. This is without a doubt, the most rapidly evolving landscape I have seen in more than 30 years of software engineering. There's a lot to keep your eye on to see where it goes next. And hey, I will be there with you. Thanks.

