# Don't learn AI Agents without Learning these Fundamentals

source_url: https://www.youtube.com/watch?v=ZaPbP9DwBOE
author: KodeKloud

---

# Don't learn AI Agents without Learning these Fundamentals

🧪AI Agents Labs for Free: https://kode.wiki/3Wh4DZ6

# Description

🧪AI Agents Labs for Free: https://kode.wiki/3Wh4DZ6

Learn everything about AI agents from scratch in this comprehensive tutorial. No prior knowledge required. We'll take you from zero to building production-ready AI systems with hands-on labs.

🎯 What You'll Learn:
• AI Fundamentals - LLMs, tokens, embeddings, and context windows
• LangChain - Simplify AI development with pre-built components
• Prompt Engineering - Zero-shot, few-shot, and chain-of-thought techniques
• Vector Databases - Semantic search with ChromaDB and Pinecone
• RAG (Retrieval Augmented Generation) - Build intelligent document search
• LangGraph - Create multi-step AI workflows and agents
• MCP (Model Context Protocol) - Connect AI to external tools

🔧 Hands-On Labs Include:
✓ Making your first OpenAI API calls
✓ Building semantic search engines
✓ Creating RAG systems for document retrieval
✓ Developing multi-agent workflows
✓ Integrating external tools with MCP

Perfect for developers, data scientists, and anyone wanting to understand modern AI development. Follow along with free labs and build a real-world AI assistant that searches 500GB of documents in under 30 seconds.

🚨Start Your AI Journey with KodeKloud: https://kode.wiki/4qsrspX

⏰ TIMESTAMPS:
00:00 - Introduction to AI Agents
00:40 - How LLMs work in real time?
04:56 - Embeddings & Vector Representations
05:56 - How LangChain works?
10:12 - Practice Labs - Your First AI API Call
14:57 - Practice Labs - LangChain
17:57 - Prompt Engineering Techniques
21:21 - Practice Labs - Master Prompt Engineering
24:46 - Vector Databases Deep Dive
31:27 - Practice Labs - Build Semantic Search Engine
35:15 - RAG (Retrieval Augmented Generation)
38:14 - Practice Labs - RAG Implementation
42:14 - LangGraph for AI Workflows
45:51 - Practice Labs - Build Stateful AI Workflow
48:51 - Model Context Protocol (MCP)
51:56 - Practice Labs - Advanced MCP Concepts
55:21 - Conclusion

🔔 Subscribe to KodeKloud for more AI development tools and tutorials!

#AiAgents #AI #Aifundamentals #LangChain #MCP #LLMs #RAG #Langgraph #vectordb #promptengineering #VectorDatabases #Tutorial #kodekloud

# Chapters

* [00:00:00] - Introduction to AI Agents
* [00:00:40] - How LLMs work in real time?
* [00:04:56] - Embeddings & Vector Representations
* [00:05:56] - How LangChain works?
* [00:10:12] - Practice Labs - Your First AI API Call
* [00:14:57] - Practice Labs - LangChain
* [00:17:57] - Prompt Engineering Techniques
* [00:21:21] - Practice Labs - Master Prompt Engineering
* [00:24:46] - Vector Databases Deep Dive
* [00:31:27] - Practice Labs - Build Semantic Search Engine
* [00:35:15] - RAG (Retrieval Augmented Generation)
* [00:38:14] - Practice Labs - RAG Implementation
* [00:42:14] - LangGraph for AI Workflows
* [00:45:51] - Practice Labs - Build Stateful AI Workflow
* [00:48:51] - Model Context Protocol (MCP)
* [00:51:56] - Practice Labs - Advanced MCP Concepts
* [00:55:21] - Conclusion

# Transcript

1
00:00:00,080 --> 00:00:02,560
A lot has been going on with AI over the

2
00:00:02,560 --> 00:00:04,480
past few years. Prompt engineering,

3
00:00:04,480 --> 00:00:06,799
context, windows, tokens, embeddings,

4
00:00:06,799 --> 00:00:10,000
rag, vector DB, MCPS, agents, lang

5
00:00:10,000 --> 00:00:12,480
chain, langraph, claude, Gemini, and

6
00:00:12,480 --> 00:00:14,559
more. If you felt left out, this is the

7
00:00:14,559 --> 00:00:16,480
only video you'll need to watch to catch

8
00:00:16,480 --> 00:00:18,720
up. In this video, we assume you know

9
00:00:18,720 --> 00:00:20,800
absolutely nothing and try to explain

10
00:00:20,800 --> 00:00:22,720
all of these concept through a single

11
00:00:22,720 --> 00:00:24,800
project so that by the end of it, you go

12
00:00:24,800 --> 00:00:26,720
from zero to gaining an overall

13
00:00:26,720 --> 00:00:28,400
understanding of everything that's going

14
00:00:28,400 --> 00:00:30,080
on with AI. We'll start with AI

15
00:00:30,080 --> 00:00:32,239
fundamentals, then move on to rag,

16
00:00:32,239 --> 00:00:35,200
vector DB, lang chain, langraph, MCP,

17
00:00:35,200 --> 00:00:37,120
prompt engineering, and finally put it

18
00:00:37,120 --> 00:00:39,120
all together with a complete system.

19
00:00:39,120 --> 00:00:40,719
Let's start with the basics. When you

20
00:00:40,719 --> 00:00:42,800
ask an AI model a question, it's

21
00:00:42,800 --> 00:00:44,960
typically answered by a subset of AI

22
00:00:44,960 --> 00:00:46,879
called large language models. Large

23
00:00:46,879 --> 00:00:48,480
language models have gotten popular

24
00:00:48,480 --> 00:00:50,480
right around when Chachib was released

25
00:00:50,480 --> 00:00:52,640
in late 2022 when we started to see

26
00:00:52,640 --> 00:00:54,879
language models get larger in size

27
00:00:54,879 --> 00:00:56,719
because of their obvious benefits in

28
00:00:56,719 --> 00:00:58,960
performance. So let's dig a bit deeper

29
00:00:58,960 --> 00:01:00,960
to understand how large language models

30
00:01:00,960 --> 00:01:02,960
are able to process requests that we

31
00:01:02,960 --> 00:01:06,240
send. Popular LLMs like OpenASGPT,

32
00:01:06,240 --> 00:01:08,640
Enthropics Claude, and Google's Gemini

33
00:01:08,640 --> 00:01:10,720
are all transformer models that are

34
00:01:10,720 --> 00:01:13,119
trained on large sets of data. The size

35
00:01:13,119 --> 00:01:15,520
of training tokens can go up to tens of

36
00:01:15,520 --> 00:01:17,280
trillions of tokens that are used to

37
00:01:17,280 --> 00:01:19,119
train these models. And the training

38
00:01:19,119 --> 00:01:21,280
data includes data from thousands of

39
00:01:21,280 --> 00:01:23,360
different domains like healthcare, law,

40
00:01:23,360 --> 00:01:25,680
coding, science, and more. But when we

41
00:01:25,680 --> 00:01:28,400
work in TechCorb, the 500 GB of data

42
00:01:28,400 --> 00:01:30,159
that we have aren't part of the training

43
00:01:30,159 --> 00:01:32,240
data that was used to train the model,

44
00:01:32,240 --> 00:01:34,240
which means that in order for us to use

45
00:01:34,240 --> 00:01:36,240
the LLMs to ask questions about the

46
00:01:36,240 --> 00:01:38,479
TechCorp's internal documents, we need

47
00:01:38,479 --> 00:01:41,520
the ability to pass in data to the LLM.

48
00:01:41,520 --> 00:01:43,280
One of the ways that we can pass the

49
00:01:43,280 --> 00:01:45,680
data into the model is by adding them to

50
00:01:45,680 --> 00:01:47,600
the conversation history functions like

51
00:01:47,600 --> 00:01:49,520
a short-term memory where during the

52
00:01:49,520 --> 00:01:51,600
duration of the conversation, all of

53
00:01:51,600 --> 00:01:54,159
this context is kept in memory. And this

54
00:01:54,159 --> 00:01:56,479
memory is called the context window.

55
00:01:56,479 --> 00:01:58,880
Context windows are measured in tokens

56
00:01:58,880 --> 00:02:01,280
which is roughly 3/4 of a word for

57
00:02:01,280 --> 00:02:03,439
English text. The context window is

58
00:02:03,439 --> 00:02:05,360
typically limited in size and the upper

59
00:02:05,360 --> 00:02:07,520
limit varies depending on the model.

60
00:02:07,520 --> 00:02:11,440
Some models like XAI GO 4 have 256,000

61
00:02:11,440 --> 00:02:14,239
tokens whereas Enthropics Cloud Opus 4

62
00:02:14,239 --> 00:02:16,879
has 200,000 tokens and Google's Gemini

63
00:02:16,879 --> 00:02:20,080
2.5 Pro has 1 million tokens. So as you

64
00:02:20,080 --> 00:02:22,239
can see the total upper bound for how

65
00:02:22,239 --> 00:02:24,160
much context can be stored for each

66
00:02:24,160 --> 00:02:26,480
model can vary. While the context window

67
00:02:26,480 --> 00:02:28,319
plays an important role in storing them

68
00:02:28,319 --> 00:02:30,080
in memory, there are practical

69
00:02:30,080 --> 00:02:32,480
limitations in how LLM treats what's

70
00:02:32,480 --> 00:02:34,959
inside the context window. For example,

71
00:02:34,959 --> 00:02:37,519
if I asked you to memorize the pi digits

72
00:02:37,519 --> 00:02:40,519
3.141592653589791

73
00:02:42,000 --> 00:02:44,239
and asked you to recite it, some of you

74
00:02:44,239 --> 00:02:45,680
might have a hard time committing that

75
00:02:45,680 --> 00:02:47,680
many numbers all at once, which is

76
00:02:47,680 --> 00:02:49,920
similar to how LLM's context window

77
00:02:49,920 --> 00:02:52,160
works. So therein lies the current

78
00:02:52,160 --> 00:02:55,040
limitations in LLM. How much context can

79
00:02:55,040 --> 00:02:57,599
it hold in a given time? This can vary

80
00:02:57,599 --> 00:02:59,519
depending on model to model. For

81
00:02:59,519 --> 00:03:02,239
example, a lot of nano, mini, and flash

82
00:03:02,239 --> 00:03:04,239
models can have very small context

83
00:03:04,239 --> 00:03:06,800
windows in the size of 2,000 to 4,000

84
00:03:06,800 --> 00:03:09,680
tokens, which amounts to about 1,500 to

85
00:03:09,680 --> 00:03:12,480
3,000 words. Conversely, bigger models

86
00:03:12,480 --> 00:03:16,080
like GPT4.1 and Gemini 2.5 Pro offer

87
00:03:16,080 --> 00:03:18,640
context windows up to 1 million tokens,

88
00:03:18,640 --> 00:03:21,360
which is equivalent to roughly 7,500

89
00:03:21,360 --> 00:03:24,480
words or 50,000 lines of code. So, as

90
00:03:24,480 --> 00:03:26,400
you can see, choosing the right model

91
00:03:26,400 --> 00:03:29,120
for the task can be very important. For

92
00:03:29,120 --> 00:03:31,519
example, if you downloaded a novel in a

93
00:03:31,519 --> 00:03:34,080
txt format and you wanted to change the

94
00:03:34,080 --> 00:03:36,480
script, choosing a model that offers a

95
00:03:36,480 --> 00:03:38,640
large context window would be best.

96
00:03:38,640 --> 00:03:40,640
Conversely, if you are working on a

97
00:03:40,640 --> 00:03:42,480
small document and require very low

98
00:03:42,480 --> 00:03:45,360
latency, meaning faster responses, using

99
00:03:45,360 --> 00:03:47,680
flash and nano variants would be best.

100
00:03:47,680 --> 00:03:49,519
Here's another angle to look at when it

101
00:03:49,519 --> 00:03:52,239
comes to memory in LLMs. Let's say I ask

102
00:03:52,239 --> 00:03:54,799
you this question. Sally and Bob own an

103
00:03:54,799 --> 00:03:58,159
apple farm. Sally has 14 apples. Apples

104
00:03:58,159 --> 00:04:01,040
are often red. 12 is a nice number. Bob

105
00:04:01,040 --> 00:04:03,439
has no red apple, but he has two green

106
00:04:03,439 --> 00:04:06,159
apples. Green apples often taste bad.

107
00:04:06,159 --> 00:04:08,640
How many apples do they all have? This

108
00:04:08,640 --> 00:04:10,159
might require you to think about the

109
00:04:10,159 --> 00:04:12,000
problem a little bit to get to the final

110
00:04:12,000 --> 00:04:14,480
answer, which is 16. That's because the

111
00:04:14,480 --> 00:04:16,639
context here includes information that

112
00:04:16,639 --> 00:04:18,479
is completely irrelevant to the

113
00:04:18,479 --> 00:04:20,239
question, which is to count how many

114
00:04:20,239 --> 00:04:22,639
apples they have in total. The fact that

115
00:04:22,639 --> 00:04:25,440
apples are red or green or how it tastes

116
00:04:25,440 --> 00:04:27,120
have nothing to do with the total number

117
00:04:27,120 --> 00:04:29,120
of apples that they have because they

118
00:04:29,120 --> 00:04:31,680
either have the apple or they don't. Now

119
00:04:31,680 --> 00:04:33,520
that we have a grasp on what context

120
00:04:33,520 --> 00:04:36,240
window provides, Techorp's 500 GB of

121
00:04:36,240 --> 00:04:38,240
documents, this creates an immediate

122
00:04:38,240 --> 00:04:40,560
problem. Even the largest context

123
00:04:40,560 --> 00:04:43,199
window, like Gemini 2.5 Pro's 1 million

124
00:04:43,199 --> 00:04:46,160
tokens, can hold only about 50 files of

125
00:04:46,160 --> 00:04:48,639
typical business documents all at once.

126
00:04:48,639 --> 00:04:51,280
We need our AI model to understand all

127
00:04:51,280 --> 00:04:54,080
500 gigabytes, but it can only see a

128
00:04:54,080 --> 00:04:56,720
tiny fraction at a given moment. This is

129
00:04:56,720 --> 00:04:58,720
where embedding comes in, and they're

130
00:04:58,720 --> 00:05:00,960
absolutely crucial to understand.

131
00:05:00,960 --> 00:05:02,880
Embeddings transform the way we think

132
00:05:02,880 --> 00:05:05,120
about information. Instead of storing

133
00:05:05,120 --> 00:05:07,759
text as words, we convert meaning into

134
00:05:07,759 --> 00:05:10,320
numbers. The sentence employee vacation

135
00:05:10,320 --> 00:05:13,039
policy and staff time off guidelines use

136
00:05:13,039 --> 00:05:15,199
completely different words, but they

137
00:05:15,199 --> 00:05:17,199
mean essentially the same thing.

138
00:05:17,199 --> 00:05:18,960
Embeddings capture that semantic

139
00:05:18,960 --> 00:05:21,600
similarity. And here's how it works. An

140
00:05:21,600 --> 00:05:23,680
embedding model takes a text and

141
00:05:23,680 --> 00:05:26,639
converts it into a vector. Typically,

142
00:05:26,639 --> 00:05:29,759
1536 numbers that represent the meaning.

143
00:05:29,759 --> 00:05:31,919
Similar concepts end up with similar

144
00:05:31,919 --> 00:05:34,000
number patterns like vacation and

145
00:05:34,000 --> 00:05:35,840
holiday will have vectors that are

146
00:05:35,840 --> 00:05:38,240
mathematically close to each other. For

147
00:05:38,240 --> 00:05:40,240
TechCorb, this means that we can find

148
00:05:40,240 --> 00:05:42,479
relevant documents based on what someone

