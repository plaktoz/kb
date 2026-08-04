---
title: "From LOOPS to GRAPHS: AI Agents Learn Graph-Based Error Corrections"
channel: Discover AI
date: 2026-07-20
url: "https://www.youtube.com/watch?v=yC9cd3gKaIc"
cover: imgs/cover.jpg
description: From LOOPS to GRAPHS.
language: en
---

# From LOOPS to GRAPHS: AI Agents Learn Graph-Based Error Corrections

From LOOPS to GRAPHS.

# Description

From LOOPS to GRAPHS.

Test-time RAG, prompt injection, skill.md files, Fused Gromov-Wasserstein (FGW) algorithm, training-time graph-theoretical mathematics. Negative knowledge patterns,  highly specific IF-THEN conditional rules.

Language Models as Agents are too brittle if left to figure everything out on the fly.
MemoHarness introduces Dynamic System Configuration.
EMG introduces Algorithmic Error Routing.

Start with MemoHarness RAG-based control layer to dynamically configure the agent's memory and tools, and then you would use EMG's graph-matching inside the agent's procedural memory to ensure it executes the precise sequence of actions without needing costly reflection loops.

all rights w/ authors:
Experience Memory Graph: One-Shot Error Correction for Agents
Wenjun Wang∗
University of Electronic Science and
Technology of China
Chengdu, China
202522080926@std.uestc.edu.cn
Yuchen Fang∗
University of Electronic Science and
Technology of China
Chengdu, China
fangyuchen@std.uestc.edu.cn
Fengrui Liu
University of Electronic Science and
Technology of China
Chengdu, China
202522080925@std.uestc.edu.cn
Zibo Liang
University of Electronic Science and
Technology of China
Chengdu, China
zbliang@std.uestc.edu.cn
Kai Zheng†
University of Electronic Science and
Technology of China
Chengdu, China
zhengkai@uestc.edu.cn
arXiv:2607.13884

#airesearch 
#aiexplained 
#aitechnology 
#nextbots 
#nextgen 
#futuretech

# Transcript

1
00:00:00,350 --> 00:00:01,935
Welcome, everyone. We are happy to have

2
00:00:01,935 --> 00:00:04,884
you back. Today we have a

3
00:00:05,241 --> 00:00:06,852
brand new research paper on integrating

4
00:00:06,852 --> 00:00:08,167
memory optimization with

5
00:00:08,167 --> 00:00:09,185
graph structures

6
00:00:09,185 --> 00:00:11,468
. Let's take a look

7
00:00:11,468 --> 00:00:13,499
. This is the

8
00:00:13,499 --> 00:00:15,726
main idea of ​​ this paper

9
00:00:15,726 --> 00:00:17,835
, and we will talk about it, and

10
00:00:17,835 --> 00:00:19,418
within five minutes

11
00:00:19,418 --> 00:00:21,914
you will understand everything clearly.

12
00:00:21,914 --> 00:00:23,664
But first, yes, we

13
00:00:23,664 --> 00:00:25,414
humans still need

14
00:00:25,414 --> 00:00:27,262
some research, and here is a

15
00:00:27,262 --> 00:00:29,207
paper published on

16
00:00:29,207 --> 00:00:31,152
July 15, 2026. It is an experiment

17
00:00:31,152 --> 00:00:32,659
to improve a

18
00:00:32,659 --> 00:00:34,507
memory graph with one-time error correction for

19
00:00:34,507 --> 00:00:36,403
our agents, and

20
00:00:36,403 --> 00:00:38,153
it is from the University of Electronic Science

21
00:00:38,153 --> 00:00:39,369
and Technology

22
00:00:39,369 --> 00:00:40,730
in

23
00:00:40,730 --> 00:00:42,743
Changdu, China. I asked,

24
00:00:42,743 --> 00:00:45,431
"Where is it located? Changdo!"

25
00:00:45,431 --> 00:00:46,893
I replied, "Look at this

26
00:00:46,893 --> 00:00:49,821
. It's amazing, truly incredible!"

27
00:00:49,821 --> 00:00:51,229
Today we have a

28
00:00:51,229 --> 00:00:52,456
research paper from these

29
00:00:52,456 --> 00:00:55,022
experts, so let's begin. In the

30
00:00:55,022 --> 00:00:56,615
last video,

31
00:00:56,615 --> 00:00:58,527
I showed you here the

32
00:00:58,527 --> 00:01:00,651
MIMO Harness technology, where we talked about an

33
00:01:00,651 --> 00:01:02,563
agent technology that learns from

34
00:01:02,563 --> 00:01:04,528
experience how to optimize its

35
00:01:04,528 --> 00:01:06,599
technology for a

36
00:01:06,599 --> 00:01:08,437
particular task. This is the

37
00:01:08,437 --> 00:01:10,017
thumbnail on YouTube,

38
00:01:10,017 --> 00:01:11,341
if you want to find

39
00:01:11,341 --> 00:01:12,723
and view it.

40
00:01:12,723 --> 00:01:14,554
And now we talk again about

41
00:01:14,554 --> 00:01:16,289
Maimo. Why memory

42
00:01:16,289 --> 00:01:18,196
specifically? Well, it turns out to be the most

43
00:01:18,196 --> 00:01:20,214
important element for

44
00:01:20,214 --> 00:01:22,132
agents and

45
00:01:22,132 --> 00:01:24,189
system dynamics. I have shown you

46
00:01:24,189 --> 00:01:25,850
how the Maimo system learns to

47
00:01:25,850 --> 00:01:27,555
configure the appropriate system for a

48
00:01:27,555 --> 00:01:28,997
new task. This

49
00:01:28,997 --> 00:01:30,390
includes context building,

50
00:01:30,390 --> 00:01:32,445
all the different tools

51
00:01:32,585 --> 00:01:34,021
we need,

52
00:01:34,021 --> 00:01:35,203
full coordination of agents and

53
00:01:35,203 --> 00:01:36,723
sub-agents,

54
00:01:36,723 --> 00:01:38,328
memory dynamics and

55
00:01:38,328 --> 00:01:39,848
creation,

56
00:01:39,848 --> 00:01:41,199
generation settings,

57
00:01:41,199 --> 00:01:42,677
output processing, and

58
00:01:42,677 --> 00:01:45,058
much more. You may be wondering:

59
00:01:45,058 --> 00:01:46,587
What is the main new idea

60
00:01:46,587 --> 00:01:48,158
of ​​ this

61
00:01:48,158 --> 00:01:49,567
initial research paper from our

62
00:01:49,567 --> 00:01:50,996
Chinese colleagues?

63
00:01:50,996 --> 00:01:52,730
It's simple. We

64
00:01:52,730 --> 00:01:54,308
now move from text structures

65
00:01:54,308 --> 00:01:55,595
to

66
00:01:55,595 --> 00:01:57,319
graphical structures. That is, we move from

67
00:01:57,319 --> 00:01:59,026
something for which we do not have a

68
00:01:59,026 --> 00:02:00,732
mathematical basis, such as texts, to

69
00:02:00,732 --> 00:02:02,308
something for which we have a theory of

70
00:02:02,308 --> 00:02:03,839
graphs in

71
00:02:03,839 --> 00:02:05,239
mathematics, and we are

72
00:02:05,239 --> 00:02:06,569
more precise. This is the

73
00:02:06,569 --> 00:02:08,391
qualitative leap today.

74
00:02:08,391 --> 00:02:11,227
Let's take a look. EMG, or

75
00:02:11,227 --> 00:02:13,032
Experience Memory Schema,

76
00:02:13,032 --> 00:02:14,838
now learns the

77
00:02:14,838 --> 00:02:16,643
procedure-level corrections and

78
00:02:16,643 --> 00:02:18,036
workflows that need to be

79
00:02:18,036 --> 00:02:19,912
entered into the agent. Here he is

80
00:02:19,912 --> 00:02:21,853
comparing a

81
00:02:21,853 --> 00:02:26,151
failed path with a successful one.

82
00:02:26,151 --> 00:02:27,812
This represents both the

83
00:02:27,812 --> 00:02:30,339
graph as a

84
00:02:30,462 --> 00:02:32,034
decision-making graph based on the

85
00:02:32,034 --> 00:02:33,696
structure of nodes and edges, and

86
00:02:33,696 --> 00:02:34,864
mathematically calculates the

87
00:02:34,864 --> 00:02:37,436
structural adjustments

88
00:02:38,717 --> 00:02:40,706
needed to turn failure

89
00:02:40,706 --> 00:02:44,366
into success. These patches are stored

90
00:02:44,958 --> 00:02:46,216
offline and can be

91
00:02:46,216 --> 00:02:47,766
retrieved before a

92
00:02:47,766 --> 00:02:50,011
new implementation. You might ask: Why do

93
00:02:50,011 --> 00:02:51,737
we do this? Okay, so what

94
00:02:51,737 --> 00:02:53,076
's the current situation?

95
00:02:53,076 --> 00:02:54,262
Currently, if a

96
00:02:54,262 --> 00:02:55,481
customer fails, you say, "

97
00:02:55,481 --> 00:02:56,634
I failed," and you think about

98
00:02:56,634 --> 00:02:57,755
why you failed, and then you try

99
00:02:57,755 --> 00:02:59,842
again, hoping that the

100
00:02:59,963 --> 00:03:01,182
Directed Learning (LLM) model is smart

101
00:03:01,182 --> 00:03:02,415
enough. But as it turns out,

102
00:03:02,415 --> 00:03:03,623
especially for small-scale

103
00:03:03,623 --> 00:03:04,429
directed learning models

104
00:03:04,429 --> 00:03:06,482
, such as

105
00:03:06,504 --> 00:03:07,495
free-trainable parameter models

106
00:03:07,495 --> 00:03:08,673
that contain four

107
00:03:08,673 --> 00:03:09,695
or eight billion

108
00:03:09,695 --> 00:03:10,624
parameters and reside

109
00:03:10,624 --> 00:03:11,646
locally on your laptop

110
00:03:11,646 --> 00:03:12,669
, this has two

111
00:03:12,669 --> 00:03:14,098
drawbacks. First, it is

112
00:03:14,098 --> 00:03:15,630
extremely expensive, because

113
00:03:15,630 --> 00:03:17,359
running the directed learning model

114
00:03:17,359 --> 00:03:19,138
multiple times for each

115
00:03:19,138 --> 00:03:20,867
test case drains

116
00:03:20,867 --> 00:03:22,696
all of

117
00:03:22,696 --> 00:03:24,505
your tokens. Secondly, as I

118
00:03:24,505 --> 00:03:27,480
mentioned, it depends on the intelligence of

119
00:03:28,508 --> 00:03:30,057
your guided learning model to diagnose its

120
00:03:30,057 --> 00:03:33,067
errors. And guess what?

121
00:03:33,894 --> 00:03:35,435
Small, guided learning models simply do not

122
00:03:35,435 --> 00:03:37,217
excel at this task.

