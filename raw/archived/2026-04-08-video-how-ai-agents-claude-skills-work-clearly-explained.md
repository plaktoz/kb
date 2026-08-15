# How AI agents & Claude skills work (Clearly Explained)

source_url: https://www.youtube.com/watch?v=S_oN3vlzpMw
author: Greg Isenberg

---

# How AI agents & Claude skills work (Clearly Explained)

I sit down with Ras Mic to break down how AI agents actually work and why most people are using them wrong. Ras Mic explains the mechanics of context windows, makes the case that agent md files are largely unnecessary, and shares his step-by-step methodology for building custom skills that make agen

# Description

I sit down with Ras Mic to break down how AI agents actually work and why most people are using them wrong. Ras Mic explains the mechanics of context windows, makes the case that agent md files are largely unnecessary, and shares his step-by-step methodology for building custom skills that make agents dramatically more productive. Whether you're coding with Claude Code or automating workflows with OpenClaw, this episode gives you the foundational knowledge to stop wasting tokens and start getting real results from your AI tools.

Timestamps
00:00 – Intro
00:42 – The Models Are Good Now
01:20 – How Context Windows Actually Work
04:55 – The Power of Skills
09:17 – How to create Skills
16:35 – Skill Maxxing
19:05 – What you need too build a project
20:40 – Recursively Building and Improving Skills
29:23 – Context Window Management and Token Efficiency
33:02 – Closing Thoughts

Key Points

* The models (Opus 4.6, GPT 5.4) are exceptionally good now — the differentiator is the context and harness you build around them.
* Agent md and claude md files get loaded into context on every single turn, burning tokens and degrading performance as the context window fills up. 95% of users can skip them entirely.
* Skills use progressive disclosure: only the name and description sit in context until the agent determines it needs the full file, saving thousands of tokens per conversation.
* The best way to create a skill is to walk through the workflow with the agent step by step, achieve a successful run, and then have the agent write the skill based on that real context.
* Recursively refine skills by feeding failures back into the agent and having it update the skill file so the same mistake is avoided going forward.
* Scale for productivity by starting with one agent and building up workflows before adding sub-agents — start simple, then expand.

Numbered Section Summaries

1. The Models Are Good — Context Is What Matters

Ras Mic opens by declaring that the current generation of models, Opus 4.6 and GPT 5.4, are exceptionally capable. The conversation is no longer about which model is "better" in a general sense. What matters now is the quality of context you feed them — that is what separates quality output from slop.

2. How Context Windows Work

Ras Mic walks through the anatomy of a context window: system prompt, agent.md files, skills, tools, the codebase, and the user conversation. All of these stack up as tokens, and the window has a hard limit (around 250,000 tokens). When you hit that limit, agents compact — and performance drops. Understanding this structure is the foundation for everything else in the episode.

3. Skills and Progressive Disclosure

Skills solve the token-bloat problem. A skill file contains a name, description, and the detailed instructions — but only the name and description are loaded into context. The agent reads the full file only when it determines the skill is relevant. This means a skill costs roughly 53 tokens per turn versus 944+ for an equivalent agent.md file.

4. Building Skills the Right Way

Ras Mic shares his methodology: identify a workflow, walk through it with the agent step by step, correct mistakes in real time, and only create the skill after you have completed a successful run. He illustrates this with his sponsor email screening agent — the first attempt returned all-positive results because the agent had no criteria for rejection.

5. Recursively Improving Skills

Even after a skill is created, the agent will still hit edge cases and fail. Ras Mic treats each failure as an opportunity: identify the error, have the agent fix it, then tell the agent to update the skill so the failure is documented. After five iterations of this loop on his YouTube analytics report generator, the agent now executes flawlessly across eight data sources in about ten minutes.

6. Scaling for Productivity Over Flash

Ras Mic started with a single agent handling everything — email, spreadsheets, research. Only after building reliable skills did he add sub-agents for marketing, business, and personal tasks. He argues that jumping straight to multi-agent architectures (or adopting tools like Paperclip without building foundational workflows first) optimizes for what looks cool rather than what is productive.

The #1 tool to find startup ideas/trends - https://www.ideabrowser.com/

LCA helps Fortune 500s and fast-growing startups build their future - from Warner Music to Fortnite to Dropbox. We turn 'what if' into reality with AI, apps, and next-gen products https://latecheckout.agency/

The Vibe Marketer - Resources for people into vibe marketing/marketing with AI: https://www.thevibemarketer.com/

FIND ME ON SOCIAL
X/Twitter: https://twitter.com/gregisenberg
Instagram: https://instagram.com/gregisenberg/
LinkedIn: https://www.linkedin.com/in/gisenberg/

FIND MIC ON SOCIAL
X/Twitter: https://x.com/Rasmic
Youtube: https://www.youtube.com/@rasmic

# Chapters

* [00:00:00] – Intro
* [00:00:42] – The Models Are Good Now
* [00:01:20] – How Context Windows Actually Work
* [00:04:55] – The Power of Skills
* [00:09:17] – How to create Skills
* [00:16:35] – Skill Maxxing
* [00:19:05] – What you need too build a project
* [00:20:40] – Recursively Building and Improving Skills
* [00:29:23] – Context Window Management and Token Efficiency
* [00:33:02] – Closing Thoughts

# Transcript

1
00:00:00,000 --> 00:00:01,920
Ross, Mike, welcome back to the pod. By

2
00:00:01,920 --> 00:00:03,480
the end of this episode, what are people

3
00:00:03,480 --> 00:00:04,200
going to learn?

4
00:00:04,200 --> 00:00:06,560
>> I hope I'm going to share some wisdom on

5
00:00:06,560 --> 00:00:08,520
how you can use the agents better.

6
00:00:08,520 --> 00:00:10,520
There's a lot of information going on

7
00:00:10,520 --> 00:00:13,160
right now. I disagree with most of it,

8
00:00:13,160 --> 00:00:14,200
and that's what we're going to talk

9
00:00:14,200 --> 00:00:15,600
about. So, at the end, whether you're

10
00:00:15,600 --> 00:00:17,080
building something, [music] using an

11
00:00:17,080 --> 00:00:19,200
agent for some sort of work, you have

12
00:00:19,200 --> 00:00:20,560
the best outcome possible.

13
00:00:20,560 --> 00:00:21,200
>> And is this going [music] to be a

14
00:00:21,200 --> 00:00:23,760
technical dive or, you know,

15
00:00:23,760 --> 00:00:25,400
non-technical person can

16
00:00:25,400 --> 00:00:26,760
>> Anyone can watch this. There's going to

17
00:00:26,760 --> 00:00:28,820
be a lot of diagrams. That's all.

18
00:00:28,820 --> 00:00:29,240
>> [laughter]

19
00:00:29,240 --> 00:00:30,240
>> You're going to make it clear to

20
00:00:30,240 --> 00:00:31,840
understand the concepts, right?

21
00:00:31,840 --> 00:00:32,320
>> Easy.

22
00:00:32,320 --> 00:00:33,120
>> Okay.

23
00:00:33,120 --> 00:00:33,120
>> Basics.

24
00:00:33,120 --> 00:00:33,880
>> Let's go.

25
00:00:33,880 --> 00:00:36,400
>> So,

26
00:00:37,990 --> 00:00:40,010
>> [music]

27
00:00:42,640 --> 00:00:44,760
>> the first thing that I want to announce,

28
00:00:44,760 --> 00:00:46,920
previous episodes, we probably disagree

29
00:00:46,920 --> 00:00:48,640
with this point, but now

30
00:00:48,640 --> 00:00:50,600
what's true is the models are good.

31
00:00:50,600 --> 00:00:52,640
The models are exceptionally good. Opus

32
00:00:52,640 --> 00:00:55,680
4.6 is amazing. GPT 5.4 is amazing. I

33
00:00:55,680 --> 00:00:56,960
know there's like two sets of camp

34
00:00:56,960 --> 00:00:58,480
where, especially when it comes to

35
00:00:58,480 --> 00:01:00,000
programming, people are like, "Oh, Opus

36
00:01:00,000 --> 00:01:02,560
is the better UI designer. GPT 5.4 is

37
00:01:02,560 --> 00:01:04,600
the better back end." Generally

38
00:01:04,600 --> 00:01:06,280
speaking, we've reached a point We're

39
00:01:06,280 --> 00:01:08,200
not at AGI yet. Well, we reached a point

40
00:01:08,200 --> 00:01:10,160
where the models are good.

41
00:01:10,160 --> 00:01:13,280
But, context still matters, and you have

42
00:01:13,280 --> 00:01:15,360
the power to steer the models in a

43
00:01:15,360 --> 00:01:17,000
direction where you can get quality or

44
00:01:17,000 --> 00:01:19,360
you can get slop. And that's what I

45
00:01:19,360 --> 00:01:21,680
really want to talk about. But, before

46
00:01:21,680 --> 00:01:22,920
we get into all that, and feel free to

47
00:01:22,920 --> 00:01:25,400
cut me off cuz this topic excites me. Um

48
00:01:25,400 --> 00:01:28,600
we need to learn how context works. And

49
00:01:28,600 --> 00:01:31,760
context is the model assembling

50
00:01:31,760 --> 00:01:33,880
information that it needs to execute an

51
00:01:33,880 --> 00:01:36,000
action. And the way the context is

52
00:01:36,000 --> 00:01:37,600
assembled, let's say in a coding agent,

53
00:01:37,600 --> 00:01:40,000
but really in any sort of agent, is

54
00:01:40,000 --> 00:01:41,720
there's this general system prompt,

55
00:01:41,720 --> 00:01:43,640
usually by the model provider. So, for

56
00:01:43,640 --> 00:01:46,360
example, Claude code leaked recently,

57
00:01:46,360 --> 00:01:48,280
and one of the cool things that, um

58
00:01:48,280 --> 00:01:49,600
especially as a developer, I got to do

59
00:01:49,600 --> 00:01:51,440
is I got to read the system prompt. So,

60
00:01:51,440 --> 00:01:52,920
they have this general system prompt

61
00:01:52,920 --> 00:01:54,880
that guides the model on how to act,

62
00:01:54,880 --> 00:01:56,880
what to do, what not to do. The system

63
00:01:56,880 --> 00:01:58,880
prompt is very important. And then you

64
00:01:58,880 --> 00:02:01,360
have a lot of people have agent.md files

65
00:02:01,360 --> 00:02:03,360
or cloud.md files. Now, I'm just going

66
00:02:03,360 --> 00:02:04,840
to say off rip,

67
00:02:04,840 --> 00:02:07,320
95% of people don't need this.

68
00:02:07,320 --> 00:02:09,600
The reason being is, again, you have to

69
00:02:09,600 --> 00:02:12,120
assume that the models are already good,

70
00:02:12,120 --> 00:02:14,840
right? Now, imagine I told you, Greg,

71
00:02:14,840 --> 00:02:15,720
every time we're about to shoot a

72
00:02:15,720 --> 00:02:19,160
podcast, Greg, you need a microphone.

73
00:02:19,160 --> 00:02:20,280
You know you need a microphone, right?

74
00:02:20,280 --> 00:02:21,840
You've done this plenty of times, right?

75
00:02:21,840 --> 00:02:24,360
So, if I'm building, like, let's say a

76
00:02:24,360 --> 00:02:27,520
website with, uh, cloud code, and I'm

77
00:02:27,520 --> 00:02:29,680
telling cloud code, "This code base uses