149
00:05:42,479 --> 00:05:44,320
means, not just the exact word that

150
00:05:44,320 --> 00:05:46,240
they've used. When an employee asks,

151
00:05:46,240 --> 00:05:48,639
"Can I wear jeans to work?" Our system

152
00:05:48,639 --> 00:05:50,960
will find the dress code policy, even if

153
00:05:50,960 --> 00:05:52,800
it never mentions the word jeans

154
00:05:52,800 --> 00:05:54,639
specifically.

155
00:05:54,639 --> 00:05:56,639
Now that we understand how LLMs and

156
00:05:56,639 --> 00:05:59,039
embeddings work, we will need a system

157
00:05:59,039 --> 00:06:01,120
that ties everything together. In our

158
00:06:01,120 --> 00:06:03,280
case, Tech Cororb needs a chatbot where

159
00:06:03,280 --> 00:06:05,039
customers can ask questions about the

160
00:06:05,039 --> 00:06:07,520
company policy, product information, and

161
00:06:07,520 --> 00:06:09,840
support issues. The chatbot needs to

162
00:06:09,840 --> 00:06:12,080
remember conversation history, access

163
00:06:12,080 --> 00:06:14,240
the company knowledge base, and handle

164
00:06:14,240 --> 00:06:16,800
complex multi-step interactions. Your

165
00:06:16,800 --> 00:06:19,039
first instinct might be to use OpenAI's

166
00:06:19,039 --> 00:06:22,000
SDK to build a quick chat interface. But

167
00:06:22,000 --> 00:06:23,520
you quickly realize that there are

168
00:06:23,520 --> 00:06:25,759
massive missing pieces. Storing chat

169
00:06:25,759 --> 00:06:27,520
messages, maintaining conversation

170
00:06:27,520 --> 00:06:29,360
context, connecting to Tech Corp's

171
00:06:29,360 --> 00:06:31,280
internal knowledge base, and handling

172
00:06:31,280 --> 00:06:33,199
the possibility that the company might

173
00:06:33,199 --> 00:06:35,360
switch from OpenAI to Anthropic or

174
00:06:35,360 --> 00:06:37,199
Google in the future. And now what

175
00:06:37,199 --> 00:06:39,440
seemed like a simple project becomes a

176
00:06:39,440 --> 00:06:41,520
massive undertaking. While you can write

177
00:06:41,520 --> 00:06:43,759
your own implementation to connect them,

178
00:06:43,759 --> 00:06:45,440
there's already a wellestablished

179
00:06:45,440 --> 00:06:47,520
abstraction layer called langchain.

180
00:06:47,520 --> 00:06:49,600
Langchain is an abstraction layer that

181
00:06:49,600 --> 00:06:52,080
helps you build AI agents with minimal

182
00:06:52,080 --> 00:06:54,400
code. It addresses all those pain points

183
00:06:54,400 --> 00:06:56,160
using pre-built components and

184
00:06:56,160 --> 00:06:58,479
standardized interfaces. But first,

185
00:06:58,479 --> 00:07:00,319
let's understand the crucial difference

186
00:07:00,319 --> 00:07:02,720
between an LLM and an agent. When you

187
00:07:02,720 --> 00:07:04,720
use large language models like GBT,

188
00:07:04,720 --> 00:07:06,960
Claude and Gemini directly, you're using

189
00:07:06,960 --> 00:07:09,120
them as static brain that can answer

190
00:07:09,120 --> 00:07:11,199
question based on their training data.

191
00:07:11,199 --> 00:07:13,919
An agent on the other hand has autonomy,

192
00:07:13,919 --> 00:07:15,919
memory, and tools to perform whatever

193
00:07:15,919 --> 00:07:18,080
task it thinks that is necessary to

194
00:07:18,080 --> 00:07:20,080
complete your request. For TechCorp's

195
00:07:20,080 --> 00:07:22,479
customer support scenario, imagine a

196
00:07:22,479 --> 00:07:24,479
customer asks, "What's your company's

197
00:07:24,479 --> 00:07:26,639
policy on refunding my product that

198
00:07:26,639 --> 00:07:28,639
arrived damaged?" An agent will

199
00:07:28,639 --> 00:07:30,479
self-determine how it should answer that

200
00:07:30,479 --> 00:07:32,639
request based autonomously instead of

201
00:07:32,639 --> 00:07:34,400
traditional software that requires

202
00:07:34,400 --> 00:07:36,160
conditional statement that determines

203
00:07:36,160 --> 00:07:38,880
how a program should execute. Langchain

204
00:07:38,880 --> 00:07:40,560
comes with extensive pre-built

205
00:07:40,560 --> 00:07:42,639
components that handle the heavy lifting

206
00:07:42,639 --> 00:07:45,680
for Techorp Chatbot. Langchain chat

207
00:07:45,680 --> 00:07:48,000
models provide direct access to LLM

208
00:07:48,000 --> 00:07:50,400
providers. Instead of writing custom API

209
00:07:50,400 --> 00:07:52,720
integration code, you can set up OpenAI

210
00:07:52,720 --> 00:07:55,280
with open bracket model equals GPT3

211
00:07:55,280 --> 00:07:57,840
turbo. So if the requirements change to

212
00:07:57,840 --> 00:07:59,919
use enthropic instead, you simply change

213
00:07:59,919 --> 00:08:02,800
one line LLM equals chat enthropic open

214
00:08:02,800 --> 00:08:05,360
bracket model equals claw 3 sonnet. This

215
00:08:05,360 --> 00:08:07,120
same pattern applies to every other

216
00:08:07,120 --> 00:08:09,599
capability techp needs. Memory

217
00:08:09,599 --> 00:08:11,759
management uses memory saver to

218
00:08:11,759 --> 00:08:13,840
automatically store and retrieve chat

219
00:08:13,840 --> 00:08:15,599
history, which means there's no need to

220
00:08:15,599 --> 00:08:17,440
build your own database schema or

221
00:08:17,440 --> 00:08:19,680
session management. Vector database

222
00:08:19,680 --> 00:08:21,520
integration works through standardized

223
00:08:21,520 --> 00:08:23,919
interfaces. Whether you choose Pine Cone

224
00:08:23,919 --> 00:08:26,000
or Chroma DB, Langchain provides

225
00:08:26,000 --> 00:08:27,759
consistent APIs and we'll go through

226
00:08:27,759 --> 00:08:29,759
what a vector database is in the next

227
00:08:29,759 --> 00:08:32,000
couple chapters. For text embedding, it

228
00:08:32,000 --> 00:08:34,159
uses OpenAI embeddings or similar

229
00:08:34,159 --> 00:08:36,080
components to convert Tech Corp's

230
00:08:36,080 --> 00:08:38,399
document into vector representation. The

231
00:08:38,399 --> 00:08:40,399
embedding process becomes a single

232
00:08:40,399 --> 00:08:42,719
function call instead of managing API

233
00:08:42,719 --> 00:08:44,720
connections and data transformations

234
00:08:44,720 --> 00:08:46,800
manually. Finally, tool integration

235
00:08:46,800 --> 00:08:48,959
allows the agent to access external

236
00:08:48,959 --> 00:08:51,120
system. So if you need to query Tech

237
00:08:51,120 --> 00:08:53,279
Corp's customer database, you can simply

238
00:08:53,279 --> 00:08:55,360
create a tool that the agent can call

239
00:08:55,360 --> 00:08:57,360
when it determines customer specific

240
00:08:57,360 --> 00:08:59,360
information is needed. Without lang

241
00:08:59,360 --> 00:09:01,120
chain, you would need to build all of

242
00:09:01,120 --> 00:09:03,279
this infrastructure yourself. API

243
00:09:03,279 --> 00:09:05,519
management for multiple LLM providers,

244
00:09:05,519 --> 00:09:08,160
vector databases, SDKs, embedding

245
00:09:08,160 --> 00:09:10,720
pipelines, semantic search logic, state

246
00:09:10,720 --> 00:09:12,480
management, memory system, and tool

247
00:09:12,480 --> 00:09:14,399
routing. The complexity grows

248
00:09:14,399 --> 00:09:16,480
exponentially. Lang chain's component

249
00:09:16,480 --> 00:09:18,480
library includes modules like chat

250
00:09:18,480 --> 00:09:20,800
anthropic API connections. Chromad

251
00:09:20,800 --> 00:09:23,040
vector database operations, OpenAI

252
00:09:23,040 --> 00:09:25,600
embeddings for texttoveector conversion,

253
00:09:25,600 --> 00:09:27,279
memory saver for chat history

254
00:09:27,279 --> 00:09:29,600
management, custom tool definitions for

255
00:09:29,600 --> 00:09:32,000
external system integrations. The agent

256
00:09:32,000 --> 00:09:34,240
orchestrates these components based on

257
00:09:34,240 --> 00:09:36,320
the conversation context. So as we're

258
00:09:36,320 --> 00:09:38,000
talking about tech corp depending on

259
00:09:38,000 --> 00:09:40,240
what the question is asked the agent

260
00:09:40,240 --> 00:09:42,399
will now use the given tools like vector

261
00:09:42,399 --> 00:09:44,480
databases as well as the context it

262
00:09:44,480 --> 00:09:46,720
built from conversation memory and the

263
00:09:46,720 --> 00:09:48,720
system prompt written in API layer

264
00:09:48,720 --> 00:09:51,040
autonomously handle your request and you

265
00:09:51,040 --> 00:09:53,120
can extend the agents abilities beyond

266
00:09:53,120 --> 00:09:55,440
this example by using other pre-built

267
00:09:55,440 --> 00:09:57,839
tools that lang chain offers like custom

268
00:09:57,839 --> 00:10:00,560
database access web search local file

269
00:10:00,560 --> 00:10:02,720
system access and more. Now that we

270
00:10:02,720 --> 00:10:04,640
covered the conceptual elements of lang

271
00:10:04,640 --> 00:10:06,240
chain, let's look at how it looks like

272
00:10:06,240 --> 00:10:08,080
on a practical level. We can look over

273
00:10:08,080 --> 00:10:10,160
at this lab specifically geared towards

274
00:10:10,160 --> 00:10:12,640
how to use lang chain. All right, let's

275
00:10:12,640 --> 00:10:14,560
start with the labs. In this lab, we're

276
00:10:14,560 --> 00:10:16,240
going to explore how to make your very

277
00:10:16,240 --> 00:10:18,880
first AI API calls. The mission here is

278
00:10:18,880 --> 00:10:21,200
to take you from absolute zero to being

279
00:10:21,200 --> 00:10:23,279
able to connect, call, and understand

280
00:10:23,279 --> 00:10:26,000
responses from OpenAI's APIs in just a

281
00:10:26,000 --> 00:10:28,399
few progressive steps. We begin by

282
00:10:28,399 --> 00:10:30,640
verifying our environment. In this step,

283
00:10:30,640 --> 00:10:32,480
we're asked to activate the virtual

284
00:10:32,480 --> 00:10:34,480
environment. Check that Python is

285
00:10:34,480 --> 00:10:36,880
installed. Ensure the OpenAI library is

286
00:10:36,880 --> 00:10:39,200
available and confirm that our API keys

287
00:10:39,200 --> 00:10:41,279
are set. This is important because

288
00:10:41,279 --> 00:10:43,519
without this foundation, nothing else

289
00:10:43,519 --> 00:10:45,760
will work. Once the verification runs

290
00:10:45,760 --> 00:10:47,760
successfully, the lab will confirm that

291
00:10:47,760 --> 00:10:49,920
the environment is ready. Next, we take

292
00:10:49,920 --> 00:10:52,480
a moment to understand what OpenAI is.

293
00:10:52,480 --> 00:10:54,399
Here we're introduced to the company

294
00:10:54,399 --> 00:10:57,120
behind chatbt and their family of AI

295
00:10:57,120 --> 00:11:00,480
models including GBT4, GBT4.1 Mini and

296
00:11:00,480 --> 00:11:03,200
GBT 3.5. The narration highlights that

297
00:11:03,200 --> 00:11:05,279
we'll be working with the Python OpenAI

298
00:11:05,279 --> 00:11:07,440
library which acts as a bridge between

299
00:11:07,440 --> 00:11:09,839
our code and OpenAI server. With that

300
00:11:09,839 --> 00:11:12,240
context set, we move into task one. In

301
00:11:12,240 --> 00:11:14,000
this task, we're asked to open up a

302
00:11:14,000 --> 00:11:16,000
Python script and complete the missing

303
00:11:16,000 --> 00:11:18,560
imports. Specifically, we need to import

304
00:11:18,560 --> 00:11:21,200
the OpenAI library and the OS library.

305
00:11:21,200 --> 00:11:23,600
After completing these lines, we run the

306
00:11:23,600 --> 00:11:25,360
script to make sure that the libraries

307
00:11:25,360 --> 00:11:27,680
are properly installed and ready to use.

308
00:11:27,680 --> 00:11:29,440
If everything is correct, the program

309
00:11:29,440 --> 00:11:31,519
confirms that the import worked. From

310
00:11:31,519 --> 00:11:33,760
here, we transition into authentication

311
00:11:33,760 --> 00:11:36,000
and client setup. Here, the lab explains

312
00:11:36,000 --> 00:11:38,480
the importance of an API client, an API

313
00:11:38,480 --> 00:11:41,279
key, and the base URL. The API key works

314
00:11:41,279 --> 00:11:43,440
like a password that identifies us and

315
00:11:43,440 --> 00:11:45,680
grants access, while the base URL

316
00:11:45,680 --> 00:11:47,519
defines the server location where

317
00:11:47,519 --> 00:11:49,839
requests are sent. This prepares us for

318
00:11:49,839 --> 00:11:52,560
task two. In task two, we open another

319
00:11:52,560 --> 00:11:54,240
Python script and are asked to

320
00:11:54,240 --> 00:11:56,560
initialize the client by plugging in the

321
00:11:56,560 --> 00:11:58,480
correct environment variables. This

322
00:11:58,480 --> 00:12:00,880
involves making sure we pass the OpenAI

323
00:12:00,880 --> 00:12:03,760
API key and OpenAI API base. Once those

324
00:12:03,760 --> 00:12:05,920
values are filled in, we run the script

325
00:12:05,920 --> 00:12:08,000
to verify the client has been properly

326
00:12:08,000 --> 00:12:10,160
initialized. If done correctly, the

327
00:12:10,160 --> 00:12:11,760
script confirms the connection to

328
00:12:11,760 --> 00:12:13,839
OpenAIS servers. Once the setup is

329
00:12:13,839 --> 00:12:15,760
complete, we move on to the heart of the

330
00:12:15,760 --> 00:12:18,079
lab, making an API call. Before jumping

331
00:12:18,079 --> 00:12:20,240
into it, we learn what chat completions

332
00:12:20,240 --> 00:12:22,800
are. This is OpenAI's conversational API

333
00:12:22,800 --> 00:12:24,720
where we send messages and receive

334
00:12:24,720 --> 00:12:27,040
messages just like a chat. Lab explains

335
00:12:27,040 --> 00:12:29,120
the three roles in a conversation.

336
00:12:29,120 --> 00:12:31,600
System, user, and assistant, and how the

337
00:12:31,600 --> 00:12:33,680
request format looks like in Python.

338
00:12:33,680 --> 00:12:36,320
That takes us into task three. Here we

339
00:12:36,320 --> 00:12:38,480
open the script, uncomment the lines

340
00:12:38,480 --> 00:12:40,480
that define the model, role, and

341
00:12:40,480 --> 00:12:42,639
content, and then configure it. So the

342
00:12:42,639 --> 00:12:44,880
AI introduces itself. Once we run the

343
00:12:44,880 --> 00:12:47,279
script, if all is correct, the AI should

344
00:12:47,279 --> 00:12:49,440
respond back with an introduction. This