123
00:03:37,217 --> 00:03:38,859
It's not as good as

124
00:03:38,859 --> 00:03:40,548
Fable

125
00:03:40,548 --> 00:03:42,236
Five; it's stuck in

126
00:03:42,236 --> 00:03:44,879
endless error loops. To make matters more

127
00:03:45,077 --> 00:03:46,767
complicated, look at these

128
00:03:46,767 --> 00:03:48,120
episodes we have

129
00:03:48,120 --> 00:03:50,060
. We have the LLM core, and

130
00:03:50,060 --> 00:03:52,017
then here in the

131
00:03:52,017 --> 00:03:54,080
processing system we have the Air loop which

132
00:03:54,080 --> 00:03:55,878
causes countless problems

133
00:03:55,878 --> 00:03:57,318
. Therefore,

134
00:03:57,318 --> 00:03:58,917
millions of tokens are wasted without

135
00:03:58,917 --> 00:04:01,662
any result.

136
00:04:01,983 --> 00:04:04,536
So what is the solution?

137
00:04:04,594 --> 00:04:06,609
The new idea is to move the

138
00:04:06,609 --> 00:04:08,625
error correction mechanism from a

139
00:04:08,625 --> 00:04:10,037
simple LLM guess

140
00:04:10,037 --> 00:04:12,002
to predict the next code

141
00:04:12,002 --> 00:04:13,816
in a natural human language like English

142
00:04:13,816 --> 00:04:15,328
to a much more

143
00:04:15,328 --> 00:04:18,244
powerful algorithm, the

144
00:04:20,671 --> 00:04:23,284
deterministic mathematical graph matching algorithm.

145
00:04:23,755 --> 00:04:26,445
You will now understand what we are

146
00:04:27,367 --> 00:04:29,454
dealing with. Do not ask

147
00:04:29,454 --> 00:04:31,199
the agent to verbally explain why he

148
00:04:31,199 --> 00:04:32,848
failed. Present the

149
00:04:32,848 --> 00:04:34,044
failed behavior and the

150
00:04:34,044 --> 00:04:35,838
correct behavior as

151
00:04:35,838 --> 00:04:37,602
graphs. Calculate mathematically the

152
00:04:37,602 --> 00:04:39,066
structural difference between

153
00:04:39,066 --> 00:04:40,131
these two

154
00:04:40,131 --> 00:04:41,773
different types of

155
00:04:41,773 --> 00:04:43,149
graphs in a

156
00:04:43,149 --> 00:04:44,524
mathematical space, and store this

157
00:04:44,524 --> 00:04:47,033
difference as a reusable correction memory for the

158
00:04:48,563 --> 00:04:50,561
next task. As you can see, this

159
00:04:50,561 --> 00:04:52,289
is the solution in the simplest

160
00:04:52,289 --> 00:04:54,220
possible way, and I have put an

161
00:04:54,220 --> 00:04:56,049
exclamation mark here to assure you

162
00:04:56,049 --> 00:04:57,574
that this is the

163
00:04:57,574 --> 00:04:59,861
right way. So, you might be

164
00:04:59,861 --> 00:05:01,748
wondering: how do we learn this

165
00:05:01,748 --> 00:05:03,687
on graphs? Let's assume we

166
00:05:03,687 --> 00:05:05,039
conducted

167
00:05:05,039 --> 00:05:06,672
some tests. We

168
00:05:06,672 --> 00:05:08,151
now have a failed graph

169
00:05:08,151 --> 00:05:09,466
where the worker failed to

170
00:05:09,466 --> 00:05:10,586
find a solution. We have

171
00:05:10,586 --> 00:05:11,541
a lot of

172
00:05:11,541 --> 00:05:12,727
dead ends,

173
00:05:12,727 --> 00:05:14,013
wrong ends, and so on.

174
00:05:14,013 --> 00:05:15,415
Then we have a

175
00:05:15,415 --> 00:05:17,064
successful chart where we achieved

176
00:05:17,064 --> 00:05:18,422
outstanding success.

177
00:05:18,422 --> 00:05:20,011
The task seems simple now. No

178
00:05:20,011 --> 00:05:21,492
, we are only comparing the

179
00:05:21,492 --> 00:05:22,973
complexity of this

180
00:05:22,973 --> 00:05:24,206
graph's structure.

181
00:05:24,206 --> 00:05:25,752
Sometimes the graph contains

182
00:05:25,752 --> 00:05:27,299
10,000 nodes

183
00:05:27,299 --> 00:05:28,887
or even millions of nodes, and

184
00:05:28,887 --> 00:05:30,476
you realize that this

185
00:05:30,476 --> 00:05:31,939
mathematical process is not that

186
00:05:31,939 --> 00:05:33,766
simple. So how can we

187
00:05:33,766 --> 00:05:38,294
improve it? Instead of

188
00:05:38,294 --> 00:05:40,352
asking the Learning-

189
00:05:40,352 --> 00:05:42,192
Led-Mechanism (LLM) model

190
00:05:42,192 --> 00:05:44,195
to guess the error, and relying

191
00:05:44,195 --> 00:05:46,036
on it only if we want

192
00:05:46,036 --> 00:05:48,201
prior knowledge, the

193
00:05:48,201 --> 00:05:50,096
researcher now has two entry points

194
00:05:50,096 --> 00:05:51,558
to the learning process:

195
00:05:51,558 --> 00:05:53,074
exploring the

196
00:05:53,074 --> 00:05:55,077
failing agent (this is the

197
00:05:55,077 --> 00:05:56,755
failing graph), and the

198
00:05:56,755 --> 00:05:58,812
successful expert path (the

199
00:05:58,812 --> 00:06:00,924
blue graph

200
00:06:00,924 --> 00:06:03,303
on the right). So,

201
00:06:03,303 --> 00:06:04,707
they now take both

202
00:06:04,707 --> 00:06:06,161
timelines of

203
00:06:06,161 --> 00:06:07,953
comparative learning here and

204
00:06:07,953 --> 00:06:10,697
turn them into

205
00:06:11,005 --> 00:06:12,749
direct decision-making graphs,

206
00:06:12,749 --> 00:06:14,057
where the nodes represent

207
00:06:14,057 --> 00:06:15,753
actions, such as picking up the

208
00:06:15,753 --> 00:06:18,061
apple, and the edges represent

209
00:06:18,660 --> 00:06:20,404
environmental observations, such as what's on the

210
00:06:20,404 --> 00:06:24,252
table. Then they use an

211
00:06:24,252 --> 00:06:25,812
algorithm such as Weiserstein's

212
00:06:25,812 --> 00:06:27,060
integrated graph

213
00:06:27,060 --> 00:06:29,086
. If

214
00:06:29,086 --> 00:06:31,046
you want to know the

215
00:06:31,920 --> 00:06:33,109
precise mathematical algorithms for calculating

216
00:06:33,109 --> 00:06:35,664
the differences between the two

217
00:06:35,898 --> 00:06:37,453
different graph structures, the solution is

218
00:06:37,453 --> 00:06:38,596
simple: the

219
00:06:38,596 --> 00:06:40,379
overlapping parts of the two

220
00:06:40,379 --> 00:06:43,117
graphs now become a

221
00:06:43,946 --> 00:06:45,776
common subgraph. This is the

222
00:06:45,776 --> 00:06:47,735
correct workflow, and it has been

223
00:06:47,735 --> 00:06:49,434
implemented correctly.

224
00:06:49,434 --> 00:06:50,606
Also, in the

225
00:06:50,606 --> 00:06:51,819
failed graph,

226
00:06:51,819 --> 00:06:53,437
let's say from step 1 to

227
00:06:53,437 --> 00:06:54,650
step 25, this is the

228
00:06:54,650 --> 00:06:56,146
correct path

229
00:06:56,146 --> 00:06:58,405
forward. Then, starting from

230
00:06:58,405 --> 00:06:59,984
step 25, you now see a

231
00:06:59,984 --> 00:07:01,424
difference in the structure of the

232
00:07:01,424 --> 00:07:03,050
graph, and

233
00:07:03,050 --> 00:07:04,582
this difference has become

234
00:07:04,582 --> 00:07:06,208
the paths for modifying the

235
00:07:06,208 --> 00:07:07,880
graph: that is, the action

236
00:07:07,880 --> 00:07:09,367
that should be deleted,

237
00:07:09,367 --> 00:07:11,225
new ideas added, or the

238
00:07:11,225 --> 00:07:13,036
whole renamed based

239
00:07:13,036 --> 00:07:14,476
on a

240
00:07:14,476 --> 00:07:16,102
specific observation to turn the

241
00:07:16,102 --> 00:07:17,727
failing graph into a

242
00:07:17,727 --> 00:07:22,441
successful graph. Now,

243
00:07:23,191 --> 00:07:26,087
this Fastin distance, as I mentioned earlier, is a

244
00:07:26,594 --> 00:07:28,296
precise mathematical engine that allows the system

245
00:07:28,296 --> 00:07:30,948
to compare the form and content of the

246
00:07:31,067 --> 00:07:32,963
AI's own behavior,

247
00:07:32,963 --> 00:07:34,324
using

248
00:07:34,324 --> 00:07:36,220
graph theory,

249
00:07:36,220 --> 00:07:38,019
completely eliminating the need

250
00:07:38,019 --> 00:07:39,769
for a linear linguistic model,

251
00:07:39,769 --> 00:07:41,665
as in the previous video

252
00:07:41,665 --> 00:07:43,415
, to pinpoint the error

253
00:07:43,415 --> 00:07:44,728
in

254
00:07:44,728 --> 00:07:46,672
my AI system or

255
00:07:46,672 --> 00:07:47,985
in

256
00:07:47,985 --> 00:07:50,393
another AI system. Therefore, we do

257
00:07:50,393 --> 00:07:52,286
not rely on a

258
00:07:52,286 --> 00:07:54,400
black box, but rather we have a

259
00:07:54,400 --> 00:07:56,488
mathematical model. How is that done?

260
00:07:56,488 --> 00:07:58,797
Simply put, both graphs are fed

261
00:07:58,972 --> 00:08:00,247
into this algorithm.

262
00:08:00,247 --> 00:08:02,640
The algorithm

263
00:08:03,369 --> 00:08:05,099
iteratively rearranges the nodes in a

264
00:08:05,099 --> 00:08:06,877
defined mathematical space, attempting to

265
00:08:06,877 --> 00:08:08,126
minimize the

266
00:08:08,126 --> 00:08:09,864
combined cost. As you can see,

267
00:08:09,864 --> 00:08:11,726
we have here a mathematical procedure for

268
00:08:11,726 --> 00:08:13,588
optimization, as

269
00:08:13,588 --> 00:08:14,938
in AI training

270
00:08:14,938 --> 00:08:17,521
, until the

271
00:08:19,406 --> 00:08:22,227
optimal flexible allocation matrix is ​​ found. I might ask: What is it

272
00:08:22,227 --> 00:08:24,243
? Let's take a look.