78
00:02:29,680 --> 00:02:32,120
React." I don't need to, because it has

79
00:02:32,120 --> 00:02:33,959
the code base in context. It can check

80
00:02:33,959 --> 00:02:36,240
the code, right? So, there is this

81
00:02:36,240 --> 00:02:38,800
disparity where a lot of people are

82
00:02:38,800 --> 00:02:41,000
putting a lot of onus on the harness and

83
00:02:41,000 --> 00:02:43,720
the context building, and I'm low-key

84
00:02:43,720 --> 00:02:45,800
starting to strip things off. Like, I'm

85
00:02:45,800 --> 00:02:48,040
going super, super minimal, because,

86
00:02:48,040 --> 00:02:50,360
again, not to sound like a Anthropic or

87
00:02:50,360 --> 00:02:52,040
OpenAI shill. Unfortunately, I have not

88
00:02:52,040 --> 00:02:53,920
been acquired. None of them are paying

89
00:02:53,920 --> 00:02:54,800
me.

90
00:02:54,800 --> 00:02:56,160
Um, but the models are really, really

91
00:02:56,160 --> 00:02:57,160
good.

92
00:02:57,160 --> 00:02:59,600
>> Wait, so 95% of the time I don't even

93
00:02:59,600 --> 00:03:02,080
need a bot bother with an agent.md file?

94
00:03:02,080 --> 00:03:03,920
>> You don't. Like, it unless this is some

95
00:03:03,920 --> 00:03:05,920
sort of proprietary information.

96
00:03:05,920 --> 00:03:08,040
>> Yeah, what is the 5% of of time I should

97
00:03:08,040 --> 00:03:08,519
care about it?

98
00:03:08,519 --> 00:03:10,519
>> Proprietary information that, like,

99
00:03:10,519 --> 00:03:12,480
maybe specific to your company or some

100
00:03:12,480 --> 00:03:14,800
methodology that is specific to you that

101
00:03:14,800 --> 00:03:16,959
has to be referenced in every single

102
00:03:16,959 --> 00:03:18,600
conversation, cuz the annoying part with

103
00:03:18,600 --> 00:03:21,000
an agent.md file is every time you go

104
00:03:21,000 --> 00:03:22,880
back and forth with the agent, it's

105
00:03:22,880 --> 00:03:25,440
added in the context, right? The cool

106
00:03:25,440 --> 00:03:26,640
thing about skills, and I'm going to

107
00:03:26,640 --> 00:03:28,600
talk about skills in a second, the way

108
00:03:28,600 --> 00:03:32,680
skills are designed, the skills are used

109
00:03:32,680 --> 00:03:34,160
in a way that's called progressive

110
00:03:34,160 --> 00:03:35,840
disclosure, meaning, when you have a

111
00:03:35,840 --> 00:03:37,880
skill file, the entire thing isn't added

112
00:03:37,880 --> 00:03:39,959
to context. It's just the title and the

113
00:03:39,959 --> 00:03:42,920
description. So, the agent has the title

114
00:03:42,920 --> 00:03:45,160
and description in the context, and when

115
00:03:45,160 --> 00:03:47,280
you, let's say you have a notion report

116
00:03:47,280 --> 00:03:49,160
skill, right? And you tell your agent,

117
00:03:49,160 --> 00:03:50,880
"Hey, I want you to create a notion

118
00:03:50,880 --> 00:03:53,160
report." It's then going to check its

119
00:03:53,160 --> 00:03:55,000
context and be like, "Oh, I have this

120
00:03:55,000 --> 00:03:57,200
skill. Let me check out the entire

121
00:03:57,200 --> 00:04:00,080
document." So, it's not in the context,

122
00:04:00,080 --> 00:04:02,080
what's in the context is the name and

123
00:04:02,080 --> 00:04:04,000
the description, but that's enough for

124
00:04:04,000 --> 00:04:05,240
the agent to be like, "Oh, this is a

125
00:04:05,240 --> 00:04:07,320
skill I need. Let me go use it." Which

126
00:04:07,320 --> 00:04:09,959
is fantastic. I'm a skills maxi, and I'm

127
00:04:09,959 --> 00:04:11,920
going to show later in the episode like

128
00:04:11,920 --> 00:04:14,080
how you craft the perfect skills. But,

129
00:04:14,080 --> 00:04:16,840
with agent.md and claw.md files, its

130
00:04:16,840 --> 00:04:19,239
context being added at every turn,

131
00:04:19,239 --> 00:04:20,680
right? So, let's say you have like a

132
00:04:20,680 --> 00:04:24,280
thousand line file claw.md, and let's

133
00:04:24,280 --> 00:04:26,400
say that's like 7,000 tokens. You're

134
00:04:26,400 --> 00:04:29,840
spending 7,000 tokens on every run. Now,

135
00:04:29,840 --> 00:04:32,240
do you need to? Most likely not. It

136
00:04:32,240 --> 00:04:33,840
probably should be a skill, but if you

137
00:04:33,840 --> 00:04:35,919
have some sort of company proprietary

138
00:04:35,919 --> 00:04:37,880
information, or like there's something

139
00:04:37,880 --> 00:04:40,040
specific that you do that the model

140
00:04:40,040 --> 00:04:41,919
needs to know at every single turn, then

141
00:04:41,919 --> 00:04:44,919
you use it. The thing is 95% of people

142
00:04:44,919 --> 00:04:47,440
don't have that, right? So, I'm not a

143
00:04:47,440 --> 00:04:50,440
fan unless that's the case. So, and and

144
00:04:50,440 --> 00:04:52,160
and the reason being is we're wasting

145
00:04:52,160 --> 00:04:55,160
tokens, right? It's in every single

146
00:04:55,160 --> 00:04:56,160
turn.

147
00:04:56,160 --> 00:04:57,560
But, this is where the beauty of skills

148
00:04:57,560 --> 00:05:00,840
come. Um I'll show my screen here.

149
00:05:00,840 --> 00:05:02,919
The your skill, again, this is not like

150
00:05:02,919 --> 00:05:05,360
word for word how it looks, but a skill

151
00:05:05,360 --> 00:05:07,800
basically looks like this. There is a

152
00:05:07,800 --> 00:05:10,680
name, there is a description,

153
00:05:10,680 --> 00:05:12,440
and then underneath

154
00:05:12,440 --> 00:05:14,600
is a bunch of information. I'm going to

155
00:05:14,600 --> 00:05:16,880
put bunch of info.

156
00:05:16,880 --> 00:05:19,880
What When you create a skill.md file,

157
00:05:19,880 --> 00:05:22,520
what gets added into the context is

158
00:05:22,520 --> 00:05:23,600
actually just the name and the

159
00:05:23,600 --> 00:05:24,919
description,

160
00:05:24,919 --> 00:05:27,400
right? The bunch of info doesn't get

161
00:05:27,400 --> 00:05:29,720
added. So, imagine you have two

162
00:05:29,720 --> 00:05:32,480
sentences versus an agent.md that has

163
00:05:32,480 --> 00:05:34,480
like a thousand lines that get added

164
00:05:34,480 --> 00:05:36,000
into the context. We're talking

165
00:05:36,000 --> 00:05:38,240
thousands of tokens compared to a couple

166
00:05:38,240 --> 00:05:40,800
hundred. And the agent only gets the

167
00:05:40,800 --> 00:05:43,520
bunch of info when it realizes it needs

168
00:05:43,520 --> 00:05:46,440
this skill. So, if I have, let's say, a

169
00:05:46,440 --> 00:05:48,120
certain way of generating a report, a

170
00:05:48,120 --> 00:05:50,360
certain way of structuring my code,

171
00:05:50,360 --> 00:05:52,160
why would I put that in the agent.md

172
00:05:52,160 --> 00:05:55,200
file when I can have the agent call on

173
00:05:55,200 --> 00:05:57,200
it progressively when it needs it,

174
00:05:57,200 --> 00:05:59,800
right? So, this is why skills are

175
00:05:59,800 --> 00:06:02,360
honestly, like I'm a shill, I'm a maxi,

176
00:06:02,360 --> 00:06:03,920
but people do it wrong and I'm going to

177
00:06:03,920 --> 00:06:06,000
share the right way on how do we create

178
00:06:06,000 --> 00:06:08,280
skills. So, so far we have the system

179
00:06:08,280 --> 00:06:10,960
prompt, the agent.md, the skills, and

180
00:06:10,960 --> 00:06:12,240
then we have the tools, right? So, if

181
00:06:12,240 --> 00:06:14,040
you're using cloud code, there's already

182
00:06:14,040 --> 00:06:15,680
built-in tools that read tool or write

183
00:06:15,680 --> 00:06:17,680
tool. Like there's many tools that it

184
00:06:17,680 --> 00:06:19,200
uses. This has to be added into the

185
00:06:19,200 --> 00:06:21,640
context because the model the model

186
00:06:21,640 --> 00:06:23,520
doesn't call the tools. It like it's the

187
00:06:23,520 --> 00:06:25,160
agent harness around it that allows it

188
00:06:25,160 --> 00:06:26,560
to call the tools.

189
00:06:26,560 --> 00:06:28,280
And then in this case, we also have our

190
00:06:28,280 --> 00:06:30,080
code base, right? Like whatever if we're

191
00:06:30,080 --> 00:06:32,240
building a web app, a mobile app. I know

192
00:06:32,240 --> 00:06:33,520
most people here won't care for the

193
00:06:33,520 --> 00:06:35,360
specific framework and honestly, we're

194
00:06:35,360 --> 00:06:36,440
getting to a point if you're not

195
00:06:36,440 --> 00:06:38,800
technical, you really shouldn't.

196
00:06:38,800 --> 00:06:40,120
Um and then we have the user

197
00:06:40,120 --> 00:06:42,560
conversation. So, this is what

198
00:06:42,560 --> 00:06:44,400
the complete context window is filled

199
00:06:44,400 --> 00:06:47,040
with, right? And this can total up to

200
00:06:47,040 --> 00:06:48,919
let's say like at the beginning this

201
00:06:48,919 --> 00:06:51,680
could be like 20,000 tokens and as the

202
00:06:51,680 --> 00:06:53,840
conversation continues to grow, you

203
00:06:53,840 --> 00:06:56,600
might reach your limit of 25 250,000

204
00:06:56,600 --> 00:06:59,120
tokens and that's when you see both

205
00:06:59,120 --> 00:07:01,080
cloud code and open AI codex they

206
00:07:01,080 --> 00:07:03,320
they'll compact, right? So, beautiful so

207
00:07:03,320 --> 00:07:06,280
far, right? This is how context works.

208
00:07:06,280 --> 00:07:08,120
Why skills are important and how you

209
00:07:08,120 --> 00:07:10,520
should generate skills.

210
00:07:10,520 --> 00:07:12,400
Let's say I have a specific workflow.

211
00:07:12,400 --> 00:07:14,160
For example, for my YouTube channel, you

212
00:07:14,160 --> 00:07:16,520
know, we're at a point right now Greg

213
00:07:16,520 --> 00:07:18,800
where we get sponsors now. Crazy. When I

214
00:07:18,800 --> 00:07:20,840
first joined this not when I first came

215
00:07:20,840 --> 00:07:22,680
to the pod not a thing. We get sponsors

216
00:07:22,680 --> 00:07:23,840
now. It was just your mom sponsoring the

217
00:07:23,840 --> 00:07:24,840
channel. Yeah, yeah, yeah, it was just