345
00:12:49,440 --> 00:12:51,279
is the first live call to the model.

346
00:12:51,279 --> 00:12:52,959
Next, we're guided into understanding

347
00:12:52,959 --> 00:12:54,720
the structure of the response object.

348
00:12:54,720 --> 00:12:56,800
The lab breaks down the response path,

349
00:12:56,800 --> 00:12:58,639
showing how we drill down into the

350
00:12:58,639 --> 00:13:00,800
response, choices, message content to

351
00:13:00,800 --> 00:13:02,959
extract the actual text returned by the

352
00:13:02,959 --> 00:13:04,880
AI. Although the response object

353
00:13:04,880 --> 00:13:06,800
contains other fields like usage,

354
00:13:06,800 --> 00:13:09,120
statistics, and timestamps, most of the

355
00:13:09,120 --> 00:13:11,200
time what we really need is the content

356
00:13:11,200 --> 00:13:13,440
field. That brings us to task four,

357
00:13:13,440 --> 00:13:15,200
where we're asked to update the script

358
00:13:15,200 --> 00:13:17,360
to extract the AI's response using the

359
00:13:17,360 --> 00:13:19,519
exact path. Running the script here

360
00:13:19,519 --> 00:13:21,200
confirms that we can successfully

361
00:13:21,200 --> 00:13:23,440
capture and display the text that the AI

362
00:13:23,440 --> 00:13:25,360
returns. Once we've mastered making

363
00:13:25,360 --> 00:13:28,000
calls and extracting responses, the lab

364
00:13:28,000 --> 00:13:30,560
shifts gears to tokens and costs. We

365
00:13:30,560 --> 00:13:32,399
learned that tokens are the pieces of

366
00:13:32,399 --> 00:13:34,480
text used by the model that every

367
00:13:34,480 --> 00:13:37,040
request consumes tokens. Prom tokens are

368
00:13:37,040 --> 00:13:39,279
what we send in. Completion tokens are

369
00:13:39,279 --> 00:13:41,680
what the AI sends back and total tokens

370
00:13:41,680 --> 00:13:43,680
are the sums of both. Importantly,

371
00:13:43,680 --> 00:13:45,839
output tokens are more expensive than

372
00:13:45,839 --> 00:13:48,399
input tokens. So being concise can save

373
00:13:48,399 --> 00:13:50,720
money. Finally, in task five, we're

374
00:13:50,720 --> 00:13:53,040
asked to extract the token usage values,

375
00:13:53,040 --> 00:13:55,279
prompt completion, and total tokens from

376
00:13:55,279 --> 00:13:57,199
the response. The script is already set

377
00:13:57,199 --> 00:13:59,360
up to calculate costs. So once we

378
00:13:59,360 --> 00:14:01,360
complete the extraction and run it, we

379
00:14:01,360 --> 00:14:03,600
can see exactly how much the API call

380
00:14:03,600 --> 00:14:05,519
costs. The lab wraps up by

381
00:14:05,519 --> 00:14:07,600
congratulating us. At this point, we

382
00:14:07,600 --> 00:14:09,600
verified our environment, connected to

383
00:14:09,600 --> 00:14:12,560
OpenAI, made real API calls, extracted

384
00:14:12,560 --> 00:14:14,959
responses, and calculated costs. The key

385
00:14:14,959 --> 00:14:17,120
takeaway is remembering how to navigate

386
00:14:17,120 --> 00:14:18,480
the response object with

387
00:14:18,480 --> 00:14:21,360
response.content.

388
00:14:21,360 --> 00:14:23,360
Some of the finer points and details

389
00:14:23,360 --> 00:14:25,600
like exploring usage fields or playing

390
00:14:25,600 --> 00:14:27,519
with different models are left for you

391
00:14:27,519 --> 00:14:29,680
to explore yourself. But by now, you

392
00:14:29,680 --> 00:14:31,279
should have a solid foundation for

393
00:14:31,279 --> 00:14:33,760
working with AI APIs and be ready for

394
00:14:33,760 --> 00:14:36,880
what comes next in the upcoming labs.

395
00:14:36,880 --> 00:14:38,560
All right, let's start with the labs. In

396
00:14:38,560 --> 00:14:40,320
this lab, we're going to explore Lang

397
00:14:40,320 --> 00:14:42,079
Chain and understand how it makes

398
00:14:42,079 --> 00:14:44,000
working with multiple AI provider

399
00:14:44,000 --> 00:14:46,800
simpler and faster. The key idea here is

400
00:14:46,800 --> 00:14:48,720
that instead of being locked into one

401
00:14:48,720 --> 00:14:51,120
provider's SDK and rewriting code

402
00:14:51,120 --> 00:14:53,519
whenever you switch, Langchain offers

403
00:14:53,519 --> 00:14:55,600
one interface that works everywhere.

404
00:14:55,600 --> 00:14:57,519
With it, you can move from OpenAI to

405
00:14:57,519 --> 00:15:00,240
Google's Gemini or XAI's Gro by changing

406
00:15:00,240 --> 00:15:02,160
just a single word. We begin the

407
00:15:02,160 --> 00:15:04,240
environment verification. In this step,

408
00:15:04,240 --> 00:15:06,240
we're asked to run a script that checks

409
00:15:06,240 --> 00:15:08,399
whether Langchain and its dependencies

410
00:15:08,399 --> 00:15:11,040
are installed, validates our API keys

411
00:15:11,040 --> 00:15:13,519
and our base URL, and confirms that we

412
00:15:13,519 --> 00:15:15,040
have access to different model

413
00:15:15,040 --> 00:15:17,760
providers. Once this check passes, we're

414
00:15:17,760 --> 00:15:20,240
ready to start experimenting. The first

415
00:15:20,240 --> 00:15:22,800
test compares the traditional OpenAI SDK

416
00:15:22,800 --> 00:15:25,040
approach with Lang. We have to write 10

417
00:15:25,040 --> 00:15:27,199
or more lines of boilerplate code just

418
00:15:27,199 --> 00:15:29,279
to make an API call. If we want to

419
00:15:29,279 --> 00:15:31,199
switch to another provider, we'd have to

420
00:15:31,199 --> 00:15:33,440
rewrite all of it. With Langchain, the

421
00:15:33,440 --> 00:15:35,279
same logic is cut down to just three

422
00:15:35,279 --> 00:15:37,360
lines. And switching providers is as

423
00:15:37,360 --> 00:15:39,519
simple as changing the model name. In

424
00:15:39,519 --> 00:15:41,600
this task, we're asked to complete both

425
00:15:41,600 --> 00:15:44,320
versions in a script and then run them

426
00:15:44,320 --> 00:15:46,320
side by side.

427
00:15:46,320 --> 00:15:48,800
This is where we really see the 70%

428
00:15:48,800 --> 00:15:51,600
reduction in code. The second task

429
00:15:51,600 --> 00:15:53,839
demonstrates multimodel support. Here

430
00:15:53,839 --> 00:15:55,360
we're asked to configure three

431
00:15:55,360 --> 00:15:58,160
providers. Open GPT4, Google's Gemini,

432
00:15:58,160 --> 00:16:00,959
and XAS Gro, all with the same class and

433
00:16:00,959 --> 00:16:03,120
structure. Once configured, we can run

434
00:16:03,120 --> 00:16:05,040
the exact same prompt through all of

435
00:16:05,040 --> 00:16:07,360
them and compare their responses. This

436
00:16:07,360 --> 00:16:09,120
is especially powerful when you need to

437
00:16:09,120 --> 00:16:11,839
do AB test or balance cost because you

438
00:16:11,839 --> 00:16:14,160
can evaluate multiple models instantly

439
00:16:14,160 --> 00:16:16,000
without changing your code structure. In

440
00:16:16,000 --> 00:16:17,680
the third task, we're introduced to

441
00:16:17,680 --> 00:16:19,440
prompt templates. Instead of writing

442
00:16:19,440 --> 00:16:21,360
separate hard-coded prompts for every

443
00:16:21,360 --> 00:16:23,680
variations, we create one reusable

444
00:16:23,680 --> 00:16:26,160
template with placeholders. Then we can

445
00:16:26,160 --> 00:16:28,320
fill in the variables dynamically just

446
00:16:28,320 --> 00:16:30,959
like fstrings in Python. This eliminates

447
00:16:30,959 --> 00:16:33,199
the nightmare of maintaining hundreds of

448
00:16:33,199 --> 00:16:35,519
slightly different prompt files. After

449
00:16:35,519 --> 00:16:37,519
completing the template, we test it with

450
00:16:37,519 --> 00:16:39,519
multiple inputs to see how the same

451
00:16:39,519 --> 00:16:41,920
structure generates varied responses.

452
00:16:41,920 --> 00:16:44,079
The fourth task takes a step further by

453
00:16:44,079 --> 00:16:46,800
introducing output parsers. Often AI

454
00:16:46,800 --> 00:16:49,600
responses are just free text, but what

455
00:16:49,600 --> 00:16:51,680
our code really needs are structured

456
00:16:51,680 --> 00:16:54,320
objects. Here we're asked to add parsers

457
00:16:54,320 --> 00:16:56,639
that can transform responses into lists

458
00:16:56,639 --> 00:16:59,600
or JSON objects. In this way, instead of

459
00:16:59,600 --> 00:17:01,839
dealing with unstructured sentences, we

460
00:17:01,839 --> 00:17:04,000
can access clean Python lists or

461
00:17:04,000 --> 00:17:05,919
dictionaries that our application can

462
00:17:05,919 --> 00:17:07,679
use directly.

463
00:17:07,679 --> 00:17:09,839
Finally, we reach task five, which is

464
00:17:09,839 --> 00:17:12,079
all about chain composition. Langchain

465
00:17:12,079 --> 00:17:13,919
allows us to connect components together

466
00:17:13,919 --> 00:17:16,079
with pipe operator. Just like Unix

467
00:17:16,079 --> 00:17:17,919
pipes, instead of writing multiple

468
00:17:17,919 --> 00:17:20,000
variables for each step, creating a

469
00:17:20,000 --> 00:17:22,240
prompt, sending it to the model, getting

470
00:17:22,240 --> 00:17:24,559
a response, and parsing the result, we

471
00:17:24,559 --> 00:17:26,799
simply chain everything together. With

472
00:17:26,799 --> 00:17:29,120
one line, we can link prompts, models,

473
00:17:29,120 --> 00:17:31,440
and parsers, and then invoke the chain

474
00:17:31,440 --> 00:17:33,520
to get the structure output. It's a much

475
00:17:33,520 --> 00:17:35,520
cleaner and more scalable way to build

476
00:17:35,520 --> 00:17:37,919
AI pipelines. By the end of this lab,

477
00:17:37,919 --> 00:17:39,760
we've learned how a lane chain reduces

478
00:17:39,760 --> 00:17:41,840
boiler plate, enables multimodel

479
00:17:41,840 --> 00:17:44,320
flexibility, creates reusable templates,

480
00:17:44,320 --> 00:17:46,240
parses structured outputs, and ties

481
00:17:46,240 --> 00:17:47,840
everything together with elegant

482
00:17:47,840 --> 00:17:49,919
chaining. Some of the finer details like

483
00:17:49,919 --> 00:17:52,080
experimenting with more complex parser

484
00:17:52,080 --> 00:17:54,240
setups or chaining additional steps are

485
00:17:54,240 --> 00:17:57,280
left for you to explore on your own.

486
00:17:57,280 --> 00:17:59,520
Now, we come to the technique, but it's

487
00:17:59,520 --> 00:18:01,200
not a technique in the sense of building

488
00:18:01,200 --> 00:18:03,440
lane chain application like we just did.

489
00:18:03,440 --> 00:18:05,520
No, we're talking about a technique that

490
00:18:05,520 --> 00:18:07,919
involves how you send your prompt to the

491
00:18:07,919 --> 00:18:09,760
agent that we just built. In other

492
00:18:09,760 --> 00:18:12,400
words, prompt engineering. When you send

493
00:18:12,400 --> 00:18:14,880
a prompt as an input to TechCorps AI

494
00:18:14,880 --> 00:18:16,880
document assistant that we just built,

495
00:18:16,880 --> 00:18:19,039
the quality of your prompt directly

496
00:18:19,039 --> 00:18:21,360
impacts the quality of responses you

497
00:18:21,360 --> 00:18:23,600
receive. While AI agents can certainly

498
00:18:23,600 --> 00:18:25,760
handle wide range of prompts,

499
00:18:25,760 --> 00:18:27,679
understanding prompt techniques help you

500
00:18:27,679 --> 00:18:29,280
communicate more effectively with

501
00:18:29,280 --> 00:18:31,440
TechCorp system. For example, if you

502
00:18:31,440 --> 00:18:33,120
prompt the agent with this question,

503
00:18:33,120 --> 00:18:35,440
"What is the policy?" It can pull a lot

504
00:18:35,440 --> 00:18:37,760
of details that are irrelevant. Sending

505
00:18:37,760 --> 00:18:39,919
a more specific prompt like, "What's the

506
00:18:39,919 --> 00:18:41,760
company's remote work policy for

507
00:18:41,760 --> 00:18:43,760
international employees?" will lead to a

508
00:18:43,760 --> 00:18:46,080
more accurate result from the agent. And

509
00:18:46,080 --> 00:18:47,600
the same thing applies to role

510
00:18:47,600 --> 00:18:49,440
definition when you're describing the

511
00:18:49,440 --> 00:18:51,679
role of the agent. For example, you

512
00:18:51,679 --> 00:18:53,600
might descriptively write out a detailed

513
00:18:53,600 --> 00:18:55,919
prompt like, "You are a tech customer

514
00:18:55,919 --> 00:18:57,600
support expert." When you are asked

515
00:18:57,600 --> 00:18:59,679
about the company's policy, you are to

516
00:18:59,679 --> 00:19:01,840
always respond with bullet points for

517
00:19:01,840 --> 00:19:04,000
easier readability. As you can see,

518
00:19:04,000 --> 00:19:05,600
being able to control the agents

519
00:19:05,600 --> 00:19:07,840
behavior can directly benefit from a

520
00:19:07,840 --> 00:19:09,840
well-written prompt. This type of

521
00:19:09,840 --> 00:19:11,679
technique is referred to as prompt

522
00:19:11,679 --> 00:19:13,200
engineering. And there are different

523
00:19:13,200 --> 00:19:15,760
prompt techniques like zeroot, oneshot,

524
00:19:15,760 --> 00:19:17,840
fshot, and chain of thought prompting

525
00:19:17,840 --> 00:19:20,080
have its own use case for the task. For

526
00:19:20,080 --> 00:19:22,400
example, zerootshot prompting means that

527
00:19:22,400 --> 00:19:24,960
we are asking AI to perform a task

528
00:19:24,960 --> 00:19:27,600
without providing any examples. So if

529
00:19:27,600 --> 00:19:30,160
you send a prompt, write a data privacy

530
00:19:30,160 --> 00:19:32,320
policy for our European customers,

531
00:19:32,320 --> 00:19:34,480
you're essentially relying entirely on

532
00:19:34,480 --> 00:19:36,559
the AI's existing knowledge base to

533
00:19:36,559 --> 00:19:38,640
write the data policy document. Since

534
00:19:38,640 --> 00:19:40,559
within the prompt, we're not giving any

535
00:19:40,559 --> 00:19:42,960
examples of what they are. Oneshot and

536
00:19:42,960 --> 00:19:44,559
few shot prompting is similar to

537
00:19:44,559 --> 00:19:46,640
zerootshot but in this case we're

538
00:19:46,640 --> 00:19:48,880
providing examples of how the agent

539
00:19:48,880 --> 00:19:50,880
should respond directly within the

540
00:19:50,880 --> 00:19:53,120
prompt. For example, you might say