273
00:08:24,243 --> 00:08:26,097
It's simple. The matrix

274
00:08:26,097 --> 00:08:27,389
is ​​ a network that illustrates

275
00:08:27,389 --> 00:08:28,491
here the probability that

276
00:08:28,491 --> 00:08:29,745
node I in the

277
00:08:29,745 --> 00:08:31,190
field graph (

278
00:08:31,190 --> 00:08:32,710
red graph) will match

279
00:08:32,710 --> 00:08:34,078
node J in the

280
00:08:34,078 --> 00:08:35,598
expert graph (

281
00:08:35,598 --> 00:08:36,801
blue graph).

282
00:08:36,801 --> 00:08:39,448
Thanks to the Vaserashstein component, the

283
00:08:40,494 --> 00:08:42,441
identical procedures are correctly linked here. You

284
00:08:42,441 --> 00:08:44,039
might say: Great, but we

285
00:08:44,039 --> 00:08:45,595
also need the

286
00:08:45,595 --> 00:08:47,280
grammar section because it

287
00:08:47,280 --> 00:08:48,620
represents the chronological order here

288
00:08:48,620 --> 00:08:50,075
. So, if

289
00:08:50,075 --> 00:08:52,009
you want the edges of observation, the

290
00:08:52,009 --> 00:08:53,992
"taking the

291
00:08:53,992 --> 00:08:55,777
apple" action from step 2 will not be accidentally linked to the

292
00:08:55,777 --> 00:08:57,612
"taking the apple" action

293
00:08:57,612 --> 00:08:59,348
in step 50

294
00:08:59,348 --> 00:09:01,083
, when the

295
00:09:01,083 --> 00:09:03,017
entire environment changes and

296
00:09:03,017 --> 00:09:04,554
we have a

297
00:09:04,554 --> 00:09:06,191
completely different timeline, because the

298
00:09:06,191 --> 00:09:07,778
structural penalty

299
00:09:07,778 --> 00:09:09,612
would be too high

300
00:09:09,612 --> 00:09:11,001
under the rules of this

301
00:09:11,001 --> 00:09:13,691
optimization. I am asking here, and

302
00:09:13,691 --> 00:09:15,334
this is a diagram of an

303
00:09:15,334 --> 00:09:17,165
artificial intelligence generator. I don't draw it

304
00:09:17,165 --> 00:09:18,631
.

305
00:09:18,631 --> 00:09:20,366
Some people ask me: Do you do this? No

306
00:09:20,366 --> 00:09:21,253
, I just give

307
00:09:21,253 --> 00:09:22,276
instructions to my

308
00:09:22,276 --> 00:09:23,367
AI system to

309
00:09:23,367 --> 00:09:24,815
build it. Therefore, it is a

310
00:09:24,815 --> 00:09:26,654
combined graph.

311
00:09:26,654 --> 00:09:28,104
Yes, of course we have to integrate it

312
00:09:28,104 --> 00:09:30,062
. I will explain the reason to you.

313
00:09:30,062 --> 00:09:31,520
Here we have an

314
00:09:31,520 --> 00:09:32,824
aligned graph by combining the

315
00:09:32,824 --> 00:09:34,421
node's content and structure. Let's

316
00:09:34,421 --> 00:09:35,856
begin. Here we have

317
00:09:35,856 --> 00:09:37,461
again the

318
00:09:37,461 --> 00:09:38,531
red graph, the

319
00:09:38,531 --> 00:09:40,154
unsuccessful G graph.

320
00:09:40,154 --> 00:09:41,502
Then we have the successful

321
00:09:41,502 --> 00:09:43,000
G-Blue chart

322
00:09:43,000 --> 00:09:44,916
. Now that they have

323
00:09:44,916 --> 00:09:47,427
been combined, we have what is called the cost of

324
00:09:48,040 --> 00:09:49,611
observation. Here, it

325
00:09:49,611 --> 00:09:51,236
represents a difference in content

326
00:09:51,236 --> 00:09:53,001
or feature. Then we have the

327
00:09:53,001 --> 00:09:54,780
structure cost function,

328
00:09:54,780 --> 00:09:56,253
which is a function of the difference in

329
00:09:56,253 --> 00:09:58,919
bilateral relationships. Then

330
00:09:58,919 --> 00:10:00,814
we combine them. Guess

331
00:10:00,814 --> 00:10:02,644
what? Let's take a

332
00:10:02,644 --> 00:10:05,522
closer look now. Let's start with the

333
00:10:05,703 --> 00:10:07,807
red graph. We treat

334
00:10:07,807 --> 00:10:09,748
contracts as actions and edges as

335
00:10:09,748 --> 00:10:11,341
transitions conditioned

336
00:10:11,341 --> 00:10:13,515
by observation. The dense

337
00:10:13,515 --> 00:10:14,490
red structure

338
00:10:14,490 --> 00:10:15,708
in the image,

339
00:10:15,708 --> 00:10:17,066
given its red color, indicates the

340
00:10:17,066 --> 00:10:18,180
presence of some branches of

341
00:10:18,180 --> 00:10:19,294
incorrect actions,

342
00:10:19,294 --> 00:10:20,443
perhaps some

343
00:10:20,443 --> 00:10:21,732
repetitive actions, perhaps some

344
00:10:21,732 --> 00:10:23,089
incorrect loops,

345
00:10:23,089 --> 00:10:24,099
perhaps some dead ends

346
00:10:24,099 --> 00:10:25,074
, and some

347
00:10:25,074 --> 00:10:26,119
transitions that

348
00:10:26,119 --> 00:10:27,511
differ from the expert policy

349
00:10:27,511 --> 00:10:28,904
you see here in

350
00:10:28,904 --> 00:10:31,608
blue. The blue nodes may not appear

351
00:10:31,608 --> 00:10:33,497
in the same

352
00:10:33,497 --> 00:10:36,355
order as G, because this is G-. It

353
00:10:36,355 --> 00:10:37,648
may also contain

354
00:10:37,648 --> 00:10:38,637
some

355
00:10:38,637 --> 00:10:39,702
additional actions, some

356
00:10:39,702 --> 00:10:41,147
missing actions,

357
00:10:41,147 --> 00:10:42,593
some different branches

358
00:10:42,593 --> 00:10:43,962
, and some different edge structures

359
00:10:43,962 --> 00:10:45,177
. We have

360
00:10:45,177 --> 00:10:46,753
different designations for the nodes

361
00:10:46,753 --> 00:10:48,457
or edges, and a completely different number

362
00:10:48,457 --> 00:10:49,793
of nodes.

363
00:10:49,793 --> 00:10:50,891
Now you might be wondering:

364
00:10:50,891 --> 00:10:51,953
Okay, but how

365
00:10:51,953 --> 00:10:54,260
can we compare

366
00:10:54,260 --> 00:10:55,422
these two different graph structures?

367
00:10:55,422 --> 00:10:57,077
Well, that's the beauty

368
00:10:57,077 --> 00:10:58,975
of it, because by using the

369
00:10:58,975 --> 00:11:00,338
fuse squ algorithm,

370
00:11:00,338 --> 00:11:02,042
we can do this

371
00:11:02,042 --> 00:11:03,940
even if the two graphs are not

372
00:11:03,940 --> 00:11:06,693
identical.

373
00:11:07,092 --> 00:11:09,299
Let's take a look now. I

374
00:11:09,299 --> 00:11:11,173
just want to tell you that the

375
00:11:11,173 --> 00:11:12,567
transport map, or

376
00:11:12,567 --> 00:11:14,248
heat map as I call it

377
00:11:14,248 --> 00:11:16,171
here, is the most

378
00:11:16,171 --> 00:11:18,331
important element here. Because its rows

379
00:11:18,331 --> 00:11:19,899
correspond to the nodes of the

380
00:11:19,899 --> 00:11:21,719
graph G, and its columns

381
00:11:21,719 --> 00:11:23,287
correspond to the nodes of the

382
00:11:23,287 --> 00:11:26,163
graph G-. The position of the

383
00:11:26,163 --> 00:11:28,235
bright cell, which

384
00:11:28,235 --> 00:11:30,147
glows in the dark at

385
00:11:30,147 --> 00:11:31,634
position I K,

386
00:11:31,634 --> 00:11:33,759
simply means that the note I in G

387
00:11:33,759 --> 00:11:36,619
matches the note K in G with a

388
00:11:38,970 --> 00:11:42,123
relatively high degree of match strength. So here you see,

389
00:11:42,123 --> 00:11:43,943
in a simple mathematical matrix

390
00:11:43,943 --> 00:11:46,291
, how

391
00:11:46,291 --> 00:11:49,346
this note structure relates between G and G-.

392
00:11:49,409 --> 00:11:50,904
Now note, yes, I asked

393
00:11:50,904 --> 00:11:52,063
you for a diagonal heat map

394
00:11:52,063 --> 00:11:53,558
because it produced this

395
00:11:53,558 --> 00:11:54,978
map, but it doesn't have to

396
00:11:54,978 --> 00:11:56,436
be diagonal

397
00:11:56,436 --> 00:11:57,962
. You can get

398
00:11:57,962 --> 00:11:59,664
irregular diameters,

399
00:11:59,664 --> 00:12:01,231
multiple sets, or a

400
00:12:01,231 --> 00:12:02,907
diffuse pattern. This is not what

401
00:12:02,907 --> 00:12:04,123
we are talking about in

402
00:12:04,123 --> 00:12:05,622
country mapping, or

403
00:12:05,622 --> 00:12:07,222
linking vectors to values.

404
00:12:07,222 --> 00:12:09,992
This is something different.

405
00:12:09,992 --> 00:12:11,837
Here, as I mentioned, we have a

406
00:12:11,837 --> 00:12:13,349
node cost function. What is

407
00:12:13,349 --> 00:12:15,341
its function? Yes, as you can see

408
00:12:15,341 --> 00:12:17,082
, it's a great function. But what is the

409
00:12:17,082 --> 00:12:18,443
main idea?

410
00:12:18,443 --> 00:12:20,415
Simply put, the question is: Does the

411
00:12:20,415 --> 00:12:21,882
transport plan link the

412
00:12:21,882 --> 00:12:23,753
semantically compatible contracts?

413
00:12:23,753 --> 00:12:25,634
It is obvious that linking

414
00:12:25,634 --> 00:12:28,566
which allocates a large block to

415
00:12:29,448 --> 00:12:30,983
semantically incompatible nodes incurs a

416
00:12:30,983 --> 00:12:34,712
high cost. We

417
00:12:34,712 --> 00:12:36,614
now know the contract costs,

418
00:12:36,614 --> 00:12:38,461
but immediately note that

419
00:12:38,461 --> 00:12:40,146
you can have

420
00:12:40,146 --> 00:12:41,450
two actions with the same

421
00:12:41,450 --> 00:12:43,515
ratings, say G3 and G3