218
00:07:24,840 --> 00:07:27,640
her showing love, feeding me. Uh but now

219
00:07:27,640 --> 00:07:29,480
we get sponsors. I get a lot of emails

220
00:07:29,480 --> 00:07:32,200
and some are good, some are bad and it's

221
00:07:32,200 --> 00:07:33,760
a lot of time I'm sure you're aware to

222
00:07:33,760 --> 00:07:36,240
comb through and to check. So, I have an

223
00:07:36,240 --> 00:07:39,400
open cloud agent that has its own email,

224
00:07:39,400 --> 00:07:41,320
right? I I I have it I don't I given it

225
00:07:41,320 --> 00:07:43,840
access to my email, uh cuz there's like

226
00:07:43,840 --> 00:07:45,160
attack vectors and I've been hacked

227
00:07:45,160 --> 00:07:46,800
before, so I'm very careful with these

228
00:07:46,800 --> 00:07:49,160
things, but it has its own email. And

229
00:07:49,160 --> 00:07:50,640
every time I get an email from like a

230
00:07:50,640 --> 00:07:53,720
sponsor, I forward that email to the

231
00:07:53,720 --> 00:07:56,600
agent. Now, the first time I told my

232
00:07:56,600 --> 00:07:57,840
Open Cloud agent, "I'm going to forward

233
00:07:57,840 --> 00:08:00,160
you emails. Check every 15 minutes when

234
00:08:00,160 --> 00:08:01,600
you have an email.

235
00:08:01,600 --> 00:08:02,840
Um and when you check the email, do

236
00:08:02,840 --> 00:08:04,360
research on the sponsor and tell me if

237
00:08:04,360 --> 00:08:05,760
they're worth it."

238
00:08:05,760 --> 00:08:07,760
That's all I told the agent.

239
00:08:07,760 --> 00:08:09,400
Every sponsor email I sent it, it was

240
00:08:09,400 --> 00:08:11,920
like legit, legit, legit, perfect,

241
00:08:11,920 --> 00:08:15,360
perfect, perfect. There was no like the

242
00:08:15,360 --> 00:08:16,800
There was no rejection. There's no this

243
00:08:16,800 --> 00:08:18,600
is bad or these guys are a scam or this

244
00:08:18,600 --> 00:08:20,320
product's not good. Like there was no

245
00:08:20,320 --> 00:08:22,440
deep research being done by it. So, then

246
00:08:22,440 --> 00:08:25,240
I realized, "Huh, okay. The model needs

247
00:08:25,240 --> 00:08:27,760
a step-by-step guide."

248
00:08:27,760 --> 00:08:29,680
This is when I create a skill. But

249
00:08:29,680 --> 00:08:32,560
here's the problem. A lot of people will

250
00:08:32,560 --> 00:08:34,080
I'll just write it down here will

251
00:08:34,080 --> 00:08:35,640
identify

252
00:08:35,640 --> 00:08:38,719
uh identify they have a workflow, right?

253
00:08:38,719 --> 00:08:40,520
You have some sort of workflow. And then

254
00:08:40,520 --> 00:08:41,840
they'll jump to create the skill right

255
00:08:41,840 --> 00:08:43,000
away.

256
00:08:43,000 --> 00:08:46,280
This is the Let me click hide here. This

257
00:08:46,280 --> 00:08:47,920
is the worst thing you can do. I'm just

258
00:08:47,920 --> 00:08:50,400
going to draw arrows to signify

259
00:08:50,400 --> 00:08:52,720
that this is bad. You don't do these.

260
00:08:52,720 --> 00:08:55,839
And the reason why you don't do this is

261
00:08:55,839 --> 00:08:57,800
imagine

262
00:08:57,800 --> 00:08:59,440
you hire an employee or you're mentoring

263
00:08:59,440 --> 00:09:00,680
somebody.

264
00:09:00,680 --> 00:09:02,640
Um correct me if I'm wrong.

265
00:09:02,640 --> 00:09:05,200
You're probably going to tell them what

266
00:09:05,200 --> 00:09:06,560
to do.

267
00:09:06,560 --> 00:09:08,040
And if they ask you questions on how to

268
00:09:08,040 --> 00:09:10,000
do it, you'll help them. You would

269
00:09:10,000 --> 00:09:12,280
ideally like them to fail and then you

270
00:09:12,280 --> 00:09:13,720
want to then tell them, "No, this is how

271
00:09:13,720 --> 00:09:15,640
you do it." Like there needs to be some

272
00:09:15,640 --> 00:09:17,800
sort of experiential learning. The way

273
00:09:17,800 --> 00:09:19,760
I've been creating skills, Greg, and I

274
00:09:19,760 --> 00:09:21,440
have like a 100% hit rate now when I

275
00:09:21,440 --> 00:09:23,760
tell my agent to do something specific

276
00:09:23,760 --> 00:09:26,920
is I actually walk with it step-by-step

277
00:09:26,920 --> 00:09:29,080
on doing the workflow. So, in the case

278
00:09:29,080 --> 00:09:32,560
of my YouTube uh analysis, I told the

279
00:09:32,560 --> 00:09:34,200
agent, "Okay, I just sent you an email.

280
00:09:34,200 --> 00:09:35,800
Tell me about the company." Company's

281
00:09:35,800 --> 00:09:37,600
this, this, that, and that. Okay, their

282
00:09:37,600 --> 00:09:39,480
Twitter, check their YouTube, check

283
00:09:39,480 --> 00:09:41,320
their Trustpilot, check if they raised

284
00:09:41,320 --> 00:09:44,840
any money. If two of these are have not

285
00:09:44,840 --> 00:09:46,280
If two of these don't exist or not in

286
00:09:46,280 --> 00:09:48,800
good standing, automatic rejection. It

287
00:09:48,800 --> 00:09:49,600
checked and it was like, "You're

288
00:09:49,600 --> 00:09:51,760
absolutely right." I was using Opus.

289
00:09:51,760 --> 00:09:54,800
Um these uh this is not a good company.

290
00:09:54,800 --> 00:09:56,600
And then it would just we would We have

291
00:09:56,600 --> 00:09:58,560
a spreadsheet in Google Sheets. It'd be

292
00:09:58,560 --> 00:09:59,840
like, "No contact."

293
00:09:59,840 --> 00:10:01,360
>> It's so frustrating too, right? Cuz

294
00:10:01,360 --> 00:10:04,760
you're like you give it a task and it

295
00:10:04,760 --> 00:10:06,600
seems like so binary, like right or

296
00:10:06,600 --> 00:10:09,720
wrong. And then when you tell it, "Hey,

297
00:10:09,720 --> 00:10:10,960
like why didn't you look at the

298
00:10:10,960 --> 00:10:12,560
Trustpilot? Why didn't you see if

299
00:10:12,560 --> 00:10:13,920
they've raised money?" "You're

300
00:10:13,920 --> 00:10:15,000
absolutely right."

301
00:10:15,000 --> 00:10:15,520
>> absolutely

302
00:10:15,520 --> 00:10:17,160
>> It's like, "What?"

303
00:10:17,160 --> 00:10:18,760
>> And And the thing is the reason why this

304
00:10:18,760 --> 00:10:22,080
is the case is the models uh actually

305
00:10:22,080 --> 00:10:24,120
don't think. They're predictors of

306
00:10:24,120 --> 00:10:26,320
tokens, right? So, when you give it

307
00:10:26,320 --> 00:10:27,880
English, when I give it English, it maps

308
00:10:27,880 --> 00:10:29,720
it on this vector graph and then it

309
00:10:29,720 --> 00:10:31,440
looks for the closest resemblance and it

310
00:10:31,440 --> 00:10:33,480
says, "This is the response," right? So,

311
00:10:33,480 --> 00:10:34,840
when you say, "What is the capital of

312
00:10:34,840 --> 00:10:37,120
France?" It maps it again on this graph

313
00:10:37,120 --> 00:10:38,520
and it says, "Oh, Paris is pretty close

314
00:10:38,520 --> 00:10:40,880
by." Then it gives you Paris. It has no

315
00:10:40,880 --> 00:10:42,920
It doesn't think. It doesn't understand.

316
00:10:42,920 --> 00:10:44,600
It feels like it understands. It feels

317
00:10:44,600 --> 00:10:46,440
like it thinks. Heck, it even feels like

318
00:10:46,440 --> 00:10:48,200
it has emotion. That's because it's been

319
00:10:48,200 --> 00:10:50,680
trained on so much data. But it actually

320
00:10:50,680 --> 00:10:52,280
does not know how to think. And this is

321
00:10:52,280 --> 00:10:55,400
where a lot of people be frustrated um

322
00:10:55,400 --> 00:10:56,800
with like, "Why is it not understanding

323
00:10:56,800 --> 00:10:59,280
me?" You have to walk with it. So, I

324
00:10:59,280 --> 00:11:00,320
told it, "Okay, this is how you

325
00:11:00,320 --> 00:11:01,880
research." And it's like, "Okay." It

326
00:11:01,880 --> 00:11:03,240
researches. And guess what? This is part

327
00:11:03,240 --> 00:11:05,000
of the context. And I'm like, "Okay, now

328
00:11:05,000 --> 00:11:06,560
that you're done researching, when it's

329
00:11:06,560 --> 00:11:08,120
a good company, these are the qualities

330
00:11:08,120 --> 00:11:09,960
you look for. And then when it's really

331
00:11:09,960 --> 00:11:12,120
good, send me an email."

332
00:11:12,120 --> 00:11:14,160
And then once we had a successful run

333
00:11:14,160 --> 00:11:16,800
and we did it again and again, then I

334
00:11:16,800 --> 00:11:18,640
converted it to a skill.

335
00:11:18,640 --> 00:11:20,280
Or the reason being is a lot of people

336
00:11:20,280 --> 00:11:21,960
create the skills themselves or I I

337
00:11:21,960 --> 00:11:23,280
mean, they'll use the AI to create the

338
00:11:23,280 --> 00:11:25,240
skill, but it doesn't have the context

339
00:11:25,240 --> 00:11:27,320
on what a successful run looks like.

340
00:11:27,320 --> 00:11:28,560
Right? Cuz most of the time, especially

341
00:11:28,560 --> 00:11:30,160
if you're using Open Claw, it's probably

342
00:11:30,160 --> 00:11:32,000
going to fail at the API call. It's

343
00:11:32,000 --> 00:11:33,800
probably going to call the data wrong.

344
00:11:33,800 --> 00:11:35,280
Like there's so many places it's going

345
00:11:35,280 --> 00:11:36,560
to get wrong and I see a lot of people

346
00:11:36,560 --> 00:11:38,080
saying, "It's just so frustrating. This

347
00:11:38,080 --> 00:11:39,600
is terrible technology. Why doesn't it

348
00:11:39,600 --> 00:11:41,160
work?" It's cuz you don't understand how

349
00:11:41,160 --> 00:11:43,600
an agent works, right? It will mimic you

350
00:11:43,600 --> 00:11:45,600
perfectly, but you've given it nothing

351
00:11:45,600 --> 00:11:48,760
to mimic, right? So, I will

352
00:11:48,760 --> 00:11:50,960
do the workflow myself. So, the the

353
00:11:50,960 --> 00:11:52,640
updated version is identify the

354
00:11:52,640 --> 00:11:53,880
workflow,

355
00:11:53,880 --> 00:11:55,920
go back

356
00:11:55,920 --> 00:11:58,880
and forth and teach it. So, like I'm