541
00:19:53,120 --> 00:19:54,799
here's how we format our policy

542
00:19:54,799 --> 00:19:56,799
documents. Now write a data privacy

543
00:19:56,799 --> 00:19:59,039
policy following the same structure

544
00:19:59,039 --> 00:20:01,679
because you provided a template. The AI

545
00:20:01,679 --> 00:20:03,600
follows your specific formatting and

546
00:20:03,600 --> 00:20:06,160
style preferences more consistently. And

547
00:20:06,160 --> 00:20:08,400
conversely, fusart learning is the act

548
00:20:08,400 --> 00:20:10,799
of learning from the LLM side where even

549
00:20:10,799 --> 00:20:12,720
though the LLM might not have seen the

550
00:20:12,720 --> 00:20:14,960
exact training data for how to process

551
00:20:14,960 --> 00:20:17,039
your unique request, it's able to

552
00:20:17,039 --> 00:20:19,200
demonstrate the ability to fulfill your

553
00:20:19,200 --> 00:20:21,840
request from similar examples provided.

554
00:20:21,840 --> 00:20:23,840
And finally, chain of thought prompting

555
00:20:23,840 --> 00:20:25,520
is a style of prompting where you

556
00:20:25,520 --> 00:20:27,760
provide the model with a trail of steps

557
00:20:27,760 --> 00:20:30,000
to think through how to solve specific

558
00:20:30,000 --> 00:20:32,159
problems. For example, instead of

559
00:20:32,159 --> 00:20:35,039
prompting the AI agent with fix our data

560
00:20:35,039 --> 00:20:37,440
retention policy, you might instead use

561
00:20:37,440 --> 00:20:39,440
chain of thought prompting to say here's

562
00:20:39,440 --> 00:20:41,520
how you fix data retention policy.

563
00:20:41,520 --> 00:20:43,520
Review current GDPR requirements for

564
00:20:43,520 --> 00:20:46,240
data retention periods. Then analyze our

565
00:20:46,240 --> 00:20:49,039
existing policy for specific gaps. Then

566
00:20:49,039 --> 00:20:51,039
research industry best practices for

567
00:20:51,039 --> 00:20:53,600
similar companies. And finally, draft

568
00:20:53,600 --> 00:20:55,360
specific recommendations within

569
00:20:55,360 --> 00:20:57,679
implementation steps. Now fix our

570
00:20:57,679 --> 00:20:59,760
customer policy. As you can see,

571
00:20:59,760 --> 00:21:02,080
providing how LLM should go through in

572
00:21:02,080 --> 00:21:04,480
breaking down a specific request for how

573
00:21:04,480 --> 00:21:06,640
data retention policy should be fixed

574
00:21:06,640 --> 00:21:09,440
gives an exact blueprint for how the LLM

575
00:21:09,440 --> 00:21:11,280
should then go and fix the customer

576
00:21:11,280 --> 00:21:13,440
policy, which in this case, we're not

577
00:21:13,440 --> 00:21:15,520
explicitly telling the agent how to fix

578
00:21:15,520 --> 00:21:17,760
the policy for that, but it gives the

579
00:21:17,760 --> 00:21:19,760
reasoning steps for the model to fix

580
00:21:19,760 --> 00:21:22,640
accordingly. So, in this lab, we're

581
00:21:22,640 --> 00:21:24,880
going to master prompt engineering using

582
00:21:24,880 --> 00:21:27,039
lane chain. The main problem being

583
00:21:27,039 --> 00:21:29,440
addressed here is that AI can sometimes

584
00:21:29,440 --> 00:21:32,320
give vague or inconsistent responses or

585
00:21:32,320 --> 00:21:34,480
not follow instructions properly. The

586
00:21:34,480 --> 00:21:36,400
solution is to use structured prompting

587
00:21:36,400 --> 00:21:38,480
techniques, zero shot, one shot,

588
00:21:38,480 --> 00:21:40,320
viewshot, and chain of thought. Each of

589
00:21:40,320 --> 00:21:42,640
which controls the AI's behavior in a

590
00:21:42,640 --> 00:21:44,720
different way. We begin by verifying the

591
00:21:44,720 --> 00:21:46,720
environment. The provided script checks

592
00:21:46,720 --> 00:21:48,480
that lang chain and its OpenAI

593
00:21:48,480 --> 00:21:50,480
integrations are installed, confirms

594
00:21:50,480 --> 00:21:53,120
that the API key and base URL are set

595
00:21:53,120 --> 00:21:54,799
and ensures that prompt template

596
00:21:54,799 --> 00:21:56,640
utilities are available. Once this

597
00:21:56,640 --> 00:21:58,799
verification passes, we're ready to move

598
00:21:58,799 --> 00:22:01,200
into tasks. The first task introduces

599
00:22:01,200 --> 00:22:03,760
zero prompting. In this exercise, we're

600
00:22:03,760 --> 00:22:05,840
asked to compare what happens when we

601
00:22:05,840 --> 00:22:08,080
provide a vague instruction versus when

602
00:22:08,080 --> 00:22:10,240
we write a very specific prompt. For

603
00:22:10,240 --> 00:22:12,960
example, simply asking the AI to write a

604
00:22:12,960 --> 00:22:16,000
policy results in a long generic essay.

605
00:22:16,000 --> 00:22:19,440
But when we specify write a 200word GDPR

606
00:22:19,440 --> 00:22:21,760
compliant privacy policy for European

607
00:22:21,760 --> 00:22:24,159
customer with 30-day retention period,

608
00:22:24,159 --> 00:22:26,480
the response is focused, useful, and

609
00:22:26,480 --> 00:22:28,080
aligned to the constraints. This

610
00:22:28,080 --> 00:22:30,080
demonstrates why being specific is

611
00:22:30,080 --> 00:22:32,240
crucial in zero shot prompts. The second

612
00:22:32,240 --> 00:22:35,120
task moves us to oneot prompting. Here

613
00:22:35,120 --> 00:22:37,600
we provide one example for the AI to

614
00:22:37,600 --> 00:22:39,440
follow almost like showing a single

615
00:22:39,440 --> 00:22:42,240
template. For example, if we gave the AI

616
00:22:42,240 --> 00:22:44,559
one refund policy example with five

617
00:22:44,559 --> 00:22:46,720
structured sections, we can then ask it

618
00:22:46,720 --> 00:22:49,039
to produce a remote work policy and it

619
00:22:49,039 --> 00:22:50,720
will replicate the same style in

620
00:22:50,720 --> 00:22:53,360
structure. This shows how one example

621
00:22:53,360 --> 00:22:55,840
can set the tone and ensure consistency

622
00:22:55,840 --> 00:22:58,559
across many outputs. Next, in task

623
00:22:58,559 --> 00:23:00,880
three, we expand on this with few shop

624
00:23:00,880 --> 00:23:02,960
prompting. Instead of one example, we

625
00:23:02,960 --> 00:23:05,520
provide multiple examples so the AI can

626
00:23:05,520 --> 00:23:08,000
learn not only the format but also the

627
00:23:08,000 --> 00:23:11,039
tone, patterns, and style. For example,

628
00:23:11,039 --> 00:23:13,440
giving three examples of emphatic

629
00:23:13,440 --> 00:23:15,919
support replies teaches the model how to

630
00:23:15,919 --> 00:23:17,360
handle customer support issues

631
00:23:17,360 --> 00:23:19,520
consistently. Once the examples are in

632
00:23:19,520 --> 00:23:22,159
place, the AI can generate new responses

633
00:23:22,159 --> 00:23:24,559
that follow the same tone and structure,

634
00:23:24,559 --> 00:23:26,799
making it especially powerful for use

635
00:23:26,799 --> 00:23:29,760
cases like customer service. In task 4,

636
00:23:29,760 --> 00:23:31,360
we're introduced to chain of thought

637
00:23:31,360 --> 00:23:33,679
prompting. This technique encourages the

638
00:23:33,679 --> 00:23:36,480
AI to show its reasoning step by step.

639
00:23:36,480 --> 00:23:39,200
Instead of vague oneline answer, the AI

640
00:23:39,200 --> 00:23:41,600
breaks a problem into steps and works

641
00:23:41,600 --> 00:23:43,919
through it systematically. This results

642
00:23:43,919 --> 00:23:46,240
in clear or more reliable and more

643
00:23:46,240 --> 00:23:48,240
accurate outputs, particularly for

644
00:23:48,240 --> 00:23:51,280
complex reasoning tasks. Finally, task 5

645
00:23:51,280 --> 00:23:53,120
brings all of these techniques together

646
00:23:53,120 --> 00:23:55,520
in a head-to-head comparison. We run the

647
00:23:55,520 --> 00:23:57,280
same problem through zero shot, one

648
00:23:57,280 --> 00:23:58,880
shot, few shot and chain of thought

649
00:23:58,880 --> 00:24:01,200
prompts to see the difference. Each

650
00:24:01,200 --> 00:24:03,360
approach has its strength. Zero shot is

651
00:24:03,360 --> 00:24:05,919
quick. One shot ensures formatting. Few

652
00:24:05,919 --> 00:24:08,559
shot enforces tone and consistency and

653
00:24:08,559 --> 00:24:10,480
chain of thought excels at detailed

654
00:24:10,480 --> 00:24:12,080
reasoning. The outcome shows that

655
00:24:12,080 --> 00:24:13,840
choosing the right technique can

656
00:24:13,840 --> 00:24:16,080
dramatically improve results depending

657
00:24:16,080 --> 00:24:18,000
on the task. By end of this lab, we not

658
00:24:18,000 --> 00:24:20,320
only learned what each prompt method is,

659
00:24:20,320 --> 00:24:22,320
but we've also seen them in action. The

660
00:24:22,320 --> 00:24:24,400
key takeaway is that the right technique

661
00:24:24,400 --> 00:24:26,480
can make your prompts 10 times more

662
00:24:26,480 --> 00:24:28,400
effective. Some of these exercises are

663
00:24:28,400 --> 00:24:30,799
left for you to explore and refine. But

664
00:24:30,799 --> 00:24:32,960
now you have the foundation to decide

665
00:24:32,960 --> 00:24:34,960
whether you need speed, structure,

666
00:24:34,960 --> 00:24:36,960
style, or reasoning in your AI

667
00:24:36,960 --> 00:24:39,600
responses. That wraps up this narration.

668
00:24:39,600 --> 00:24:41,520
And with it, you're now ready to move on

669
00:24:41,520 --> 00:24:43,520
to the next lab onto vector databases

670
00:24:43,520 --> 00:24:45,760
and semantic search.

671
00:24:45,760 --> 00:24:47,600
Let's do a quick recap of what we just

672
00:24:47,600 --> 00:24:50,240
built. We learned about what LLM is and

673
00:24:50,240 --> 00:24:52,720
how LLMs use what's inside the context

674
00:24:52,720 --> 00:24:54,960
window. After learning about LLMs, we

675
00:24:54,960 --> 00:24:56,799
wanted to solve Tech Corp's business

676
00:24:56,799 --> 00:24:59,440
requirements of searching for 500 GB

677
00:24:59,440 --> 00:25:01,679
worth of data. In order to do that, we

678
00:25:01,679 --> 00:25:03,760
determined that embedding is a good way

679
00:25:03,760 --> 00:25:06,159
to search a massive set of documents.

680
00:25:06,159 --> 00:25:08,320
After that, we went over Langchain and

681
00:25:08,320 --> 00:25:10,320
what functions they serve, which is that

682
00:25:10,320 --> 00:25:12,240
they allow us to easily build Gentic

683
00:25:12,240 --> 00:25:14,559
application like Tech Corps chatbot. So

684
00:25:14,559 --> 00:25:16,000
now that we have the lang chain

685
00:25:16,000 --> 00:25:17,360
application, we need to be able to

686
00:25:17,360 --> 00:25:19,200
search through these large sets of

687
00:25:19,200 --> 00:25:22,240
documents. Let's say inside the 500 GB

688
00:25:22,240 --> 00:25:24,159
of documents, your company has a

689
00:25:24,159 --> 00:25:26,240
document called employee handbook that

690
00:25:26,240 --> 00:25:28,720
covers policies like time off, dress

691
00:25:28,720 --> 00:25:31,440
code, and equipment use. Employees might

692
00:25:31,440 --> 00:25:34,320
ask terms like vacation policy, but miss

693
00:25:34,320 --> 00:25:36,640
time off guidelines. While these are

694
00:25:36,640 --> 00:25:38,080
common questions that people would

695
00:25:38,080 --> 00:25:40,159
typically ask, building a database

696
00:25:40,159 --> 00:25:42,480
around this requirement can be tricky.

697
00:25:42,480 --> 00:25:44,799
In a conventional approach where data is

698
00:25:44,799 --> 00:25:46,480
stored in a structured database like

699
00:25:46,480 --> 00:25:48,799
SQL, you typically need to do some

700
00:25:48,799 --> 00:25:50,880
amount of similarity search like select

701
00:25:50,880 --> 00:25:54,000
all from documents content like vacation

702
00:25:54,000 --> 00:25:56,240
or vacation policy with a wild card

703
00:25:56,240 --> 00:25:58,000
before and after to look for details

704
00:25:58,000 --> 00:26:00,159
about questions on holiday. To expand

705
00:26:00,159 --> 00:26:02,320
your result set, you might increase the

706
00:26:02,320 --> 00:26:05,919
scope by adding VA or VAC space P.

707
00:26:05,919 --> 00:26:07,919
However, the drawback to this approach

708
00:26:07,919 --> 00:26:10,320
is that it puts the onus on the person

709
00:26:10,320 --> 00:26:12,320
searching for the data to get the search

710
00:26:12,320 --> 00:26:14,640
term formatted correctly. But what if

711
00:26:14,640 --> 00:26:16,159
there was a different way to store the

712
00:26:16,159 --> 00:26:18,320
data? What if instead of storing them by

713
00:26:18,320 --> 00:26:20,640
the value, we store the meaning of those

714
00:26:20,640 --> 00:26:22,480
words? This way, when you search the

715
00:26:22,480 --> 00:26:24,559
database by sending the question itself

716
00:26:24,559 --> 00:26:27,200
of can I request time off on a holiday

717
00:26:27,200 --> 00:26:28,799
based on the meaning of those words

718
00:26:28,799 --> 00:26:30,799
contained in the question, the database

719
00:26:30,799 --> 00:26:33,520
returns only relevant data back. This is

720
00:26:33,520 --> 00:26:35,840
a spirit of what vector databases tries

721
00:26:35,840 --> 00:26:37,919
to address storing data by the

722
00:26:37,919 --> 00:26:40,159
embedding. So essentially instead of

723
00:26:40,159 --> 00:26:42,640
searching by value, we can now search by

724
00:26:42,640 --> 00:26:44,799
meaning. Popular implementation of

725
00:26:44,799 --> 00:26:47,120
vector databases include pine cone and

726
00:26:47,120 --> 00:26:49,840
chroma. These platforms are designed to

727
00:26:49,840 --> 00:26:52,159
handle embeddings at scale and provide

728
00:26:52,159 --> 00:26:54,159
efficient retrieval based on semantic

729
00:26:54,159 --> 00:26:56,640
similarity. And these are also great use

730
00:26:56,640 --> 00:26:58,880
cases for prototyping something quick.

731
00:26:58,880 --> 00:27:00,559
While conceptually this seems

732
00:27:00,559 --> 00:27:02,480
straightforward, there's a bit of an

733
00:27:02,480 --> 00:27:04,480
overhead in setting this up. And you

734
00:27:04,480 --> 00:27:06,640
might be asking, well, can we just throw

735
00:27:06,640 --> 00:27:08,559
the employee handbook into the database