422
00:12:43,515 --> 00:12:45,363
, and possibly another action,

423
00:12:45,363 --> 00:12:47,374
while they occupy a completely

424
00:12:47,374 --> 00:12:48,895
different causal position

425
00:12:48,895 --> 00:12:50,960
in the graph structure

426
00:12:50,960 --> 00:12:53,427
. Therefore, we must

427
00:12:53,427 --> 00:12:55,035
somehow take into account this

428
00:12:55,035 --> 00:12:56,515
difference in position

429
00:12:56,515 --> 00:12:57,996
within the graph

430
00:12:57,996 --> 00:13:00,147
itself. This is where the

431
00:13:00,147 --> 00:13:02,412
structure cost function comes in. The

432
00:13:02,412 --> 00:13:04,015
structure cost panel here is

433
00:13:04,015 --> 00:13:05,578
in blue, which

434
00:13:05,578 --> 00:13:06,820
represents the

435
00:13:06,820 --> 00:13:08,183
binary relational asymmetry,

436
00:13:08,183 --> 00:13:09,680
simple. What is required?

437
00:13:09,680 --> 00:13:11,061
The question is: If

438
00:13:11,061 --> 00:13:12,655
relation I is identical

439
00:13:12,655 --> 00:13:14,674
to relation K, and relation J is

440
00:13:14,674 --> 00:13:16,747
identical to relation L, are

441
00:13:16,747 --> 00:13:18,872
the relations from I to J and from K

442
00:13:18,872 --> 00:13:21,777
to L compatible? This is the

443
00:13:21,777 --> 00:13:23,845
essence of the rule pattern matching idea

444
00:13:23,845 --> 00:13:25,845
. It compares

445
00:13:25,845 --> 00:13:27,490
relationships within

446
00:13:27,490 --> 00:13:29,229
one space to relationships within

447
00:13:29,229 --> 00:13:30,968
another space, rather

448
00:13:30,968 --> 00:13:32,566
than requiring both graphs to be

449
00:13:32,566 --> 00:13:34,399
in a

450
00:13:34,399 --> 00:13:36,232
common coordinate system,

451
00:13:36,232 --> 00:13:38,112
where we first need a

452
00:13:38,112 --> 00:13:39,804
binding function to a

453
00:13:39,804 --> 00:13:41,450
unique mathematical space. We can

454
00:13:41,450 --> 00:13:42,942
leave these functions in

455
00:13:42,942 --> 00:13:44,621
their spaces and compare them

456
00:13:44,621 --> 00:13:47,961
using grom. Yes. The

457
00:13:47,961 --> 00:13:49,641
central objective

458
00:13:49,641 --> 00:13:51,513
now combines these two signals.

459
00:13:51,513 --> 00:13:53,373
Therefore, we now have the

460
00:13:53,373 --> 00:13:55,086
node cost function and the

461
00:13:55,086 --> 00:13:56,261
structure cost function

462
00:13:56,261 --> 00:13:58,730
combined, in

463
00:13:59,688 --> 00:14:02,848
Vaserstein's combined graph target. As you can see,

464
00:14:02,848 --> 00:14:04,403
here specifically we have

465
00:14:04,403 --> 00:14:05,770
node compatibility with

466
00:14:05,770 --> 00:14:08,279
relational compatibility.

467
00:14:09,680 --> 00:14:11,723
This is a simplified explanation of a somewhat

468
00:14:11,723 --> 00:14:13,938
complex mathematical concept

469
00:14:13,938 --> 00:14:16,837
. But, of course, you might say:

470
00:14:16,837 --> 00:14:18,385
"Okay, can you

471
00:14:18,385 --> 00:14:19,807
explain to me here the

472
00:14:19,807 --> 00:14:21,455
purely mathematical aspect of this?"

473
00:14:21,455 --> 00:14:23,390
Here it is. As you can see, I have

474
00:14:23,390 --> 00:14:25,748
explained this simple mathematical formula to you in

475
00:14:26,105 --> 00:14:27,709
easy-to-understand English words

476
00:14:27,709 --> 00:14:28,902
so that

477
00:14:28,902 --> 00:14:30,506
everyone can understand it. Even though

478
00:14:30,506 --> 00:14:32,018
some of my viewers

479
00:14:32,018 --> 00:14:33,264
feel a little intimidated

480
00:14:33,264 --> 00:14:34,643
when I see a

481
00:14:34,643 --> 00:14:36,402
mathematical equation. See

482
00:14:36,402 --> 00:14:38,291
how simple and easy it is.

483
00:14:38,291 --> 00:14:40,431
It's just two limits, and now you

484
00:14:40,431 --> 00:14:42,464
fully understand what

485
00:14:42,464 --> 00:14:44,090
each limit does. But of course,

486
00:14:44,090 --> 00:14:45,485
we can translate this

487
00:14:45,485 --> 00:14:47,015
mathematical equation

488
00:14:47,015 --> 00:14:48,758
into an understandable language. This

489
00:14:48,758 --> 00:14:50,661
sentence simply means that

490
00:14:50,661 --> 00:14:52,231
good

491
00:14:52,231 --> 00:14:54,801
contract alignment is not just linking

492
00:14:55,275 --> 00:14:57,083
semantically similar contracts, but also

493
00:14:57,083 --> 00:14:58,130
linking

494
00:14:58,130 --> 00:14:59,700
relational neighbors in

495
00:14:59,700 --> 00:15:01,270
one graph to

496
00:15:01,270 --> 00:15:03,125
compatible relational neighbors in

497
00:15:03,125 --> 00:15:04,886
another graph or

498
00:15:04,886 --> 00:15:07,083
another section of the graph. That's

499
00:15:07,083 --> 00:15:09,891
all it tells you.

500
00:15:09,891 --> 00:15:11,541
Now, if you want an

501
00:15:11,541 --> 00:15:13,142
algorithm to build this action

502
00:15:13,142 --> 00:15:14,841
decision graph

503
00:15:14,841 --> 00:15:16,155
, here it is. And

504
00:15:16,155 --> 00:15:17,698
of course, we just talked about

505
00:15:17,698 --> 00:15:19,153
this to extract

506
00:15:19,153 --> 00:15:20,740
the comments and update them

507
00:15:20,740 --> 00:15:22,296
to match the contract here.

508
00:15:22,296 --> 00:15:23,968
This is part one.

509
00:15:23,968 --> 00:15:25,524
This is the red part and

510
00:15:25,524 --> 00:15:27,356
this is the blue part.

511
00:15:27,356 --> 00:15:28,786
If you want to see that

512
00:15:28,786 --> 00:15:30,132
here in this code,

513
00:15:30,132 --> 00:15:31,815
it means that for

514
00:15:31,815 --> 00:15:33,288
this conformity, the

515
00:15:33,288 --> 00:15:34,887
system can now determine what

516
00:15:34,887 --> 00:15:36,360
was already true,

517
00:15:36,360 --> 00:15:38,043
which is here the

518
00:15:38,043 --> 00:15:39,599
common subgraph, and what

519
00:15:39,599 --> 00:15:41,240
should be deleted, inserted,

520
00:15:41,240 --> 00:15:42,461
renamed, or

521
00:15:42,461 --> 00:15:43,891
modified here in

522
00:15:43,891 --> 00:15:45,532
our graph structure,

523
00:15:45,532 --> 00:15:46,752
so that

524
00:15:46,752 --> 00:15:48,225
our G-graph becomes

525
00:15:48,225 --> 00:15:51,055
closer to G- in terms of

526
00:15:51,055 --> 00:15:54,311
structural symmetry. Now

527
00:15:54,311 --> 00:15:55,915
, here we see the

528
00:15:55,915 --> 00:15:57,688
complete process. No, we have that

529
00:15:57,688 --> 00:15:59,635
in our test here.

530
00:15:59,635 --> 00:16:03,556
Yes, this is particularly important

531
00:16:03,556 --> 00:16:05,348
during training time, because we

532
00:16:05,348 --> 00:16:07,095
want to use it later

533
00:16:07,095 --> 00:16:08,584
during reasoning.

534
00:16:08,584 --> 00:16:09,968
Therefore, we need to prepare the

535
00:16:09,968 --> 00:16:11,520
training data, and

536
00:16:11,520 --> 00:16:12,821
minute by minute,

537
00:16:12,821 --> 00:16:13,828
we have the

538
00:16:13,828 --> 00:16:15,255
failed exploration paths

539
00:16:15,255 --> 00:16:16,849
where the worker cannot

540
00:16:16,849 --> 00:16:18,359
come up with a correct solution, and

541
00:16:18,359 --> 00:16:19,744
then we have the

542
00:16:19,744 --> 00:16:21,380
successful paths, and all

543
00:16:21,380 --> 00:16:22,849
these training examples, and

544
00:16:22,849 --> 00:16:24,614
intensive training materials. Here we build

545
00:16:24,614 --> 00:16:25,787
our paths, and

546
00:16:25,787 --> 00:16:27,187
of course, if

547
00:16:27,187 --> 00:16:28,586
the system fails, we get

548
00:16:28,586 --> 00:16:30,301
failed paths where we get

549
00:16:30,301 --> 00:16:31,836
to a dead end, or

550
00:16:31,836 --> 00:16:33,506
simply see that this is not

551
00:16:33,506 --> 00:16:34,877
working. From the

552
00:16:34,877 --> 00:16:37,213
successful paths, we have here the

553
00:16:37,628 --> 00:16:39,161
ideal graph structure, we have a

554
00:16:39,161 --> 00:16:41,704
working graph structure. This is not the

555
00:16:41,767 --> 00:16:42,906
optimal graph structure, and

556
00:16:42,906 --> 00:16:44,387
we will talk about this later

557
00:16:44,387 --> 00:16:45,602
; But it works, and

558
00:16:45,602 --> 00:16:47,038
we've found a solution. Then we do

559
00:16:47,038 --> 00:16:48,604
exactly what we just talked about

560
00:16:48,604 --> 00:16:50,088
: we have the

561
00:16:50,088 --> 00:16:51,406
graph matching, and

562
00:16:51,406 --> 00:16:52,931
this alignment engine,

563
00:16:52,931 --> 00:16:54,579
where we see: "Okay,

564
00:16:54,579 --> 00:16:56,898
here in green we have the

565
00:16:57,546 --> 00:16:58,989
shared subgraph, and then in

566
00:16:58,989 --> 00:17:00,513
red the parts

567
00:17:00,513 --> 00:17:01,889
we identified." The nodes

568
00:17:01,889 --> 00:17:04,075
and edges are not identical

569
00:17:04,075 --> 00:17:06,148
in G and G-, so we need to

570
00:17:06,148 --> 00:17:08,390
pay attention to them; Therefore,

571
00:17:08,390 --> 00:17:10,071
we begin here to construct

572
00:17:10,071 --> 00:17:12,033
the graph of the

573
00:17:12,033 --> 00:17:14,219
final solution, which we call

574
00:17:14,219 --> 00:17:16,236
here the EMG, i.e., the

