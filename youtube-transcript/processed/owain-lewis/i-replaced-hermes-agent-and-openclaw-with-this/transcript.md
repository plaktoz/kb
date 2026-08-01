---
title: I Replaced Hermes Agent And OpenClaw With This
channel: Owain Lewis
date: 2026-07-17
url: "https://www.youtube.com/watch?v=lmmgzIuWEbk"
cover: imgs/cover.jpg
description: "💬 Community: https://aiengineer.co FREE agent skills: https://aiengineer.co/start/"
language: en
---

# I Replaced Hermes Agent And OpenClaw With This

💬 Community: https://aiengineer.co FREE agent skills: https://aiengineer.co/start/

# Description

💬 Community: https://aiengineer.co
FREE agent skills: https://aiengineer.co/start/

I spent the past few months using Hermes Agent as my personal AI assistant. I liked the idea, but its automatic memory and skill creation often added stale facts, unnecessary complexity, and unreliable instructions.

In this video I break down how Hermes Agent and OpenClaw work, then show the simpler personal assistant I built using the coding agents I already trust.

Push is a small gateway that connects Telegram or iMessage to Codex, Claude Code, Codex, or Pi Agent. It lets me message my assistant from anywhere, run scheduled jobs, work with voice messages, and connect the agent to tools such as Todoist, Gmail, and GitHub. 

What you’ll learn:

- How the Hermes Agent architecture works
- Why automatic memory can confuse an assistant
- The problem with agents creating skills on the fly
- How Push routes messages to Codex or Claude Code
- How Telegram polling works without exposing inbound ports
- How I structure assistant context, scheduled jobs, and personality
- How my assistant reviews email, creates tasks, drafts replies, and researches topics
- Why I treat my task list as the control plane for delegated work

This is NOT an argument against Hermes Agent or OpenClaw. Both projects are incredible. I simply wanted a smaller, more opinionated system that works with my existing agents, connectors, and workspace.

🔗 Links
Push: https://github.com/owainlewis/push
Free agent resources and skills: https://aiengineer.co/start/
Community: https://aiengineer.co

#AIAgents #PersonalAI #Codex #ClaudeCode #AIEngineering #OpenClaw #HermesAgent

# Transcript

1
00:00:00,000 --> 00:00:02,000
Reviewed 120 [music]

2
00:00:02,000 --> 00:00:04,840
incoming emails from the past 24 hours.

3
00:00:04,840 --> 00:00:06,800
Created four Todoist [music] tasks in

4
00:00:06,800 --> 00:00:07,840
inbox.

5
00:00:07,840 --> 00:00:09,280
>> Can you list out the top three

6
00:00:09,280 --> 00:00:11,400
priorities I have to work on today?

7
00:00:11,400 --> 00:00:13,440
>> Based on where things stand, [music]

8
00:00:13,440 --> 00:00:15,680
here are your top three for today.

9
00:00:15,680 --> 00:00:17,080
>> There's a lot of hype online right now

10
00:00:17,080 --> 00:00:18,760
around personal AI assistants like

11
00:00:18,760 --> 00:00:21,000
Hermes Agent and [music] Open Claw, and

12
00:00:21,000 --> 00:00:22,480
it makes a lot of sense. You get an

13
00:00:22,480 --> 00:00:23,680
agent that you can message from your

14
00:00:23,680 --> 00:00:25,400
phone from anywhere that's able to do

15
00:00:25,400 --> 00:00:26,480
work [music] for you in the background

16
00:00:26,480 --> 00:00:27,800
and knows all about you and your

17
00:00:27,800 --> 00:00:29,880
personal projects. So, I've been running

18
00:00:29,880 --> 00:00:31,720
Hermes Agent for the [music] past few

19
00:00:31,720 --> 00:00:33,920
months as my personal AI assistant, and

20
00:00:33,920 --> 00:00:35,370
initially I loved it. I could message

21
00:00:35,370 --> 00:00:36,760
[music] it from my phone, ask it to do

22
00:00:36,760 --> 00:00:37,720
something, and let it work in the

23
00:00:37,720 --> 00:00:39,440
background without opening a terminal or

24
00:00:39,440 --> 00:00:40,680
sitting at my desk. [music]

25
00:00:40,680 --> 00:00:42,120
But, the longer I used it, I kept coming

26
00:00:42,120 --> 00:00:43,960
back to the same question. Why can't I

27
00:00:43,960 --> 00:00:45,640
just use my existing coding agents like

28
00:00:45,640 --> 00:00:47,815
Codex or Claude Code to act as an

29
00:00:47,815 --> 00:00:49,680
[music] assistant for me? In this video,

30
00:00:49,680 --> 00:00:50,360
I'm going to walk through the

31
00:00:50,360 --> 00:00:52,200
architecture of Hermes Agent, talk about

32
00:00:52,200 --> 00:00:53,640
what's good and what's bad, [music]

33
00:00:53,640 --> 00:00:55,080
and then show you why I ended up

34
00:00:55,080 --> 00:00:57,400
building something custom myself. All of

35
00:00:57,400 --> 00:00:58,640
the resources and everything you need

36
00:00:58,640 --> 00:00:59,680
for this video are going to be linked

37
00:00:59,680 --> 00:01:01,240
for free in the description below. So,

38
00:01:01,240 --> 00:01:02,680
let's get into it. So, the first thing

39
00:01:02,680 --> 00:01:04,280
to say is that I do actually like Hermes

40
00:01:04,280 --> 00:01:05,280
and Open Claw. I think they're

41
00:01:05,280 --> 00:01:06,800
incredible projects, and they've given

42
00:01:06,800 --> 00:01:08,400
us so many great ideas about how to

43
00:01:08,400 --> 00:01:09,800
build AI personal assistants. They've

44
00:01:09,800 --> 00:01:12,120
completely transformed the way we think

45
00:01:12,120 --> 00:01:14,360
about this category of AI assistant in

46
00:01:14,360 --> 00:01:16,000
general. But, what's happened over the

47
00:01:16,000 --> 00:01:17,240
last few months is that many of the

48
00:01:17,240 --> 00:01:19,000
features that made tools like Hermes and

49
00:01:19,000 --> 00:01:21,000
Open Claw attractive have largely been

50
00:01:21,000 --> 00:01:23,040
adopted by the bigger coding agents. So,

51
00:01:23,040 --> 00:01:24,640
for example, you can now message Claude

52
00:01:24,640 --> 00:01:26,120
Code from your phone, and the same thing

53
00:01:26,120 --> 00:01:28,200
with Codex. Hermes can remember things

54
00:01:28,200 --> 00:01:29,880
about you, but so can Claude Code, so

55
00:01:29,880 --> 00:01:33,240
can Codex, Claude Code, and Codex can do

56
00:01:33,240 --> 00:01:36,000
background cron tasks for you. So, the

57
00:01:36,000 --> 00:01:37,720
obvious question is really what is left

58
00:01:37,720 --> 00:01:40,200
that Hermes Agent and Open Claw give you

59
00:01:40,200 --> 00:01:42,080
that the existing coding agents don't.

60
00:01:42,080 --> 00:01:44,560
And the honest answer is not that much.

61
00:01:44,560 --> 00:01:46,280
So, you get a gateway, you get some

62
00:01:46,280 --> 00:01:49,440
self-improving ideas with inside. Hermes

63
00:01:49,440 --> 00:01:50,880
Agent in particular, it has a good

64
00:01:50,880 --> 00:01:52,440
memory system and the ability to

65
00:01:52,440 --> 00:01:54,920
self-learn, but I found those to be an

66
00:01:54,920 --> 00:01:56,720
overall negative thing generally, and

67
00:01:56,720 --> 00:01:58,880
I'll talk about why in a second.