357
00:11:58,880 --> 00:12:00,480
doing it like I'll be like, "Okay, first

358
00:12:00,480 --> 00:12:03,120
do the research." Here's the result. And

359
00:12:03,120 --> 00:12:04,240
I'll be like, "What do you think about

360
00:12:04,240 --> 00:12:05,640
this?" "Oh, these guys are terrible."

361
00:12:05,640 --> 00:12:07,440
You're absolutely right. "Okay, what do

362
00:12:07,440 --> 00:12:09,440
you you should go to the Google Sheet

363
00:12:09,440 --> 00:12:11,520
and mark this as bad company."

364
00:12:11,520 --> 00:12:13,400
I've done that. Once I've had that back

365
00:12:13,400 --> 00:12:16,400
and forth, then I tell the AI,

366
00:12:16,400 --> 00:12:17,440
uh

367
00:12:17,440 --> 00:12:20,680
"Review what you did

368
00:12:20,680 --> 00:12:22,960
and then create the skill." So, now it

369
00:12:22,960 --> 00:12:26,040
has actual context with how it worked

370
00:12:26,040 --> 00:12:27,240
and it's going to create the skill

371
00:12:27,240 --> 00:12:28,600
beautifully. I don't handwrite skills. I

372
00:12:28,600 --> 00:12:30,480
don't think you need to. You can use AI

373
00:12:30,480 --> 00:12:32,040
to do it. They even have a skill to

374
00:12:32,040 --> 00:12:34,960
create skills. Skill inception.

375
00:12:34,960 --> 00:12:37,080
But, you should have the context of what

376
00:12:37,080 --> 00:12:39,280
a successful run looks like. And this is

377
00:12:39,280 --> 00:12:42,360
why, by the way, I don't install skills.

378
00:12:42,360 --> 00:12:43,520
Like I've seen people like, "Oh, this

379
00:12:43,520 --> 00:12:45,320
Notion skill, this social media skill,

380
00:12:45,320 --> 00:12:46,680
whatever." I'll I'll I'll review it.

381
00:12:46,680 --> 00:12:48,240
I'll check it out. I'll even give it to

382
00:12:48,240 --> 00:12:49,280
my AI and be like, "Oh, what are some

383
00:12:49,280 --> 00:12:50,960
things we can learn from this?" But, I

384
00:12:50,960 --> 00:12:53,600
don't download skills because your agent

385
00:12:53,600 --> 00:12:55,760
needs the context of a successful run,

386
00:12:55,760 --> 00:12:58,600
which you then turn to skills, right? Um

387
00:12:58,600 --> 00:12:59,960
and this is the big thing I see. You see

388
00:12:59,960 --> 00:13:02,200
skills marketplaces. You see download

389
00:13:02,200 --> 00:13:04,920
this and that. First of all, it's a easy

390
00:13:04,920 --> 00:13:07,280
way to attack somebody. So, I would be

391
00:13:07,280 --> 00:13:10,160
very, very careful with downloading some

392
00:13:10,160 --> 00:13:11,680
random person's skills.

393
00:13:11,680 --> 00:13:13,440
But, second of all, again, it's all

394
00:13:13,440 --> 00:13:16,120
about context, right? It's all about and

395
00:13:16,120 --> 00:13:17,680
you know, Open Claw has a memory layer

396
00:13:17,680 --> 00:13:20,120
and all these type of things. You want

397
00:13:20,120 --> 00:13:22,320
it to do the right thing and the only

398
00:13:22,320 --> 00:13:24,040
way it can do the right thing is if you

399
00:13:24,040 --> 00:13:26,120
give it the proper context. And to me,

400
00:13:26,120 --> 00:13:28,880
the best way to create a skill is to

401
00:13:28,880 --> 00:13:31,440
work with it in your specific workflow.

402
00:13:31,440 --> 00:13:33,200
Once you have a successful run, tell it,

403
00:13:33,200 --> 00:13:34,920
"Okay, review what you just did. This is

404
00:13:34,920 --> 00:13:36,640
the skill you need to create." I'll

405
00:13:36,640 --> 00:13:37,320
pause here.

406
00:13:37,320 --> 00:13:40,480
>> I mean, it makes sense, right? Cuz

407
00:13:40,480 --> 00:13:43,120
if you hired an employee, you would do

408
00:13:43,120 --> 00:13:43,880
the same thing.

409
00:13:43,880 --> 00:13:44,280
>> Yeah.

410
00:13:44,280 --> 00:13:45,680
>> You wouldn't You wouldn't just be like,

411
00:13:45,680 --> 00:13:47,440
"Okay, go do this thing. Good luck."

412
00:13:47,440 --> 00:13:48,120
>> Yeah.

413
00:13:48,120 --> 00:13:49,520
>> Uh and by the way, this is how you're

414
00:13:49,520 --> 00:13:51,440
going to go do things forever. You would

415
00:13:51,440 --> 00:13:55,160
map out a workflow. You would identify

416
00:13:55,160 --> 00:13:58,320
what right and wrong is. You would

417
00:13:58,320 --> 00:14:00,280
uh do it iteratively.

418
00:14:00,280 --> 00:14:02,320
And then, once you've gotten to that

419
00:14:02,320 --> 00:14:03,600
point, you would codify it.

420
00:14:03,600 --> 00:14:05,920
>> 100% and I think like that's the thing.

421
00:14:05,920 --> 00:14:08,320
Like, we should treat models and these

422
00:14:08,320 --> 00:14:12,800
agents like very new employees versus

423
00:14:12,800 --> 00:14:15,520
like these black magic boxes that like

424
00:14:15,520 --> 00:14:17,280
know everything, right? They know

425
00:14:17,280 --> 00:14:18,480
everything because they've been trained

426
00:14:18,480 --> 00:14:20,560
on a lot of data, but they don't know

427
00:14:20,560 --> 00:14:23,080
your workflow, your steps, right? So, I

428
00:14:23,080 --> 00:14:25,720
see a lot of people who have you know,

429
00:14:25,720 --> 00:14:27,600
15 like right off the they'll set up

430
00:14:27,600 --> 00:14:32,080
open claw and um 15 sub agents, 30

431
00:14:32,080 --> 00:14:33,320
skills.

432
00:14:33,320 --> 00:14:34,800
Yet, you haven't even set up your own

433
00:14:34,800 --> 00:14:36,320
workflows, right? And these things are

434
00:14:36,320 --> 00:14:37,880
cool right off the bat and and there's a

435
00:14:37,880 --> 00:14:39,640
perfect time to use sub agents. I use

436
00:14:39,640 --> 00:14:41,560
sub agents a lot.

437
00:14:41,560 --> 00:14:44,120
But, the way you build like I call it

438
00:14:44,120 --> 00:14:46,400
scaling for productivity, not scaling

439
00:14:46,400 --> 00:14:48,640
for what looks cool, right? Like, I've

440
00:14:48,640 --> 00:14:50,000
seen like for example, paper claw. Paper

441
00:14:50,000 --> 00:14:52,680
claw looks awesome. Cool. I used it. I

442
00:14:52,680 --> 00:14:54,800
loved it, right? But, I think people

443
00:14:54,800 --> 00:14:56,680
would be more productive if they built

444
00:14:56,680 --> 00:14:59,960
up from scratch their own version.

445
00:14:59,960 --> 00:15:01,560
Meaning like, okay, you have your own

446
00:15:01,560 --> 00:15:02,680
like

447
00:15:02,680 --> 00:15:03,240
um

448
00:15:03,240 --> 00:15:05,320
you know, like editor, right? Content

449
00:15:05,320 --> 00:15:05,760
creator.

450
00:15:05,760 --> 00:15:07,160
>> So, you're You're asking people to do

451
00:15:07,160 --> 00:15:08,000
the work, basically.

452
00:15:08,000 --> 00:15:09,920
>> 100% 100% and cuz the thing is, it's

453
00:15:09,920 --> 00:15:10,800
like

454
00:15:10,800 --> 00:15:13,400
look, I'm in the position where like

455
00:15:13,400 --> 00:15:15,880
people using like these beefed-up things

456
00:15:15,880 --> 00:15:18,120
make a lot more sense for me. And the

457
00:15:18,120 --> 00:15:19,240
reason being is like I could build a

458
00:15:19,240 --> 00:15:21,160
product like that. Like, I know what

459
00:15:21,160 --> 00:15:22,440
your audience wants. I know what my

460
00:15:22,440 --> 00:15:24,040
audience wants. Like, you know, heck, I

461
00:15:24,040 --> 00:15:25,520
could spin up agents and build this

462
00:15:25,520 --> 00:15:27,040
thing, right? But, if I'm going to be

463
00:15:27,040 --> 00:15:28,560
completely honest, if you want to scale

464
00:15:28,560 --> 00:15:30,400
for productivity, it starts with one

465
00:15:30,400 --> 00:15:32,560
agent and you building up the skills.

466
00:15:32,560 --> 00:15:34,160
And then, okay, now you've built up some

467
00:15:34,160 --> 00:15:36,200
skills and now you add a sub agent and

468
00:15:36,200 --> 00:15:38,280
your one agent manages multiple agents.

469
00:15:38,280 --> 00:15:40,520
Right? Like, imagine this. Like, imagine

470
00:15:40,520 --> 00:15:43,440
I start a company and off rip, I have 10

471
00:15:43,440 --> 00:15:44,760
employees.

472
00:15:44,760 --> 00:15:47,240
Never managed a team in my life. Heck, I

473
00:15:47,240 --> 00:15:49,440
don't even have a really big family. So,

474
00:15:49,440 --> 00:15:50,560
like, I'm a little Like, you know what I

475
00:15:50,560 --> 00:15:53,800
mean? So, it's like you have to sort of

476
00:15:53,800 --> 00:15:56,040
Yeah, it's not sexy. Um and I apologize

477
00:15:56,040 --> 00:15:57,640
if this is not the cool thing people

478
00:15:57,640 --> 00:15:59,240
wanted to hear. But, you sort of have to

479
00:15:59,240 --> 00:16:00,760
put in the work and build it up. And I

480
00:16:00,760 --> 00:16:02,840
And I personally believe you're building

481
00:16:02,840 --> 00:16:04,680
skills, like, your personal human

482
00:16:04,680 --> 00:16:06,240
skills, not

483
00:16:06,240 --> 00:16:08,560
skill that MD files, that when the

484
00:16:08,560 --> 00:16:10,080
models get better, when the agents get

485
00:16:10,080 --> 00:16:12,120
better, you will be more valuable cuz at

486
00:16:12,120 --> 00:16:14,080
the end of the day, as long as there's

487
00:16:14,080 --> 00:16:16,920
no new paradigm for models, LLMs just

488
00:16:16,920 --> 00:16:18,560
predict tokens.

489
00:16:18,560 --> 00:16:20,640
They don't understand or know the way

490
00:16:20,640 --> 00:16:22,880
you and I do, right? And this is why

491
00:16:22,880 --> 00:16:24,560
although like yeah, the job scene and

492
00:16:24,560 --> 00:16:26,520
all this stuff is scary, I genuinely

493
00:16:26,520 --> 00:16:28,480
believe anyone who knows how these tools

494
00:16:28,480 --> 00:16:30,760
work and like knows how to build agents

495
00:16:30,760 --> 00:16:33,040
and like craft skills and like knows how

496
00:16:33,040 --> 00:16:35,080
to make them productive, we're in it for