736
00:27:08,559 --> 00:27:10,880
like we just did for SQL database? Not

737
00:27:10,880 --> 00:27:12,880
quite. And here's why. With SQL

738
00:27:12,880 --> 00:27:15,200
database, the burden is put on the user

739
00:27:15,200 --> 00:27:17,520
searching to structure the database. But

740
00:27:17,520 --> 00:27:19,760
with vector databases, the burden is put

741
00:27:19,760 --> 00:27:21,600
on you who is setting up the database

742
00:27:21,600 --> 00:27:23,440
since you are trying to make it easier

743
00:27:23,440 --> 00:27:25,440
for someone searching for the data. And

744
00:27:25,440 --> 00:27:27,440
you can imagine why a method like this

745
00:27:27,440 --> 00:27:29,520
is becoming extremely popular when

746
00:27:29,520 --> 00:27:31,840
paired with large language models in AI

747
00:27:31,840 --> 00:27:33,760
since you don't have to train separately

748
00:27:33,760 --> 00:27:36,480
on how LLM should search your database.

749
00:27:36,480 --> 00:27:39,120
Instead, the LLM can freely search based

750
00:27:39,120 --> 00:27:41,200
on meaning and have the confidence that

751
00:27:41,200 --> 00:27:43,279
your database will return relevant data

752
00:27:43,279 --> 00:27:45,840
it needs. So let's explore some of the

753
00:27:45,840 --> 00:27:47,840
key concepts behind what goes into

754
00:27:47,840 --> 00:27:50,080
setting up a basic vector database.

755
00:27:50,080 --> 00:27:52,400
Let's start with embedding. Embedding is

756
00:27:52,400 --> 00:27:54,240
really the key concept that makes the

757
00:27:54,240 --> 00:27:57,360
medium go from value to meaning. In SQL,

758
00:27:57,360 --> 00:27:59,200
we store the values contained in the

759
00:27:59,200 --> 00:28:01,520
employee handbook as a straightup value.

760
00:28:01,520 --> 00:28:03,600
But in a vector database, you need to do

761
00:28:03,600 --> 00:28:06,000
some extra work up front to convert the

762
00:28:06,000 --> 00:28:08,000
value into semantic meanings. And these

763
00:28:08,000 --> 00:28:09,679
meanings are stored in what's called

764
00:28:09,679 --> 00:28:12,000
embeddings. For example, the words

765
00:28:12,000 --> 00:28:14,480
holiday and vacation should semantically

766
00:28:14,480 --> 00:28:16,640
share a similar space since the meaning

767
00:28:16,640 --> 00:28:18,720
of those words are close to each other.

768
00:28:18,720 --> 00:28:20,960
So before the sentence employee shall

769
00:28:20,960 --> 00:28:23,360
not request time off on holidays in the

770
00:28:23,360 --> 00:28:25,679
document is added to the database. The

771
00:28:25,679 --> 00:28:27,919
system runs through an embedding model

772
00:28:27,919 --> 00:28:29,760
and the embedding model converts that

773
00:28:29,760 --> 00:28:32,320
sentence into a long vector of numbers

774
00:28:32,320 --> 00:28:34,399
and when you search the database you are

775
00:28:34,399 --> 00:28:36,559
actually comparing this exact vector.

776
00:28:36,559 --> 00:28:38,559
That way when someone later asks can I

777
00:28:38,559 --> 00:28:40,480
take vacation during a holiday even

778
00:28:40,480 --> 00:28:42,000
though the phrasing is a little bit

779
00:28:42,000 --> 00:28:44,080
different the database can still service

780
00:28:44,080 --> 00:28:46,399
the request. And this is the fundamental

781
00:28:46,399 --> 00:28:48,399
shift. Instead of searching by exact

782
00:28:48,399 --> 00:28:50,960
wording, we're now searching by meaning.

783
00:28:50,960 --> 00:28:52,480
Another important concept is

784
00:28:52,480 --> 00:28:54,880
dimensionality. And you might be asking,

785
00:28:54,880 --> 00:28:56,000
why do I have to worry about

786
00:28:56,000 --> 00:28:58,080
dimensionality? Can't I just throw the

787
00:28:58,080 --> 00:29:00,000
words into embedding and store it into

788
00:29:00,000 --> 00:29:02,240
the database? There's one more aspect in

789
00:29:02,240 --> 00:29:03,919
embedding that you need to think about,

790
00:29:03,919 --> 00:29:06,480
and that's dimensionality. Typically, a

791
00:29:06,480 --> 00:29:08,480
word doesn't just have one meaning to

792
00:29:08,480 --> 00:29:10,559
learn from. For example, the word

793
00:29:10,559 --> 00:29:12,720
vacation can have different semantics

794
00:29:12,720 --> 00:29:14,480
depending on the context that is used

795
00:29:14,480 --> 00:29:17,120
in. and capturing all those intricacies

796
00:29:17,120 --> 00:29:19,760
like tone, formality, and other features

797
00:29:19,760 --> 00:29:21,840
can give richness to those words.

798
00:29:21,840 --> 00:29:24,720
Typically, dimensions we use today are

799
00:29:24,720 --> 00:29:27,679
1536 dimensions, which is a good mix of

800
00:29:27,679 --> 00:29:29,919
not having too much burden in size, but

801
00:29:29,919 --> 00:29:31,919
also giving enough context to allow for

802
00:29:31,919 --> 00:29:34,399
depth in each search. Once the embedding

803
00:29:34,399 --> 00:29:36,480
is stored with proper dimension, there

804
00:29:36,480 --> 00:29:38,480
are two other major angles that we need

805
00:29:38,480 --> 00:29:40,080
to consider when we're working with

806
00:29:40,080 --> 00:29:42,320
vector databases. And this is the

807
00:29:42,320 --> 00:29:44,640
retrieval side. Meaning now that we

808
00:29:44,640 --> 00:29:46,640
store the meaning of those words, we

809
00:29:46,640 --> 00:29:48,240
have to take on the burden of the

810
00:29:48,240 --> 00:29:50,720
retrieval side of embeddings. Since we

811
00:29:50,720 --> 00:29:52,480
are not doing searches like we did in

812
00:29:52,480 --> 00:29:55,600
SQL with a wear query, we need to make a

813
00:29:55,600 --> 00:29:57,360
decision on what would technically be

814
00:29:57,360 --> 00:30:00,000
counted as a much and by how much. This

815
00:30:00,000 --> 00:30:02,159
is done by looking at scoring and chunk

816
00:30:02,159 --> 00:30:03,840
overlap. And if you're at this point

817
00:30:03,840 --> 00:30:05,679
wondering, this seems like a lot of

818
00:30:05,679 --> 00:30:07,760
tweaking just to use vector database.

819
00:30:07,760 --> 00:30:09,440
And that's the serious trade-off you

820
00:30:09,440 --> 00:30:11,039
ought to consider when using a vector

821
00:30:11,039 --> 00:30:13,520
database, which is that while a properly

822
00:30:13,520 --> 00:30:15,360
set up vector database makes searching

823
00:30:15,360 --> 00:30:17,440
so much more flexible, getting the

824
00:30:17,440 --> 00:30:19,600
vector database properly configured

825
00:30:19,600 --> 00:30:22,080
often adds complexity up front. So with

826
00:30:22,080 --> 00:30:24,399
that in mind, scoring is a threshold you

827
00:30:24,399 --> 00:30:26,480
set to how similar the results need to

828
00:30:26,480 --> 00:30:28,640
be to be considered a proper match. For

829
00:30:28,640 --> 00:30:30,799
example, the word Florida might have

830
00:30:30,799 --> 00:30:32,880
some similarity to the word vacation

831
00:30:32,880 --> 00:30:34,799
since it's often where people go for

832
00:30:34,799 --> 00:30:37,600
vacation. But asking the question, can I

833
00:30:37,600 --> 00:30:39,919
take my company laptop to Florida is

834
00:30:39,919 --> 00:30:41,679
very different than does my company

835
00:30:41,679 --> 00:30:44,480
allow vacation to Florida? Since one is

836
00:30:44,480 --> 00:30:47,600
asking about a policy in IT jurisdiction

837
00:30:47,600 --> 00:30:50,399
and the other is about vacation policy.

838
00:30:50,399 --> 00:30:52,559
So setting up a score threshold based on

839
00:30:52,559 --> 00:30:54,559
the question can help you limit those

840
00:30:54,559 --> 00:30:57,200
low similarities to count as a match.

841
00:30:57,200 --> 00:30:59,440
Okay, there's one final angle which is

842
00:30:59,440 --> 00:31:02,240
chunk overlap. So in SQL, we're used to

843
00:31:02,240 --> 00:31:04,640
storing things rowby row, but in vector

844
00:31:04,640 --> 00:31:06,480
databases, things look a little bit

845
00:31:06,480 --> 00:31:08,559
different. When we're storing values in

846
00:31:08,559 --> 00:31:10,880
vector databases, they're often chunked

847
00:31:10,880 --> 00:31:12,640
going into the database. So when we

848
00:31:12,640 --> 00:31:14,720
chunk down an entire employee handbook

849
00:31:14,720 --> 00:31:16,799
into chunks, it's possible that the

850
00:31:16,799 --> 00:31:19,120
meaning gets chunked with it. That's why

851
00:31:19,120 --> 00:31:21,200
we allow chunk overlap so that the

852
00:31:21,200 --> 00:31:23,520
context spills over to leave enough

853
00:31:23,520 --> 00:31:26,320
margin for the search to work properly.

854
00:31:26,320 --> 00:31:28,080
In this app, we're going to build a

855
00:31:28,080 --> 00:31:30,399
semantic search engine step by step. The

856
00:31:30,399 --> 00:31:32,559
story begins with TechDoc Inc. where

857
00:31:32,559 --> 00:31:34,399
users search through documentation

858
00:31:34,399 --> 00:31:36,880
10,000 times a day. But more than half

859
00:31:36,880 --> 00:31:39,440
of those searches fail. Why? Because

860
00:31:39,440 --> 00:31:41,600
traditional keyword search can't connect

861
00:31:41,600 --> 00:31:44,320
reset password with password recovery

862
00:31:44,320 --> 00:31:47,039
process. Our mission is to fix that by

863
00:31:47,039 --> 00:31:48,640
building a search system that

864
00:31:48,640 --> 00:31:51,039
understands meaning, not just words. We

865
00:31:51,039 --> 00:31:53,120
begin with the environment setup. In

866
00:31:53,120 --> 00:31:54,880
this step, we're asked to install the

867
00:31:54,880 --> 00:31:56,640
libraries that make vector search

868
00:31:56,640 --> 00:31:58,799
possible. Sentence transformers for

869
00:31:58,799 --> 00:32:00,399
embeddings. lang chain for

870
00:32:00,399 --> 00:32:02,720
orchestration, chromadb for vector

871
00:32:02,720 --> 00:32:04,960
database and few utility libraries like

872
00:32:04,960 --> 00:32:07,440
numpy. Once installed, we verify the

873
00:32:07,440 --> 00:32:09,360
setup using a provided script. If

874
00:32:09,360 --> 00:32:10,960
everything checks out, we're ready to

875
00:32:10,960 --> 00:32:13,120
move forward. Next, we take a moment to

876
00:32:13,120 --> 00:32:14,880
understand embeddings. These are the

877
00:32:14,880 --> 00:32:16,880
backbone of semantic search. Instead of

878
00:32:16,880 --> 00:32:19,039
treating texts as words, embedding

879
00:32:19,039 --> 00:32:21,279
converts text into numerical vectors.

880
00:32:21,279 --> 00:32:23,200
Similar meanings end up close to each

881
00:32:23,200 --> 00:32:25,600
other in this mathematical space. That

882
00:32:25,600 --> 00:32:28,240
means forgot my password in account

883
00:32:28,240 --> 00:32:30,720
recovery looks very different in words

884
00:32:30,720 --> 00:32:33,200
but almost identical in vector 4. This

885
00:32:33,200 --> 00:32:35,519
is a magic that allows our search engine

886
00:32:35,519 --> 00:32:38,159
to succeed where keyword search fails.

887
00:32:38,159 --> 00:32:40,240
That takes us into task number one where

888
00:32:40,240 --> 00:32:42,720
we put embedding into action. We open

889
00:32:42,720 --> 00:32:44,799
the script, initialize the mini LM

890
00:32:44,799 --> 00:32:47,440
model, encode both queries and documents

891
00:32:47,440 --> 00:32:49,519
and then calculate similarity using

892
00:32:49,519 --> 00:32:51,760
cosign similarity. Running the script

893
00:32:51,760 --> 00:32:53,840
demonstrates how a search for forgot

894
00:32:53,840 --> 00:32:56,080
password successfully matches password

895
00:32:56,080 --> 00:32:58,480
recovery, showing semantic understanding

896
00:32:58,480 --> 00:33:00,240
in real time. Once we understand

897
00:33:00,240 --> 00:33:01,919
embeddings, we move to document

898
00:33:01,919 --> 00:33:04,159
chunking. Large documents can't be

899
00:33:04,159 --> 00:33:06,240
embedded all at once. So, we need to

900
00:33:06,240 --> 00:33:08,320
split them into smaller chunks, but if

901
00:33:08,320 --> 00:33:11,039
we cut too bluntly, we lose context.

902
00:33:11,039 --> 00:33:12,880
That's why overlapping chunks are

903
00:33:12,880 --> 00:33:15,200
important. They preserve meanings across

904
00:33:15,200 --> 00:33:17,519
boundaries. For example, setting a chunk

905
00:33:17,519 --> 00:33:19,919
size of 500 characters with 100

906
00:33:19,919 --> 00:33:22,159
characters overlap can improve retrieval

907
00:33:22,159 --> 00:33:25,039
accuracy by almost 40%. Lang chain helps

908
00:33:25,039 --> 00:33:27,279
us do this intelligently. In task number

909
00:33:27,279 --> 00:33:29,440
two, we put this into practice by

910
00:33:29,440 --> 00:33:31,600
editing a script to import lane chain's

911
00:33:31,600 --> 00:33:33,919
recursive characters text splitter and

912
00:33:33,919 --> 00:33:35,760
set the chunking parameters. Running the

913
00:33:35,760 --> 00:33:37,760
script confirms that our documents are

914
00:33:37,760 --> 00:33:40,240
now split into overlapping pieces ready

915
00:33:40,240 --> 00:33:42,559
for storage. The next concept we explore

916
00:33:42,559 --> 00:33:45,120
is vector stores. Embeddings alones are

917
00:33:45,120 --> 00:33:47,440
just numbers. We need a system to store

918
00:33:47,440 --> 00:33:49,360
and search through them efficiently.

919
00:33:49,360 --> 00:33:51,679
That's where Chromma comes in. It's a

920
00:33:51,679 --> 00:33:53,519
production ready vector database that

921
00:33:53,519 --> 00:33:55,600
can handle millions of embeddings,

922
00:33:55,600 --> 00:33:57,039
perform similarity search in

923
00:33:57,039 --> 00:33:58,960
milliseconds, and support metadata

924
00:33:58,960 --> 00:34:01,120
filtering. In task number three, we're

925
00:34:01,120 --> 00:34:02,880
asked to create a vector store using

926
00:34:02,880 --> 00:34:04,960
Chroma DB. We import the necessary

927
00:34:04,960 --> 00:34:07,200
classes, configure the embedding model,

928
00:34:07,200 --> 00:34:09,440
and then run the script. Once confirmed,

929
00:34:09,440 --> 00:34:11,520
we have a working vector store that can

930
00:34:11,520 --> 00:34:13,440
accept documents and retrieve them

931
00:34:13,440 --> 00:34:15,359
semantically. Finally, we bring

932
00:34:15,359 --> 00:34:16,879
everything together with semantic