68
00:01:58,880 --> 00:02:00,840
So, it's worth knowing how Hermes and

69
00:02:00,840 --> 00:02:02,560
Open Claw actually work. They're pretty

70
00:02:02,560 --> 00:02:04,720
simple under the covers. The main

71
00:02:04,720 --> 00:02:06,520
innovation with these products was the

72
00:02:06,520 --> 00:02:08,160
messaging gateway. So, a traditional

73
00:02:08,160 --> 00:02:10,960
coding agent can run on your computer,

74
00:02:10,960 --> 00:02:12,360
you send it a prompt, it will do some

75
00:02:12,360 --> 00:02:14,440
work and give you a response.

76
00:02:14,440 --> 00:02:15,760
But, what happened with Open Claw is

77
00:02:15,760 --> 00:02:17,600
they put a gateway in front. This allows

78
00:02:17,600 --> 00:02:19,840
you to have a messaging integration

79
00:02:19,840 --> 00:02:22,080
point. So, you can send messages to the

80
00:02:22,080 --> 00:02:25,520
gateway from Telegram, from email, SMS,

81
00:02:25,520 --> 00:02:27,280
whatever you want, you can send messages

82
00:02:27,280 --> 00:02:29,600
to your assistant. The gateway is always

83
00:02:29,600 --> 00:02:32,080
running, so it's running 24/7,

84
00:02:32,080 --> 00:02:33,680
which gives these these agents like the

85
00:02:33,680 --> 00:02:36,040
feeling of being always available.

86
00:02:36,040 --> 00:02:37,640
But, the gateway would then dispatch a

87
00:02:37,640 --> 00:02:40,360
request to an agent runtime, which would

88
00:02:40,360 --> 00:02:41,640
just do the work and then send a

89
00:02:41,640 --> 00:02:43,280
response back. There are some other

90
00:02:43,280 --> 00:02:44,600
really nice features of Open Claw and

91
00:02:44,600 --> 00:02:46,320
Hermes Agent, things like the ability to

92
00:02:46,320 --> 00:02:48,040
create scheduled tasks that can run in

93
00:02:48,040 --> 00:02:49,320
the background. These are essentially

94
00:02:49,320 --> 00:02:50,959
cron jobs, and again, you can now do

95
00:02:50,959 --> 00:02:53,280
these in Cloud Code and Code X as well.

96
00:02:53,280 --> 00:02:54,040
The other thing that's really

97
00:02:54,040 --> 00:02:56,040
interesting about Hermes Agent is the

98
00:02:56,040 --> 00:02:58,480
memory capability. I actually found this

99
00:02:58,480 --> 00:02:59,880
to be a negative, but one of the main

100
00:02:59,880 --> 00:03:01,920
features or promises of Hermes Agent is

101
00:03:01,920 --> 00:03:04,440
the ability to self-learn and improve

102
00:03:04,440 --> 00:03:06,360
over time, which is which is sensible if

103
00:03:06,360 --> 00:03:08,160
you're building an AI assistant, right?

104
00:03:08,160 --> 00:03:09,080
So, as you can see, this is the

105
00:03:09,080 --> 00:03:10,680
architecture of Hermes Agent. You have

106
00:03:10,680 --> 00:03:12,320
this gateway, so this is written in

107
00:03:12,320 --> 00:03:14,320
Python. You have this gateway server

108
00:03:14,320 --> 00:03:16,640
that accepts incoming message requests.

109
00:03:16,640 --> 00:03:18,360
It's worth saying that Hermes Agent can

110
00:03:18,360 --> 00:03:20,440
actually do polling as well. So, you

111
00:03:20,440 --> 00:03:22,760
don't have to expose any ports, which

112
00:03:22,760 --> 00:03:24,440
presents a security risk. You don't have

113
00:03:24,440 --> 00:03:27,200
to have in incoming traffic. The

114
00:03:27,200 --> 00:03:28,880
integrations, things like Telegram, can

115
00:03:28,880 --> 00:03:30,880
actually do long polling, which means

116
00:03:30,880 --> 00:03:32,560
the gateway can be polling Telegram for

117
00:03:32,560 --> 00:03:34,440
messages rather than allowing incoming

118
00:03:34,440 --> 00:03:36,280
connections, which is just a little bit

119
00:03:36,280 --> 00:03:38,880
more secure in general, in my opinion.

120
00:03:38,880 --> 00:03:40,480
And then, once the gateway gets a

121
00:03:40,480 --> 00:03:41,800
message, it will then send it to a

122
00:03:41,800 --> 00:03:44,040
coding agent, but generally, these are

123
00:03:44,040 --> 00:03:45,720
pretty much a commodity at this point in

124
00:03:45,720 --> 00:03:47,519
terms of what they can do. The other

125
00:03:47,519 --> 00:03:48,920
thing that's interesting about Hermes

126
00:03:48,920 --> 00:03:51,160
Agent is it has this session storage,

127
00:03:51,160 --> 00:03:52,720
which allows it to save all of the

128
00:03:52,720 --> 00:03:53,840
information. So, as you have a

129
00:03:53,840 --> 00:03:55,880
conversation with it, it will save that

130
00:03:55,880 --> 00:03:57,600
into an SQLite database, and you can do

131
00:03:57,600 --> 00:03:59,000
a full text search over your

132
00:03:59,000 --> 00:04:00,960
conversation history. Again, this is

133
00:04:00,960 --> 00:04:02,200
useful if you want to kind of search

134
00:04:02,200 --> 00:04:03,840
your past conversations, as you would

135
00:04:03,840 --> 00:04:06,000
expect for a personal assistant,

136
00:04:06,000 --> 00:04:07,040
basically.

137
00:04:07,040 --> 00:04:08,040
And then the other feature that really

138
00:04:08,040 --> 00:04:09,680
stands out for Hermes Agent is the

139
00:04:09,680 --> 00:04:11,520
persistent memory and the ability to

140
00:04:11,520 --> 00:04:13,520
self-learn. So, the memory system in

141
00:04:13,520 --> 00:04:16,519
Hermes Agent is relatively simple. You

142
00:04:16,519 --> 00:04:18,440
can extend it in multiple ways. There's

143
00:04:18,440 --> 00:04:19,880
lots of different integrations you can

144
00:04:19,880 --> 00:04:21,959
have. But, out of the box, it does

145
00:04:21,959 --> 00:04:24,080
something pretty simple. It will save

146
00:04:24,080 --> 00:04:26,280
facts about you to a memory.md file.

147
00:04:26,280 --> 00:04:27,880
There's nothing particularly complicated

148
00:04:27,880 --> 00:04:29,919
here. After the conversation or the turn

149
00:04:29,919 --> 00:04:32,040
is finished, the agent will then decide

150
00:04:32,040 --> 00:04:33,360
whether it's going to save anything

151
00:04:33,360 --> 00:04:36,280
useful into the memory.md file. Then,

152
00:04:36,280 --> 00:04:38,400
the memory.md file will get reloaded in

153
00:04:38,400 --> 00:04:40,440
the next conversation turn, and so the

154
00:04:40,440 --> 00:04:42,280
agent is able to then remember things

155
00:04:42,280 --> 00:04:43,600
about you. Because, if you think about

156
00:04:43,600 --> 00:04:45,600
it, LLMs and agents are stateless. They

157
00:04:45,600 --> 00:04:46,600
don't know anything about you. They

158
00:04:46,600 --> 00:04:48,440
don't remember things. And so, this

159
00:04:48,440 --> 00:04:50,400
allows your AI personal assistant to

160
00:04:50,400 --> 00:04:51,760
feel more personal, because it can

161
00:04:51,760 --> 00:04:53,760
remember stuff about you. So, this is a