497
00:16:35,080 --> 00:16:37,360
a good run. Mhm. So, you're saying that

498
00:16:37,360 --> 00:16:39,360
if you know how to do this, you won't

499
00:16:39,360 --> 00:16:40,960
join the permanent underclass.

500
00:16:40,960 --> 00:16:43,960
>> The permanent underclass. [laughter]

501
00:16:43,960 --> 00:16:45,520
So, is the permanent underclass

502
00:16:45,520 --> 00:16:48,400
basically like I've seen this these this

503
00:16:48,400 --> 00:16:50,600
this on Twitter a lot. Is that basically

504
00:16:50,600 --> 00:16:53,680
AI has replaced you, so now you're just

505
00:16:53,680 --> 00:16:56,600
>> From what I understand, it's

506
00:16:56,600 --> 00:16:59,320
once AGI comes,

507
00:16:59,320 --> 00:17:01,920
all these white-collar workers are going

508
00:17:01,920 --> 00:17:03,400
to lose their jobs.

509
00:17:03,400 --> 00:17:06,040
And if you don't know how to build

510
00:17:06,040 --> 00:17:08,640
skills, use AI,

511
00:17:08,640 --> 00:17:10,240
people say you're joining the permanent

512
00:17:10,240 --> 00:17:12,760
underclass. That's That's the term.

513
00:17:12,760 --> 00:17:14,911
>> It's permanent, too. That's scary.

514
00:17:14,911 --> 00:17:15,319
>> [laughter]

515
00:17:15,319 --> 00:17:16,760
>> So, I just have a little bit of time

516
00:17:16,760 --> 00:17:19,640
left. Yeah, by the way, like

517
00:17:19,640 --> 00:17:21,439
it's ridiculous to call it a permanent

518
00:17:21,439 --> 00:17:22,280
underclass.

519
00:17:22,280 --> 00:17:23,560
>> Yeah, cuz that's terrifying. [laughter]

520
00:17:23,560 --> 00:17:25,640
>> understand underclass, but permanent

521
00:17:25,640 --> 00:17:27,360
permanent it's like

522
00:17:27,360 --> 00:17:28,880
>> Like you're saying there's no hope like

523
00:17:28,880 --> 00:17:29,880
>> No

524
00:17:29,880 --> 00:17:33,320
>> Yeah, um I mean, we are in like

525
00:17:33,320 --> 00:17:35,800
knowledge that took 20 people 20 years

526
00:17:35,800 --> 00:17:37,760
to acquire is now like 20 bucks a month,

527
00:17:37,760 --> 00:17:39,360
right? So, there is like a huge shift,

528
00:17:39,360 --> 00:17:41,560
right? People who are non-technical are

529
00:17:41,560 --> 00:17:44,440
I I think I saw yesterday like some guy

530
00:17:44,440 --> 00:17:46,600
hit like a hundred million dollars um

531
00:17:46,600 --> 00:17:48,680
and he vibe coded the whole app. I think

532
00:17:48,680 --> 00:17:49,320
it was him and his friend.

533
00:17:49,320 --> 00:17:51,280
>> 1.8 billion

534
00:17:51,280 --> 00:17:51,920
>> billion?

535
00:17:51,920 --> 00:17:54,040
>> Yeah.

536
00:17:54,040 --> 00:17:56,000
>> So, you know what I mean? Like it is the

537
00:17:56,000 --> 00:17:58,200
there is a shift, right? And I think

538
00:17:58,200 --> 00:17:59,960
this idea of like well, I'm not

539
00:17:59,960 --> 00:18:01,120
>> how you were like billion. You were

540
00:18:01,120 --> 00:18:02,920
about to just leave this podcast and

541
00:18:02,920 --> 00:18:03,680
just be like

542
00:18:03,680 --> 00:18:04,840
>> No, you know what it is? I just

543
00:18:04,840 --> 00:18:06,680
realized, man, I overthink things. Like

544
00:18:06,680 --> 00:18:08,640
I just need to drop the thing, release

545
00:18:08,640 --> 00:18:09,880
the thing and there's like wisdom in

546
00:18:09,880 --> 00:18:11,480
that like

547
00:18:11,480 --> 00:18:12,800
there needs to be this level of

548
00:18:12,800 --> 00:18:14,440
delusion, which I don't have. Like I'm

549
00:18:14,440 --> 00:18:15,880
trying to work on where you're like this

550
00:18:15,880 --> 00:18:17,520
is just going to work out. We're just

551
00:18:17,520 --> 00:18:19,040
going to launch the product. It's going

552
00:18:19,040 --> 00:18:20,840
to succeed and if it doesn't, onto the

553
00:18:20,840 --> 00:18:23,120
next one cuz 1.8 billion

554
00:18:23,120 --> 00:18:24,600
>> Yeah, dude.

555
00:18:24,600 --> 00:18:25,520
>> Like B?

556
00:18:25,520 --> 00:18:26,040
>> B

557
00:18:26,040 --> 00:18:27,200
>> USD?

558
00:18:27,200 --> 00:18:30,237
>> We're Yeah, we're not talking Monopoly

559
00:18:30,237 --> 00:18:30,960
>> [laughter]

560
00:18:30,960 --> 00:18:32,720
>> Cuz it was Canadian.

561
00:18:32,720 --> 00:18:34,960
Uh it's it's uh

562
00:18:34,960 --> 00:18:37,442
>> We're not talking carny coins.

563
00:18:37,442 --> 00:18:39,462
>> [laughter]

564
00:18:40,360 --> 00:18:42,520
>> We're talk we're talking real Benjamins.

565
00:18:42,520 --> 00:18:43,040
>> Yeah.

566
00:18:43,040 --> 00:18:44,560
>> Yeah, that makes sense. That makes

567
00:18:44,560 --> 00:18:46,600
sense. But yeah, like I I hope this like

568
00:18:46,600 --> 00:18:48,760
understanding of like again, I

569
00:18:48,760 --> 00:18:50,120
personally don't think you don't need an

570
00:18:50,120 --> 00:18:52,200
agent.md file unless you have something

571
00:18:52,200 --> 00:18:53,680
proprietary.

572
00:18:53,680 --> 00:18:56,760
Um skills are valuable. Build your own

573
00:18:56,760 --> 00:18:58,960
though. Build build your own. Like you

574
00:18:58,960 --> 00:19:00,240
know like when you ask your mom when you

575
00:19:00,240 --> 00:19:01,840
were a kid, oh, can we have McDonald's?

576
00:19:01,840 --> 00:19:03,600
And she's like we have food at home. We

577
00:19:03,600 --> 00:19:05,000
have food at home. Build your own

578
00:19:05,000 --> 00:19:07,960
skills. For coding perspective, from

579
00:19:07,960 --> 00:19:09,560
coding wise,

580
00:19:09,560 --> 00:19:11,080
um

581
00:19:11,080 --> 00:19:13,240
a lot of the companies model companies

582
00:19:13,240 --> 00:19:15,600
have realized that the agents are really

583
00:19:15,600 --> 00:19:18,040
good at writing code, particularly

584
00:19:18,040 --> 00:19:21,400
TypeScript. And this is why there's been

585
00:19:21,400 --> 00:19:23,520
like you see this advancement with like

586
00:19:23,520 --> 00:19:26,200
Claude co-work and like even open claw.

587
00:19:26,200 --> 00:19:27,320
Really what they're doing under the hood

588
00:19:27,320 --> 00:19:28,680
is they're writing code, right? They're

589
00:19:28,680 --> 00:19:30,440
writing code calling APIs and all this

590
00:19:30,440 --> 00:19:33,040
stuff. So, when it comes to building a

591
00:19:33,040 --> 00:19:37,160
project um you actually don't need

592
00:19:37,160 --> 00:19:39,160
skills or like you don't need an agent

593
00:19:39,160 --> 00:19:41,480
MD file specific to the tech stack you

594
00:19:41,480 --> 00:19:43,080
use. Like I remember we used to I'm

595
00:19:43,080 --> 00:19:46,000
using React and you know, Convex or I'm

596
00:19:46,000 --> 00:19:48,000
using Next.js and Supabase I'm using

597
00:19:48,000 --> 00:19:49,640
this and I'm using that and you put that

598
00:19:49,640 --> 00:19:51,880
in the agent MD file and you have like

599
00:19:51,880 --> 00:19:53,280
all these lines.

600
00:19:53,280 --> 00:19:54,920
For the most part, unless again you have

601
00:19:54,920 --> 00:19:57,880
a specific specific workflow

602
00:19:57,880 --> 00:19:59,920
unnecessary. And the reason being is

603
00:19:59,920 --> 00:20:02,920
code itself has become context now. So,

604
00:20:02,920 --> 00:20:05,000
the more the more important thing is

605
00:20:05,000 --> 00:20:06,440
starting with a solid foundation.

606
00:20:06,440 --> 00:20:07,840
Templates used to be big back in the

607
00:20:07,840 --> 00:20:09,360
day. People made lots of money with

608
00:20:09,360 --> 00:20:11,120
templates. I believe templates are going

609
00:20:11,120 --> 00:20:13,240
to have a renaissance because if you

610
00:20:13,240 --> 00:20:16,080
have a solid like template, right? Like

611
00:20:16,080 --> 00:20:17,960
whether it be like for web app or mobile

612
00:20:17,960 --> 00:20:18,960
app

613
00:20:18,960 --> 00:20:20,600
because that becomes context for the

614
00:20:20,600 --> 00:20:23,120
agent, it's going to build on top of

615
00:20:23,120 --> 00:20:25,800
that, right? And again, I didn't need

616
00:20:25,800 --> 00:20:28,200
some large agent.md file. I didn't need

617
00:20:28,200 --> 00:20:30,920
any large cloud.md file. What I needed

618
00:20:30,920 --> 00:20:34,520
was again, minimal context usage and

619
00:20:34,520 --> 00:20:38,000
skills. So, if there's anything

620
00:20:38,000 --> 00:20:39,800
anyone can learn from me is build your

621
00:20:39,800 --> 00:20:42,360
own skills. Build your own skills. And

622
00:20:42,360 --> 00:20:44,080
there's this methodology I don't know if

623
00:20:44,080 --> 00:20:45,400
I've shared this with you, recursively

624
00:20:45,400 --> 00:20:47,000
building skills. So, let's say you've

625
00:20:47,000 --> 00:20:49,360
built your skill, right? I have I'll

626
00:20:49,360 --> 00:20:52,280
draw a diagram cuz why not?

627
00:20:52,280 --> 00:20:55,000
Let's say I have a workflow

628
00:20:55,000 --> 00:20:57,560
and after you like setting up my

629
00:20:57,560 --> 00:20:59,320
workflow with an agent, I've decided,

630
00:20:59,320 --> 00:21:01,840
you know what? I'm going to turn this

631
00:21:01,840 --> 00:21:05,560
into a skill, right? So, this is my uh

632
00:21:05,560 --> 00:21:07,480
skill.md.

633
00:21:07,480 --> 00:21:09,960
Now, here's the thing. Even though you

634
00:21:09,960 --> 00:21:12,400
have the skill.md, the agent at some

635
00:21:12,400 --> 00:21:14,520
point is still going to mess up because

636
00:21:14,520 --> 00:21:16,120
there's probably gaps in the information

637
00:21:16,120 --> 00:21:18,840
it has in the skill. So, when it messes

638
00:21:18,840 --> 00:21:21,160
up, I'm going to work with it again. How