575
00:17:16,236 --> 00:17:18,702
experience memory graph. That's all

576
00:17:18,702 --> 00:17:20,376
, in the simplest way possible

577
00:17:20,376 --> 00:17:21,749
, but of course, we don't give up

578
00:17:21,749 --> 00:17:22,865
on everything we

579
00:17:22,865 --> 00:17:24,195
've learned during this

580
00:17:24,195 --> 00:17:27,277
process. Here we use

581
00:17:27,277 --> 00:17:29,067
every element, even

582
00:17:29,067 --> 00:17:31,144
failures. We put it into a

583
00:17:31,144 --> 00:17:32,828
database. Therefore, we know

584
00:17:32,828 --> 00:17:34,702
exactly what did not succeed in a

585
00:17:34,702 --> 00:17:36,423
particular task in a

586
00:17:36,423 --> 00:17:38,348
particular situation at a particular level of complexity

587
00:17:38,348 --> 00:17:40,521
. And imagine what

588
00:17:40,521 --> 00:17:42,198
exactly happens: the more we develop

589
00:17:42,198 --> 00:17:43,695
this, the

590
00:17:43,695 --> 00:17:45,191
deeper understanding we gain of how to

591
00:17:45,191 --> 00:17:46,824
build a better graph structure

592
00:17:46,824 --> 00:17:48,592
next time

593
00:17:48,592 --> 00:17:49,768
. Faster,

594
00:17:49,768 --> 00:17:51,520
uses less code, and has higher

595
00:17:51,520 --> 00:17:53,030
accuracy. While

596
00:17:53,030 --> 00:17:54,566
reading this

597
00:17:54,566 --> 00:17:56,377
research paper, a question came to mind.

598
00:17:56,377 --> 00:17:58,597
I said: Just a moment, we are

599
00:17:58,597 --> 00:18:00,720
now comparing G and G Dash. But

600
00:18:00,720 --> 00:18:02,578
what about how to devise a

601
00:18:02,578 --> 00:18:05,144
new mathematical structure for the

602
00:18:05,414 --> 00:18:06,700
non-

603
00:18:06,700 --> 00:18:07,986
shared subpart of the

604
00:18:07,986 --> 00:18:09,355
graph, i.e., the

605
00:18:09,355 --> 00:18:11,082
open part? No, there is no solution to this

606
00:18:11,082 --> 00:18:12,591
, because the system is now

607
00:18:12,591 --> 00:18:13,848
required to almost

608
00:18:13,848 --> 00:18:15,441
find a new path on a

609
00:18:15,441 --> 00:18:16,866
graph of

610
00:18:16,866 --> 00:18:18,249
unknown complexity for my

611
00:18:18,249 --> 00:18:19,716
particular problem in

612
00:18:19,716 --> 00:18:21,759
theoretical physics. But how does the

613
00:18:21,759 --> 00:18:24,530
system do that? I continued

614
00:18:24,530 --> 00:18:26,266
reading the paper,

615
00:18:26,266 --> 00:18:28,788
and it became clear to me that it simply does

616
00:18:28,788 --> 00:18:30,099
not do that at

617
00:18:30,099 --> 00:18:31,804
all, because I had

618
00:18:31,804 --> 00:18:33,072
previously stated that

619
00:18:33,072 --> 00:18:35,645
this database, the offline database

620
00:18:36,394 --> 00:18:37,793
, is built

621
00:18:37,793 --> 00:18:39,644
during training. This

622
00:18:39,644 --> 00:18:41,319
means how is the training data constructed

623
00:18:41,319 --> 00:18:42,966
? This means that for

624
00:18:42,966 --> 00:18:44,264
each task in the

625
00:18:44,264 --> 00:18:45,714
training set, there are two things:

626
00:18:45,714 --> 00:18:47,050
failed attempts (

627
00:18:47,050 --> 00:18:48,195
G-chart,

628
00:18:48,195 --> 00:18:49,683
red chart)

629
00:18:49,683 --> 00:18:51,172
, and the expert's path (

630
00:18:51,172 --> 00:18:52,508
G-Dash chart,

631
00:18:52,508 --> 00:18:54,123
blue chart). Now

632
00:18:54,123 --> 00:18:55,810
, the authors of this

633
00:18:55,810 --> 00:18:57,241
research paper either

634
00:18:57,241 --> 00:18:59,235
provided human solutions,

635
00:18:59,235 --> 00:19:01,126
or used a dataset

636
00:19:01,126 --> 00:19:03,017
from the internet,

637
00:19:03,017 --> 00:19:04,908
or used

638
00:19:04,908 --> 00:19:08,020
expert gold trails. So, as you

639
00:19:08,020 --> 00:19:10,011
understand, the algorithm does

640
00:19:10,011 --> 00:19:12,441
not explore an infinite unknown space

641
00:19:13,229 --> 00:19:15,272
to search for the optimal solution, and

642
00:19:15,272 --> 00:19:17,212
then look for

643
00:19:17,212 --> 00:19:19,153
optimization algorithms. Rather, we

644
00:19:19,153 --> 00:19:21,042
already have the correct solution, but

645
00:19:21,042 --> 00:19:23,085
initially we have an agent that does

646
00:19:23,085 --> 00:19:25,720
not know how to implement it.

647
00:19:26,083 --> 00:19:28,202
It fails repeatedly

648
00:19:28,202 --> 00:19:30,377
, and then we bring it closer and closer to the

649
00:19:30,377 --> 00:19:32,274
expert path on a

650
00:19:32,274 --> 00:19:34,505
graphical structure, not on a

651
00:19:34,505 --> 00:19:37,671
textual structure. Here we calculate the

652
00:19:37,671 --> 00:19:38,968
shortest bridge between the two

653
00:19:38,968 --> 00:19:40,333
known graphs.

654
00:19:40,333 --> 00:19:41,322
If you want the

655
00:19:41,322 --> 00:19:42,654
G graph (red), it is

656
00:19:42,654 --> 00:19:43,780
where

657
00:19:43,780 --> 00:19:45,111
the agent ended up wrong

658
00:19:45,111 --> 00:19:46,203
, and if you want the

659
00:19:46,203 --> 00:19:48,500
G- graph (blue), it is where he should have

660
00:19:48,899 --> 00:19:51,164
ended up. Remember

661
00:19:51,164 --> 00:19:52,490
that I explained to you here

662
00:19:52,490 --> 00:19:53,940
how to derive

663
00:19:53,940 --> 00:19:55,390
and modify the graph from the

664
00:19:55,390 --> 00:19:56,715
matching node,

665
00:19:56,715 --> 00:20:01,270
and how to build and modify G

666
00:20:01,270 --> 00:20:04,630
to get G-. Now,

667
00:20:04,630 --> 00:20:07,242
I will explain this code in

668
00:20:07,863 --> 00:20:10,191
simple words. Let's take a

669
00:20:10,191 --> 00:20:12,159
look at what's happening. The

670
00:20:12,159 --> 00:20:13,754
ZIP system examines the

671
00:20:13,754 --> 00:20:15,176
non-matching parts here and

672
00:20:15,176 --> 00:20:17,469
classifies them into three

673
00:20:17,718 --> 00:20:19,310
distinct mathematical groups. This is the simplest

674
00:20:19,310 --> 00:20:21,041
set, and you can add

675
00:20:21,041 --> 00:20:22,405
any number you want.

676
00:20:22,405 --> 00:20:24,303
First, you have the

677
00:20:24,303 --> 00:20:25,812
delete operations, then the

678
00:20:25,812 --> 00:20:27,418
add operations, and then the

679
00:20:27,418 --> 00:20:29,694
rename operations. Why? This is a

680
00:20:29,694 --> 00:20:31,415
simple process that will take us

681
00:20:31,415 --> 00:20:33,275
to the next step in

682
00:20:33,275 --> 00:20:34,696
our procedure. Let's look

683
00:20:34,696 --> 00:20:35,927
first at the

684
00:20:35,927 --> 00:20:37,365
deletions. The nodes and edges

685
00:20:37,365 --> 00:20:38,509
present in the

686
00:20:38,509 --> 00:20:39,860
failed graph, but which

687
00:20:39,860 --> 00:20:41,212
have no mathematical outlet in the

688
00:20:41,212 --> 00:20:42,528
expert graph

689
00:20:42,528 --> 00:20:43,880
, simply mean deleting that

690
00:20:43,880 --> 00:20:45,438
procedure. No, because it is not

691
00:20:45,438 --> 00:20:47,090
included in the expert solution.

692
00:20:47,090 --> 00:20:48,150
So,

693
00:20:48,150 --> 00:20:49,142
young customer, you're

694
00:20:49,142 --> 00:20:50,576
completely off track.

695
00:20:50,576 --> 00:20:51,683
Addition operations: The nodes

696
00:20:51,683 --> 00:20:52,708
and edges present in the

697
00:20:52,708 --> 00:20:53,788
expert chart are

698
00:20:53,788 --> 00:20:54,646
completely missing in the

699
00:20:54,646 --> 00:20:55,827
failed chart.

700
00:20:55,827 --> 00:20:57,252
We know that we have

701
00:20:57,252 --> 00:20:58,991
missing parts of the solution. Therefore, as a

702
00:20:58,991 --> 00:21:01,009
general rule, we say: add

703
00:21:01,009 --> 00:21:02,354
these

704
00:21:02,354 --> 00:21:04,061
specific actions, and then we have

705
00:21:04,061 --> 00:21:05,862
renaming. This means

706
00:21:05,862 --> 00:21:06,952
that the

707
00:21:06,952 --> 00:21:08,217
failed graph matched a node in the

708
00:21:08,217 --> 00:21:09,588
expert graph

709
00:21:09,588 --> 00:21:10,642
with a node in the

710
00:21:10,642 --> 00:21:11,697
expert graph,

711
00:21:11,697 --> 00:21:12,962
because they appeared in exactly the same

712
00:21:12,962 --> 00:21:13,947
structural place

713
00:21:13,947 --> 00:21:15,036
in the

714
00:21:15,036 --> 00:21:15,810
timeline, but

715
00:21:15,810 --> 00:21:17,035
their labels were different.

716
00:21:17,035 --> 00:21:18,314
Let's suppose, for

717
00:21:18,314 --> 00:21:19,429
example, that in

718
00:21:19,429 --> 00:21:21,039
note y, you chose to put a

719
00:21:21,039 --> 00:21:22,526
pencil on a table,

720
00:21:22,526 --> 00:21:24,094
but the expert chose to put a

721
00:21:24,094 --> 00:21:25,857
pencil on a shelf. So

722
00:21:25,857 --> 00:21:27,517
, we now have a

723
00:21:27,517 --> 00:21:29,275
rebranding from table to

724
00:21:29,275 --> 00:21:31,710
shelf. It looks like a simple process

725
00:21:31,710 --> 00:21:33,675
, but notice something.