162
00:04:53,760 --> 00:04:55,160
thing that people will often claim is

163
00:04:55,160 --> 00:04:56,680
really beneficial, but in reality, I

164
00:04:56,680 --> 00:04:58,520
found this incredibly annoying, and I'll

165
00:04:58,520 --> 00:04:59,919
show you why. So, what I'm going to do

166
00:04:59,919 --> 00:05:01,600
is go over into the terminal now, and

167
00:05:01,600 --> 00:05:02,880
I'm going to show you how this memory

168
00:05:02,880 --> 00:05:04,400
feature actually works. It's actually

169
00:05:04,400 --> 00:05:06,320
really simple. So, I'm going to go SSH

170
00:05:06,320 --> 00:05:09,240
root at Hermes. So, I have Hermes Agent

171
00:05:09,240 --> 00:05:11,919
running on a remote virtual machine. And

172
00:05:11,919 --> 00:05:14,840
if we go into the Hermes Agent

173
00:05:14,840 --> 00:05:16,600
directory, so if you go and look in this

174
00:05:16,600 --> 00:05:18,040
file, what you'll see is a bunch of

175
00:05:18,040 --> 00:05:20,280
facts. So, it's saved these facts about

176
00:05:20,280 --> 00:05:22,960
me into this memory.md file, and each of

177
00:05:22,960 --> 00:05:24,720
these facts is then separated by this

178
00:05:24,720 --> 00:05:26,360
delimiter character.

179
00:05:26,360 --> 00:05:28,800
So, in theory, this is great. So, the

180
00:05:28,800 --> 00:05:30,640
the agent is saving things about me.

181
00:05:30,640 --> 00:05:31,800
But, when you actually look at what it's

182
00:05:31,800 --> 00:05:34,560
saving, for example, "Owen's current

183
00:05:34,560 --> 00:05:37,520
stack is Rails and PostgreSQL." This is

184
00:05:37,520 --> 00:05:40,240
not true. This is This is false. I said

185
00:05:40,240 --> 00:05:41,840
this once as an offhand comment, and now

186
00:05:41,840 --> 00:05:43,520
Hermes has decided to save that as a

187
00:05:43,520 --> 00:05:45,160
fact. But, the problem is I said this a

188
00:05:45,160 --> 00:05:46,880
while ago, and it's no longer true. I

189
00:05:46,880 --> 00:05:48,520
just said in an offhand comment, I like

190
00:05:48,520 --> 00:05:50,640
to use this stack. But it's not true

191
00:05:50,640 --> 00:05:52,840
that my current workspace stack is this

192
00:05:52,840 --> 00:05:54,480
at all. I use different technology

193
00:05:54,480 --> 00:05:56,680
stacks for my projects. And as you go

194
00:05:56,680 --> 00:05:57,800
through this, what you'll see is that a

195
00:05:57,800 --> 00:05:59,480
lot of the facts that Hermes is saving

196
00:05:59,480 --> 00:06:01,840
are just either false or misleading to

197
00:06:01,840 --> 00:06:03,880
the agent. So it's talking about a

198
00:06:03,880 --> 00:06:06,560
deprecated CLI tool. Again, this is kind

199
00:06:06,560 --> 00:06:07,800
of just not very useful. It's going to

200
00:06:07,800 --> 00:06:09,600
confuse the agent. I was using a

201
00:06:09,600 --> 00:06:11,280
different tool at one point. I'm not

202
00:06:11,280 --> 00:06:12,720
anymore. The other big feature that in

203
00:06:12,720 --> 00:06:14,200
Hermes is that it can create skills on

204
00:06:14,200 --> 00:06:15,600
the fly. What it what you're doing and

205
00:06:15,600 --> 00:06:17,600
then creates reusable skills for you.

206
00:06:17,600 --> 00:06:18,960
And it sounds really good in theory. If

207
00:06:18,960 --> 00:06:20,400
you go online, people on YouTube will

208
00:06:20,400 --> 00:06:22,240
rave about this feature, but I found it

209
00:06:22,240 --> 00:06:23,360
to be a real negative. What was

210
00:06:23,360 --> 00:06:24,480
happening is the agent would do

211
00:06:24,480 --> 00:06:26,320
something that's not quite correct, and

212
00:06:26,320 --> 00:06:27,919
then it would store that as a skill, and

213
00:06:27,919 --> 00:06:29,560
so it was basically generating loads and

214
00:06:29,560 --> 00:06:31,720
loads of these skills for very random

215
00:06:31,720 --> 00:06:32,960
things that weren't particularly

216
00:06:32,960 --> 00:06:35,120
accurate or useful. And I find that the

217
00:06:35,120 --> 00:06:36,440
more skills you have, the worse your

218
00:06:36,440 --> 00:06:38,280
agent will perform generally because

219
00:06:38,280 --> 00:06:40,040
every time it runs, it has to decide

220
00:06:40,040 --> 00:06:41,720
whether to load any of those skills. It

221
00:06:41,720 --> 00:06:43,880
starts to get confused. And so basically

222
00:06:43,880 --> 00:06:44,794
I found that Hermes was creating

223
00:06:44,794 --> 00:06:46,080
[clears throat] all of these little junk

224
00:06:46,080 --> 00:06:48,400
skills that weren't particularly useful.

225
00:06:48,400 --> 00:06:50,680
The agent writing markdown files isn't

226
00:06:50,680 --> 00:06:52,240
really learning. It's just automatic

227
00:06:52,240 --> 00:06:54,400
documentation. And so I would rather

228
00:06:54,400 --> 00:06:56,080
have more control over that process

229
00:06:56,080 --> 00:06:57,760
personally. All right. So what I built

230
00:06:57,760 --> 00:06:59,360
was a much simpler approach. It's a

231
00:06:59,360 --> 00:07:01,400
single Rust binary, which makes it

232
00:07:01,400 --> 00:07:02,680
really easy to install. You can

233
00:07:02,680 --> 00:07:04,240
literally just install this one thing on

234
00:07:04,240 --> 00:07:06,640
your host. It will then act as a gateway

235
00:07:06,640 --> 00:07:08,760
and then dispatch tasks to your existing

236
00:07:08,760 --> 00:07:10,400
coding agents. So essentially what we're

237
00:07:10,400 --> 00:07:12,280
doing with Push is taking the gateway

238
00:07:12,280 --> 00:07:14,480
element that exists in Hermes agent and

239
00:07:14,480 --> 00:07:15,640
open core,

240
00:07:15,640 --> 00:07:17,360
but we're not building our own back end.

241
00:07:17,360 --> 00:07:19,200
We're allowing the agent runtime to be

242
00:07:19,200 --> 00:07:20,919
configurable. One of the reasons, which

243
00:07:20,919 --> 00:07:22,560
might not be obvious why I much prefer

244
00:07:22,560 --> 00:07:24,320
this approach to using Hermes agent, is

245
00:07:24,320 --> 00:07:25,840
if you try and configure things like

246
00:07:25,840 --> 00:07:28,200
Gmail integration or any kind of OAuth

247
00:07:28,200 --> 00:07:30,200
integration, what you'll find is you

248
00:07:30,200 --> 00:07:31,919
have to go to Google Cloud, configure

249
00:07:31,919 --> 00:07:34,040
all of the OAuth credentials yourself,

250
00:07:34,040 --> 00:07:36,000
manage all of the security credentials

251
00:07:36,000 --> 00:07:38,360
on your host, and that's a real security

252
00:07:38,360 --> 00:07:40,240
risk. It's also a nightmare to kind of

253
00:07:40,240 --> 00:07:41,800
configure in general. It's really kind

254
00:07:41,800 --> 00:07:43,520
of annoying to set up in Humanness