639
00:21:21,160 --> 00:21:23,720
do I work with it? You messed up.

640
00:21:23,720 --> 00:21:25,760
Try calling the API again. Try doing

641
00:21:25,760 --> 00:21:27,800
this again. Or even ask it when it tells

642
00:21:27,800 --> 00:21:29,120
you, "Oh, I failed. I couldn't do this

643
00:21:29,120 --> 00:21:30,920
task." Believe it or not, when you tell

644
00:21:30,920 --> 00:21:33,120
the agent, "Why did you fail?" When you

645
00:21:33,120 --> 00:21:35,040
ask it, like, "What's the error that you

646
00:21:35,040 --> 00:21:36,840
got?" It will tell you descriptively,

647
00:21:36,840 --> 00:21:39,480
"Oh, I got a 505 error. You uh, you have

648
00:21:39,480 --> 00:21:41,320
insufficient credits." Like, "Oh, okay.

649
00:21:41,320 --> 00:21:43,560
So, it's a credit issue. Fine." So, I

650
00:21:43,560 --> 00:21:46,040
would tell it that. And then,

651
00:21:46,040 --> 00:21:49,400
I would pass that failure back to the

652
00:21:49,400 --> 00:21:52,200
agent. So, let's say uh, it did

653
00:21:52,200 --> 00:21:53,800
something wrong. We identified the

654
00:21:53,800 --> 00:21:56,320
failure. All I did was asking it. I will

655
00:21:56,320 --> 00:21:57,840
give that failure back to the agent.

656
00:21:57,840 --> 00:21:59,840
I'll be like, "You failed here. This

657
00:21:59,840 --> 00:22:02,480
didn't work. Fix this."

658
00:22:02,480 --> 00:22:03,680
It's going to fix. It's going to write

659
00:22:03,680 --> 00:22:05,360
code. It's going to do whatever it does.

660
00:22:05,360 --> 00:22:07,800
Once it fixes it and it's done it right,

661
00:22:07,800 --> 00:22:09,800
now you tell it with the new fix,

662
00:22:09,800 --> 00:22:12,040
"Update the skill so this doesn't happen

663
00:22:12,040 --> 00:22:13,240
again."

664
00:22:13,240 --> 00:22:15,320
I have, like, for my YouTube channel, I

665
00:22:15,320 --> 00:22:17,640
have like a report generator. It calls

666
00:22:17,640 --> 00:22:19,800
Notion, Dub Analytics, YouTube

667
00:22:19,800 --> 00:22:22,200
Analytics, Twitter Analytics. Pulls from

668
00:22:22,200 --> 00:22:23,560
my It pulls from like eight data

669
00:22:23,560 --> 00:22:25,920
sources. There's no way you're going to

670
00:22:25,920 --> 00:22:28,000
one prompt and the agent's going to do

671
00:22:28,000 --> 00:22:30,280
it. But, every time I tell it to do that

672
00:22:30,280 --> 00:22:32,120
workflow, it takes like 10 minutes. It

673
00:22:32,120 --> 00:22:34,200
executes it flawlessly. Why? I went

674
00:22:34,200 --> 00:22:36,200
through five loops of this.

675
00:22:36,200 --> 00:22:38,880
Five iterations of recursively building

676
00:22:38,880 --> 00:22:41,720
the skill. And that skill is so good. I

677
00:22:41,720 --> 00:22:44,200
genuinely think if anyone's going to if

678
00:22:44,200 --> 00:22:45,720
like skills marketplace is going to be a

679
00:22:45,720 --> 00:22:47,520
thing, there's going to be people who

680
00:22:47,520 --> 00:22:50,280
sell skills. Like, really well-defined,

681
00:22:50,280 --> 00:22:52,880
like, step-by-step skills because people

682
00:22:52,880 --> 00:22:55,440
are just creating them without having

683
00:22:55,440 --> 00:22:57,600
built out the workflow with the agent,

684
00:22:57,600 --> 00:23:00,400
right? So, use the workflow by hand,

685
00:23:00,400 --> 00:23:02,640
like, telling it each step. Once it's

686
00:23:02,640 --> 00:23:04,640
done it completely, create the scale out

687
00:23:04,640 --> 00:23:07,000
MD file, continue to use it. It's going

688
00:23:07,000 --> 00:23:09,760
to mess up. When he messes up, you thank

689
00:23:09,760 --> 00:23:11,080
God you don't complain cuz a lot of

690
00:23:11,080 --> 00:23:12,320
people are like, "Oh, I messed up. I'm

691
00:23:12,320 --> 00:23:14,480
angry." No, this is a moment where you

692
00:23:14,480 --> 00:23:16,520
identify the error, tell it, "This is

693
00:23:16,520 --> 00:23:18,920
the error, fix it." It'll fix it itself,

694
00:23:18,920 --> 00:23:20,720
and then you tell it to update the skill

695
00:23:20,720 --> 00:23:23,240
file so that this doesn't happen again.

696
00:23:23,240 --> 00:23:25,320
>> So, that's a little bit about shifting

697
00:23:25,320 --> 00:23:27,560
your expectation, right? Cuz people just

698
00:23:27,560 --> 00:23:29,600
assume uh

699
00:23:29,600 --> 00:23:31,200
it's going to work in the beginning.

700
00:23:31,200 --> 00:23:33,040
You're saying basically it's not going

701
00:23:33,040 --> 00:23:35,240
to work initially. There's going to be

702
00:23:35,240 --> 00:23:38,240
two, three, five, six hiccups. Um and

703
00:23:38,240 --> 00:23:40,600
over time, it should

704
00:23:40,600 --> 00:23:41,200
be good.

705
00:23:41,200 --> 00:23:44,520
>> So, this is most people's expectations.

706
00:23:44,520 --> 00:23:45,000
Right?

707
00:23:45,000 --> 00:23:45,360
>> Yeah.

708
00:23:45,360 --> 00:23:46,640
>> And

709
00:23:46,640 --> 00:23:49,360
the way I've personally experienced is

710
00:23:49,360 --> 00:23:51,040
it's like this.

711
00:23:51,040 --> 00:23:53,440
So, there's like this early area of

712
00:23:53,440 --> 00:23:55,880
investment that you have to make that

713
00:23:55,880 --> 00:23:58,440
sucks, that nobody will tell you,

714
00:23:58,440 --> 00:24:00,560
especially Agent Harness's company cuz

715
00:24:00,560 --> 00:24:01,640
they wouldn't raise as much money if

716
00:24:01,640 --> 00:24:04,080
they did. But like this maybe I would

717
00:24:04,080 --> 00:24:06,520
give it 2 weeks cuz it took me 2 weeks

718
00:24:06,520 --> 00:24:07,880
like OpenClaw when I first set up

719
00:24:07,880 --> 00:24:09,600
OpenClaw, I thought the same thing. I'm

720
00:24:09,600 --> 00:24:12,120
like, "What What is this garbage? Right?

721
00:24:12,120 --> 00:24:13,200
Like it doesn't understand anything.

722
00:24:13,200 --> 00:24:14,560
It's confusing." Then I realized like,

723
00:24:14,560 --> 00:24:15,760
"Oh, like

724
00:24:15,760 --> 00:24:18,280
let me go lower level." The models and

725
00:24:18,280 --> 00:24:20,320
the agents like they they don't think

726
00:24:20,320 --> 00:24:21,840
like you and me. Right? Like I could I

727
00:24:21,840 --> 00:24:23,760
could tell you, "Hey,

728
00:24:23,760 --> 00:24:26,600
um Greg, we need a report on like, you

729
00:24:26,600 --> 00:24:28,920
know, the financials in Notion."

730
00:24:28,920 --> 00:24:30,760
Because you're probably were in the same

731
00:24:30,760 --> 00:24:32,080
business, we worked together, you would

732
00:24:32,080 --> 00:24:33,720
understand based on the context you have

733
00:24:33,720 --> 00:24:35,520
of the business what that means. But

734
00:24:35,520 --> 00:24:36,920
imagine a new guy joins like, "Yeah, I

735
00:24:36,920 --> 00:24:39,000
need a report on the financials."

736
00:24:39,000 --> 00:24:40,040
So, where do I even start?

737
00:24:40,040 --> 00:24:41,600
>> reminds me? I wonder if we can put this

738
00:24:41,600 --> 00:24:42,800
clip in.

739
00:24:42,800 --> 00:24:45,120
But in the office, you watch The Office?

740
00:24:45,120 --> 00:24:46,600
>> I am not an office watcher,

741
00:24:46,600 --> 00:24:47,400
unfortunately.

742
00:24:47,400 --> 00:24:49,880
>> There's a clip that

743
00:24:49,880 --> 00:24:51,680
uh there's a new boss

744
00:24:51,680 --> 00:24:53,320
and

745
00:24:53,320 --> 00:24:55,480
the new boss goes to Jim, one of the

746
00:24:55,480 --> 00:24:58,240
main characters. Yeah, and he asked for

747
00:24:58,240 --> 00:24:59,880
a rundown.

748
00:24:59,880 --> 00:25:02,480
So go go The Office

749
00:25:02,480 --> 00:25:05,760
The Office rundown.

750
00:25:05,760 --> 00:25:07,360
>> I don't know.

751
00:25:07,360 --> 00:25:10,400
>> Basically, Charles

752
00:25:10,400 --> 00:25:13,440
the whole episode is about

753
00:25:13,440 --> 00:25:15,840
Jim trying to ask around and be like,

754
00:25:15,840 --> 00:25:18,240
"What What is a rundown? Like what is a

755
00:25:18,240 --> 00:25:19,760
rundown?" He's like calling his dad,

756
00:25:19,760 --> 00:25:21,600
like "What is a rundown?" You know what

757
00:25:21,600 --> 00:25:24,200
I mean? He's just Um he didn't have the

758
00:25:24,200 --> 00:25:24,960
context.

759
00:25:24,960 --> 00:25:26,320
>> Yeah. He didn't have the context.

760
00:25:26,320 --> 00:25:27,960
>> Yeah. And and and it goes back to my

761
00:25:27,960 --> 00:25:30,280
initial point, the models are really

762
00:25:30,280 --> 00:25:33,160
really good now, but the context matters

763
00:25:33,160 --> 00:25:35,040
more than anything, right? So when you

764
00:25:35,040 --> 00:25:37,520
see like these large agent like

765
00:25:37,520 --> 00:25:39,360
companies and sub agents, and again, I'm

766
00:25:39,360 --> 00:25:41,320
not saying those don't work, but I'm

767
00:25:41,320 --> 00:25:42,680
saying

768
00:25:42,680 --> 00:25:44,520
probably won't work for you off rip

769
00:25:44,520 --> 00:25:46,240
because you haven't built it up to get

770
00:25:46,240 --> 00:25:48,680
to that point, right? So let's say like

771
00:25:48,680 --> 00:25:51,440
for me for example, I started with um

772
00:25:51,440 --> 00:25:53,720
one agent. Let me draw this. I started

773
00:25:53,720 --> 00:25:55,520
with one agent. And this was like my

774
00:25:55,520 --> 00:25:57,040
main agent. This did everything, right?

775
00:25:57,040 --> 00:25:59,520
This checked my spreadsheet, this

776
00:25:59,520 --> 00:26:01,800
checked my sponsors email, and all these

777
00:26:01,800 --> 00:26:03,640
type of things. And once I had like

778
00:26:03,640 --> 00:26:07,080
predefined workflows, let's say for like