933
00:34:16,879 --> 00:34:19,040
search. Here we implement the full

934
00:34:19,040 --> 00:34:21,679
pipeline, convert the user query into an

935
00:34:21,679 --> 00:34:24,079
embedding, search the Chromma store,

936
00:34:24,079 --> 00:34:25,760
retrieve the most relevant document

937
00:34:25,760 --> 00:34:28,159
chunks, and return them to the user. For

938
00:34:28,159 --> 00:34:30,639
example, a query like work from home

939
00:34:30,639 --> 00:34:33,359
policy will now correctly surface remote

940
00:34:33,359 --> 00:34:36,320
work guidelines. In task 4, we configure

941
00:34:36,320 --> 00:34:38,879
the query, set the number of top results

942
00:34:38,879 --> 00:34:41,359
to return, and establish a threshold for

943
00:34:41,359 --> 00:34:43,599
similarity scores. Running the script

944
00:34:43,599 --> 00:34:45,679
validates our search engine end to end.

945
00:34:45,679 --> 00:34:48,159
The lab closes with a recap. We started

946
00:34:48,159 --> 00:34:50,159
with a broken keyword search system

947
00:34:50,159 --> 00:34:52,560
where 60% of the search failed. Along

948
00:34:52,560 --> 00:34:54,639
the way, we learned about embeddings,

949
00:34:54,639 --> 00:34:56,800
smart document chunking, vector stores,

950
00:34:56,800 --> 00:34:58,960
and semantic search. By the end, we

951
00:34:58,960 --> 00:35:01,200
built a productionready search engine

952
00:35:01,200 --> 00:35:04,000
with 95% success rate. Some of the

953
00:35:04,000 --> 00:35:06,079
deeper experiments like adjusting chunk

954
00:35:06,079 --> 00:35:08,160
sizes, testing different embedding

955
00:35:08,160 --> 00:35:10,560
models and or adding metadata filters

956
00:35:10,560 --> 00:35:14,079
are left for you to explore on your own.

957
00:35:14,079 --> 00:35:15,839
So is it possible that instead of

958
00:35:15,839 --> 00:35:18,480
searching through the entire 500 GB of

959
00:35:18,480 --> 00:35:20,880
documents, AI assistant can fit them

960
00:35:20,880 --> 00:35:22,800
into their context window and generate

961
00:35:22,800 --> 00:35:25,839
output. This is called rag or retrieval

962
00:35:25,839 --> 00:35:27,839
augmented generation. Let's say your

963
00:35:27,839 --> 00:35:30,079
company used the AI assistant to ask

964
00:35:30,079 --> 00:35:32,000
this question. What's our remote work

965
00:35:32,000 --> 00:35:34,400
policy for international employees? In

966
00:35:34,400 --> 00:35:36,640
order to understand how rag works, we

967
00:35:36,640 --> 00:35:38,560
need to break them into three simple

968
00:35:38,560 --> 00:35:40,880
steps. Retrieval, augmented, and

969
00:35:40,880 --> 00:35:43,440
generation. Starting with retrieval,

970
00:35:43,440 --> 00:35:45,119
just like how we convert the document

971
00:35:45,119 --> 00:35:47,119
into vector embeddings to store them

972
00:35:47,119 --> 00:35:49,359
inside the database, we do the exact

973
00:35:49,359 --> 00:35:51,359
same step for the question that reads,

974
00:35:51,359 --> 00:35:53,280
"What's our remote work policy for

975
00:35:53,280 --> 00:35:55,520
international employees?" Once the word

976
00:35:55,520 --> 00:35:56,880
embedding for this question is

977
00:35:56,880 --> 00:35:58,640
generated, the embedding for that

978
00:35:58,640 --> 00:36:00,720
question is compared against embeddings

979
00:36:00,720 --> 00:36:03,200
of the documents. This type of search is

980
00:36:03,200 --> 00:36:05,200
called semantic search where instead of

981
00:36:05,200 --> 00:36:07,359
searching by the static keywords to find

982
00:36:07,359 --> 00:36:09,599
relevant contents, the meaning and the

983
00:36:09,599 --> 00:36:12,000
context of the query is used to match

984
00:36:12,000 --> 00:36:14,079
against the existing data set. Moving on

985
00:36:14,079 --> 00:36:16,560
to augmentation in rag refers to the

986
00:36:16,560 --> 00:36:18,640
process where the retrieved data is

987
00:36:18,640 --> 00:36:21,119
injected into the prompt at runtime. And

988
00:36:21,119 --> 00:36:22,880
you might think why is this all that

989
00:36:22,880 --> 00:36:25,520
special? Typically, AI assistants rely

990
00:36:25,520 --> 00:36:26,960
on what they learned during

991
00:36:26,960 --> 00:36:28,800
pre-training, which is static knowledge

992
00:36:28,800 --> 00:36:31,520
that can become outdated. Instead, our

993
00:36:31,520 --> 00:36:34,000
goal here is to have the AI assistant

994
00:36:34,000 --> 00:36:36,400
rely on up-to-date information stored in

995
00:36:36,400 --> 00:36:38,480
the vector database. In the case of RAG,

996
00:36:38,480 --> 00:36:40,640
the semantic search result pends to the

997
00:36:40,640 --> 00:36:42,720
prompt that essentially serves as an

998
00:36:42,720 --> 00:36:44,800
augmented knowledge. So, for your

999
00:36:44,800 --> 00:36:47,200
company, the AI assistant is given

1000
00:36:47,200 --> 00:36:49,200
details from company's documents that

1001
00:36:49,200 --> 00:36:51,680
are real, up-to-date, and private data

1002
00:36:51,680 --> 00:36:54,000
set. And all this can occur without

1003
00:36:54,000 --> 00:36:56,320
needing to fine-tune or modify the large

1004
00:36:56,320 --> 00:36:58,480
language model with custom data. The

1005
00:36:58,480 --> 00:37:01,200
final step of rag is generation. This is

1006
00:37:01,200 --> 00:37:03,760
a step where AI assistant generates the

1007
00:37:03,760 --> 00:37:05,599
response given the semantic relevant

1008
00:37:05,599 --> 00:37:08,000
data retrieved from the vector database.

1009
00:37:08,000 --> 00:37:10,160
So the initial prompt that says what's

1010
00:37:10,160 --> 00:37:12,400
our remote work policy for international

1011
00:37:12,400 --> 00:37:14,960
employees? The AI assistant will now

1012
00:37:14,960 --> 00:37:16,800
demonstrate its understanding of your

1013
00:37:16,800 --> 00:37:18,720
company's knowledge base by using the

1014
00:37:18,720 --> 00:37:20,960
documents that relate to remote work and

1015
00:37:20,960 --> 00:37:23,359
policy. And since the initial prompt

1016
00:37:23,359 --> 00:37:25,680
specifies a criteria of international

1017
00:37:25,680 --> 00:37:28,240
employees, the generation step will use

1018
00:37:28,240 --> 00:37:30,320
its own reasoning to wrestle with the

1019
00:37:30,320 --> 00:37:32,480
data provided to best answer the

1020
00:37:32,480 --> 00:37:34,880
question. Now, RAG is a very powerful

1021
00:37:34,880 --> 00:37:36,880
system that can instantly improve the

1022
00:37:36,880 --> 00:37:39,119
depth of knowledge beyond its training

1023
00:37:39,119 --> 00:37:41,520
data. But just like any other system,

1024
00:37:41,520 --> 00:37:43,680
learning how to calibrate is an acquired

1025
00:37:43,680 --> 00:37:45,680
skill that needs to be learned to get

1026
00:37:45,680 --> 00:37:47,920
the best results. Setting up a rag

1027
00:37:47,920 --> 00:37:49,599
system will look different from one

1028
00:37:49,599 --> 00:37:51,520
system to another because it heavily

1029
00:37:51,520 --> 00:37:53,200
depends on the data set that you're

1030
00:37:53,200 --> 00:37:55,359
trying to store. For example, legal

1031
00:37:55,359 --> 00:37:56,880
documents will require different

1032
00:37:56,880 --> 00:37:58,960
chunking strategies than a customer

1033
00:37:58,960 --> 00:38:01,200
support transcript document. This is

1034
00:38:01,200 --> 00:38:03,599
because legal documents often have long

1035
00:38:03,599 --> 00:38:05,200
structured paragraph that need to be

1036
00:38:05,200 --> 00:38:06,800
preserved and intact. While

1037
00:38:06,800 --> 00:38:08,720
conversational transcript can be just

1038
00:38:08,720 --> 00:38:10,960
fine with sentence level chunking with

1039
00:38:10,960 --> 00:38:14,079
high overlap to preserve context. In

1040
00:38:14,079 --> 00:38:16,000
this lab, we're taking our semantic

1041
00:38:16,000 --> 00:38:17,920
search system to the next level by

1042
00:38:17,920 --> 00:38:20,720
adding AI power generation. Up until

1043
00:38:20,720 --> 00:38:22,800
now, we've been able to find relevant

1044
00:38:22,800 --> 00:38:24,800
documents with high accuracy. For

1045
00:38:24,800 --> 00:38:27,119
example, matching remote work policy

1046
00:38:27,119 --> 00:38:29,119
when someone searches work from home.

1047
00:38:29,119 --> 00:38:31,119
But the CEO wants more. Instead of

1048
00:38:31,119 --> 00:38:33,520
retrieving a document, the system should

1049
00:38:33,520 --> 00:38:35,280
actually answer the user's questions

1050
00:38:35,280 --> 00:38:37,440
directly. something like yes, you can

1051
00:38:37,440 --> 00:38:39,440
work three days from home, not just

1052
00:38:39,440 --> 00:38:42,000
showing a PDF. We begin the environment

1053
00:38:42,000 --> 00:38:43,920
setup. In this step, we're asked to

1054
00:38:43,920 --> 00:38:45,920
activate the Python environment and

1055
00:38:45,920 --> 00:38:48,160
install the key libraries. These include

1056
00:38:48,160 --> 00:38:50,560
Chroma DB for vector storage, sentence

1057
00:38:50,560 --> 00:38:52,720
transformers for embeddings within lane

1058
00:38:52,720 --> 00:38:54,720
chain with integrations for OpenAI and

1059
00:38:54,720 --> 00:38:57,200
hugging face. Once installed, we verify

1060
00:38:57,200 --> 00:38:59,040
everything using the provided script to

1061
00:38:59,040 --> 00:39:01,280
ensure the rack framework is ready.

1062
00:39:01,280 --> 00:39:03,680
Next, we move into task number one,

1063
00:39:03,680 --> 00:39:05,920
setting up the vector store. Here we

1064
00:39:05,920 --> 00:39:08,400
initialize a chromabb client. Create our

1065
00:39:08,400 --> 00:39:11,520
get collection named tech corp brag and

1066
00:39:11,520 --> 00:39:13,440
configure the embedding model all

1067
00:39:13,440 --> 00:39:15,839
mini6v2.

1068
00:39:15,839 --> 00:39:17,920
This is where we get our system of

1069
00:39:17,920 --> 00:39:20,320
memory. A place where all of our company

1070
00:39:20,320 --> 00:39:22,560
documents will be stored as vectors so

1071
00:39:22,560 --> 00:39:25,280
that we can search them semantically. In

1072
00:39:25,280 --> 00:39:28,000
task number two, the focus shifts to

1073
00:39:28,000 --> 00:39:30,160
document processing and chunking. Unlike

1074
00:39:30,160 --> 00:39:32,880
our earlier lab where we split text into

1075
00:39:32,880 --> 00:39:35,280
fixed-size character chunks, here we

1076
00:39:35,280 --> 00:39:37,680
upgrade to paragraph-based chunking with

1077
00:39:37,680 --> 00:39:40,079
smart overlaps. The goal is to preserve

1078
00:39:40,079 --> 00:39:42,400
meaning so that each chunk contains

1079
00:39:42,400 --> 00:39:44,640
complete thoughts. This is crucial for

1080
00:39:44,640 --> 00:39:47,040
RAG because when AI generates answers,

1081
00:39:47,040 --> 00:39:49,280
the quality depends on having coherent

1082
00:39:49,280 --> 00:39:51,680
chunks of context.

1083
00:39:51,680 --> 00:39:54,160
From there, we go to task number three,

1084
00:39:54,160 --> 00:39:56,640
LLM integration. This is where we

1085
00:39:56,640 --> 00:40:00,000
connect OpenA model GPD4.1 Mini. The API

1086
00:40:00,000 --> 00:40:02,240
key and base are already preconfigured

1087
00:40:02,240 --> 00:40:04,079
for us. We just need to set the

1088
00:40:04,079 --> 00:40:06,079
generation parameters like temperature,

1089
00:40:06,079 --> 00:40:08,720
max tokens, and top P values. Once

1090
00:40:08,720 --> 00:40:10,720
integrated, we can test simple text

1091
00:40:10,720 --> 00:40:12,960
generation before layering on retrieval

1092
00:40:12,960 --> 00:40:15,280
and augmented steps. Task number four

1093
00:40:15,280 --> 00:40:17,520
introduces prompt engineering for rag.

1094
00:40:17,520 --> 00:40:19,359
We're asked to build a structured prompt

1095
00:40:19,359 --> 00:40:21,760
template that always ensures context is

1096
00:40:21,760 --> 00:40:23,680
included. The system prompt makes it

1097
00:40:23,680 --> 00:40:25,760
clear that answers must come only from

1098
00:40:25,760 --> 00:40:27,440
the retrieved documents. If the

1099
00:40:27,440 --> 00:40:29,920
information isn't in context, the AI

1100
00:40:29,920 --> 00:40:31,920
must respond with, "I don't have that

1101
00:40:31,920 --> 00:40:33,920
information in the provided documents."

1102
00:40:33,920 --> 00:40:35,839
This keeps our answers factual and

1103
00:40:35,839 --> 00:40:38,480
prevents hallucinations. Finally, we

1104
00:40:38,480 --> 00:40:41,040
reach task number five, the complete rag

1105
00:40:41,040 --> 00:40:43,520
pipeline. Here we wire everything

1106
00:40:43,520 --> 00:40:46,240
together. The flow is embed the user

1107
00:40:46,240 --> 00:40:49,040
query, search Chromad, retrieve the top

1108
00:40:49,040 --> 00:40:51,359
three chunks, build a contextaware

1109
00:40:51,359 --> 00:40:53,280
prompt, and generate an answer using

1110
00:40:53,280 --> 00:40:55,760
LLM. The final touch is a source

1111
00:40:55,760 --> 00:40:58,640
attribution. Every answer points back to

1112
00:40:58,640 --> 00:41:01,119
the document it was derived from. This

1113
00:41:01,119 --> 00:41:03,359
transforms the system into a full

1114
00:41:03,359 --> 00:41:06,160
production ready Q&A engine. At the end,

1115
00:41:06,160 --> 00:41:08,960
we celebrate rag mastery. What started

1116
00:41:08,960 --> 00:41:11,040
as simple document search has evolved

1117
00:41:11,040 --> 00:41:13,760
into a powerful system that retrieves,

1118
00:41:13,760 --> 00:41:16,400
augments, and generates answers. This is

1119
00:41:16,400 --> 00:41:18,319
the same architecture that powers tools

1120
00:41:18,319 --> 00:41:21,359
like catchupt, claude, and gemini. Some

1121
00:41:21,359 --> 00:41:23,359
parts like experimenting with different

1122
00:41:23,359 --> 00:41:25,680
trunk strategy, refining prompts are

1123
00:41:25,680 --> 00:41:27,680
left for you to explore yourself. But by

1124
00:41:27,680 --> 00:41:30,319
now you've built a complete RAG system

1125
00:41:30,319 --> 00:41:32,720
that answers questions with context,

1126
00:41:32,720 --> 00:41:35,760
accuracy, and confidence.