255
00:07:43,520 --> 00:07:45,920
Agent, in my opinion. Whereas if you're

256
00:07:45,920 --> 00:07:47,560
using something like Codex, you get all

257
00:07:47,560 --> 00:07:49,880
of these features out of the box and the

258
00:07:49,880 --> 00:07:51,480
credential management, doing the things

259
00:07:51,480 --> 00:07:53,080
like refresh tokens for your OAuth

260
00:07:53,080 --> 00:07:55,720
credentials, all of it is handled by the

261
00:07:55,720 --> 00:07:57,920
OpenAI team. And so this makes it more

262
00:07:57,920 --> 00:08:00,240
secure and much more user-friendly, in

263
00:08:00,240 --> 00:08:01,760
my opinion. You can obviously have any

264
00:08:01,760 --> 00:08:03,680
kind of integration. You can have your

265
00:08:03,680 --> 00:08:05,360
agent automate your browser, integrate

266
00:08:05,360 --> 00:08:06,760
with Google Chrome. You can do things

267
00:08:06,760 --> 00:08:08,800
like Gmail configuration. This is

268
00:08:08,800 --> 00:08:10,880
literally just a one-click setup.

269
00:08:10,880 --> 00:08:12,200
Whereas if you're using Humanness Agent,

270
00:08:12,200 --> 00:08:13,560
you have to kind of jump through hoops

271
00:08:13,560 --> 00:08:15,800
to kind of get the OAuth credentials,

272
00:08:15,800 --> 00:08:16,720
you have to save them to your

273
00:08:16,720 --> 00:08:18,080
environment files. It's just really,

274
00:08:18,080 --> 00:08:19,960
really annoying to set these things up.

275
00:08:19,960 --> 00:08:21,720
And also it's less secure generally, in

276
00:08:21,720 --> 00:08:23,480
my opinion, because you're managing

277
00:08:23,480 --> 00:08:24,840
those credentials yourself. You have to

278
00:08:24,840 --> 00:08:27,200
remember to deal with refresh tokens and

279
00:08:27,200 --> 00:08:28,560
you have to know how to set those things

280
00:08:28,560 --> 00:08:30,400
up securely. Whereas if you're using

281
00:08:30,400 --> 00:08:32,479
something like Codex, out of the box

282
00:08:32,479 --> 00:08:34,120
it's going to be using best practices in

283
00:08:34,120 --> 00:08:35,479
terms of security, because obviously

284
00:08:35,479 --> 00:08:37,680
this is a public consumer product. They

285
00:08:37,680 --> 00:08:39,240
put a lot of time into how seamlessly

286
00:08:39,240 --> 00:08:40,800
you can integrate to all of your

287
00:08:40,800 --> 00:08:42,680
different external tools. Pretty much

288
00:08:42,680 --> 00:08:43,840
everything you're going to need is

289
00:08:43,840 --> 00:08:45,400
available within site Codex. You can

290
00:08:45,400 --> 00:08:47,400
connect to GitHub, your Google Drive,

291
00:08:47,400 --> 00:08:49,600
your Notion, your calendar, pretty much

292
00:08:49,600 --> 00:08:52,040
anything from Codex. So what we're going

293
00:08:52,040 --> 00:08:53,720
to do is go ahead and install this

294
00:08:53,720 --> 00:08:55,120
assistant. So if you want to install it,

295
00:08:55,120 --> 00:08:56,720
it's one click. You can just do this one

296
00:08:56,720 --> 00:08:59,280
click install and then it will run the

297
00:08:59,280 --> 00:09:00,520
agent. It will download the latest

298
00:09:00,520 --> 00:09:02,440
version and then run it. I'm going to

299
00:09:02,440 --> 00:09:03,440
actually just run it here in my

300
00:09:03,440 --> 00:09:05,000
directory, so I can see how it works.

301
00:09:05,000 --> 00:09:06,280
You can actually see the logs more

302
00:09:06,280 --> 00:09:07,680
easily.

303
00:09:07,680 --> 00:09:08,920
So we're just building the binary and

304
00:09:08,920 --> 00:09:10,360
now it's running and now it's polling

305
00:09:10,360 --> 00:09:12,440
Telegram for new messages. So every 3

306
00:09:12,440 --> 00:09:14,640
seconds we'll check in on Telegram

307
00:09:14,640 --> 00:09:15,800
looking for new messages. And the

308
00:09:15,800 --> 00:09:17,120
important thing to say here is we're not

309
00:09:17,120 --> 00:09:19,560
exposing any ports. If you run this on a

310
00:09:19,560 --> 00:09:21,720
virtual machine or your own machine,

311
00:09:21,720 --> 00:09:23,600
there's no inbound connectivity. This is

312
00:09:23,600 --> 00:09:25,680
just reaching out to Telegram. The

313
00:09:25,680 --> 00:09:27,040
advantage of this strategy is we're

314
00:09:27,040 --> 00:09:29,080
polling Telegram, so we're not opening

315
00:09:29,080 --> 00:09:30,880
any ports on our machine, so there's no

316
00:09:30,880 --> 00:09:32,600
security vulnerability in terms of

317
00:09:32,600 --> 00:09:34,200
someone else can access your webhook

318
00:09:34,200 --> 00:09:35,360
endpoint, for example. We're not

319
00:09:35,360 --> 00:09:37,480
exposing a web dashboard or anything

320
00:09:37,480 --> 00:09:39,480
else to the public internet. This is

321
00:09:39,480 --> 00:09:41,320
just polling from our virtual machine.

322
00:09:41,320 --> 00:09:42,520
So you could run this in a private

323
00:09:42,520 --> 00:09:44,800
network with no internet connectivity

324
00:09:44,800 --> 00:09:46,400
inbound. All right, so what I'm going to

325
00:09:46,400 --> 00:09:48,920
do now is just send a hello world

326
00:09:48,920 --> 00:09:50,440
message to my assistant. And kind of

327
00:09:50,440 --> 00:09:52,000
just what you should see then is that

328
00:09:52,000 --> 00:09:54,600
the message comes in. So new message

329
00:09:54,600 --> 00:09:56,480
accepted routing to Codex. So we're

330
00:09:56,480 --> 00:09:58,160
basically taking the message I just sent

331
00:09:58,160 --> 00:10:01,760
on Telegram. It sent then a message back

332
00:10:01,760 --> 00:10:02,880
and I'll just quickly show you what that

333
00:10:02,880 --> 00:10:04,400
looks like. So what I can see here is my

334
00:10:04,400 --> 00:10:06,160
Telegram account. These are my two AI

335
00:10:06,160 --> 00:10:07,720
personal assistants running on different

336
00:10:07,720 --> 00:10:09,920
machines. So this first one David, I

337
00:10:09,920 --> 00:10:11,440
just sent a message saying hello world

338
00:10:11,440 --> 00:10:13,520
and then it responded back. You can also

339
00:10:13,520 --> 00:10:15,000
send a voice message as well. So what

340
00:10:15,000 --> 00:10:16,400
I'm going to do is just send a voice

341
00:10:16,400 --> 00:10:18,440
message. And then when you do that, you

342
00:10:18,440 --> 00:10:20,040
should get a voice message back. So

343
00:10:20,040 --> 00:10:21,600
we're going to say

344
00:10:21,600 --> 00:10:23,920
"Hey, can you remind me of my priorities

345
00:10:23,920 --> 00:10:25,960
for this week? Tell me my goals. Don't

346
00:10:25,960 --> 00:10:27,560
reveal any sensitive information cuz I'm

347
00:10:27,560 --> 00:10:29,320
doing a demo." Okay, so what you can see

348
00:10:29,320 --> 00:10:30,800
here is the agent has now responded.

349
00:10:30,800 --> 00:10:32,760
Again, the agent has context about me,