726
00:21:33,675 --> 00:21:35,235
This is no longer a

727
00:21:35,235 --> 00:21:37,004
purely mathematical operation, but rather a

728
00:21:37,004 --> 00:21:39,030
graphical mathematical operation.

729
00:21:39,030 --> 00:21:40,536
But we are now in the process of establishing

730
00:21:40,536 --> 00:21:42,085
rules, and these rules

731
00:21:42,085 --> 00:21:43,090
are formulated in

732
00:21:43,090 --> 00:21:44,526
English. Now

733
00:21:44,526 --> 00:21:46,148
we go back to the starting point

734
00:21:46,148 --> 00:21:47,521
, and I think this is the

735
00:21:47,521 --> 00:21:48,644
weak point, or

736
00:21:48,644 --> 00:21:50,225
rather the weak point, in

737
00:21:50,225 --> 00:21:51,681
this wonderful research paper

738
00:21:51,681 --> 00:21:52,679
that

739
00:21:52,679 --> 00:21:54,212
we will now discuss. Did

740
00:21:54,212 --> 00:21:55,625
you understand?

741
00:21:55,625 --> 00:21:57,060
Built-in spaces. But before I

742
00:21:57,060 --> 00:21:58,257
go into detail,

743
00:21:58,257 --> 00:21:59,488
let's take a look at

744
00:21:59,488 --> 00:22:00,838
one of the results. Let's see

745
00:22:00,838 --> 00:22:02,389
how good it is. We

746
00:22:02,389 --> 00:22:04,199
now have the Alpha world, the

747
00:22:04,199 --> 00:22:05,466
Science world, and the Average

748
00:22:05,466 --> 00:22:06,764
Performance. As you can see,

749
00:22:06,764 --> 00:22:08,018
for the 4 billion

750
00:22:08,018 --> 00:22:09,305
miles in the third quarter,

751
00:22:09,305 --> 00:22:10,660
you have all the other models here

752
00:22:10,660 --> 00:22:12,346
. And here in the

753
00:22:12,346 --> 00:22:13,840
pink line, you have EMG, our

754
00:22:13,840 --> 00:22:15,534
new methodology.

755
00:22:15,534 --> 00:22:16,911
Just look at the average

756
00:22:16,911 --> 00:22:18,325
here, in the last column

757
00:22:18,325 --> 00:22:19,548
. As you can see, all the

758
00:22:19,548 --> 00:22:21,157
other elements here are in

759
00:22:21,157 --> 00:22:22,444
the twenties, and

760
00:22:22,444 --> 00:22:24,013
our new methodology is in the

761
00:22:24,013 --> 00:22:25,960
forties. This is a

762
00:22:25,960 --> 00:22:27,570
preliminary indicator, and it seems

763
00:22:27,570 --> 00:22:29,736
interesting, but you

764
00:22:29,736 --> 00:22:31,902
might wonder: why is it

765
00:22:31,902 --> 00:22:34,679
better here specifically?

766
00:22:34,726 --> 00:22:36,387
Especially if we look at the

767
00:22:36,387 --> 00:22:38,048
cost of time in the world of

768
00:22:38,048 --> 00:22:39,848
visible science and the world of

769
00:22:39,848 --> 00:22:41,556
invisible science,

770
00:22:41,556 --> 00:22:43,125
we see that the cost of time

771
00:22:43,125 --> 00:22:44,707
here is measured in minutes.

772
00:22:44,707 --> 00:22:46,414
Our new methodology

773
00:22:46,414 --> 00:22:48,268
wastes almost no time.

774
00:22:48,268 --> 00:22:49,690
Look at the

775
00:22:49,690 --> 00:22:51,477
other reflection here. It takes approximately

776
00:22:51,477 --> 00:22:53,572
four times as much time here

777
00:22:53,572 --> 00:22:55,614
to achieve a certain success rate

778
00:22:55,614 --> 00:22:58,398
. You might ask: Why?

779
00:22:58,398 --> 00:23:00,696
Why does this happen? Think

780
00:23:00,696 --> 00:23:02,926
about it. It's simple.

781
00:23:02,926 --> 00:23:04,289
By framing

782
00:23:04,289 --> 00:23:06,608
error correction as a set of discrete,

783
00:23:08,289 --> 00:23:09,828
case-related editing factors, as I just explained to

784
00:23:09,828 --> 00:23:11,454
you, and derived

785
00:23:11,454 --> 00:23:13,861
from expert templates, the

786
00:23:14,048 --> 00:23:15,954
mathematical complexity collapses. Certainly,

787
00:23:15,954 --> 00:23:17,569
as I told you, we lose

788
00:23:17,569 --> 00:23:19,282
mathematical precision when we

789
00:23:19,282 --> 00:23:20,799
revert to

790
00:23:20,799 --> 00:23:23,685
human language. Now, at the time of

791
00:23:23,685 --> 00:23:24,969
testing, when

792
00:23:24,969 --> 00:23:26,466
the worker is faced with your

793
00:23:26,466 --> 00:23:28,007
real unknown task, and the

794
00:23:28,007 --> 00:23:29,547
expert path is no longer

795
00:23:29,547 --> 00:23:31,259
available, he does not need

796
00:23:31,259 --> 00:23:32,543
to make any graph

797
00:23:32,543 --> 00:23:34,705
. Why? Okay, you've

798
00:23:34,705 --> 00:23:36,565
seen the process.

799
00:23:36,565 --> 00:23:37,590
Simply put,

800
00:23:37,590 --> 00:23:38,873
the program takes the

801
00:23:38,873 --> 00:23:40,283
current task and searches a

802
00:23:40,283 --> 00:23:41,779
database containing

803
00:23:41,779 --> 00:23:43,104
all the

804
00:23:43,104 --> 00:23:44,216
human language corrections

805
00:23:44,216 --> 00:23:45,541
resulting from the

806
00:23:45,541 --> 00:23:48,080
graphing process; It searches

807
00:23:48,362 --> 00:23:50,901
this vector database, applies

808
00:23:51,268 --> 00:23:52,935
simple cosine similarity, and extracts the

809
00:23:52,935 --> 00:23:54,303
presupposed editing path

810
00:23:54,303 --> 00:23:55,457
from the

811
00:23:55,457 --> 00:23:56,953
training task that looks

812
00:23:56,953 --> 00:23:58,712
similar.

813
00:23:58,712 --> 00:24:01,131
This resulting solution is passed from the

814
00:24:01,205 --> 00:24:02,709
vector database to the

815
00:24:02,709 --> 00:24:04,429
language model, to the language model prompt

816
00:24:04,429 --> 00:24:07,569
, as human-like text such as: "

817
00:24:07,569 --> 00:24:09,706
Avoid making mistake X

818
00:24:09,706 --> 00:24:11,781
here, instead,

819
00:24:11,781 --> 00:24:14,585
do Y." And again, you see

820
00:24:14,585 --> 00:24:16,583
how close he is to the skills.

821
00:24:16,583 --> 00:24:17,682
When we have

822
00:24:17,682 --> 00:24:19,100
skills in Markdown files,

823
00:24:19,100 --> 00:24:20,448
and skills that we put here in

824
00:24:20,448 --> 00:24:22,647
databases or in

825
00:24:22,647 --> 00:24:23,711
vector databases, we

826
00:24:23,711 --> 00:24:24,810
include here the

827
00:24:24,810 --> 00:24:25,910
skill configuration in

828
00:24:25,910 --> 00:24:28,929
vector databases. It's almost always the same

829
00:24:29,382 --> 00:24:30,751
basic idea of

830
00:24:30,751 --> 00:24:32,162
how to deal with the

831
00:24:32,162 --> 00:24:33,359
complexities of

832
00:24:33,359 --> 00:24:36,872
artificial intelligence. Therefore, I think we

833
00:24:36,872 --> 00:24:38,732
take

834
00:24:38,732 --> 00:24:40,546
this beautiful graph result,

835
00:24:40,546 --> 00:24:42,035
then translate it back into

836
00:24:42,035 --> 00:24:43,756
human language, and put

837
00:24:43,756 --> 00:24:45,523
these human language instructions into a

838
00:24:45,523 --> 00:24:47,261
database. Well,

839
00:24:47,261 --> 00:24:48,424
whether it's a

840
00:24:48,424 --> 00:24:50,029
regular database or a

841
00:24:50,029 --> 00:24:51,593
vector database, it doesn't matter

842
00:24:51,593 --> 00:24:53,368
. We then derive these

843
00:24:53,368 --> 00:24:54,882
textual instructions

844
00:24:54,882 --> 00:24:56,585
based on the similarity of the

845
00:24:56,585 --> 00:24:59,383
cosine function from the task description.

846
00:24:59,391 --> 00:25:01,115
I believe this is the

847
00:25:01,115 --> 00:25:02,467
weakness of the

848
00:25:02,467 --> 00:25:05,542
research paper. Let's talk

849
00:25:05,542 --> 00:25:10,629
about the limitations. This new methodology does not guarantee

850
00:25:11,015 --> 00:25:12,192
the discovery of the

851
00:25:12,192 --> 00:25:14,379
global minimum conversion. It is

852
00:25:14,379 --> 00:25:16,183
not the best graphical structure

853
00:25:16,183 --> 00:25:17,928
we could find. No,

854
00:25:17,928 --> 00:25:19,137
because it depends on the

855
00:25:19,137 --> 00:25:20,387
training data,

856
00:25:20,387 --> 00:25:21,596
and perhaps in the

857
00:25:21,596 --> 00:25:23,138
training dataset, we

858
00:25:23,138 --> 00:25:24,638
just had an average solution that

859
00:25:24,638 --> 00:25:26,323
worked. No, but it wasn't the

860
00:25:26,323 --> 00:25:27,791
ideal solution in terms of

861
00:25:27,791 --> 00:25:29,260
energy, time, or

862
00:25:29,260 --> 00:25:31,176
number of tokens. It was just a

863
00:25:31,176 --> 00:25:32,901
middle ground solution. Therefore, since we are

864
00:25:32,901 --> 00:25:35,135
relying here on a

865
00:25:35,145 --> 00:25:36,528
training dataset, we have no

866
00:25:36,528 --> 00:25:37,837
idea whether

867
00:25:37,837 --> 00:25:39,109
this is the

868
00:25:39,109 --> 00:25:40,268
global minimum in

869
00:25:40,268 --> 00:25:41,603
our multi-group complexity.

870
00:25:41,603 --> 00:25:43,072
Secondly, when

871
00:25:43,072 --> 00:25:44,750
we have an invisible task, the

872
00:25:44,750 --> 00:25:46,387
system almost breaks down

873
00:25:46,387 --> 00:25:47,688
because this

874
00:25:47,688 --> 00:25:49,367
new methodology does not build the

875
00:25:49,367 --> 00:25:50,836
correct unknown graph

876
00:25:50,836 --> 00:25:52,347
because it was not

877
00:25:52,347 --> 00:25:53,732
present in the