779
00:26:07,080 --> 00:26:09,320
working with sponsors, then I can

780
00:26:09,320 --> 00:26:10,960
actually have a sub agent. What's the

781
00:26:10,960 --> 00:26:12,600
purpose of the sub agent? The sub agent

782
00:26:12,600 --> 00:26:15,360
does all the marketing stuff, right? But

783
00:26:15,360 --> 00:26:16,880
I'm not creating the sub agent for the

784
00:26:16,880 --> 00:26:18,680
sake of creating it. It's going to have

785
00:26:18,680 --> 00:26:20,800
skills, it's going to have context, and

786
00:26:20,800 --> 00:26:22,240
it actually makes sense for me to have

787
00:26:22,240 --> 00:26:24,400
sub agents, right? So I've built out my

788
00:26:24,400 --> 00:26:26,400
thing to like now I have five sub

789
00:26:26,400 --> 00:26:29,040
agents. I have one for marketing, one

790
00:26:29,040 --> 00:26:32,120
uh for business, one for personal, and

791
00:26:32,120 --> 00:26:34,640
and that's it. And I'm willing to bet if

792
00:26:34,640 --> 00:26:36,240
I went open claw to open claw with

793
00:26:36,240 --> 00:26:39,040
anyone, my system is more productive

794
00:26:39,040 --> 00:26:40,440
because I didn't scale for what looks

795
00:26:40,440 --> 00:26:44,160
cool, I scale for productivity.

796
00:26:44,160 --> 00:26:45,080
>> That was a bar.

797
00:26:45,080 --> 00:26:46,520
>> That was a huge bar. We got to clip

798
00:26:46,520 --> 00:26:48,480
that. I was just thinking that clip,

799
00:26:48,480 --> 00:26:50,160
that's going to rip.

800
00:26:50,160 --> 00:26:52,600
>> Yeah, that was a bar. Um what else do

801
00:26:52,600 --> 00:26:54,240
you want to leave people with or is this

802
00:26:54,240 --> 00:26:56,120
this is the main point? Yeah, like

803
00:26:56,120 --> 00:26:58,360
here's like the we've got to a point

804
00:26:58,360 --> 00:26:59,880
where the models are good. The models

805
00:26:59,880 --> 00:27:01,960
are really good. The context matters

806
00:27:01,960 --> 00:27:04,200
plus the harness, right? So, for

807
00:27:04,200 --> 00:27:05,480
example,

808
00:27:05,480 --> 00:27:07,480
there was this benchmark, although I'm

809
00:27:07,480 --> 00:27:10,160
not 100% supporting it, that there was a

810
00:27:10,160 --> 00:27:13,200
difference between the quality of output

811
00:27:13,200 --> 00:27:15,840
that cursor generated versus Claude code

812
00:27:15,840 --> 00:27:18,440
versus Codex, right?

813
00:27:18,440 --> 00:27:21,600
Um So, what that tells me is that we've

814
00:27:21,600 --> 00:27:23,040
reached a point where the models are

815
00:27:23,040 --> 00:27:24,560
really really good. They're probably

816
00:27:24,560 --> 00:27:25,920
going to get better. The next iteration

817
00:27:25,920 --> 00:27:27,680
is probably going to get better, but the

818
00:27:27,680 --> 00:27:30,040
harness and the tools that you surround

819
00:27:30,040 --> 00:27:33,000
it, the context that you give it is

820
00:27:33,000 --> 00:27:35,600
going to matter even more. And just like

821
00:27:35,600 --> 00:27:38,160
in everything in life, less is more,

822
00:27:38,160 --> 00:27:40,720
right? Like building up step by step,

823
00:27:40,720 --> 00:27:43,000
making it productive for you first

824
00:27:43,000 --> 00:27:45,400
before you add the shiny new thing. Like

825
00:27:45,400 --> 00:27:46,880
cuz I tried all these tools all the time

826
00:27:46,880 --> 00:27:49,280
like especially paper paperclip blew up

827
00:27:49,280 --> 00:27:50,480
and a lot of people are talking about

828
00:27:50,480 --> 00:27:52,480
and it's fantastic, but I'm willing to

829
00:27:52,480 --> 00:27:54,960
bet if people took 2 weeks to build up

830
00:27:54,960 --> 00:27:56,600
to the version cuz you can prompt open

831
00:27:56,600 --> 00:27:58,120
Claude to do all that stuff. If they

832
00:27:58,120 --> 00:28:00,720
built up their own version of paperclip

833
00:28:00,720 --> 00:28:02,760
in 2 3 weeks where like they're building

834
00:28:02,760 --> 00:28:04,560
things that they actually need, their

835
00:28:04,560 --> 00:28:06,160
productivity level will skyrocket

836
00:28:06,160 --> 00:28:07,040
through the roof.

837
00:28:07,040 --> 00:28:08,360
>> It's a hot take.

838
00:28:08,360 --> 00:28:09,040
>> It's a hot take.

839
00:28:09,040 --> 00:28:10,240
>> Might get me in trouble.

840
00:28:10,240 --> 00:28:11,400
>> No, it won't get Who's it going to get

841
00:28:11,400 --> 00:28:13,080
you in trouble with? Maybe paperclip

842
00:28:13,080 --> 00:28:14,520
raises a billion dollars and they don't

843
00:28:14,520 --> 00:28:15,814
acquire my podcast.

844
00:28:15,814 --> 00:28:17,779
>> [laughter]

845
00:28:17,779 --> 00:28:18,640
[gasps]

846
00:28:18,640 --> 00:28:20,040
>> I think

847
00:28:20,040 --> 00:28:21,280
Listen, you're you're out there, you're

848
00:28:21,280 --> 00:28:22,480
trying things and you're just sharing

849
00:28:22,480 --> 00:28:24,480
what you're learning in real time. So,

850
00:28:24,480 --> 00:28:26,080
if you're just

851
00:28:26,080 --> 00:28:26,360
You're not

852
00:28:26,360 --> 00:28:27,720
>> Things can change by the way. Hey, like

853
00:28:27,720 --> 00:28:29,200
2 weeks from now it could be like no

854
00:28:29,200 --> 00:28:31,560
give the agent everything. There's this

855
00:28:31,560 --> 00:28:34,040
new memory paper that Google released

856
00:28:34,040 --> 00:28:35,960
and like now like it has the ability to

857
00:28:35,960 --> 00:28:38,560
index information and stuff, but

858
00:28:38,560 --> 00:28:41,000
as it as it pertains to real life, less

859
00:28:41,000 --> 00:28:43,480
is more, simple is better, right? If you

860
00:28:43,480 --> 00:28:46,040
can't explain it in in a few sentences,

861
00:28:46,040 --> 00:28:47,840
you probably don't really understand it,

862
00:28:47,840 --> 00:28:50,560
right? And I find that the models are

863
00:28:50,560 --> 00:28:52,040
trained on so much information,

864
00:28:52,040 --> 00:28:53,680
especially when it comes to programming,

865
00:28:53,680 --> 00:28:56,280
building, and like and um what do you

866
00:28:56,280 --> 00:28:57,760
call like day-to-day work, like

867
00:28:57,760 --> 00:28:59,960
financial work, or like any sort of

868
00:28:59,960 --> 00:29:01,880
like, you know, checking contracts and

869
00:29:01,880 --> 00:29:03,480
stuff. Like they the model companies are

870
00:29:03,480 --> 00:29:05,520
focusing on that, like on white-collar

871
00:29:05,520 --> 00:29:07,800
work. The models are really, really

872
00:29:07,800 --> 00:29:09,880
good. What matters more is the harness

873
00:29:09,880 --> 00:29:11,720
and the tools you provided. And the one

874
00:29:11,720 --> 00:29:13,040
thing that you and I have that the

875
00:29:13,040 --> 00:29:15,400
models don't have is my specific

876
00:29:15,400 --> 00:29:18,360
workflow, my specific taste, my specific

877
00:29:18,360 --> 00:29:20,640
strategy of doing things. And those can

878
00:29:20,640 --> 00:29:22,800
be codified in skills, right? This is

879
00:29:22,800 --> 00:29:25,320
why like skills make sense when you

880
00:29:25,320 --> 00:29:27,480
build them. Not if you download my

881
00:29:27,480 --> 00:29:29,760
skill. Like I have this one skill.

882
00:29:29,760 --> 00:29:32,160
Um like again, don't download it. Do I'm

883
00:29:32,160 --> 00:29:33,560
telling you now, do not download it.

884
00:29:33,560 --> 00:29:36,000
Don't use it. I just put it so I can get

885
00:29:36,000 --> 00:29:39,440
some GitHub stars. Um

886
00:29:39,440 --> 00:29:40,880
I have this one skill, and it's

887
00:29:40,880 --> 00:29:43,000
literally a code structure skill.

888
00:29:43,000 --> 00:29:45,000
And I'll put the markdown so people can

889
00:29:45,000 --> 00:29:46,000
see it.

890
00:29:46,000 --> 00:29:49,680
Um it's 116 lines. It's basically after

891
00:29:49,680 --> 00:29:51,960
AI has generated a bunch of code, I like

892
00:29:51,960 --> 00:29:53,520
it structured in a certain way, so it's

893
00:29:53,520 --> 00:29:55,640
easy for me to review it. And like I

894
00:29:55,640 --> 00:29:57,480
mentioned earlier with skills, the only

895
00:29:57,480 --> 00:29:59,040
thing that gets added into context is

896
00:29:59,040 --> 00:30:00,920
the name and description. So when I look

897
00:30:00,920 --> 00:30:02,640
at the name, it's code structure. When I

898
00:30:02,640 --> 00:30:04,200
look at the description, use when

899
00:30:04,200 --> 00:30:05,960
multiple workflows duplicate the same

900
00:30:05,960 --> 00:30:08,120
operational logic when deciding that

901
00:30:08,120 --> 00:30:09,240
blah blah blah blah blah some nerd

902
00:30:09,240 --> 00:30:11,480
stuff. So when I tell the agent, I want

903
00:30:11,480 --> 00:30:12,280
to

904
00:30:12,280 --> 00:30:14,480
clean up the code structure, it checks

905
00:30:14,480 --> 00:30:17,080
the skills it has, it sees the name, it

906
00:30:17,080 --> 00:30:18,880
reads the description. It's like, oh,

907
00:30:18,880 --> 00:30:21,040
this makes sense. Then it progressively

908
00:30:21,040 --> 00:30:22,720
discloses, meaning once it realizes it

909
00:30:22,720 --> 00:30:24,920
needs this skill, then it adds the rest

910
00:30:24,920 --> 00:30:26,840
of this, right? Versus if this was my

911
00:30:26,840 --> 00:30:29,400
agent.md file, imagine every single

912
00:30:29,400 --> 00:30:31,960
time, and we can actually check how many

913
00:30:31,960 --> 00:30:33,680
tokens this is.

914
00:30:33,680 --> 00:30:35,600
Let me check. Um

915
00:30:35,600 --> 00:30:39,800
what was it? OpenAI token tokenizer.

916
00:30:39,800 --> 00:30:42,880
If I go to this,

917
00:30:42,880 --> 00:30:46,320
So, this is 944 tokens. So, if this was

918
00:30:46,320 --> 00:30:49,560
an agent.md file, every single time I

919
00:30:49,560 --> 00:30:52,280
have a chat, I'm adding 944 tokens.

920
00:30:52,280 --> 00:30:53,400
Tokens ain't cheap now.