350
00:10:32,760 --> 00:10:34,880
my goals, my to-do list, my emails, and

351
00:10:34,880 --> 00:10:36,920
everything that's going on. So priority

352
00:10:36,920 --> 00:10:39,560
one is to re-record a course by Friday.

353
00:10:39,560 --> 00:10:41,000
You can see here I'm actually currently

354
00:10:41,000 --> 00:10:42,760
re-recording this video which I failed

355
00:10:42,760 --> 00:10:44,400
to record yesterday.

356
00:10:44,400 --> 00:10:46,400
And there's some uh sponsorship emails I

357
00:10:46,400 --> 00:10:48,760
need to respond to. And I'm working on a

358
00:10:48,760 --> 00:10:50,720
side project over here.

359
00:10:50,720 --> 00:10:53,000
And my primary goals make AI engineer

360
00:10:53,000 --> 00:10:55,520
the best practical program for AI

361
00:10:55,520 --> 00:10:57,440
builders in general and grow YouTube to

362
00:10:57,440 --> 00:11:00,000
100,000 subs. So these are my two goals

363
00:11:00,000 --> 00:11:01,280
for this year and then it's kind of

364
00:11:01,280 --> 00:11:02,880
giving me my focus. This is how I think

365
00:11:02,880 --> 00:11:05,000
about AI personal assistants in general.

366
00:11:05,000 --> 00:11:06,960
You want to make them just like useful

367
00:11:06,960 --> 00:11:08,360
useful assistants that can keep you

368
00:11:08,360 --> 00:11:10,040
focused, help you organize your week.

369
00:11:10,040 --> 00:11:11,720
Any kind of coding tasks I will just use

370
00:11:11,720 --> 00:11:13,960
a coding agent for. When I'm building a

371
00:11:13,960 --> 00:11:15,320
personal assistant, I want it to just

372
00:11:15,320 --> 00:11:17,280
help me stay organized basically.

373
00:11:17,280 --> 00:11:19,200
>> Your priorities for the rest of this

374
00:11:19,200 --> 00:11:20,360
week are:

375
00:11:20,360 --> 00:11:23,839
One, publish AI Architect V2 by Friday,

376
00:11:23,839 --> 00:11:26,640
17 July. This is the highest priority

377
00:11:26,640 --> 00:11:27,560
task.

378
00:11:27,560 --> 00:11:29,240
>> So one of the tasks I like to use my AI

379
00:11:29,240 --> 00:11:30,640
assistant for is is read through my

380
00:11:30,640 --> 00:11:32,280
emails and then put things on my to-do

381
00:11:32,280 --> 00:11:34,280
list that I need to take action on.

382
00:11:34,280 --> 00:11:36,120
So, let's go ahead and do that.

383
00:11:36,120 --> 00:11:37,520
Can you go through my emails for the

384
00:11:37,520 --> 00:11:39,640
past 24 hours and then add anything to

385
00:11:39,640 --> 00:11:41,440
my to do list that I need to take action

386
00:11:41,440 --> 00:11:42,480
on?

387
00:11:42,480 --> 00:11:43,800
So, this is my current to do list. You

388
00:11:43,800 --> 00:11:45,240
can see here I don't have very much on

389
00:11:45,240 --> 00:11:46,920
it. I've got, you know, responding to

390
00:11:46,920 --> 00:11:49,840
emails, the course I need to update,

391
00:11:49,840 --> 00:11:51,800
onboarding video. And this is the task

392
00:11:51,800 --> 00:11:53,160
I'm currently working on now, which is

393
00:11:53,160 --> 00:11:55,440
recording this YouTube video itself.

394
00:11:55,440 --> 00:11:56,720
And what we should see now is that the

395
00:11:56,720 --> 00:11:58,080
agent should go through my emails and

396
00:11:58,080 --> 00:11:59,680
then add any kind of follow-up actions I

397
00:11:59,680 --> 00:12:01,720
need to take. And you can even delegate

398
00:12:01,720 --> 00:12:04,360
some of these tasks to the AI agent. So,

399
00:12:04,360 --> 00:12:06,000
for example, if I wanted to, I could go

400
00:12:06,000 --> 00:12:07,720
ahead and delegate this task to my

401
00:12:07,720 --> 00:12:09,840
agent. So, for example, this is drafting

402
00:12:09,840 --> 00:12:12,200
a reply. Pretty much my agent knows what

403
00:12:12,200 --> 00:12:13,720
I'm going to send here anyway, so I can

404
00:12:13,720 --> 00:12:15,120
pretty much delegate this task to my

405
00:12:15,120 --> 00:12:17,000
agent to take care of. So, in terms of

406
00:12:17,000 --> 00:12:18,200
how this works in terms of the

407
00:12:18,200 --> 00:12:19,960
architecture, we have a gateway. So,

408
00:12:19,960 --> 00:12:22,040
this is the the main component of your

409
00:12:22,040 --> 00:12:23,960
personal assistant. This is where we're

410
00:12:23,960 --> 00:12:25,800
sending messages to and this is what's

411
00:12:25,800 --> 00:12:27,480
scheduling all of the automated work.

412
00:12:27,480 --> 00:12:29,720
So, this gateway is responsible for

413
00:12:29,720 --> 00:12:31,400
accepting incoming messages and then

414
00:12:31,400 --> 00:12:33,160
dispatching them to an agent runtime.

415
00:12:33,160 --> 00:12:35,040
It's firing up an agent to handle the

416
00:12:35,040 --> 00:12:36,240
request.

417
00:12:36,240 --> 00:12:37,720
And then we also have scheduled jobs.

418
00:12:37,720 --> 00:12:40,320
This is running cron jobs, basically,

419
00:12:40,320 --> 00:12:42,000
that will run on in the background. So,

420
00:12:42,000 --> 00:12:43,400
for example, every Monday morning you

421
00:12:43,400 --> 00:12:45,880
might have a task to triage your email.

422
00:12:45,880 --> 00:12:47,400
It will delegate that to an agent to do

423
00:12:47,400 --> 00:12:48,800
the work and then it will send you a

424
00:12:48,800 --> 00:12:50,920
message to say that it's done. The nice

425
00:12:50,920 --> 00:12:52,240
thing about this personal assistant

426
00:12:52,240 --> 00:12:53,839
pattern is you get notified when the

427
00:12:53,839 --> 00:12:55,920
agent is doing work for you. You get a

428
00:12:55,920 --> 00:12:57,320
notification on your phone to say the

429
00:12:57,320 --> 00:12:59,080
agent has finished triaging your emails

430
00:12:59,080 --> 00:13:00,760
or it's reviewed your priorities for

431
00:13:00,760 --> 00:13:02,360
today. It will take action. It will be

432
00:13:02,360 --> 00:13:04,160
proactive.

433
00:13:04,160 --> 00:13:05,720
And then in terms of the agent runtime,

434
00:13:05,720 --> 00:13:07,520
all of the kind of heavy lifting is now

435
00:13:07,520 --> 00:13:10,040
done by Codex or cloud code. You can use

436
00:13:10,040 --> 00:13:11,760
your existing connectors, your existing

437
00:13:11,760 --> 00:13:13,839
skills. Really, you're not having to

438
00:13:13,839 --> 00:13:15,760
customize too much or change much about

439
00:13:15,760 --> 00:13:17,640
the way you work. The only thing we're

440
00:13:17,640 --> 00:13:19,560
kind of adding to this setup is this

441
00:13:19,560 --> 00:13:22,240
gateway. You can also define a soul.md,

442
00:13:22,240 --> 00:13:23,760
which defines the assistant and its

443
00:13:23,760 --> 00:13:25,480
personality as well.

444
00:13:25,480 --> 00:13:28,120
And the gateway will also persist any