1127
00:41:35,760 --> 00:41:37,520
Now that we covered the conceptual

1128
00:41:37,520 --> 00:41:39,680
elements of RAG, let's look at how it

1129
00:41:39,680 --> 00:41:41,680
looks on a practical level. To better

1130
00:41:41,680 --> 00:41:43,359
understand this, we can look over at

1131
00:41:43,359 --> 00:41:45,520
this lab specifically geared towards how

1132
00:41:45,520 --> 00:41:48,319
to use Rag. Now we covered the basic

1133
00:41:48,319 --> 00:41:50,720
concepts of simple chat application that

1134
00:41:50,720 --> 00:41:52,800
allows us to chat with documents using

1135
00:41:52,800 --> 00:41:55,599
vector databases and rag. Most business

1136
00:41:55,599 --> 00:41:58,000
cases in the real world may be slightly

1137
00:41:58,000 --> 00:42:00,560
more complicated. For example, in tech

1138
00:42:00,560 --> 00:42:02,400
corp's case, the business requirement

1139
00:42:02,400 --> 00:42:04,400
might extend to more complex

1140
00:42:04,400 --> 00:42:06,640
requirements like being able to connect

1141
00:42:06,640 --> 00:42:08,800
the agent to human resource management

1142
00:42:08,800 --> 00:42:11,200
system to pull employee documents to

1143
00:42:11,200 --> 00:42:13,119
cross reference and make personalized

1144
00:42:13,119 --> 00:42:15,440
responses. However, lang chain has

1145
00:42:15,440 --> 00:42:17,440
limitations. When business requirements

1146
00:42:17,440 --> 00:42:19,520
become more complex like multi-step

1147
00:42:19,520 --> 00:42:21,599
workflows, conditional branching or

1148
00:42:21,599 --> 00:42:23,599
iterative processes, you need something

1149
00:42:23,599 --> 00:42:25,280
more sophisticated for better

1150
00:42:25,280 --> 00:42:27,440
orchestration. That's where langraph

1151
00:42:27,440 --> 00:42:30,160
becomes essential. Langraph extends lane

1152
00:42:30,160 --> 00:42:32,480
chain to handle more complex multi-step

1153
00:42:32,480 --> 00:42:34,640
workflows that go beyond simple question

1154
00:42:34,640 --> 00:42:37,200
and answer interactions. For example, if

1155
00:42:37,200 --> 00:42:39,119
a customer asks, I need to understand

1156
00:42:39,119 --> 00:42:41,520
our data privacy policy for EU

1157
00:42:41,520 --> 00:42:44,240
customers. Since we assume that inside

1158
00:42:44,240 --> 00:42:46,960
the 500 GB of database, it contains

1159
00:42:46,960 --> 00:42:49,440
details about EU specific regulations,

1160
00:42:49,440 --> 00:42:51,040
we need to create a system that can

1161
00:42:51,040 --> 00:42:53,040
analyze Tech Corp's data privacy

1162
00:42:53,040 --> 00:42:55,200
policies for EU customers, ensuring

1163
00:42:55,200 --> 00:42:57,920
compliance with GDPR, local regulations,

1164
00:42:57,920 --> 00:43:00,160
and company standards. While in a

1165
00:43:00,160 --> 00:43:01,760
traditional software development, you

1166
00:43:01,760 --> 00:43:04,000
need to write code that can sequentially

1167
00:43:04,000 --> 00:43:05,599
and conditionally call different

1168
00:43:05,599 --> 00:43:07,760
sections of the code to process this

1169
00:43:07,760 --> 00:43:10,160
request. With lang graph, this becomes a

1170
00:43:10,160 --> 00:43:12,560
graph where each node handles a specific

1171
00:43:12,560 --> 00:43:15,440
responsibility. For example, node one,

1172
00:43:15,440 --> 00:43:17,280
search and gather privacy policy

1173
00:43:17,280 --> 00:43:19,920
documents. Node two, extract and clean

1174
00:43:19,920 --> 00:43:22,560
document content. Node three, evaluate

1175
00:43:22,560 --> 00:43:26,079
GDPR compliance using LLM analysis. Node

1176
00:43:26,079 --> 00:43:28,160
four, cross reference the local EU

1177
00:43:28,160 --> 00:43:30,640
regulations. And node five, identify

1178
00:43:30,640 --> 00:43:32,240
compliance gaps and generate

1179
00:43:32,240 --> 00:43:34,560
recommendation. A node is an individual

1180
00:43:34,560 --> 00:43:36,960
unit of computation. So think of a

1181
00:43:36,960 --> 00:43:39,040
function that you can call. Once you

1182
00:43:39,040 --> 00:43:41,359
have all the nodes created in langraph,

1183
00:43:41,359 --> 00:43:43,200
you will then need to connect them and

1184
00:43:43,200 --> 00:43:45,920
this connection is called an edge. Edges

1185
00:43:45,920 --> 00:43:48,800
in langraph define execution flow. For

1186
00:43:48,800 --> 00:43:51,040
example, after node one gathers

1187
00:43:51,040 --> 00:43:53,680
documents, the edge routes to node two

1188
00:43:53,680 --> 00:43:56,480
for content extraction. And after node 3

1189
00:43:56,480 --> 00:43:59,200
evaluates compliance, a conditional edge

1190
00:43:59,200 --> 00:44:00,960
either routes to node four for

1191
00:44:00,960 --> 00:44:03,359
additional analysis or jumps to node

1192
00:44:03,359 --> 00:44:06,000
five for report generation. And one

1193
00:44:06,000 --> 00:44:07,920
final concept to keep in mind beyond

1194
00:44:07,920 --> 00:44:10,480
nodes and edges is shared state between

1195
00:44:10,480 --> 00:44:13,359
each node. This is possible by using

1196
00:44:13,359 --> 00:44:15,440
state graph that essentially stores

1197
00:44:15,440 --> 00:44:17,200
information throughout the entire

1198
00:44:17,200 --> 00:44:20,240
workflow. For example, class compliance

1199
00:44:20,240 --> 00:44:23,280
state type dictionary topic string

1200
00:44:23,280 --> 00:44:25,200
documents list of string current

1201
00:44:25,200 --> 00:44:27,359
documents optional string compliance

1202
00:44:27,359 --> 00:44:30,160
score optional integer gaps list of

1203
00:44:30,160 --> 00:44:32,319
string recommendation list of string can

1204
00:44:32,319 --> 00:44:34,960
be used for nodes we identified before.

1205
00:44:34,960 --> 00:44:37,359
As the workflow progresses, each node

1206
00:44:37,359 --> 00:44:39,920
updates relevant state variables. Node

1207
00:44:39,920 --> 00:44:42,079
one populates documents with found

1208
00:44:42,079 --> 00:44:44,560
policy files. Node two processes

1209
00:44:44,560 --> 00:44:46,800
individual documents and updates current

1210
00:44:46,800 --> 00:44:49,359
document. Node 3 calculates compliance

1211
00:44:49,359 --> 00:44:52,800
score. Node 4 identifies gaps. Node 5

1212
00:44:52,800 --> 00:44:54,560
generates recommendation. The state

1213
00:44:54,560 --> 00:44:56,800
graph orchestrates execution based on

1214
00:44:56,800 --> 00:44:59,280
configured flow. If node 3 determines

1215
00:44:59,280 --> 00:45:01,920
compliance score is below 75% the

1216
00:45:01,920 --> 00:45:04,160
conditional edge routes back to node one

1217
00:45:04,160 --> 00:45:06,800
to gather additional documents. If the

1218
00:45:06,800 --> 00:45:10,319
score exceeds 75% execution proceeds to

1219
00:45:10,319 --> 00:45:13,040
node 5 for final report generation. As

1220
00:45:13,040 --> 00:45:14,880
you can see this creates powerful

1221
00:45:14,880 --> 00:45:17,040
capabilities loops for iterative

1222
00:45:17,040 --> 00:45:18,880
analysis conditional branching on

1223
00:45:18,880 --> 00:45:21,119
intermediate results persistent state

1224
00:45:21,119 --> 00:45:23,599
that maintains context across the entire

1225
00:45:23,599 --> 00:45:26,160
workflow. So for Tech Corps compliance

1226
00:45:26,160 --> 00:45:28,880
assistant, Langraph is an essential tool

1227
00:45:28,880 --> 00:45:31,520
for workflow automation. All right,

1228
00:45:31,520 --> 00:45:33,359
let's start with the labs. In this lab,

1229
00:45:33,359 --> 00:45:35,359
we're diving into Langraph, a framework

1230
00:45:35,359 --> 00:45:37,119
designed for building stateful

1231
00:45:37,119 --> 00:45:40,000
multi-step AI workflows. Unlike simple

1232
00:45:40,000 --> 00:45:42,079
chains, Langraph gives us specific

1233
00:45:42,079 --> 00:45:44,560
control over how data moves, letting us

1234
00:45:44,560 --> 00:45:46,960
create branching logic, loops, and

1235
00:45:46,960 --> 00:45:48,880
decision points. By the end of this

1236
00:45:48,880 --> 00:45:50,800
journey, we'll have built a complete

1237
00:45:50,800 --> 00:45:53,119
research assistant that can use multiple

1238
00:45:53,119 --> 00:45:55,520
tools intelligently. We begin with

1239
00:45:55,520 --> 00:45:57,680
environment setup. In this setup, we

1240
00:45:57,680 --> 00:45:59,760
activate the Python virtual environment

1241
00:45:59,760 --> 00:46:01,599
and install the required libraries.

1242
00:46:01,599 --> 00:46:04,480
Langraph itself, Langchain, and OpenAI

1243
00:46:04,480 --> 00:46:06,240
integration. Once everything is

1244
00:46:06,240 --> 00:46:08,400
installed, we run a verification script

1245
00:46:08,400 --> 00:46:10,480
to make sure our setup is ready. With

1246
00:46:10,480 --> 00:46:12,800
the environment ready, we start small.

1247
00:46:12,800 --> 00:46:14,960
Task number one introduces us to

1248
00:46:14,960 --> 00:46:17,040
essential import. We bring in state

1249
00:46:17,040 --> 00:46:19,839
graph end and type dict to define the

1250
00:46:19,839 --> 00:46:21,920
data that flows through the workflow.

1251
00:46:21,920 --> 00:46:24,160
Then we add a simple state field for

1252
00:46:24,160 --> 00:46:26,880
messages. This is the foundation. State

1253
00:46:26,880 --> 00:46:29,520
graph holds the workflow and marks

1254
00:46:29,520 --> 00:46:31,760
completion and the state holds shared

1255
00:46:31,760 --> 00:46:34,720
data. In task number two, we create our

1256
00:46:34,720 --> 00:46:37,119
first nodes. Nodes are just Python

1257
00:46:37,119 --> 00:46:39,760
functions that take state as inputs and

1258
00:46:39,760 --> 00:46:42,319
return partial updates. In this case, we

1259
00:46:42,319 --> 00:46:44,000
define a greeting node and an

1260
00:46:44,000 --> 00:46:46,319
enhancement node. Once connected, one

1261
00:46:46,319 --> 00:46:48,480
node outputs a basic greeting and the

1262
00:46:48,480 --> 00:46:50,400
next node improves it with a bit of a

1263
00:46:50,400 --> 00:46:52,480
flare. This demonstrates how state

1264
00:46:52,480 --> 00:46:54,720
accumulates step by step. Pass number

1265
00:46:54,720 --> 00:46:56,960
three is about edges. The connections

1266
00:46:56,960 --> 00:46:59,359
between nodes. Here we use add nodes and

1267
00:46:59,359 --> 00:47:01,839
add edges to wire greeting nodes to the

1268
00:47:01,839 --> 00:47:04,079
enhancement node. With that, we built

1269
00:47:04,079 --> 00:47:06,560
our first mini workflow. Data flows from

1270
00:47:06,560 --> 00:47:08,880
one function to another. The state

1271
00:47:08,880 --> 00:47:11,280
updates along the way. In task number

1272
00:47:11,280 --> 00:47:13,040
four, we take it further with a

1273
00:47:13,040 --> 00:47:15,599
multi-step flow. We add new nodes like a

1274
00:47:15,599 --> 00:47:17,839
draft step and a review step. Connect

1275
00:47:17,839 --> 00:47:19,920
them and see how the data moves through

1276
00:47:19,920 --> 00:47:22,480
multiple stages. Each step preserves

1277
00:47:22,480 --> 00:47:25,520
states, adds detail and passes it on.

1278
00:47:25,520 --> 00:47:27,760
This mimics real world pipelines where

1279
00:47:27,760 --> 00:47:30,240
content is outlined, drafted and

1280
00:47:30,240 --> 00:47:32,640
polished. Pass number five introduces

1281
00:47:32,640 --> 00:47:34,640
conditional routing. Instead of a fixed

1282
00:47:34,640 --> 00:47:36,560
flow, the system now decides

1283
00:47:36,560 --> 00:47:39,280
dynamically. For example, if the query

1284
00:47:39,280 --> 00:47:41,440
is short, it routes one way. If

1285
00:47:41,440 --> 00:47:44,000
detailed, it routes another. The router

1286
00:47:44,000 --> 00:47:46,079
inspects the state and returns the next

1287
00:47:46,079 --> 00:47:48,720
node name, making workflows flexible and

1288
00:47:48,720 --> 00:47:51,599
adaptive. Then comes task number six,

1289
00:47:51,599 --> 00:47:53,599
tool integration. Here we add a

1290
00:47:53,599 --> 00:47:55,760
calculator tool. The router checks if

1291
00:47:55,760 --> 00:47:58,319
the query is math related. If so, it

1292
00:47:58,319 --> 00:48:00,319
routes to the calculator node which

1293
00:48:00,319 --> 00:48:02,720
computes the answer. This is our first

1294
00:48:02,720 --> 00:48:04,880
glimpse at how Langraph lets us

1295
00:48:04,880 --> 00:48:06,880
integrate specialized tools directly

1296
00:48:06,880 --> 00:48:09,520
into workflows. Finally, task number

1297
00:48:09,520 --> 00:48:11,599
seven puts everything together into

1298
00:48:11,599 --> 00:48:13,760
research agent. We combine the

1299
00:48:13,760 --> 00:48:15,680
calculator with a web search tool like

1300
00:48:15,680 --> 00:48:18,000
duck.go. Depending on the query, the

1301
00:48:18,000 --> 00:48:20,079
system decides whether to perform a

1302
00:48:20,079 --> 00:48:22,720
calculation, run a web search, or handle

1303
00:48:22,720 --> 00:48:25,680
a text normally. This is a dynamic tool

1304
00:48:25,680 --> 00:48:28,079
orchestration, the foundation of modern

1305
00:48:28,079 --> 00:48:30,800
AI agents. By the end of this lab, we've

1306
00:48:30,800 --> 00:48:32,880
gone from simple imports to a fully

1307
00:48:32,880 --> 00:48:34,800
functional research assistant. We've

1308
00:48:34,800 --> 00:48:37,040
seen how to build nodes, connect them,

1309
00:48:37,040 --> 00:48:39,440
design multi-step flows, and add routing

1310
00:48:39,440 --> 00:48:41,920
logic and integrate tools. Some of the

1311
00:48:41,920 --> 00:48:43,760
deeper experiments like chaining more

1312
00:48:43,760 --> 00:48:45,760
advanced tools or refining the router

1313
00:48:45,760 --> 00:48:47,760
logic are left for you to explore on

1314
00:48:47,760 --> 00:48:50,920
your own.

1315
00:48:51,520 --> 00:48:53,200
Now that we covered lang chain and

1316
00:48:53,200 --> 00:48:55,599
langraph and understood how techp

1317
00:48:55,599 --> 00:48:57,440
business requirements can be met by