921
00:30:53,400 --> 00:30:54,000
>> No.

922
00:30:54,000 --> 00:30:57,040
>> But, if I just have the name

923
00:30:57,040 --> 00:30:58,280
and the description, it's just 53

924
00:30:58,280 --> 00:30:58,480
tokens.

925
00:30:58,480 --> 00:31:00,080
>> And it's not even cheap. It's just like

926
00:31:00,080 --> 00:31:02,760
you're not trying to

927
00:31:02,760 --> 00:31:04,040
hit the limit quicker than you need to

928
00:31:04,040 --> 00:31:04,880
hit the limit.

929
00:31:04,880 --> 00:31:06,240
>> Cuz the model will get dumb as the

930
00:31:06,240 --> 00:31:08,160
context window closes, right? So, if you

931
00:31:08,160 --> 00:31:10,320
have like a context window, and I can

932
00:31:10,320 --> 00:31:12,480
draw this out. If this is your context

933
00:31:12,480 --> 00:31:13,800
window,

934
00:31:13,800 --> 00:31:19,680
and like the optimal is you're between

935
00:31:19,680 --> 00:31:21,800
like there's always like maybe like 10%

936
00:31:21,800 --> 00:31:23,400
is already filled with all the

937
00:31:23,400 --> 00:31:24,680
system prompt and all that stuff. You

938
00:31:24,680 --> 00:31:27,400
want to be between like

939
00:31:27,400 --> 00:31:29,960
you know, fresh to like 70% cuz the

940
00:31:29,960 --> 00:31:33,160
closer you get to 99, 100% like 99, 90,

941
00:31:33,160 --> 00:31:35,320
80%, it starts to get dumb, right? And

942
00:31:35,320 --> 00:31:36,680
you can think of this like a human. Like

943
00:31:36,680 --> 00:31:39,840
imagine you throw a bunch of information

944
00:31:39,840 --> 00:31:41,400
again and again and again and again. And

945
00:31:41,400 --> 00:31:43,680
this is why like when I like was in

946
00:31:43,680 --> 00:31:46,120
school, like last minute studying never

947
00:31:46,120 --> 00:31:47,360
worked for me cuz like I didn't pay

948
00:31:47,360 --> 00:31:49,240
attention the entire year. Now I have to

949
00:31:49,240 --> 00:31:51,960
learn about polynomials, and I have to

950
00:31:51,960 --> 00:31:53,640
do these graphs, and there's this weird

951
00:31:53,640 --> 00:31:56,080
notation. It's impossible for me to

952
00:31:56,080 --> 00:31:57,960
catch up, right? And it's the same way

953
00:31:57,960 --> 00:31:59,760
with the agents. You want to keep your

954
00:31:59,760 --> 00:32:01,080
context window You want to save your

955
00:32:01,080 --> 00:32:02,280
context window cuz hey, it saves you

956
00:32:02,280 --> 00:32:04,680
money. But not only that, it makes a

957
00:32:04,680 --> 00:32:06,320
more performant

958
00:32:06,320 --> 00:32:09,440
um agent. So, less is more. Less is

959
00:32:09,440 --> 00:32:11,680
more. Rely more on the model's strength,

960
00:32:11,680 --> 00:32:13,920
and what the model needs is what's

961
00:32:13,920 --> 00:32:15,560
unique and special about you, your

962
00:32:15,560 --> 00:32:17,480
workflow, your business, not general

963
00:32:17,480 --> 00:32:19,680
knowledge. Don't tell the model use

964
00:32:19,680 --> 00:32:20,920
React.

965
00:32:20,920 --> 00:32:22,520
It knows to use React. Don't tell the

966
00:32:22,520 --> 00:32:25,800
model um you know, things that like

967
00:32:25,800 --> 00:32:28,560
should already be known uh for the uh

968
00:32:28,560 --> 00:32:29,560
like you know,

969
00:32:29,560 --> 00:32:31,520
task. Like for example, like let's say

970
00:32:31,520 --> 00:32:33,080
I'm doing a financial report, and then

971
00:32:33,080 --> 00:32:36,280
the agent.md file, I say um

972
00:32:36,280 --> 00:32:39,680
to denote money use a dollar sign.

973
00:32:39,680 --> 00:32:41,080
It's going to use a dollar sign. Right

974
00:32:41,080 --> 00:32:43,440
now, if you have a specific currency,

975
00:32:43,440 --> 00:32:46,480
then you like, oh, use this currency.

976
00:32:46,480 --> 00:32:48,200
This is the You know, like for something

977
00:32:48,200 --> 00:32:51,080
that the agent won't do manually, like

978
00:32:51,080 --> 00:32:52,560
won't know manually, that's when you

979
00:32:52,560 --> 00:32:54,960
have like your agent.md's, Claude.md's,

980
00:32:54,960 --> 00:32:56,920
but honestly, these are a farce. You

981
00:32:56,920 --> 00:32:59,840
don't need them. Um, skills skills

982
00:32:59,840 --> 00:33:03,560
skills skills skills is what it's at.

983
00:33:03,560 --> 00:33:05,160
>> Thanks for keeping it real. I appreciate

984
00:33:05,160 --> 00:33:05,720
you, man.

985
00:33:05,720 --> 00:33:06,800
>> That's all I'm going to do. Thank you,

986
00:33:06,800 --> 00:33:07,320
man.

987
00:33:07,320 --> 00:33:08,200
>> it.

988
00:33:08,200 --> 00:33:09,800
Uh, like always, I'll include links

989
00:33:09,800 --> 00:33:11,520
where you can follow

990
00:33:11,520 --> 00:33:14,000
Ross Mike on YouTube and X and other

991
00:33:14,000 --> 00:33:15,520
places in the show notes in the

992
00:33:15,520 --> 00:33:17,880
description, so go follow him there.

993
00:33:17,880 --> 00:33:20,320
Always clearly breaking down things. We,

994
00:33:20,320 --> 00:33:21,703
uh,

995
00:33:21,703 --> 00:33:21,840
>> [sighs]

996
00:33:21,840 --> 00:33:22,880
>> I have to be real with you. You weren't

997
00:33:22,880 --> 00:33:24,520
going to come on the show today.

998
00:33:24,520 --> 00:33:26,640
>> I wasn't, and I'll be honest, I I told

999
00:33:26,640 --> 00:33:27,960
Greg, and I'm just going to be frank.

1000
00:33:27,960 --> 00:33:31,760
I'm like, I don't have that banger, you

1001
00:33:31,760 --> 00:33:33,200
know, something new dropping, let's

1002
00:33:33,200 --> 00:33:35,640
review it, cuz if we going to be honest,

1003
00:33:35,640 --> 00:33:36,960
there's not that many tools dropping

1004
00:33:36,960 --> 00:33:39,280
nowadays. Like, unfortunately, the big

1005
00:33:39,280 --> 00:33:40,400
dogs are running the show.

1006
00:33:40,400 --> 00:33:40,920
>> Yeah.

1007
00:33:40,920 --> 00:33:42,920
>> Um, the Clauds and the

1008
00:33:42,920 --> 00:33:44,760
the Anthropics and the Open AI,

1009
00:33:44,760 --> 00:33:46,120
especially when it comes to general

1010
00:33:46,120 --> 00:33:47,560
purpose and

1011
00:33:47,560 --> 00:33:49,000
and coding,

1012
00:33:49,000 --> 00:33:50,840
they sort of run the game, so they're

1013
00:33:50,840 --> 00:33:53,680
releasing updates, and like all the

1014
00:33:53,680 --> 00:33:54,720
stuff has already been covered. So, I

1015
00:33:54,720 --> 00:33:56,280
was like, Greg, I don't know if I have

1016
00:33:56,280 --> 00:33:57,120
anything valuable to add.

1017
00:33:57,120 --> 00:33:58,200
>> And what did I say?

1018
00:33:58,200 --> 00:33:59,240
>> You're like, the people, you know, you

1019
00:33:59,240 --> 00:34:00,560
got to think about impact. You got to

1020
00:34:00,560 --> 00:34:02,240
think about what, you know, this could

1021
00:34:02,240 --> 00:34:03,760
apply to someone's And you showed me

1022
00:34:03,760 --> 00:34:05,600
like a a text someone, right?

1023
00:34:05,600 --> 00:34:07,000
>> I sent a text to you.

1024
00:34:07,000 --> 00:34:09,399
>> Yeah. I'm going to pull it up.

1025
00:34:09,399 --> 00:34:14,159
Uh, I sent a text to you of someone who

1026
00:34:14,159 --> 00:34:16,399
saw a video that we did together,

1027
00:34:16,399 --> 00:34:20,200
and it that video got him into coding.

1028
00:34:20,200 --> 00:34:21,919
Now, he's running a cake business, and

1029
00:34:21,919 --> 00:34:25,240
he's making $150,000 a year and growing.

1030
00:34:25,240 --> 00:34:26,879
And he said,

1031
00:34:26,879 --> 00:34:29,280
"The Greg and Ross Mike

1032
00:34:29,280 --> 00:34:31,240
episode in November last year is what

1033
00:34:31,240 --> 00:34:33,120
got me into coding. I've recommended to

1034
00:34:33,120 --> 00:34:36,760
everyone asking how to start out. And I

1035
00:34:36,760 --> 00:34:37,840
just sent you that text and I said,

1036
00:34:37,840 --> 00:34:39,040
"It's not about the numbers. It's not

1037
00:34:39,040 --> 00:34:41,639
about, you know, cuz you said in the

1038
00:34:41,639 --> 00:34:43,240
text

1039
00:34:43,240 --> 00:34:45,200
>> You don't see it sometimes, right?

1040
00:34:45,200 --> 00:34:47,919
>> everything we do to get to 200k views

1041
00:34:47,919 --> 00:34:48,600
minimum.

1042
00:34:48,600 --> 00:34:49,320
>> yeah, yeah, yeah.

1043
00:34:49,320 --> 00:34:50,800
>> And I'm just like

1044
00:34:50,800 --> 00:34:52,960
I hope this gets 200k views or more, so

1045
00:34:52,960 --> 00:34:54,560
like and comment to to juice those

1046
00:34:54,560 --> 00:34:57,320
algorithms, but if it gets 2,000 and two

1047
00:34:57,320 --> 00:34:59,520
people end up taking this information

1048
00:34:59,520 --> 00:35:01,440
and changes their business, their

1049
00:35:01,440 --> 00:35:03,080
productivity, how they think about

1050
00:35:03,080 --> 00:35:05,120
things, then you know, I think that's

1051
00:35:05,120 --> 00:35:08,200
why I think that's why you and myself

1052
00:35:08,200 --> 00:35:10,600
have been put on this planet Earth is to

1053
00:35:10,600 --> 00:35:12,400
inspire people to get their creative

1054
00:35:12,400 --> 00:35:15,200
juices flowing. And so I thank you for

1055
00:35:15,200 --> 00:35:17,720
for coming on and and taking time out of

1056
00:35:17,720 --> 00:35:18,080
your day.

1057
00:35:18,080 --> 00:35:19,720
>> And I appreciate the motivation and

1058
00:35:19,720 --> 00:35:21,640
yeah, I hope this helps somebody and I

1059
00:35:21,640 --> 00:35:23,160
can't wait to be back with more.

1060
00:35:23,160 --> 00:35:24,480
>> Absolutely. All right, catch you later,

1061
00:35:24,480 --> 00:35:26,840
dude.