445
00:13:28,120 --> 00:13:30,040
conversations you have in SQLite as a

446
00:13:30,040 --> 00:13:31,920
database, so it can also get access to

447
00:13:31,920 --> 00:13:33,920
your past conversations, your past

448
00:13:33,920 --> 00:13:35,400
conversational history as well. So, it

449
00:13:35,400 --> 00:13:37,000
saves the memory of everything you've

450
00:13:37,000 --> 00:13:38,800
discussed with your agent. Okay, so you

451
00:13:38,800 --> 00:13:40,040
can see here now that the agent has

452
00:13:40,040 --> 00:13:41,840
responded to us. We can see here that

453
00:13:41,840 --> 00:13:43,320
it's given us a message, so we can go

454
00:13:43,320 --> 00:13:45,640
ahead and listen to that one.

455
00:13:45,640 --> 00:13:47,400
Let's go ahead and see what the agent

456
00:13:47,400 --> 00:13:48,520
has said.

457
00:13:48,520 --> 00:13:51,760
>> Reviewed 120 incoming emails from the

458
00:13:51,760 --> 00:13:54,560
past 24 hours. Created four to-do list

459
00:13:54,560 --> 00:13:56,120
tasks in inbox.

460
00:13:56,120 --> 00:13:57,360
>> Okay, so now you can see in my to-do

461
00:13:57,360 --> 00:13:59,000
list, the agent has added these tasks.

462
00:13:59,000 --> 00:14:01,360
It's even added due dates as well. So,

463
00:14:01,360 --> 00:14:02,760
now that we have all of the tasks in our

464
00:14:02,760 --> 00:14:05,160
to-do list, this is great because now

465
00:14:05,160 --> 00:14:06,120
what we can do is we can actually

466
00:14:06,120 --> 00:14:07,760
delegate these tasks to our agent. So,

467
00:14:07,760 --> 00:14:10,320
for example, if I wanted the agent to

468
00:14:10,320 --> 00:14:11,960
handle some of these tasks, I could just

469
00:14:11,960 --> 00:14:13,440
ask it to pick up one of these tasks for

470
00:14:13,440 --> 00:14:14,440
me.

471
00:14:14,440 --> 00:14:15,480
And this is the way I like to think

472
00:14:15,480 --> 00:14:16,800
about agents. You've got a control

473
00:14:16,800 --> 00:14:18,520
plane, which is your task list, all the

474
00:14:18,520 --> 00:14:20,360
things you need to do. You can either

475
00:14:20,360 --> 00:14:21,880
pick them up yourself, so I could either

476
00:14:21,880 --> 00:14:24,040
pick up this and do it myself, or I

477
00:14:24,040 --> 00:14:26,080
could just delegate that one to my AI

478
00:14:26,080 --> 00:14:28,640
agent. So, let's for example

479
00:14:28,640 --> 00:14:31,240
try and draft a response to this one.

480
00:14:31,240 --> 00:14:32,480
So, again, what I'm going to do is go

481
00:14:32,480 --> 00:14:33,880
back to my agent and see if it can

482
00:14:33,880 --> 00:14:36,120
handle this task for me. Now, the agent

483
00:14:36,120 --> 00:14:37,600
has finished responding to our message.

484
00:14:37,600 --> 00:14:38,880
You can see here,

485
00:14:38,880 --> 00:14:40,160
uh thanks for reaching out. Looks

486
00:14:40,160 --> 00:14:42,480
relevant. I'd be open to testing the pro

487
00:14:42,480 --> 00:14:44,240
account. You can obviously configure

488
00:14:44,240 --> 00:14:45,360
this. So, if you have any preferences,

489
00:14:45,360 --> 00:14:47,120
so for example, I often don't handle

490
00:14:47,120 --> 00:14:49,000
sponsorship requests at the moment

491
00:14:49,000 --> 00:14:50,600
because I'm really kind of focused on

492
00:14:50,600 --> 00:14:52,560
content in general. But, obviously you

493
00:14:52,560 --> 00:14:54,600
can kind of have predefined responses

494
00:14:54,600 --> 00:14:55,720
that you want for a certain type of

495
00:14:55,720 --> 00:14:57,600
email. You can kind of customize your

496
00:14:57,600 --> 00:14:59,080
agent to handle these tasks and get

497
00:14:59,080 --> 00:15:00,480
better over time. In terms of

498
00:15:00,480 --> 00:15:01,800
configuring the agent, the other thing I

499
00:15:01,800 --> 00:15:03,440
wanted was to for this to be very, very

500
00:15:03,440 --> 00:15:05,240
simple. If you look at a tool like

501
00:15:05,240 --> 00:15:06,920
Hamish or Open Claw, the configuration

502
00:15:06,920 --> 00:15:08,440
is really complicated. There are so many

503
00:15:08,440 --> 00:15:10,000
different options, so many messaging

504
00:15:10,000 --> 00:15:12,640
platforms, so much to configure. I

505
00:15:12,640 --> 00:15:14,040
wanted to keep this as simple as

506
00:15:14,040 --> 00:15:15,960
possible. So, you can see here, the

507
00:15:15,960 --> 00:15:17,560
configuration is super, super minimal.

508
00:15:17,560 --> 00:15:19,560
We have a single channel, so you can

509
00:15:19,560 --> 00:15:21,400
have Telegram or iMessage. I'll probably

510
00:15:21,400 --> 00:15:23,400
add some more channels later. But then

511
00:15:23,400 --> 00:15:24,720
you can choose your agents. So, this

512
00:15:24,720 --> 00:15:26,200
will dispatch to Codex, but you could

513
00:15:26,200 --> 00:15:28,200
change this to Claude. You could also

514
00:15:28,200 --> 00:15:29,880
change it to something like Pi as well

515
00:15:29,880 --> 00:15:31,960
if you wanted to. So, the assistant

516
00:15:31,960 --> 00:15:33,760
route is where we store our context

517
00:15:33,760 --> 00:15:35,800
about us, our goals, our priorities, any

518
00:15:35,800 --> 00:15:37,280
information the assistant needs to know,

519
00:15:37,280 --> 00:15:39,320
and also all of our jobs.

520
00:15:39,320 --> 00:15:41,040
And then Telegram is just the basic

521
00:15:41,040 --> 00:15:43,000
configuration, the allowed user ID, the

522
00:15:43,000 --> 00:15:45,200
bot token, etc.

523
00:15:45,200 --> 00:15:46,520
Very, very simple and easy to set up.

524
00:15:46,520 --> 00:15:47,960
And then if you want voice replies,

525
00:15:47,960 --> 00:15:50,520
you'll need an OpenAI API key. And so,

526
00:15:50,520 --> 00:15:52,440
this is my actual personal assistant.

527
00:15:52,440 --> 00:15:54,760
And what I like about this approach is

528
00:15:54,760 --> 00:15:56,040
one of the things I found difficult with

529
00:15:56,040 --> 00:15:57,720
tools like open claw and Hermes agent is

530
00:15:57,720 --> 00:15:59,360
that they were so unopinionated about

531
00:15:59,360 --> 00:16:01,360
how to build an assistant.

532
00:16:01,360 --> 00:16:02,720
I wanted something that was much more

533
00:16:02,720 --> 00:16:04,360
opinionated. So, we only have two things

534
00:16:04,360 --> 00:16:06,240
to think about in my opinion with a

535
00:16:06,240 --> 00:16:07,440
personal assistant. Well, three

536
00:16:07,440 --> 00:16:09,600
actually. First one is context. So, what

537
00:16:09,600 --> 00:16:11,760
does the agent know about you? So, for

538
00:16:11,760 --> 00:16:13,600
example, here is some information about