1318
00:48:57,440 --> 00:48:59,359
leveraging pre-built tools that it

1319
00:48:59,359 --> 00:49:01,760
offers, there's one final piece that's

1320
00:49:01,760 --> 00:49:03,760
been popular since Anthropics released

1321
00:49:03,760 --> 00:49:06,880
back in November 2022 called MCP or

1322
00:49:06,880 --> 00:49:09,760
model context protocol. Techorps AI

1323
00:49:09,760 --> 00:49:11,920
document assistant is working well for

1324
00:49:11,920 --> 00:49:14,160
internal knowledge base, but employees

1325
00:49:14,160 --> 00:49:16,160
might now need to access external

1326
00:49:16,160 --> 00:49:18,640
systems like customer database, support

1327
00:49:18,640 --> 00:49:21,119
systems, inventory management software,

1328
00:49:21,119 --> 00:49:23,839
and other thirdparty APIs. And writing

1329
00:49:23,839 --> 00:49:26,000
custom integrations to all these API

1330
00:49:26,000 --> 00:49:28,000
connections will take a huge amount of

1331
00:49:28,000 --> 00:49:31,040
time. MCP functions like an API, but

1332
00:49:31,040 --> 00:49:32,880
with crucial differences that make it

1333
00:49:32,880 --> 00:49:36,079
perfect for AI agents. Traditional APIs

1334
00:49:36,079 --> 00:49:38,160
expose endpoints that require you to

1335
00:49:38,160 --> 00:49:40,240
understand implementation details

1336
00:49:40,240 --> 00:49:42,480
leading to rigid integrations tied to

1337
00:49:42,480 --> 00:49:45,440
specific systems. MCP doesn't just

1338
00:49:45,440 --> 00:49:47,040
expose tools. It provides

1339
00:49:47,040 --> 00:49:49,680
self-describing interfaces that AI

1340
00:49:49,680 --> 00:49:51,280
agents can understand and use

1341
00:49:51,280 --> 00:49:54,000
autonomously. The key advantage here is

1342
00:49:54,000 --> 00:49:57,119
that unlike traditional APIs, MCP puts

1343
00:49:57,119 --> 00:49:59,359
the burden on the AI agent rather than

1344
00:49:59,359 --> 00:50:02,160
the developer. So when you start an MCP

1345
00:50:02,160 --> 00:50:04,640
server, an instance starts and establish

1346
00:50:04,640 --> 00:50:07,040
a connection with your AI agent. For

1347
00:50:07,040 --> 00:50:09,359
example, the Techorps document assistant

1348
00:50:09,359 --> 00:50:11,839
might easily have these MCP servers to

1349
00:50:11,839 --> 00:50:14,000
enable powerful integration. Let's say

1350
00:50:14,000 --> 00:50:16,240
customer database MCP. When someone

1351
00:50:16,240 --> 00:50:18,720
asks, "What's the status of the order 1

1352
00:50:18,720 --> 00:50:22,240
2 3 4?" The AI uses an MCP to query

1353
00:50:22,240 --> 00:50:24,400
TechCorb's order management system,

1354
00:50:24,400 --> 00:50:25,920
retrieves the current status, and

1355
00:50:25,920 --> 00:50:28,559
provides a complete response. The same

1356
00:50:28,559 --> 00:50:30,800
logic applies for support tickets,

1357
00:50:30,800 --> 00:50:32,960
inventory databases and notification

1358
00:50:32,960 --> 00:50:34,960
system mentioned earlier where we can

1359
00:50:34,960 --> 00:50:37,040
simply plug into existing integrations

1360
00:50:37,040 --> 00:50:40,160
of MCP servers to allow the agent to now

1361
00:50:40,160 --> 00:50:42,880
extend its capabilities. For example, we

1362
00:50:42,880 --> 00:50:45,200
can create a very simple MCP server code

1363
00:50:45,200 --> 00:50:47,359
that looks something like this. Here we

1364
00:50:47,359 --> 00:50:50,079
have fast MCP customer DB that starts

1365
00:50:50,079 --> 00:50:53,359
the MCP server with the name customer DB

1366
00:50:53,359 --> 00:50:56,160
at MCB tool that exposes a function to

1367
00:50:56,160 --> 00:50:59,839
MCP clients. the AI can call like an API

1368
00:50:59,839 --> 00:51:01,839
function parameters and return types

1369
00:51:01,839 --> 00:51:04,400
that tells the MCP client what inputs

1370
00:51:04,400 --> 00:51:06,400
are required and what type of output to

1371
00:51:06,400 --> 00:51:09,040
expect. Finally, customers variable that

1372
00:51:09,040 --> 00:51:11,040
is a fake database in this case stored

1373
00:51:11,040 --> 00:51:13,200
in memory, but in your company's case,

1374
00:51:13,200 --> 00:51:15,119
you can connect this to a SQL database

1375
00:51:15,119 --> 00:51:17,680
or MongoDB or any other custom database

1376
00:51:17,680 --> 00:51:19,839
you might hold customer information on.

1377
00:51:19,839 --> 00:51:21,599
Now, looking at this code might confuse

1378
00:51:21,599 --> 00:51:24,319
you on what MCP really is, since it's

1379
00:51:24,319 --> 00:51:26,400
typically being talked about as a simple

1380
00:51:26,400 --> 00:51:28,559
plugand play, and you're right to think

1381
00:51:28,559 --> 00:51:30,400
that way. The difference here is that

1382
00:51:30,400 --> 00:51:33,119
this MCP server code that's written only

1383
00:51:33,119 --> 00:51:35,200
needs to be written once, and it doesn't

1384
00:51:35,200 --> 00:51:37,359
necessarily have to be you. In other

1385
00:51:37,359 --> 00:51:40,160
words, a community of MCP developers

1386
00:51:40,160 --> 00:51:42,240
might have written custom MCP servers

1387
00:51:42,240 --> 00:51:44,400
for other popular tools like GitHub,

1388
00:51:44,400 --> 00:51:46,800
GitLabs, or SQL databases, and you can

1389
00:51:46,800 --> 00:51:49,200
simply use them directly on your agent

1390
00:51:49,200 --> 00:51:50,559
without having to write the code

1391
00:51:50,559 --> 00:51:53,200
yourself. That's where the power of MCP

1392
00:51:53,200 --> 00:51:56,000
really comes from. In this lab, we're

1393
00:51:56,000 --> 00:51:58,800
going deeper into MCP, model context

1394
00:51:58,800 --> 00:52:00,559
protocol, and learning how to extend

1395
00:52:00,559 --> 00:52:03,040
Langraph with external tools. Think of

1396
00:52:03,040 --> 00:52:06,559
MCP as a universal port like USB that

1397
00:52:06,559 --> 00:52:08,960
allows AI system to connect to any tool,

1398
00:52:08,960 --> 00:52:11,680
database or API in a standardized way.

1399
00:52:11,680 --> 00:52:14,000
With it, our langraph agents can go

1400
00:52:14,000 --> 00:52:16,400
beyond built-in logic and integrate

1401
00:52:16,400 --> 00:52:18,960
external services seamlessly. We begin

1402
00:52:18,960 --> 00:52:21,200
with the environment step. In this step,

1403
00:52:21,200 --> 00:52:23,520
we activate our virtual environment and

1404
00:52:23,520 --> 00:52:26,000
install the key packages. Lang graph for

1405
00:52:26,000 --> 00:52:28,160
the workflow framework, Langchain for

1406
00:52:28,160 --> 00:52:30,240
the core abstractions, and Langchain

1407
00:52:30,240 --> 00:52:32,880
OpenAI for the model integration. The

1408
00:52:32,880 --> 00:52:35,520
setup also prepares for fast MCP, the

1409
00:52:35,520 --> 00:52:37,200
framework we'll use to build MCP

1410
00:52:37,200 --> 00:52:40,160
servers. Once installed, we verify by

1411
00:52:40,160 --> 00:52:42,319
learning the provided script, ensuring

1412
00:52:42,319 --> 00:52:44,720
everything is ready for MCP development.

1413
00:52:44,720 --> 00:52:46,800
Next, we get a conceptual overview of

1414
00:52:46,800 --> 00:52:49,440
the MCP architecture. Here the lab

1415
00:52:49,440 --> 00:52:52,079
explains that the MCP protocol acts as a

1416
00:52:52,079 --> 00:52:54,480
bridge between an AI assistant built

1417
00:52:54,480 --> 00:52:57,119
with Langraph and external tools. The

1418
00:52:57,119 --> 00:52:59,440
flow works like this. The MCP server

1419
00:52:59,440 --> 00:53:02,079
exposes tools and schemas. Langraph

1420
00:53:02,079 --> 00:53:04,240
integrates with them and queries are

1421
00:53:04,240 --> 00:53:06,319
routed intelligently. The naming

1422
00:53:06,319 --> 00:53:10,240
convention MCP server tool ensures

1423
00:53:10,240 --> 00:53:12,079
clarity when multiple tools are

1424
00:53:12,079 --> 00:53:14,640
involved. A helpful analogy is comparing

1425
00:53:14,640 --> 00:53:17,680
MCP to USB devices. A protocol is a

1426
00:53:17,680 --> 00:53:20,319
port. The server is a device. The tools

1427
00:53:20,319 --> 00:53:22,480
are its functions. And Langraph is a

1428
00:53:22,480 --> 00:53:24,960
computer that uses them. That brings us

1429
00:53:24,960 --> 00:53:27,920
to task number one, MCP basics. Here

1430
00:53:27,920 --> 00:53:30,160
we're asked to create our very first MCP

1431
00:53:30,160 --> 00:53:32,880
server. The task involves initializing a

1432
00:53:32,880 --> 00:53:34,960
server called calculator, defining a

1433
00:53:34,960 --> 00:53:37,760
function as a tool with at MCP.tool

1434
00:53:37,760 --> 00:53:40,319
decorator and running it with the SCDIO

1435
00:53:40,319 --> 00:53:42,559
transport. This shows how simple it is

1436
00:53:42,559 --> 00:53:45,040
to expose a structured function as an

1437
00:53:45,040 --> 00:53:47,280
external tool. that langraph can later

1438
00:53:47,280 --> 00:53:49,760
consume. In task number two, we

1439
00:53:49,760 --> 00:53:52,160
integrate MCP with langraph. The

1440
00:53:52,160 --> 00:53:53,760
challenge here is to connect the

1441
00:53:53,760 --> 00:53:55,920
calculator server to an agent. This

1442
00:53:55,920 --> 00:53:58,000
involves configuring the client fetching

1443
00:53:58,000 --> 00:54:00,640
tools from the server create react agent

1444
00:54:00,640 --> 00:54:02,480
that can decide when to call the

1445
00:54:02,480 --> 00:54:06,000
calculator selected when needed. Next,

1446
00:54:06,000 --> 00:54:08,000
task number three scales things up with

1447
00:54:08,000 --> 00:54:10,640
multiple MCP servers. Instead of just a

1448
00:54:10,640 --> 00:54:13,200
calculator, we add another server, in

1449
00:54:13,200 --> 00:54:15,280
this case, a weather service. Now,

1450
00:54:15,280 --> 00:54:17,760
Langraph orchestrates between both. The

1451
00:54:17,760 --> 00:54:19,599
system retrieves available tools,

1452
00:54:19,599 --> 00:54:21,599
creates an agent with access to both

1453
00:54:21,599 --> 00:54:23,680
servers, and intelligently routes

1454
00:54:23,680 --> 00:54:26,480
queries. If a user asks a math question,

1455
00:54:26,480 --> 00:54:28,800
the calculator responds. If they ask

1456
00:54:28,800 --> 00:54:30,559
about the weather, the weather tool

1457
00:54:30,559 --> 00:54:32,720
responds. This is where we see the true

1458
00:54:32,720 --> 00:54:35,280
power of MCP. Multiple servers are

1459
00:54:35,280 --> 00:54:37,520
working together under a unified AI

1460
00:54:37,520 --> 00:54:39,839
agent. The lab wraps up by celebrating

1461
00:54:39,839 --> 00:54:43,040
MCP mastery. By now, we've created MCP

1462
00:54:43,040 --> 00:54:45,280
servers, integrated them with ElangRaph,

1463
00:54:45,280 --> 00:54:47,680
and orchestrated multiple tools. The key

1464
00:54:47,680 --> 00:54:50,640
takeaways are that MCP is universal. It

1465
00:54:50,640 --> 00:54:53,440
can connect any tool to any AI. Routing

1466
00:54:53,440 --> 00:54:55,760
is what gives it power. The design is

1467
00:54:55,760 --> 00:54:57,760
extendable, so we can add servers

1468
00:54:57,760 --> 00:55:00,720
anytime. Some deeper explorations like

1469
00:55:00,720 --> 00:55:03,760
exposing databases, APIs or file systems

1470
00:55:03,760 --> 00:55:05,839
through MCP are left for you to explore

1471
00:55:05,839 --> 00:55:07,839
on your own. That concludes this

1472
00:55:07,839 --> 00:55:10,000
narration. Next, we'll continue the

1473
00:55:10,000 --> 00:55:12,000
journey by experimenting with resource

1474
00:55:12,000 --> 00:55:13,920
exposure, human in the loop approval

1475
00:55:13,920 --> 00:55:15,760
flows, and eventually deploying

1476
00:55:15,760 --> 00:55:19,040
production ready MCP packages.

1477
00:55:19,040 --> 00:55:20,720
Now that we have put all these pieces

1478
00:55:20,720 --> 00:55:22,960
together like context windows, vector

1479
00:55:22,960 --> 00:55:26,079
databases, lang chain, langraph, MCP,

1480
00:55:26,079 --> 00:55:28,559
and prompt engineering, Techorp is now

1481
00:55:28,559 --> 00:55:30,880
able to do complex document search that

1482
00:55:30,880 --> 00:55:32,800
went from manual searching that could

1483
00:55:32,800 --> 00:55:35,200
have taken up to 30 minutes to now less

1484
00:55:35,200 --> 00:55:38,079
than 30 seconds using our AI agent. And

1485
00:55:38,079 --> 00:55:40,559
we also have a higher accuracy using

1486
00:55:40,559 --> 00:55:42,800
contextaware semantic search like using

1487
00:55:42,800 --> 00:55:45,280
rag. And finally, the chat application

1488
00:55:45,280 --> 00:55:47,440
UI allows users to have more

1489
00:55:47,440 --> 00:55:49,760
satisfaction in working with a tool that

1490
00:55:49,760 --> 00:55:51,520
can help keep track of conversation

1491
00:55:51,520 --> 00:55:54,319
history and better intuition overall.

1492
00:55:54,319 --> 00:55:57,359
And the availability for this is 24/7 as

1493
00:55:57,359 --> 00:55:59,599
long as the application is running. And

1494
00:55:59,599 --> 00:56:01,839
this is just the beginning. Imagine

1495
00:56:01,839 --> 00:56:03,839
layering on predictive analytics,

1496
00:56:03,839 --> 00:56:05,839
proactive compliance agents, and

1497
00:56:05,839 --> 00:56:07,839
workflow automation that doesn't just

1498
00:56:07,839 --> 00:56:09,920
answer questions, but actively solves

1499
00:56:09,920 --> 00:56:12,400
problems before employees can even ask.

1500
00:56:12,400 --> 00:56:14,559
The shift from static documents to

1501
00:56:14,559 --> 00:56:16,799
living intelligent system marks a

1502
00:56:16,799 --> 00:56:18,960
turning point not just for Tech Corp,

1503
00:56:18,960 --> 00:56:20,960
but for how every other business can

1504
00:56:20,960 --> 00:56:23,200
unlock a full value of its knowledge

1505
00:56:23,200 --> 00:56:26,520
using agents.