878
00:25:53,732 --> 00:25:55,625
training dataset. Therefore, we can

879
00:25:55,625 --> 00:25:57,242
only hope that

880
00:25:57,242 --> 00:25:58,903
the similarity

881
00:25:58,903 --> 00:26:00,952
in our known vector embedding space to our

882
00:26:02,530 --> 00:26:04,973
artificial mathematical space gives us

883
00:26:05,934 --> 00:26:07,948
an indication, or perhaps

884
00:26:07,948 --> 00:26:10,016
this is close to another solution,

885
00:26:10,016 --> 00:26:12,136
and perhaps this provides the

886
00:26:12,136 --> 00:26:14,257
next step in our solution path,

887
00:26:14,257 --> 00:26:17,376
or perhaps not. So this is here

888
00:26:17,376 --> 00:26:20,111
this is also rather weak and then at

889
00:26:20,111 --> 00:26:22,402
test time the correct graph is

890
00:26:22,402 --> 00:26:24,989
genuinely unknown but EMG does not

891
00:26:24,989 --> 00:26:28,003
reconstruct it at all mathematically.

892
00:26:28,003 --> 00:26:30,724
Yes, because we had the training time

893
00:26:30,724 --> 00:26:33,446
where the beautiful mathematical graph

894
00:26:33,446 --> 00:26:36,238
operation took place and we fed all the

895
00:26:36,238 --> 00:26:39,029
results from the training time into our

896
00:26:39,029 --> 00:26:41,633
database. And now at test time, we do

897
00:26:41,633 --> 00:26:44,483
n't do any uh algebra at all or any

898
00:26:44,483 --> 00:26:47,227
graph structure at all. We just go to

899
00:26:47,227 --> 00:26:49,721
the database and have a rag retrieval

900
00:26:49,721 --> 00:26:52,151
from a database and it retrieves the

901
00:26:52,151 --> 00:26:54,711
correction principles learned from the

902
00:26:54,711 --> 00:26:57,206
previous known graph pairs during the

903
00:26:57,206 --> 00:26:59,635
training time and relies here on the

904
00:26:59,635 --> 00:27:02,130
LLM now to apply this new instruction

905
00:27:02,130 --> 00:27:05,285
to the new task. Big question mark will

906
00:27:05,285 --> 00:27:07,908
the LLM exceed success will it be able

907
00:27:07,908 --> 00:27:10,330
to understand the complexity of the

908
00:27:10,330 --> 00:27:13,820
instruction from another task or not?

909
00:27:13,985 --> 00:27:15,693
So you see, during test time compute,

910
00:27:15,693 --> 00:27:17,446
there's zero graph mathematic happening

911
00:27:17,446 --> 00:27:19,020
, and I think this is yet the weak

912
00:27:19,020 --> 00:27:20,818
point; At the time of testing, it is

913
00:27:20,818 --> 00:27:22,617
limited to searching a

914
00:27:22,617 --> 00:27:24,370
vector database

915
00:27:24,370 --> 00:27:25,898
, and we go back to the RAG system

916
00:27:25,898 --> 00:27:27,472
that we used

917
00:27:27,472 --> 00:27:29,180
five years ago, and I think

918
00:27:29,180 --> 00:27:30,754
we have better ideas

919
00:27:30,754 --> 00:27:32,148
about how to implement this

920
00:27:32,148 --> 00:27:33,823
particular step. But what I

921
00:27:33,823 --> 00:27:35,270
like about this

922
00:27:35,270 --> 00:27:36,671
paper is the

923
00:27:36,671 --> 00:27:38,434
first step in the training process

924
00:27:38,434 --> 00:27:40,016
, which is training the graphing of this

925
00:27:40,016 --> 00:27:41,508
data on a

926
00:27:41,508 --> 00:27:42,684
graph structure and applying an

927
00:27:42,684 --> 00:27:44,040
advanced algorithm

928
00:27:44,040 --> 00:27:45,306
to compare the

929
00:27:45,306 --> 00:27:48,315
graphs and find a

930
00:27:48,315 --> 00:27:49,968
consistent development path, especially for

931
00:27:49,968 --> 00:27:51,822
asymmetric graphs

932
00:27:51,822 --> 00:27:54,031
. It's a

933
00:27:54,031 --> 00:27:58,156
great solution. Is there anything left? Yes,

934
00:27:58,156 --> 00:27:59,990
of course. By moving

935
00:27:59,990 --> 00:28:02,478
all the complex mathematical graphing operations

936
00:28:03,014 --> 00:28:04,549
to the

937
00:28:04,549 --> 00:28:06,271
offline training stage

938
00:28:06,271 --> 00:28:08,085
, EMG achieves what

939
00:28:08,085 --> 00:28:09,853
the authors now call a "

940
00:28:09,853 --> 00:28:11,621
one-time implementation,"

941
00:28:11,621 --> 00:28:13,343
because everything they trained

942
00:28:13,343 --> 00:28:15,018
their model on (and remember,

943
00:28:15,018 --> 00:28:16,693
that training is a

944
00:28:16,693 --> 00:28:19,508
graph structure they built) is

945
00:28:20,455 --> 00:28:22,298
now the content of the

946
00:28:22,298 --> 00:28:23,680
database, the

947
00:28:23,680 --> 00:28:26,063
vector database.

948
00:28:26,391 --> 00:28:28,074
You can send

949
00:28:28,074 --> 00:28:29,859
this database file

950
00:28:29,859 --> 00:28:33,666
to any other device.

951
00:28:33,666 --> 00:28:35,303
Now think about my research paper from

952
00:28:35,303 --> 00:28:36,735
yesterday and this paper from

953
00:28:36,735 --> 00:28:38,372
today, and you will see that it is the same

954
00:28:38,372 --> 00:28:39,804
philosophy of test time

955
00:28:39,804 --> 00:28:41,318
that is also used in the

956
00:28:41,318 --> 00:28:42,873
Mayo project that was published

957
00:28:42,873 --> 00:28:44,353
yesterday. No, both of the

958
00:28:44,353 --> 00:28:46,049
first papers

959
00:28:46,049 --> 00:28:47,510
were published yesterday from

960
00:28:47,510 --> 00:28:49,347
America, and this one is from China

961
00:28:49,347 --> 00:28:51,502
. Both of them realized, just

962
00:28:51,502 --> 00:28:53,231
one day apart,

963
00:28:53,231 --> 00:28:54,768
that the secret to developing

964
00:28:54,768 --> 00:28:56,401
independent agents lies not in

965
00:28:56,401 --> 00:28:58,322
giving them more time to

966
00:28:58,322 --> 00:29:00,955
think when a user asks a

967
00:29:01,444 --> 00:29:03,365
particular question, but in providing them with a

968
00:29:03,365 --> 00:29:05,998
huge,

969
00:29:06,487 --> 00:29:07,976
instantly retrievable database of pre-

970
00:29:07,976 --> 00:29:12,028
calculated lessons. This

971
00:29:12,028 --> 00:29:13,520
means we are going back to the

972
00:29:13,520 --> 00:29:16,692
familiar solutions. We do not

973
00:29:16,692 --> 00:29:17,851
have

974
00:29:17,851 --> 00:29:19,735
artificial intelligence capable of

975
00:29:19,735 --> 00:29:21,233
finding new, unique, and

976
00:29:21,233 --> 00:29:23,634
unprecedented solutions.

977
00:29:23,634 --> 00:29:25,481
Everything falls apart, and we revert

978
00:29:25,481 --> 00:29:27,918
to the same old patterns

979
00:29:28,202 --> 00:29:30,203
we discovered years ago,

980
00:29:30,203 --> 00:29:32,154
to the same old programming solutions

981
00:29:32,154 --> 00:29:35,255
. We never take

982
00:29:35,255 --> 00:29:36,855
this

983
00:29:36,855 --> 00:29:38,662
evolutionary step to a

984
00:29:38,662 --> 00:29:40,624
higher level of complexity, to

985
00:29:40,624 --> 00:29:42,586
unique software solutions that have never been seen before

986
00:29:42,586 --> 00:29:44,341
, or

987
00:29:44,341 --> 00:29:46,096
mathematical explanations, or explanations in

988
00:29:46,096 --> 00:29:47,955
physics, medicine, or

989
00:29:47,955 --> 00:29:52,229
finance. So, when

990
00:29:52,229 --> 00:29:54,074
you have this

991
00:29:54,074 --> 00:29:56,124
second part that requires you to

992
00:29:56,124 --> 00:29:57,713
go back to

993
00:29:57,713 --> 00:29:59,251
database structures, and

994
00:29:59,251 --> 00:30:01,301
you rely primarily

995
00:30:01,301 --> 00:30:03,301
on the comparability modification

996
00:30:03,301 --> 00:30:05,248
of all solution paths in the

997
00:30:05,248 --> 00:30:06,786
database,

998
00:30:06,786 --> 00:30:08,785
and you hope that a smart solution will suddenly appear out

999
00:30:08,785 --> 00:30:11,579
of nowhere, I think that would be an

1000
00:30:12,373 --> 00:30:15,159
unscientific approach. Therefore, the

1001
00:30:15,159 --> 00:30:16,807
first part of this

1002
00:30:16,807 --> 00:30:18,697
paper was excellent, and I

1003
00:30:18,697 --> 00:30:20,125
highly recommend it. I have some

1004
00:30:20,125 --> 00:30:21,980
doubts about the uniqueness of the

1005
00:30:21,980 --> 00:30:23,511
second part of the paper,

1006
00:30:23,511 --> 00:30:25,227
because you see, as in the

1007
00:30:25,227 --> 00:30:26,665
Memo Hornis research, they

1008
00:30:26,665 --> 00:30:29,474
used the same test-time idea for a

1009
00:30:29,912 --> 00:30:31,721
vector database, and I think we

1010
00:30:31,721 --> 00:30:33,159
got past that

1011
00:30:33,159 --> 00:30:34,597
problem three

1012
00:30:34,597 --> 00:30:36,273
years ago. I hope you

1013
00:30:36,273 --> 00:30:37,925
enjoyed it a little. Oh, I still have

1014
00:30:37,925 --> 00:30:39,784
something left.

1015
00:30:39,784 --> 00:30:40,891
Okay,

1016
00:30:40,891 --> 00:30:42,675
test reasoning. What is happening?

1017
00:30:42,675 --> 00:30:44,506
Well, why not? When the

1018
00:30:44,506 --> 00:30:45,799
user deploys

1019
00:30:45,799 --> 00:30:47,165
the agent and gives it a

1020
00:30:47,165 --> 00:30:48,606
completely new task,

1021
00:30:48,606 --> 00:30:49,899
the system ignores all the

1022
00:30:49,899 --> 00:30:51,339
graph data, says there is

1023
00:30:51,339 --> 00:30:52,373
no more

1024
00:30:52,373 --> 00:30:53,592
graph data,

1025
00:30:53,592 --> 00:30:54,959
takes the user's request,