539
00:16:13,600 --> 00:16:16,120
my current focus, my current goals. The

540
00:16:16,120 --> 00:16:17,720
agent can kind of read through this. So,

541
00:16:17,720 --> 00:16:19,680
you know, make AI engineer the best

542
00:16:19,680 --> 00:16:21,720
practical AI software program, grow

543
00:16:21,720 --> 00:16:24,120
YouTube to 100,000 subs. These are my

544
00:16:24,120 --> 00:16:25,280
goals.

545
00:16:25,280 --> 00:16:26,960
And then also it has information about

546
00:16:26,960 --> 00:16:29,000
me, how I like to handle sponsorships,

547
00:16:29,000 --> 00:16:30,440
etc.

548
00:16:30,440 --> 00:16:32,320
And then we also have jobs as well. So,

549
00:16:32,320 --> 00:16:34,320
these are the recurring jobs. So, I

550
00:16:34,320 --> 00:16:36,280
wanted the job system to be as simple as

551
00:16:36,280 --> 00:16:38,080
possible and reviewable. So, these are

552
00:16:38,080 --> 00:16:40,160
the cron jobs. So, for example, here's

553
00:16:40,160 --> 00:16:42,480
an example of a job to do a weekly

554
00:16:42,480 --> 00:16:45,400
review. It's literally just a prompt.

555
00:16:45,400 --> 00:16:47,520
We can schedule where the job runs, the

556
00:16:47,520 --> 00:16:49,920
working directory. We can also schedule

557
00:16:49,920 --> 00:16:51,520
how how often it runs. This could be

558
00:16:51,520 --> 00:16:53,680
every week, etc. But this is basically

559
00:16:53,680 --> 00:16:56,080
preparing my weekly review, go through

560
00:16:56,080 --> 00:16:59,120
my tasks, my emails, my calendar, figure

561
00:16:59,120 --> 00:17:01,360
out what I need to work on, use to do

562
00:17:01,360 --> 00:17:02,839
list to look through my, you know,

563
00:17:02,839 --> 00:17:04,760
completed tasks. Basically triage all of

564
00:17:04,760 --> 00:17:07,240
the stuff I need to do. And then return

565
00:17:07,240 --> 00:17:08,439
things that I need to focus on

566
00:17:08,439 --> 00:17:10,120
basically. So, you can just add jobs,

567
00:17:10,120 --> 00:17:11,520
anything that you like here. So, this

568
00:17:11,520 --> 00:17:13,760
could be your daily focus, an email

569
00:17:13,760 --> 00:17:16,720
triage, research jobs, anything you want

570
00:17:16,720 --> 00:17:18,079
that you to run on a schedule,

571
00:17:18,079 --> 00:17:20,520
basically, you can just define in here.

572
00:17:20,520 --> 00:17:22,600
The nice thing then is this is all

573
00:17:22,600 --> 00:17:24,520
reviewable. You can store it in GitHub.

574
00:17:24,520 --> 00:17:26,000
You can keep it all version controlled

575
00:17:26,000 --> 00:17:28,000
and nice and organized. And then the

576
00:17:28,000 --> 00:17:29,800
other thing we have is the soul.md. This

577
00:17:29,800 --> 00:17:32,760
describes how the agent should act. So,

578
00:17:32,760 --> 00:17:34,960
you are Owen's chief of staff for his

579
00:17:34,960 --> 00:17:37,200
work. Your job is to turn a noisy stream

580
00:17:37,200 --> 00:17:39,400
of tasks, messages, and meetings into

581
00:17:39,400 --> 00:17:41,160
clear decisions and useful action.

582
00:17:41,160 --> 00:17:43,040
Protect his attention. Keep the

583
00:17:43,040 --> 00:17:44,720
important work moving. Reduce

584
00:17:44,720 --> 00:17:47,400
operational drag without taking control.

585
00:17:47,400 --> 00:17:49,080
So, again, just be calm, lead with what

586
00:17:49,080 --> 00:17:50,880
matters now, make recommendations,

587
00:17:50,880 --> 00:17:52,480
challenge distractions and false

588
00:17:52,480 --> 00:17:54,600
urgency. We're just defining how you

589
00:17:54,600 --> 00:17:56,960
want the assistant to act, basically.

590
00:17:56,960 --> 00:17:59,400
And then in the agent.md file,

591
00:17:59,400 --> 00:18:00,880
this is going to be read by tools like

592
00:18:00,880 --> 00:18:03,320
Claude Code or Codex. You can basically

593
00:18:03,320 --> 00:18:05,120
define what the agent should know. So,

594
00:18:05,120 --> 00:18:07,680
for example, the priorities, the working

595
00:18:07,680 --> 00:18:09,200
rules, and then the tools that are

596
00:18:09,200 --> 00:18:11,000
available. So, you can see here, I'm

597
00:18:11,000 --> 00:18:13,480
using Todoist with the TD-CLI to get my

598
00:18:13,480 --> 00:18:16,320
to-do list tasks. Uh email and calendar

599
00:18:16,320 --> 00:18:18,840
are connected. We have passage, which is

600
00:18:18,840 --> 00:18:21,360
what I use for research, GitHub, and

601
00:18:21,360 --> 00:18:23,520
then also the push agent itself. So, it

602
00:18:23,520 --> 00:18:26,520
can call back into the runtime and and

603
00:18:26,520 --> 00:18:28,120
do things like query the jobs we have

604
00:18:28,120 --> 00:18:30,360
running, query the memory, and things

605
00:18:30,360 --> 00:18:31,520
like that. So, it's really, really

606
00:18:31,520 --> 00:18:34,320
simple setup. And this is kind of

607
00:18:34,320 --> 00:18:36,320
relatively opinionated and easy to get

608
00:18:36,320 --> 00:18:38,120
started with. When you first build the

609
00:18:38,120 --> 00:18:39,880
agent, you can run push in it and it

610
00:18:39,880 --> 00:18:42,080
will create this repository for you. So,

611
00:18:42,080 --> 00:18:43,600
another key idea I think that's really

612
00:18:43,600 --> 00:18:44,800
important when you build a personal

613
00:18:44,800 --> 00:18:46,760
assistant is to give the agents access

614
00:18:46,760 --> 00:18:48,200
to your workspace. What I mean by that

615
00:18:48,200 --> 00:18:50,320
is you don't want the agent running on a

616
00:18:50,320 --> 00:18:52,360
remote virtual machine or on a Mac Mini

617
00:18:52,360 --> 00:18:54,080
somewhere else. You often want to be

618
00:18:54,080 --> 00:18:55,400
able to read the documents or the

619
00:18:55,400 --> 00:18:57,080
research it produces. So, I have a

620
00:18:57,080 --> 00:18:58,880
writing application that I have

621
00:18:58,880 --> 00:19:00,360
connected to this.

622
00:19:00,360 --> 00:19:01,920
So, what I can do here is say something

623
00:19:01,920 --> 00:19:04,160
like, "Can you research the latest AI

624
00:19:04,160 --> 00:19:07,560
news in the last 48 hours? Anything

625
00:19:07,560 --> 00:19:09,360
that's relevant to an AI engineer." And

626
00:19:09,360 --> 00:19:11,720
then save the information to a passage

627
00:19:11,720 --> 00:19:13,680
document that I can read on my phone.

628
00:19:13,680 --> 00:19:15,000
All right, so let's go into my writing

629
00:19:15,000 --> 00:19:16,720
application and then I should be able to

630
00:19:16,720 --> 00:19:18,320
find this document that it's created. So

631
00:19:18,320 --> 00:19:20,440
it should have created a document here.

632
00:19:20,440 --> 00:19:23,240
And so let's go ahead and share this.

633
00:19:23,240 --> 00:19:25,160
And let's go ahead and view. So this is