1026
00:30:54,959 --> 00:30:56,436
and passes it through an embedded form

1027
00:30:56,436 --> 00:30:57,508
to get a

1028
00:30:57,508 --> 00:30:59,874
specific query vector embedded in the

1029
00:30:59,945 --> 00:31:01,885
correct mathematical space. Let's assume a space with

1030
00:31:01,885 --> 00:31:03,844
24 dimensions. This

1031
00:31:03,844 --> 00:31:05,219
system performs a simple

1032
00:31:05,219 --> 00:31:06,594
similarity and convergence search

1033
00:31:06,594 --> 00:31:08,081
using the nearest 20 neighbors

1034
00:31:08,081 --> 00:31:09,159
in an

1035
00:31:09,159 --> 00:31:10,534
offline memory database

1036
00:31:10,534 --> 00:31:11,909
, which is

1037
00:31:11,909 --> 00:31:13,173
assumed to have been

1038
00:31:13,173 --> 00:31:14,400
trained on your

1039
00:31:14,400 --> 00:31:16,440
specific domain and on

1040
00:31:16,518 --> 00:31:22,931
your device's complexity class. It then retrieves

1041
00:31:23,846 --> 00:31:25,362
previously translated and analyzed natural language insights, and

1042
00:31:25,362 --> 00:31:26,957
then incorporates this text string

1043
00:31:26,957 --> 00:31:28,154
, as in a

1044
00:31:28,154 --> 00:31:29,630
traditional racking system, into an

1045
00:31:29,630 --> 00:31:31,502
agent-guided context.

1046
00:31:31,502 --> 00:31:33,538
I believe this will not be

1047
00:31:33,538 --> 00:31:35,638
available until the end of

1048
00:31:35,638 --> 00:31:40,923
July 2026. Compare several

1049
00:31:40,923 --> 00:31:42,177
research papers; you will find

1050
00:31:42,177 --> 00:31:43,583
a lot of

1051
00:31:43,583 --> 00:31:44,829
useful information. I believe that the

1052
00:31:44,829 --> 00:31:45,873
Mayo system offers a

1053
00:31:45,873 --> 00:31:47,169
dynamic

1054
00:31:47,169 --> 00:31:49,249
system configuration around the

1055
00:31:49,473 --> 00:31:50,725
underlying Language-Led Learning (LLM) model. The

1056
00:31:50,725 --> 00:31:52,249
EMG system here offers

1057
00:31:52,249 --> 00:31:53,904
something completely different

1058
00:31:53,904 --> 00:31:55,341
, let's call it

1059
00:31:55,341 --> 00:31:57,108
algorithmic error guidance.

1060
00:31:57,108 --> 00:31:59,590
And if you are creating a

1061
00:31:59,650 --> 00:32:00,836
high-

1062
00:32:00,836 --> 00:32:02,489
quality, integrated AI agent, let's end on a

1063
00:32:02,489 --> 00:32:04,183
positive note: why not combine the

1064
00:32:04,183 --> 00:32:05,892
two? Therefore, I will

1065
00:32:05,892 --> 00:32:08,161
now use the MIMO system rack-based control layer

1066
00:32:08,726 --> 00:32:09,953
to configure

1067
00:32:09,953 --> 00:32:11,433
system elements around the kernel,

1068
00:32:11,433 --> 00:32:12,829
in order to dynamically configure the

1069
00:32:12,829 --> 00:32:14,479
proxy memory and all tools

1070
00:32:14,479 --> 00:32:16,745
. Then, if I

1071
00:32:16,745 --> 00:32:18,545
have to use this

1072
00:32:18,545 --> 00:32:21,068
method, I will use

1073
00:32:21,315 --> 00:32:23,069
MG's graph matching

1074
00:32:23,069 --> 00:32:24,177
inside the

1075
00:32:24,177 --> 00:32:25,654
agent's procedural memory

1076
00:32:25,654 --> 00:32:27,177
to ensure that the sequence of

1077
00:32:27,177 --> 00:32:28,793
actions is executed accurately without the

1078
00:32:28,793 --> 00:32:30,224
need for

1079
00:32:30,224 --> 00:32:31,886
costly reflection loops at

1080
00:32:31,886 --> 00:32:34,179
test runtime.

1081
00:32:34,360 --> 00:32:36,095
Therefore, you can save a

1082
00:32:36,095 --> 00:32:37,385
lot of time and

1083
00:32:37,385 --> 00:32:38,987
money if you have

1084
00:32:38,987 --> 00:32:43,129
this solution ready. But the

1085
00:32:43,129 --> 00:32:45,322
downside is that there is a

1086
00:32:45,322 --> 00:32:47,131
known backup solution, and

1087
00:32:47,131 --> 00:32:48,940
therefore not a

1088
00:32:48,940 --> 00:32:50,749
unique solution discovered

1089
00:32:50,749 --> 00:32:52,887
by artificial intelligence,

1090
00:32:52,887 --> 00:32:57,789
but just a search table. This

1091
00:32:57,789 --> 00:32:59,246
is the part that I don't

1092
00:32:59,246 --> 00:33:01,139
think is keeping up with our times

1093
00:33:01,139 --> 00:33:06,793
. So, if you were to ask here:

1094
00:33:06,793 --> 00:33:08,712
What is being fixed?

1095
00:33:08,712 --> 00:33:10,243
What elements are

1096
00:33:10,243 --> 00:33:12,397
used? The

1097
00:33:12,397 --> 00:33:14,285
Memo Harness system views the

1098
00:33:14,285 --> 00:33:16,383
agent failure and assumes it is a

1099
00:33:16,383 --> 00:33:18,481
structural failure in the system's configuration

1100
00:33:18,481 --> 00:33:21,153
itself. While the EMG system looks

1101
00:33:21,153 --> 00:33:22,699
at the agent's failure

1102
00:33:22,699 --> 00:33:24,295
and assumes that it failed to

1103
00:33:24,295 --> 00:33:26,115
make an internal decision. That is, it

1104
00:33:26,115 --> 00:33:27,373
assumes the agent

1105
00:33:27,373 --> 00:33:28,211
has the

1106
00:33:28,211 --> 00:33:29,503
right tools but presses the

1107
00:33:29,503 --> 00:33:30,912
wrong button. Therefore,

1108
00:33:30,912 --> 00:33:32,291
the system, under

1109
00:33:32,291 --> 00:33:33,914
observation X, asks whether the

1110
00:33:33,914 --> 00:33:35,537
operator chose action

1111
00:33:35,537 --> 00:33:37,160
Y when they should have

1112
00:33:37,160 --> 00:33:38,255
chosen action Z.

1113
00:33:38,255 --> 00:33:39,473
Thus,

1114
00:33:39,473 --> 00:33:40,974
the sequence of actions is determined based

1115
00:33:40,974 --> 00:33:43,232
on the known solution. The

1116
00:33:43,543 --> 00:33:45,006
reason this

1117
00:33:45,006 --> 00:33:46,125
model (EMG) is successful with

1118
00:33:46,125 --> 00:33:47,803
small models, such as the

1119
00:33:47,803 --> 00:33:48,965
four-

1120
00:33:48,965 --> 00:33:50,385
billion-coupled model in

1121
00:33:50,385 --> 00:33:51,719
the experiments of this

1122
00:33:51,719 --> 00:33:53,441
research paper, is that the

1123
00:33:53,441 --> 00:33:54,775
hard work of

1124
00:33:54,775 --> 00:33:57,066
analyzing all aspects of the

1125
00:33:57,702 --> 00:33:59,208
mathematical graph geometry is done by

1126
00:33:59,208 --> 00:34:00,714
mathematics in the

1127
00:34:00,714 --> 00:34:02,134
training phase, and then

1128
00:34:02,134 --> 00:34:03,554
all the information is stored in the

1129
00:34:03,554 --> 00:34:04,937
database.

1130
00:34:04,937 --> 00:34:06,489
Therefore, you do not need

1131
00:34:06,489 --> 00:34:08,174
to deal with four

1132
00:34:08,174 --> 00:34:09,726
billion operators at

1133
00:34:09,726 --> 00:34:10,879
all during

1134
00:34:10,879 --> 00:34:12,165
testing or

1135
00:34:12,165 --> 00:34:13,761
overlap time; All you have to

1136
00:34:13,761 --> 00:34:15,092
do is search for the

1137
00:34:15,092 --> 00:34:16,467
results in the

1138
00:34:16,467 --> 00:34:19,913
database. This is amazing. There

1139
00:34:19,913 --> 00:34:22,669
are no complex calculations other than the

1140
00:34:23,155 --> 00:34:24,731
neural network parameters of your

1141
00:34:24,731 --> 00:34:26,082
four-billion-

1142
00:34:26,082 --> 00:34:27,613
parameter model, because everything is

1143
00:34:27,613 --> 00:34:29,521
utilitarian. The intelligence

1144
00:34:29,521 --> 00:34:31,627
and knowledge are in the

1145
00:34:31,627 --> 00:34:33,335
database, and

1146
00:34:33,335 --> 00:34:35,385
I imagine this is similar to an

1147
00:34:35,385 --> 00:34:37,321
MD skills bank, where

1148
00:34:37,321 --> 00:34:41,988
the knowledge of how to build a

1149
00:34:41,988 --> 00:34:44,117
code solution is in MD files, and this is

1150
00:34:44,117 --> 00:34:45,843
done here at a

1151
00:34:45,843 --> 00:34:48,602
higher level.

1152
00:34:48,602 --> 00:34:50,505
Yesterday I explained to you the structure of the

1153
00:34:50,505 --> 00:34:53,746
system itself. Now,

1154
00:34:53,746 --> 00:34:55,396
we have moved to a

1155
00:34:55,396 --> 00:34:57,258
decision-making framework for

1156
00:34:57,258 --> 00:34:59,333
long-term tasks,

1157
00:34:59,333 --> 00:35:01,089
whether they take three

1158
00:35:01,089 --> 00:35:03,110
hours or twenty hours,

1159
00:35:03,110 --> 00:35:05,239
to ensure we stay on a

1160
00:35:05,239 --> 00:35:07,343
consistent path to resolution. I hope you

1161
00:35:07,343 --> 00:35:08,584
enjoyed it and that you

1162
00:35:08,584 --> 00:35:09,906
gained

1163
00:35:09,906 --> 00:35:11,374
new ideas. You may

1164
00:35:11,374 --> 00:35:13,004
disagree with me

1165
00:35:13,004 --> 00:35:14,408
on the second part, which

1166
00:35:14,408 --> 00:35:15,676
relates to

1167
00:35:15,676 --> 00:35:17,465
vector databases. In

1168
00:35:17,465 --> 00:35:19,119
any case, I hope there is something that interests

1169
00:35:19,119 --> 00:35:20,961
you

1170
00:35:20,961 --> 00:35:22,372
. I'm happy to see you in the

1171
00:35:22,372 --> 00:35:24,513
next video.