634
00:19:25,160 --> 00:19:28,000
AI engineer news in the last 48 hours.

635
00:19:28,000 --> 00:19:29,560
The general point here is that not only

636
00:19:29,560 --> 00:19:31,280
did it it do the research, but also

637
00:19:31,280 --> 00:19:32,720
pushed it into a document that I can go

638
00:19:32,720 --> 00:19:34,080
and read later. I found this pattern

639
00:19:34,080 --> 00:19:36,240
really useful where the agent is able to

640
00:19:36,240 --> 00:19:37,800
connect into your project management

641
00:19:37,800 --> 00:19:40,320
tools, your writing applications, push

642
00:19:40,320 --> 00:19:42,120
stuff into them so that you don't have

643
00:19:42,120 --> 00:19:43,520
this kind of disconnect between the

644
00:19:43,520 --> 00:19:45,440
agent and your actual workplace. So you

645
00:19:45,440 --> 00:19:47,760
can see here, GitHub Copilot at

646
00:19:47,760 --> 00:19:50,120
endpoints with local sandboxes.

647
00:19:50,120 --> 00:19:51,760
Basically just some interesting news

648
00:19:51,760 --> 00:19:53,280
that I can read any day. You could also

649
00:19:53,280 --> 00:19:54,600
schedule a job that would do something

650
00:19:54,600 --> 00:19:57,280
similar and kind of push the latest news

651
00:19:57,280 --> 00:19:58,760
into a document that you can check out

652
00:19:58,760 --> 00:19:59,880
on your phone.

653
00:19:59,880 --> 00:20:00,720
All right, just to give you one more

654
00:20:00,720 --> 00:20:02,480
example just to show how it's possible

655
00:20:02,480 --> 00:20:04,400
to switch out the runtime. So what we're

656
00:20:04,400 --> 00:20:05,760
going to do is run this application, but

657
00:20:05,760 --> 00:20:06,880
now what I've done is I've changed my

658
00:20:06,880 --> 00:20:08,880
configuration to use Claude. So

659
00:20:08,880 --> 00:20:10,320
previously I was sending all of our

660
00:20:10,320 --> 00:20:12,040
messages to Codex, but now I want to use

661
00:20:12,040 --> 00:20:14,160
Claude code. And I could do the same

662
00:20:14,160 --> 00:20:16,080
thing for like the Pi agent as well, but

663
00:20:16,080 --> 00:20:18,080
we're going to try and see if we can

664
00:20:18,080 --> 00:20:19,320
make sure that this is running

665
00:20:19,320 --> 00:20:20,440
correctly. So I'm going to go on ahead

666
00:20:20,440 --> 00:20:23,680
and ask the agent what model it's using.

667
00:20:23,680 --> 00:20:27,320
>> Model ID, Claude Fable 5. It's the first

668
00:20:27,320 --> 00:20:30,080
model in Anthropic's Claude 5 family.

669
00:20:30,080 --> 00:20:31,880
>> So overall, I really do think Hermes

670
00:20:31,880 --> 00:20:33,480
Agent and Open Claude are great

671
00:20:33,480 --> 00:20:35,640
projects. They've done an amazing job of

672
00:20:35,640 --> 00:20:36,720
changing [music] how we think about

673
00:20:36,720 --> 00:20:38,800
personal AI assistants in general. They

674
00:20:38,800 --> 00:20:41,000
invented this entire category, but the

675
00:20:41,000 --> 00:20:43,160
more time I spent with some of the

676
00:20:43,160 --> 00:20:44,680
deeper features of Hermes Agent, the

677
00:20:44,680 --> 00:20:46,560
more frustrated I got. I found that the

678
00:20:46,560 --> 00:20:48,080
memory was not actually useful. The

679
00:20:48,080 --> 00:20:49,480
agent was saving things which just

680
00:20:49,480 --> 00:20:51,320
didn't make sense. The agent was

681
00:20:51,320 --> 00:20:52,560
actually just getting confused [music]

682
00:20:52,560 --> 00:20:55,120
or picking up incorrect facts. And the

683
00:20:55,120 --> 00:20:56,760
self-improvement element which everyone

684
00:20:56,760 --> 00:20:58,800
hypes about, I found that to be actually

685
00:20:58,800 --> 00:21:01,080
really really not [music] useful at all.

686
00:21:01,080 --> 00:21:02,720
In fact, I had to disable the skill

687
00:21:02,720 --> 00:21:04,200
creation cuz I found that the agent was

688
00:21:04,200 --> 00:21:05,360
creating all of these [music] basically

689
00:21:05,360 --> 00:21:07,720
junk skills all of the time that were

690
00:21:07,720 --> 00:21:09,320
not useful, that were actually making

691
00:21:09,320 --> 00:21:11,560
the agent perform worse over time. So, I

692
00:21:11,560 --> 00:21:13,080
think while the ideas are very, very

693
00:21:13,080 --> 00:21:14,800
good, it's nice to think about an AI

694
00:21:14,800 --> 00:21:16,800
assistant that self-learns and improves

695
00:21:16,800 --> 00:21:19,040
over time, the reality is that doing

696
00:21:19,040 --> 00:21:21,120
this well [music] is exceptionally hard,

697
00:21:21,120 --> 00:21:22,680
and there are definitely some trade-offs

698
00:21:22,680 --> 00:21:25,000
if you want to have your agent learning

699
00:21:25,000 --> 00:21:28,280
from you dynamically on the fly.

700
00:21:28,280 --> 00:21:29,440
So, I would still recommend trying

701
00:21:29,440 --> 00:21:30,720
Hermez and Open Claw. I think they're

702
00:21:30,720 --> 00:21:32,520
great projects, but for me personally, I

703
00:21:32,520 --> 00:21:34,720
wanted something simpler, much easier to

704
00:21:34,720 --> 00:21:36,280
set up, that kind of integrated with my

705
00:21:36,280 --> 00:21:38,560
existing tools. And for me going

706
00:21:38,560 --> 00:21:39,680
forward, this is how I'm going to be

707
00:21:39,680 --> 00:21:42,000
building AI personal assistants. If you

708
00:21:42,000 --> 00:21:43,440
found the video useful, please remember

709
00:21:43,440 --> 00:21:44,760
to like and subscribe. It massively

710
00:21:44,760 --> 00:21:46,040
helps out the channel, and I really,

711
00:21:46,040 --> 00:21:47,680
really appreciate it. If you have any

712
00:21:47,680 --> 00:21:49,720
questions or comments about this video,

713
00:21:49,720 --> 00:21:51,720
let me know in the comments below. I

714
00:21:51,720 --> 00:21:53,120
know a lot of people really love these

715
00:21:53,120 --> 00:21:54,720
tools, and they get a lot of value out

716
00:21:54,720 --> 00:21:56,400
of them. So, I want to make sure that

717
00:21:56,400 --> 00:21:58,040
I'm not dismissing these tools in any

718
00:21:58,040 --> 00:21:59,760
way. I think Hermez is a amazing

719
00:21:59,760 --> 00:22:01,880
project, and the same for Open Claw. I

720
00:22:01,880 --> 00:22:03,240
think these tools are incredibly

721
00:22:03,240 --> 00:22:05,000
valuable. It's just that for me

722
00:22:05,000 --> 00:22:06,560
personally, most of the features that

723
00:22:06,560 --> 00:22:08,080
they offered weren't really particularly

724
00:22:08,080 --> 00:22:09,560
useful compared to just using my

725
00:22:09,560 --> 00:22:11,440
existing coding agents. Thanks again for

726
00:22:11,440 --> 00:22:12,560
watching, and I'll see you in the next

727
00:22:12,560 --> 00:22:15,480
video. Take care.
