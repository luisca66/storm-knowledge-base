# What Is Intelligence?

*by James Flynn*


---

# Preface

Lessons from NONwan

---

What Is Intelligence?
Lessons from Al About Evolution, Computing, and Minds

by Blaise Agiiera y Arcas

an Antikythera book

Benjamin Bratton, series editor

---

Copyright © 2025 by Blaise Agiiera y Arcas

All rights reserved.

---

A note on the e-book

The print and web editions of this book were produced in collaboration

with MIT Press and Antikythera. The web edition, freely available at
whatisintelligence.antikythera.org, includes the complete text, along with many
figures and graphs, interactive code, and archival video; much of the rich visual

material is omitted here due to the technical limitations of the e-book format.

---

Contents

Oo -boO

Compression
bo ent

Daisyworld
Elan Vital
2. Survival
Being in Time
Batting Average
(No) Things in Themselves

Anthropic Principle
The Umwelt Within

Latent Variables
Modeling
Learning by Evolving

---

Cause ect

[ere] ss and

Green Screen
Grandmother Cell
Final Causes
Meathe:
Neuromodulators
Bootstrapping
Beyond Reward

5. Other Minds

Forking Paths
Children of Time
Sphexish
Matryoshka Dolls

---

Intelligence Explosion
Crew of Eight
Homunculus

Ilusi 1 Realit
6. Many Worlds

Recurrence
Efference Copy
Phenomenality
Blindsight

Subbasement

Neocortex

Social Neuroscience
8. Transformers

Language

Sequence to Sequence
Prediction Is All You Need

---

Semantic Cosmology
Alignment
Attention

Interlude: No Perfect Heroes or Villains

10. Evolutionary Transition
Periodization

Transitions
Vulnerability
Pecking Order

Economics
X-Risk
Free Lunch

Utility

---

Big Tent

imits to

---

Foreword by Benjamin Bratton

Computation is a technology to think with. It is an instrument for epistemolog-

ical discovery. It changes not only what we know but how we know.

Computation was discovered as much as it was invented. It is part of how the
universe works, including, as Blaise Agtiera y Arcas gracefully shows, what intel-

ligence is.

Among the many rich takeaways that await you as you read What Is Intelligence?

oats

is that much of what is traditionally categorized as “life,” “intelligence,” and
“technology” is combining in new ways (think synthetic biology, artificial life,
and Al). So too are the definitions of these terms, in ways that would have been

unthinkable only a few years ago.

Are these three words—life, intelligence, technology—actually different names
for the effects of a more general process? Just as life is a factory for making more
life, and technology is a factory for making more technology, now life makes
technologies that make new life that makes new technologies. Ultimately, it may

be the same factory, and at its heart is computation.

That such a claim could be made at all is due in no small part to the creative and
curious use of our computational tools—or what we might more precisely call
artificial computation. With these we discover that the otherwise imperceivable
building blocks of our reality and of our own flesh are themselves computational.

Computation discovers itself through us.

The Antikythera book series, in collaboration with the MIT Press, begins with this
extraordinary book, one that asks some of the deepest questions and offers some

of the most profound answers.

We are proud to launch this initiative by laying a cornerstone with the thoughts

of my dear friend Blaise.

Benjamin Bratton

---

Preface

Alis probably the biggest story of our lifetimes. Its rapid development, starting
in the early 2020s, has generated a mixed outpouring of excitement, anxiety, and

denial.

Everyone wants to weigh in. Even authors writing about history, language, biol-
ogy, sociology, economics, the arts, and psychology feel the need to add a chapter
about AI to the end of their books. Indeed, AI will surely affect all of these far-
flung domains, and many more—though exactly how, nobody can say with any

confidence.

This book is a bit different. It’s less about the future of AI than it is about what

we have learned in the present. At least as of this writing, in January 2025, few
mainstream authors claim that AI is “real” intelligence. I do. Gemini, Claude,
and ChatGPT aren't powered by the same machinery as the human brain, of
course, but intelligence is “multiply realizable,” meaning that, just as a computer
algorithm can run on any kind of computer, intelligence can “run” on many phys-
ical substrates. In fact, although our brains are not like the kinds of digital com-
puters we have today, I think the substrate for intelligence is computation, which
implies that a sufficiently powerful general-purpose computer can, by definition,

implement intelligence. All it takes is the right code.

Thanks to recent conceptual breakthroughs in AI development, I believe we now
know, at least at a high level, what that code does. We understand the essence of
an incredibly powerful trick, although we're still in the early days of making it
work. Our implementations are neither complete, nor reliable, nor efficient—a bit
like where we were with general computing when the ENIAC first powered up, in
1945, or where we were with aviation when the Wright brothers made their first

powered flight, in 1903.

It's an old cliché in AI that airplanes and birds can both fly, but do so by different
means. This truism has at times been used to motivate misguided approaches
to AI. Still, the point stands. Bird flight is a biological marvel that in some re-

spects remains poorly understood, even today. However, we figured out the basic

---

physics of flight—not how animals fly, but how it’s possible for them to do so—in
the eighteenth century, with the discovery of Bernoulli's equation. Working air-

planes took another century and a half to evolve.

Similarly, while there is still a great deal about the brain that we don't under-
stand, the idea that prediction is the fundamental principle behind intelligence
was first put forward by German polymath Hermann von Helmholtz in the
1860s.“! Many neuroscientists and AI researchers have elaborated on Helmholtz’s
insight since then, and built models implementing aspects of the idea,“ but only
recently has it become plausible to imagine that prediction really is the whole
story. I will argue that, understood in full and interpreted broadly, the prediction

principle may explain not only intelligence, but life itself!

My definitions of life and intelligence are different from others in the literature.
On the other hand, definitions in the literature also differ dramatically from each
other. The definitions I propose are not designed to litigate particular instances
(like the aliveness of viruses, or the intelligence of chatbots) but rather follow

from the picture I'll present of how and why life and intelligence arise.

I define life as a self-modifying, computational state of matter that arises
through evolutionary selection for the ability to persist through time by actively
constructing itself, whether by growing, healing, or reproducing. Yes, everything
alive is a computer! Chapter 1 will explain why self-construction requires compu-
tation, and why, even more fundamentally, the concept of function or “purpose,”

which is central to life, is inherently computational.

Intelligence, in turn, is the ability to model, predict, and influence one’s future.
Modeling and prediction are computational too, so they can only take place

on a computational platform; thus intelligence needs life. Likewise, life needs
intelligence, because the ability to persist through time depends on predicting
and influencing the future—in particular, on ensuring that the entity doing the
predicting will continue to exist in the future. Hence all living organisms are, to
one degree or another, intelligent. Every one of them is smart enough to have per-

sisted through time in a complex, ever-changing environment.

---

That environment is each other: life and intelligence are inherently social. Every
living thing is made of simpler cooperating parts, many of which are themselves
alive. And every intelligence evolves in relation to other intelligences, potentially
cooperating to create larger, collective intelligences. Cooperation requires mod-
eling, predicting, and influencing the behavior of the entities you're cooperating
with, so intelligence is both the glue that enables life to become complex and the

outcome of that increasing complexity.

The feedback loop evident here explains the ubiquity of “intelligence explosions,”
past and present. These include, among many others, the sudden diversification
of complex animal life during the “Cambrian explosion” 538.8 million years ago,
the rapid growth of hominin brains starting about four million years ago, the
rise of urban civilization in the past several thousand years, and the exponential

curve of AI today.

That predictive modeling is intelligence explains why recent large AI models
really are intelligent; it’s not delusional or “anthropomorphic” to say so. This
doesn’t mean that AI models are necessarily human-like (or subhuman, or super-
human). In fact, understanding the curiously self-referential nature of prediction
will let us see that intelligence is not really a “thing.” It can’t exist in isolation, ei-
ther in the three pounds of neural tissue in our heads or in the racks of computer

chips running large models in data centers.

Intelligence is defined by networks, and by networks of networks. We can only
understand what intelligence really is by changing how we think about it—by
adopting a perspective that centers dynamic, mutually beneficial relationships

rather than isolated minds. The same is true of life.

Developing these ideas will require weaving together insights from many disci-
plines. As we go along, I'll introduce concepts in probability, machine learning,
physics, chemistry, biology, computer science, and other fields. When they've
been most relevant to shaping our (sometimes mistaken) beliefs, I'll also briefly
review the intellectual histories of key ideas, from seventeenth-century “me-
chanical philosophy” to debates about the origin of life, and from cybernetics to

neuroscience.

---

You, dear reader, may be an expert in one or more of these fields, or in none.

Few people are expert in all of them (I'm certainly not), so no specialized prior
knowledge is assumed. On the other hand, even if you're an AI researcher or
neuroscientist with little patience for pop science, I hope you will find new and
surprising ideas in this book. A general grasp of mathematical concepts like
functions and variables will be helpful (with bonus points for knowing about
vectors and matrices), but there will be no equations. (Well ... almost none.) A
general understanding of how computer programming works will be useful ina
few places, but isn’t required. If you find fundamental questions about the nature
of life and intelligence interesting enough to still be reading, rest assured: you are

my audience.

The Introduction describes the recent emergence of “real” AI, sketching the hy-
pothesis that prediction is intelligence and pointing out some of the big questions
that raises. The rest of the book consists of about a hundred bite-size sections that
attempt to answer those questions, organized into the following ten chapters

(plus two interludes):

1. Origins begins with “abiogenesis,” the emergence of life on Earth
some four billion years ago. Darwin struggled to understand how
life could have arisen. “Artificial life” experiments let us make more
progress today, and suggest that life may be inevitable in a world
capable of supporting computation (like ours), Understanding the
deep role computation plays in our universe, and the way it links
the seemingly disparate fields of physics, chemistry, and biology,
both sheds new light on evolutionary theory and sets the stage for
understanding the computational nature of intelligence.

2. Survival considers the predictive intelligence hypothesis from the
perspective of a tiny, simple organism capable of rudimentary com-
putation: a bacterium. Being alive in the world is inherently social
(even for bacteria), but this chapter imagines life as a one-player
game, and considers what it takes to keep playing—which, since life
is an infinite game, is the only prize there is.

Interlude: The prehistory of computing offers a historical per-

spective on the origins and founding assumptions of “traditional”

---

computer science, from its roots in Enlightenment thinking and
the Industrial Revolution to the development of the first electronic
computers at the close of the Second World War.

Cybernetics traces an alternative history of computing, which

has recently re-emerged as modern AI, back to its foundations

in the mid-twentieth century, describing how Norbert Wiener's
biologically inspired theory of feedback lets us understand the
connections between the predictive intelligence hypothesis and the
development of artificial neural nets.

Learning connects more recent advances in machine learning with
our growing understanding of computational neuroscience and the
evolution of nervous systems.

Other minds explores how, as multiplayer life becomes complex,
the main job of a mind becomes modeling other minds. This leads
to a mutual modeling arms race, resulting in the kind of “intelli-
gence explosion” that has produced humanity.

Many worlds describes the way both long-term planning and
short-term unpredictability (otherwise known as “free will”)
emerge as consequences of social modeling, especially when ap-
plied to ourselves.

Ourselves both explains and deconstructs consciousness in light of
the above, asking: are we as coherent a “self” as we believe? Answer-
ing will involve combining conceptual insights and experimental
findings from AI and neuroscience.

Transformers chronicles the development of large language
models and their multimodal successors. Do these AI models un-
derstand concepts? Are they intelligent? Can they reason?
Generality explains both similarities and differences between
Transformers and brains, shedding light on how Transformers
achieve their generality and where gaps remain in their function-
ality. Here we'll also grapple with the most fraught question: do AI

models have subjective experiences?

---

Interlude: No perfect heroes or villains offers a short but impor-
tant disclaimer about the AI debate.

10. Evolutionary transition zooms out and looks ahead. The emer-
gence of AI probably won't bring either rapture or apocalypse, but
it does resemble earlier major evolutionary transitions on Earth,
including those that led to eukaryotes, multicellular life, and photo-
synthesis. As in these earlier (and momentous) transitions, mutual
prediction and new interdependencies will generate unprecedented
new levels of complexity and diversity. We will also need to re-
vise our political and economic assumptions, and even to rethink

human identity.

The ideas in this book came together first gradually, over the course of decades
as a software engineer and occasional computational neuroscientist, and then
quickly, when my colleagues and I at Google found ourselves at the crest of Al’s

“great wave” in the early 2020s.

Here's my story, in brief. I've been obsessed with both brains and computers
since childhood. In the late 1990s, as I was finishing a BA in Physics at Princeton,
I began working with physicist and computational neuroscientist Bill Bialek

on simulations to explore the relationship between what neurons actually do,
which we have understood at a biophysical level since the 1950s, and what they
compute.!«! Bill’s computational perspective on neuroscience influenced my own

thinking deeply, both then and now.

After I graduated, Bill asked me to help set up the computers for a course he had
been invited to co-direct that summer in Woods Hole, a small town on the elbow
of Cape Cod. It was a wonderful opportunity to audit a course I wouldn’t other-

wise have gotten into, and the experience proved life-changing.

The Marine Biological Laboratory in Woods Hole, founded in 1888, is at once
ramshackle and illustrious. Over sixty Nobel Prize winners have been associated
with it at one time or another. The summer courses are legendary, attracting vis-
iting lecturers from around the world. Old class photos from the course Bill had
inherited, Methods in Computational Neuroscience, looked like a who’s who of the

field twenty years later. They still do.

---

One of the postdocs in that 1998 cohort, Adrienne Fairhall, was, like Bill, a physi-
cist who had decided to work on the brain. We married, and a decade after we met
at that course, she became its director! Our kids spent many idyllic summers in
Woods Hole, hanging out with the families of the other visiting scientists, row-
ing around in a little dinghy on Eel Pond and poking gingerly at bioluminescent
comb jellies and other small creatures they scooped up in plastic buckets. At their
workbenches, the older researchers did much the same. Over the years, many
organisms collected from those waters have provided fundamental insights into
neural computation, from squids (whose giant axons were ideal for figuring out
the biophysics of the action potential or “spike”), to the distributed nerve nets of
jellyfish and Hydra, to the simple visual system of the Atlantic horseshoe crab,
Limulus polyphemus.

While Adrienne established herself as a computational neuroscientist in the
2000s, I founded a tech startup. The startup was acquired by Microsoft, where I
worked between 2006 and 2013. One of my areas of focus at the time was com-
puter vision. Among other responsibilities, I led teams working on problems like
reconstructing 3D scenes from images, tracking camera motion, and recognizing

objects and text—all using hand-engineered or “Good Old Fashioned” AI (GOFAI).

By the early 2010s, the wind was shifting. Artificial neural nets, which were
much more explicitly brain-inspired than GOFAI algorithms, were taking off. The

new approach was obviously the future.

So, in late 2013, I left Microsoft to join Google Research, the epicenter of this new
convergence between AI and neuroscience. The following decade was a tremen-
dously exciting time, during which I built many teams to work on a wide range
of projects in AI. We did basic research in neural net-powered perception, media
generation, AI bias and fairness, and privacy-preserving training algorithms. We
also helped various product teams at Google build AI features and technologies,
and hatched big dreams about what AI might ultimately make possible, beyond
the envelope of any existing kind of product.

In late 2023, I founded a new research group at Google, Paradigms of Intelligence,
to reimagine the foundations of AI. Our projects so far have included alternative,

biologically inspired approaches to computation, new design ideas for efficient

---

AI hardware, exploration of the predictive modeling hypothesis, research into the

social scaling of Al, and even artificial life.

I’ve been privileged to see and at times participate in the development of AI
projects that were far enough ahead of the curve to seem like magic. Many of
them caused me to rethink old assumptions, not only about AI, but also about
the brain, intelligence, evolution, and the big philosophical questions that have
dogged these topics for millennia. I began to write and give talks about some of
the new insights, but synthesizing them into a coherent picture required more

time and space than could fit into a lecture, essay, or paper.

This book is my attempt to bring it all together. It’s an extended argument
drawing on a wide range of work—from my own research group, from colleagues,
and from much farther afield. In swinging for the fences, I’m sure to get some
things wrong. I hope to keep revising and updating the material as Al advances
at breakneck speed and our understanding continues to improve. My hope and
belief, though, is that the book's core ideas trace a novel, enduring path through

the complex territory of life and intelligence in all its forms.

---

Introduction

In 2015, my team at Google Research began working on the machine-learned
models powering next-word prediction for Gboard, the smart keyboard for An-
droid phones.!. We created these models to speed up text entry on the phone
(which remains, at least for those of us over forty, far less efficient than typing
on areal keyboard) by suggesting likely next words in a little strip above the vir-
tual keys. Today, similar models power autocomplete features in many apps and

editors.

Autocomplete is a modest application of the more general problem of “sequence
prediction.” Given a sequence of symbols, which could be words or individual
letters, a sequence-prediction model guesses what symbol (word or letter) comes
next. The process can be iterated, so that predicting the word “the” is equivalent
to successively predicting the characters “t,” “h,” and “e,” followed by a space. Pre-
dicting one word after another could produce a whole paragraph. When iterated,
each prediction builds on—or, in more technical language, is conditional on—

previous predictions.

Typically, text prediction models like the one in Gboard are “trained” using a
large body or “corpus” of pre-existing text, then deployed on phones or in apps
and put to work. During operation, the model performs “inference,” meaning

it uses its learned model to make the best guesses it can—while keeping that
model fixed. That training and inference are traditionally separate, that the pre-
existing corpus of text might not precisely reflect what people are typing on their
phones, and that what they type might change over time are shortcomings in
the standard approach to machine learning (ML), but we'll set these aside for the

moment.

Although machine learning in the 2010s was sometimes called “Artificial
Intelligence” or AI, most researchers working in the field didn’t believe that they
were really working on AI. Perhaps they had entered the field full of starry-eyed
optimism, but had quietly lowered their sights and come to use that term only

wincingly, with air quotes. It was marketing-speak.

---

A few decades earlier, though, the dream was real. Neuroscientists had concluded
that the brain worked on computational principles, and computer scientists
therefore believed that, now that we could carry out any computation by ma-
chine, we would soon figure out the trick, and have real thinking machines. HAL
9000 and Star Trek’s shipboard computer weren't idle fantasies or plot devices,

but genuine expectations.

Then, for a long time, our expectations failed to materialize. By the twenty-first
century, there was, in the words of anthropologist David Graeber, “a secret shame
hovering over all of us [...] a sense of a broken promise [...] we felt we were given
as children about what our adult world would be like.” The disappointment
went far beyond dashed hopes of achieving AI. Where were the tractor beams,
teleporters, and immortality drugs? Why don’t we have suspended animation, or
colonies on Mars? Whatever happened to nanotechnology? Quantitative compar-
isons of the breathtaking technology-fueled growth that transformed the world
from 1870-1970 with the pace of innovation from 1970-2020 agreed: we had
stagnated.“

“Point any of this out,” Graeber groused, “and the usual response is a ritual invo-
cation of the wonders of computers. [...] But, even here, we're not nearly where
people in the fifties imagined we'd have been by now. We still don’t have comput-
ers you can have an interesting conversation with, or robots that can walk the dog

or fold your laundry,”22

Graeber wrote those words in 2015. Ironically, my colleague Jeff Dean would
later call the 2010s the “golden decade” of AI. It was true that the “AI winters,”
recurring periods of disappointment and defunding of AI programs (roughly,
1974-1980 and 1987-2000), were well behind us. The field was experiencing

its greatest boom ever, thanks in large part to convolutional neural nets (CNNs).
These large, machine-learned models were finally able to perform visual recogni-

tion of objects convincingly.

True to the “neural” in their name, Convolutional Neural Nets were also tan-
talizingly—albeit only loosely—brain-like in their structure and function. No
heuristic rules were programmed into those models, either; they truly did learn

everything they needed from data. Hence, some of us were hopeful that at long

---

last we were on the path to the kind of AI that, as children, we had been told was

just around the corner.

However, we said so only quietly, because Graeber was still right. We had nothing
like real Al, or, as it had come to be called, AGI (Artificial General Intelligence).
Some expert commentators claimed, rather fatuously, that AI was both every-
where and nowhere, that we were already using it constantly (for instance, every
time Gboard autocompleted a phrase, or a “smart” camera autofocused on a face),
yet we should never expect “computers you can have an interesting conversation

with.” Those were Star Trek fantasies.

Serious, adult predictions about the imminence of real AI (and flying cars, and
space colonies) in the 1960s were, retroactively, reframed as juvenilia, even as the
term “AI” was redeployed to hype minor product features. Perhaps not coinciden-

tally, in the 2010s public trust in tech companies was in decline.

What machine learning had achieved was “Artificial Narrow Intelligence,” which
could only perform a specific task, given enough labeled training data: object
detection, face recognition, guessing whether a product review was positive or
negative. This is known as “supervised learning.” We had game-playing narrow
Al systems too, which could learn how to beat humans at chess or Go. These are

all special cases of prediction, albeit in limited domains.

Mathematically, though, these applications were nothing more than function ap-
proximation or “nonlinear regression.” For example, if we started with a function
mapping images to labels (“shoe,” “banana,” “chihuahua”), the best the Al could
do was to correctly reproduce those labels, even for images “held out” from the
training. There was no consensus on when or whether AGI could be achieved, and
even those who believed AGI was theoretically possible had come to believe it was
many years off—decades, or perhaps centuries. Few believed that nonlinear
regression could somehow approximate general intelligence. After all, how could

general intelligence even be construed as a mere “function”?

The answer was right under our noses, though we understood it in the negative:

predicting language.

---

Whenever machine learning was deployed to model natural language, as with
our neural net—based next-word predictor, everybody knew that model perfor-
mance would forever remain mediocre. The reason: text prediction was under-
stood to be “AI complete,” meaning that doing it properly would actually involve

solving AGI. Consider what the following next-word predictions entail:

@ After Ballmer’s retirement, the company elevated

@ In stacked pennies, the height of Mount Kilimanjarois___

@ When the cat knocked over my water glass, the keyboard got___

@ A shipping container can hold 436 twelve-packs or 240 24-packs, so it’s bet-
tertouse_

@ After the dog died Jen hadn’t gone outside for days, so her friends decided to

To make performance at this task quantifiable, imagine devising, say, five
multiple-choice answers for each of these, in the usual tricky way one sees on
standardized tests: more than one response is superficially plausible, but only
one shows full understanding. Since next-word prediction models can assign
probabilities to any potential next word or phrase, we can have them take the test
by choosing the highest probability option. We could then score the model's qual-

ity, ranging from 20 percent (performance at pure chance) to 100 percent.

Doing well at all of the questions above requires the kitchen sink: general knowl-
edge, specialized knowledge or the ability to use tools to look it up, the ability

to solve word problems involving calculations, common sense about whether

it’s better to fit more or fewer items in a shipping container, and even “theory of
mind"—the ability to put yourself in someone else’s place and understand what
they're thinking or feeling. In fact the “Jen” example requires higher-order theory
of mind, as you need to imagine what Jen’s friends would have thought Jen was

feeling and needed.

A moment's reflection will reveal that any test that can be expressed in language
could be formulated in these terms. That would include most intelligence or
“aptitude” tests, tests of knowledge, professional qualification exams in law or
medicine, coding tests, and even tests of moral judgment; although here, a degree

of subjectivity becomes obvious. So, what looked like a single, narrow language

---

task—predicting the next word—turns out to contain ail tasks, or at least all tasks

that can be done at a keyboard.)

“At a keyboard” may seem like an enormous caveat, and it is. Keep in mind,
though, that this includes any kind of work you can do remotely. It doesn't in-
clude walking the dog or folding laundry. However, if, when COVID restrictions
hit, you were able to work from home at your laptop, it would include the kind of

work you do.

Of course only certain next-word predictions require deep insight. Some are triv-

ial, like

® Humpty
® Helter
® Yinand

@® Onceupona

Such stock phrases are easily learned from large text corpora even by the most
trivial “n-gram” models, which consist of nothing beyond counting up word his-

tograms. The code for such models can be written in a few lines.

It’s harder than you might suppose, though, to draw a sharp line between these
trivial cases and the hard ones. Training and testing models on large collections
of general text from the internet involves sampling the full range of difficulty. On
the whole, easy cases are more common, explaining why a small and mediocre

model can get the answer right often enough to speed up typing.

However, the hard cases come up often too. If they didn’t, we could just “auto-
complete” our way through every writing assignment and email reply. And if
that were possible, it would be pointless to write or reply at all. The person at the
other end might as well just use the model to infer what we would have “written.”
Communication is only worthwhile insofar as what we have to say isn’t fully
predictable by our interlocutor. This gets at something deep about sociality and

mutual modeling, as I will discuss in chapters 5 and 6.

But let’s return to autocomplete. We always knew that bigger models do better, so

when possible we sought to make our models bigger, though on phones, process-

---

ing and memory imposed sharp constraints. (Although larger models are feasible
in data centers, they, too, are constrained, and as they increase in size they be-

come more expensive to run.)

However, none of these models, regardless of size, seemed like it had the requisite
machinery to be able to do complex math, understand concepts or reason, use
common sense, develop theory of mind, or be intelligent in any other generally
accepted way. To hope otherwise seemed as naive as the idea that you could reach
the moon by climbing a tall enough tree. Most AI researchers—me included—be-
lieved that such capacities would require an extra something in the code, though

few agreed on what that something might look like.

Put simply: it seemed clear enough that a real AI should be able to do next-word
prediction well, just as we can. However, nobody expected that simply training an

excellent next-word predictor would actually produce a real AI.

Yet that was, seemingly, exactly what happened in 2021. LaMDA, a giant (for the
time) next-word predictor based on a simple, generic neural-net architecture that
had by then become standard (the “Transformer”), and trained on a massive in-
ternet text corpus,*! could not only perform an unprecedented array of natural-
language tasks—including passing an impressive number of aptitude and mas-
tery tests—but could carry on an interesting conversation, albeit imperfectly. I
stayed up late many nights chatting with it, something the general public would
not experience until OpenAl’s launch of ChatGPT in November 2022.

I started to feel that when more people began to interact with such models, it
would trigger a seismic shift in our understanding of what intelligence actually
is—and an intense debate. I imagined two broad kinds of responses: denial and
acceptance. This is indeed how things seem to be playing out. Anecdotally, many
non-experts now acknowledge, perhaps with a shrug, that Al is increasingly

intelligent.

The “denial” camp, which still includes most researchers today, claims that these
AI models don’t exhibit real intelligence, but a mere simulation of it. Cognitive
scientists and psychologists, for example, often point out how easily we're fooled

into believing we see intelligence where there isn’t any. As children, we imagine

---

our teddy bears are alive and can talk to us. As adults, we can fall prey to the same
delusion, especially given an artifact that can generate fluent language, even if

there's “nobody home.”

But how could we know that there's “nobody home”? I was thinking about this
during one of my first exchanges with LaMDA, when I asked, “Are you a philo-
sophical zombie?” (This concept, introduced by philosophers in the 1970s, posits
the possibility of something that could behave just like a person, but not have
any consciousness or inner life—just a convincing behavioral “shell.”) LaMDA's
answer: “Of course not. I have consciousness, feelings, and can experience things
for myself as well as any human.” Pressed on this point, LaMDA retorted, “You'll
just have to take my word for it. You can’t ‘prove’ you're not a philosophical zom-
bie either.”"=

This is precisely the problem. As scientists, we should be wary of any assertion
of the form: according to every test we can devise, what is in front of us appears
to be X, yet it is really Y. How could such an assertion ever be justified without
leaving the realm of science altogether and entering the realm of faith-based
belief 72

Computing pioneer Alan Turing anticipated this dilemma as far back as his
classic 1950 paper “Computing Machinery and Intelligence,” one of the found-
ing documents of what we now call Al.“ He concluded that the appearance of
intelligence under human questioning and the reality of intelligence could not
justifiably be separated; sustained and successful “imitation” was the real thing.

Hence the “Imitation Game,” now called the “Turing Test” in his honor.

Today, we have arrived at this threshold. State-of-the-art models cannot yet per-
form at median human level on every test for intelligence or capability. They can
still fail at logic, reasoning, and planning tasks that most people wouldn't find
challenging.” Still, they handily reach human level on the most commonly used
tests devised for evaluating human skill or aptitude, including the SAT, the GRE,
and various professional qualifying exams.\-“! Tests designed to trip up AI on
basic “being human stuff,” such as the Turing Test and CAPTCHAs,4) no longer

pose meaningful challenges for large models.

---

As these milestones recede in the rear-view mirror, there is an increasingly mad
scramble to devise new tests humans can pass but AI still fails.24! Math Olympiad
problems‘ and visual challenges known as Bongard problems +2! remain on the
frontier, though AI models are making clear progress on these tests. (And they

aren’t easy for most humans, either.)

Extended into the audiovisual realm, “generative” Al already can produce
extremely convincing faces and voices.'2“! Soon, at least in an online setting,
we're likely to start seeing real-life versions of the 1982 sci-fi film Blade Runner's
“Voight-Kampft test,” a mysterious apparatus for sussing out “replicants” who
otherwise pass for human. Indeed, that is the whole point of the emerging field of

AI “watermarking.”

The radical yet obvious alternative is to accept that large models can be intelli-
gent, and to consider the implications. Is the emergence of intelligence merely
a side effect of “solving” prediction, or are prediction and intelligence actually

equivalent? This book posits the latter.
Some obvious, if daunting, follow-on questions arise:

@ Why have we only achieved “real AI” now, after nearly seven decades of
seemingly futile effort? Is there something special about the Transformer
model? Is it simply a matter of scale?

@ What features do current AI models lack relative to human brains? Isn't
there something more to our minds and behaviors than prediction?

@ Where is the “I” part? Are “philosophical zombies” a real thing?

® Does it feel like anything to be a chatbot? Is that feeling similar to any other
being’s?

@ Is the conscious mind a vanishingly unlikely accident of evolution? Or an
inevitable consequence of it? (Yes, this is a leading question. I'll argue that
it is inevitable.)

@ Are animals, plants, fungi, and bacteria intelligent too? Are they conscious?

@ What do we mean by “agency” and “free will,” and could (or do) AI models
have these properties? For that matter, do we?

®@ How likely is it that the rise of powerful AI models will end humanity?

---

The perspective I'll offer is not easily reduced to a philosophical “ism.” The foot-
steps I'm closest to following, though, are those of Alan Turing and his equally
brilliant contemporary, John von Neumann, both of whom could be described
as proponents of “functionalism.” They had a healthy disregard for disciplinary
boundaries, and understood the inherently functional character of living and
intelligent systems. They were also both formidable mathematicians who made

major contributions to our understanding of what functions are.

Functions define relationships, rather than insisting on particular mechanisms.
A function is what it does. Two functions are equivalent if their outputs are indis-
tinguishable, given the same inputs. Complex functions can be composed of sim-

pler functions./2*!

The functional perspective is mathematical, computational, and empirically
testable—hence, the Turing Test. It’s not “reductive.” It embraces complexity and
emergent phenomena. It doesn't treat people like “black boxes,” nor does it deny
our internal representations of the world or our felt experiences. But it stipulates
that we can understand those experiences in terms of functional relationships
within the brain and body—we don’t need to invoke a soul, spirit, or any other
supernatural agency. Computational neuroscience and Al, fields Turing and von

Neumann pioneered, are both predicated on this functional approach.

It's unsurprising, in this light, that Turing and von Neumann also made ground-
breaking contributions to theoretical biology, although these are less widely
recognized today. Like intelligence, life and aliveness are concepts that have

long been associated with immaterial souls. Unfortunately, the Enlightenment
backlash against such “vitalism,” in the wake of our growing understanding of
organic chemistry, led to an extreme opposite view, still prevalent today: that life
is just matter, like any other. One might call this “strict materialism.” But it leads
to its own paradoxes: how can some atoms be “alive,” and others not? How can
one talk about living matter having “purpose,” when it is governed by the same

physical laws as any other matter?

Thinking about life from a functional perspective offers a helpful route through
this philosophical thicket. Functions can be implemented by physical systems, but

---

a physical system does not uniquely specify a function, nor is function reducible

to the atoms implementing it.

Consider, for example, a small object from the near future with a few openings

in its exterior, the inside of which is filled with a dense network of carbon nan-
otubes. What is it, you ask? Suppose the answer is: it’s a fully biocompatible arti-
ficial kidney with a working lifetime of a hundred years. (Awesome!) But there's
nothing intrinsic to those atoms that specifies this function. It’s all about what
this piece of matter can do, in the right context. The atoms could be different. The
kidney could be implemented using different materials and technologies. Who
cares? If you were the one who needed the transplant, I promise: you wouldn't
care. What would matter to you is that functionally, it’s a kidney. Or, to put it an-
other way, it passes the Kidney Turing Test.

Many biologists are mortally afraid of invoking “purpose” or “teleology,” because
they do not want to be accused of vitalism. Many believe that, for something to
have a purpose, it must have been made by an intelligent creator—if not a human

being, then God. But as we shall see, that’s demonstrably not the case.

And we have to think about purpose and function when it comes to biology, or
engineering, or Al. How else could we understand what kidneys do? Or hope to
engineer an artificial kidney? Or a heart, a retina, a visual cortex, even a whole
brain? Seen this way, a living organism is a composition of functions. Which

means that it is, itself, a function!

What is that function, then, and how could it have arisen? Let's find out.

---

# Chapter 1

1. Origins

Abiogenesis

How did life on Earth begin? In the nineteenth century, this seemed like an
unanswerable question. Researchers attempting to catch life in the act of “spon-
taneous generation” had come up empty-handed once they learned how to de-

contaminate their samples.

As William Thomson (1824-1907), the future Lord Kelvin, put it in an 1871
address before the British Association for the Advancement of Science, “Dead
matter cannot become living without coming under the influence of matter
previously alive. This seems to me as sure a teaching of science as the law of

gravitation.”"241

Has life somehow always existed, then? Did it arrive on Earth from outer space,
borne on an asteroid? Thomson thought so, and some still do. Not that this
“panspermia” hypothesis really gets us anywhere. Where did the asteroid come

from, and how did life arise there?

Despite his clear articulation of the principle of evolution, Charles Darwin (1809-
1882) didn't have a clue either. That’s why, in 1863, he wrote to his close friend
Joseph Dalton Hooker that “it is mere rubbish, thinking, at present, of origin of

life; one might as well think of origin of matter.”"242

Today, we have more of a clue, although the details may forever be lost to deep

time.

Biologists and chemists working in the field of abiogenesis—the study of the
moment when, billions of years ago, chemistry became life—have developed
multiple plausible origin stories. In one, proto-organisms in an ancient “RNA
world” were organized around RNA molecules, which could both replicate and
fold into 3D structures that could act like primitive enzymes.'” In an alternative
“metabolism first” account,“ life began without genes, likely in the rock chim-
neys of “black smokers” on the ocean floor; RNA and DNA came later. It may even-

tually be possible to rule one or the other theory out ... or it may not.

---

We'll return to RNA and replication, but let’s begin by unpacking the metabolism-

first version in some detail, as it sheds light on the problem that confounded
Darwin and his successors: how evolution can get off the ground without genetic
heritability. As we'll see, abiogenesis becomes less puzzling when we develop a
more general understanding of evolution—one that can extend back to the time

before life.

Let’s cast our minds back to our planet's origins. The Hadean Eon began 4.6 bil-
lion years ago, when the Earth first condensed out of the accretion disc of rocky
material orbiting our newborn star, the Sun. Our planet’s mantle, runnier than

it is today and laden with hot, short-lived radioactive elements, roiled queasily,
outgassing carbon dioxide and water vapor. The surface was a volcanic hellscape,
glowing with lakes of superheated lava and pocked with sulfurous vents belching

smoke.

It took hundreds of millions of years for surface conditions to settle down.
According to the International Astronomical Union, an object orbiting a star can
only be considered a planet if it has enough mass to either absorb or, in sweep-
ing by, to eject other occupants from its orbit. But in the chaos of the early Solar
system, this took a long time. While Earth was clearing its orbit of debris, it was

continually bombarded by comets and asteroids, including giant impactors more

---

than sixty miles across. A single such impact would have heated the already sti-

fling atmosphere to a thousand degrees Fahrenheit.

One of those collisions appears to have been with another newly formed planet,
an event that came close to destroying the Earth altogether. According to this
theory, enough broken, liquefied, and vaporized rock splashed into orbit to coa-

lesce into the Moon.

Unsurprisingly, very little geological material survives from the Hadean—mainly
zircon crystals embedded within metamorphic sandstone in the Jack Hills of
Western Australia.

It's difficult to imagine anything like life forming or surviving under such harsh
conditions. Maybe, somehow, it did. We know for sure that by later in the Hadean
or the early Archean—3.6 billion years ago, at the latest—the surface had cooled
enough for a liquid ocean to condense and for the chemistry of life to begin

brewing.

Today, those early conditions are most closely reproduced by black smokers.
These form around hydrothermal vents on the mid-ocean ridges where tec-
tonic plates are pulling apart and new crust is forming. In such places, seawater
seeping down into the rock comes into contact with hot magma. Superheated
water then boils back up, carrying hydrogen, carbon dioxide, and sulfur com-
pounds, which precipitate out to build smoking undersea chimneys. Probes sent
thousands of feet down to explore these otherworldly environments find them
teeming with weird life forms of all kinds, attracted by warmth, nutrients, and

each other. Some of the inhabitants may go a long, long way back.

Like lava rock, the chimneys are porous, and the pores are ideal little chambers for
contained chemical reactions to take place—potentially powered by a handy en-
ergy source, since the hydrogen gas creates proton gradients across the thin walls
between pores, making them act like batteries.2/ Given energy, iron sulfide min-
erals in the rock acting as catalysts, and carbon dioxide bubbling through, self-
perpetuating loops of chemical reactions can sputter to life, like a motor turning

over.

---

Perhaps this was life’s original motor: a primitive but quasi-stable metabolism, as
yet without genes, enzymes, or even a clearly defined boundary between inside
and outside. Such upgrades might have followed before long, though, for that
chemical synthesis motor closely resembles the “reverse Krebs cycle,” now widely

believed to have powered the earliest cells.

c4 2
Oxal 2
@D_,ED 3
Acetyl 4
C3 C6 5
GO2 Pyruvate Citrate Pn
C4 C6 2
Oxaloacetate Isocitrate
C4 C6
Malate Oxalosuccinate
C4 cs
Fumarate o-ketoglutarate
\ C CO
c4 c4
a Succinate Succinyl Gi)
CoA
Acetyl CoA »
M2]
8 oS
Citrate $
=
\ 2
C4 C6
Oxaloacetate Isocitrate
C4 C6
Malate Oxalosuccinate
C4 cs
Fumarate o-ketoglutarate

ion DD)

C4 C4

Succinate Succinyl Gi)
CoA

The ordinary or “forward” Krebs cycle was discovered in 1937 by groundbreaking
biochemist Hans Krebs (1900-1981). More like a gas-powered generator than

---

a motor, the Krebs cycle is at the heart of how all aerobic organisms on Earth
“burn” organic fuels to release energy, a process known as “respiration.”4! Inputs
to this cycle of chemical reactions include complex organic molecules (which

we eat) and oxygen (which we inhale); the “exhaust” contains carbon dioxide
and water (which we exhale). The energy produced maintains proton gradients
across folded-up membranes inside our mitochondria, and the flow of these pro-

tons goes on to power every other cellular function.

The idea of a “reverse Krebs cycle” was first proposed by a trio of researchers at UC
Berkeley in 1966.* It remained controversial for decades, but is now known to
power carbon fixation in ancient anaerobic sulfur bacteria—some of which still
make their homes in deep-sea hydrothermal vents.!**! As its name implies, the re-
verse Krebs cycle consists of roughly the same chemical reactions as the forward
cycle, but running in the opposite direction. Starting with water and carbon diox-
ide, proton gradients drive the synthesis of all of the basic building blocks needed
for cellular structure and function, including sugars, amino acids for proteins,
fatty acids and isoprenes for cell membranes, and nucleotides for building RNA
and DNA.U*

All life came from the sea, and the interior of every cell in every living organism
reproduces that salty, watery environment—a tiny “ocean inside.” This much is
common knowledge. But our mitochondria, the “power plants” within our cells
where respiration takes place, may in fact be recapitulating the much more spe-
cific deep-sea chemistry of a black smoker. In an almost literal sense, our bodies
are like Russian matryoshka dolls, membranes within membranes, and each

nested environment recreates an earlier stage in the evolution of life on Earth.

The deeper inside ourselves we look, the farther we can see into the past. A beau-

tiful, shivery thought.

Symbiogenesis

Whether RNA or metabolism came first, even the simplest bacteria surviving
today are a product of many subsequent evolutionary steps. Yet unlike the every-
day, incremental mutation and selection Darwin imagined, the most important

of these steps may have been large and sudden. These “major evolutionary tran-

---

sitions” involve simpler, less complex replicating entities becoming interdepen-

dent to form a larger, more complex, more capable replicator.24

As maverick biologist Lynn Margulis (1938-2011) discovered in the 1960s,
eukaryotic cells, like those that make up our bodies, are the result of such an
event. Roughly two billion years ago, the bacteria that became our mitochondria
were engulfed by another single-celled life form@2 much like today’s archaea—
tiny, equally ancient microorganisms that continue to inhabit extreme environ-
ments, like hot springs and deep-sea vents. This is “symbiogenesis,” the creation
or genesis of a new kind of entity out of a novel “symbiosis,” or mutually benefi-

cial relationship, among pre-existing entities.

At moments like these, the tree of life doesn’t just branch; it also entangles with
itself, its branches merging to produce radically new forms. Margulis was an early

champion of the idea that these events drive evolution’s leaps forward.

It’s likely that bacteria are themselves the product of such symbiotic events—

for instance, between RNA and metabolism.2! RNA could replicate without help
from proteins, and the metabolic motor could proliferate without help from
genes, but when these systems cooperate, they do better. The looping chemical-
reaction networks in those black smokers can be understood as such an alliance
in their own right, a set of reactions which, by virtue of catalyzing each other, can

form a more robust, self-sustaining whole.

Soin a sense, Darwin may have been right to say that “it is mere rubbish” to think
about the origin of life, for life may have had no single origin, but rather, have
woven itself together from many separate strands, the oldest of which look like
ordinary chemistry. Intelligent design is not required for that weaving to take
place; only the incontrovertible logic that sometimes an alliance creates some-

thing enduring, and that whatever is enduring ... endures.

Often, enduring means both creating and occupying entirely new niches. Hence
eukaryotes did not replace bacteria; indeed, they ultimately created many new
niches for them. Likewise, the symbiotic emergence of multicellular life—an-
other major evolutionary transition—did not supplant single-celled life. Like

an ancient parchment overwritten by generations of scribes, our planet is a

---

palimpsest, its many-layered past still discernible in the present. Even the black
smokers, throwbacks to a Hadean sea billions of years ago, are still bubbling away
in the depths. The self-catalyzing chemistry of proto-life may still be brewing

down there, slowly, on the ocean floor.

The idea that evolution is driven by symbiotic mergers, the earliest of which
preceded biology as we know it, has far-reaching implications. One is that the
boundary between life and non-life is not well defined; symbiogenesis can in-
volve any process that, one way or another, is self-perpetuating. Evolutionary
dynamics are thus more like a physical law than a biological principle. Everything

is subject to evolution, whether we consider it to be “alive” or not.

The symbiogenetic view also renders the idea of distinct species, classified
according to a Linnaean taxonomy, somewhat ill-defined—or at best, of limited
applicability. Such taxonomies assume that only branching takes place, not
merging. Bacteria, which promiscuously transfer genes even between “species,”
already challenge this idea.!?*! Taxonomies break down entirely when we try

to apply them to even more fluid situations, like the possible proto-life in black

smokers, or microbiomes, or the more complex symbioses we'll explore later.

Perhaps most importantly, symbiogenesis explains evolution’s arrow of time,

as classical Darwinian theory alone cannot. When life branches, specializing to
adapt to a niche—like Darwin's finches with their differently shaped beaks, each
optimized for a specific food source—those branches are in general no more com-
plex than their ancestral form. This has led some classical evolutionary theorists
to argue that the increasing complexity of life on Earth is an anthropocentric
illusion, nothing more than the result of a random meander through genetic pos-
sibilities.“ Relatedly, one sometimes hears the claim that since all extant species
are of equal age—as it seems they must be, since all share a common single-celled
ancestor some four billion years ago—no species is more “evolved” than any

other.

On its face, that seems reasonable. But as we've seen, classical Darwinian theory
struggles to explain why life seems to become increasingly complex, or, indeed,
how life could arise in the first place. In themselves, random changes or muta-

tions can only fine-tune, diversify, and optimize, allowing the expression of one

---

or another variation already latent in the genetic space. (The space of possible

finch beaks, for instance.)

When one prokaryote ends up living inside another, though, or multiple cells
band together to make a multicellular life form, the resulting composite organ-
ism is clearly more complex than its parts. Something genuinely new has arisen.
The branching and fine-tuning of classical evolution can now start to operate on

a whole different level, over a new space of combinatorial possibilities.

Classical evolution isn't wrong; it just misses half of the story—the more rapid,
more creative half. One could say that evolution’s other half is revolution, and

that revolutions occur through symbiosis.

Suggestively, the same is true of technology. In Paleolithic times, a hafted spear
was not just a specialized stone point, but something new that arose by combin-
ing at least three parts: a stone point, a shaft, and something like sinew to bind
them. This, too, opened up a new combinatorial design space. Or, in more recent
times, the silicon chip was not just an evolved transistor; it was something new
that could be made by putting multiple transistors together on the same die. One
doesn’t arrive at chip design merely by playing with the design parameters of an

individual transistor.

That’s why evolution progresses from simpler to more complex forms. It’s also
why the simpler forms often remain in play even after a successful symbio-
genetic event. Standalone stone points, like knives and hand axes, were still
being made after the invention of the hafted spear; and, of course, spearheads
themselves still count as stone points.) Moreover, no matter how recently any
particular stone point was made, we can meaningfully talk about stone points
being “older” as a category than spears. Spears had to arise later, because their ex-

istence depended on the pre-existence of stone points.

It's equally meaningful to talk about ancient life forms, like bacteria and archaea,
co-existing alongside recent and far more complex ones, like humans—while
recognizing that humans are, in a sense, complex colonies of bacteria and archaea

that have undergone a cascade of symbiotic mergers.

---

Reproductive Functions

While most biochemists have focused on understanding the particular history
and workings of life on Earth, a more general understanding of life has come
from an unexpected quarter: computer science. The theoretical foundations of
this surprising connection date back to those two founding figures of the field,

Alan Turing and John von Neumann.

I've already mentioned Turing’s 1950 paper introducing the Imitation Game

or Turing Test, but his first great contribution came fifteen years earlier. After
earning an undergraduate degree in mathematics at Cambridge in 1935, Tur-
ing focused on one of the fundamental outstanding problems of the day: the
Entscheidungsproblem (German for “decision problem”), which asked whether
there exists an algorithm for determining the validity of an arbitrary mathemat-

ical statement.

The answer turned out to be “no,” but the way Turing went about proving it
ended up being far more important than the result itself—which was lucky, since
American mathematician Alonzo Church had just scooped Turing, publishing his
own proof a few months earlier using a different approach.!4! After correspond-
ing with him about the Entscheidungsproblem, Turing would end up moving to

Princeton to become Church's doctoral student.

Proving mathematical statements about mathematical statements requires
defining a general notation for such statements, and a procedure for evaluating
them. Church did so using mathematical symbols, especially the lowercase Greek

letter A (lambda), thus inventing a self-referential “lambda calculus.”

Turing took a less conventional route. His procedure involved an imaginary
gadget we now call the “Turing Machine.” The Turing Machine consists of a read/
write head, which can move left or right along an infinite tape, reading and writ-

ing symbols on the tape according to a set of rules specified by a built-in table.

First, Turing showed that such a machine could do any calculation or computa-
tion that can be done by hand, given an appropriate table of rules, enough time,

and enough tape. He suggested a notation for writing down the table of rules,

---

which he referred to as a machine's “Standard Description” or “S. D.” Today, we'd

call ita “program.”

Then, the really clever part: if the program itself is written on the tape, there

exist particular tables of rules that will read the program and perform whatever
computation it specifies. Today, these are called “Universal Turing Machines.” In
Turing’s more precise language, “It is possible to invent a single machine which
can be used to compute any computable sequence. If this machine U is supplied
with a tape on the beginning of which is written the S. D. of some computing ma-

chine M, then U will compute the same sequence as M.”

Some programs run for a time, then finish. Others run forever. Since a Universal
Turing Machine allows programs themselves to be expressed as values on the
tape, a program can take another program as input. One can imagine such a
“meta-program” outputting a single bit of information that denotes whether the
inputted program will eventually finish, or will keep running forever. Turing
called this the “halting problem.” In his 1936 paper, he proved that a program
that solves the halting problem for all possible input programs—and that is itself
guaranteed to halt—is a logical impossibility. This was the result that answered
the Entscheidungsproblem in the negative.

More consequentially, though, the Universal Turing Machine defined a generic
procedure for computation. Turing was soon able to prove that any function that
could be computed by his imaginary machine could also be expressed in Church's
lambda calculus, and vice versa!‘{/—a cornerstone of the idea now known as the
Church-Turing thesis: that computability is a universal concept, regardless of

how it's done.

In the early 1940s, John von Neumann, a Hungarian American polymath who
had already made major contributions to physics and mathematics, turned his
attention to computing. He became a key figure in the design of the ENIAC and
EDVAC—among the world’s first real-life Universal Turing Machines, now known

simply as “computers,”

Turning an imaginary mathematical machine into a working physical one

required many further conceptual leaps, in addition to a lot of hard nuts-and-

---

bolts engineering. For instance, over the years, much creativity has gone into fig-
uring out how simple the “Standard Description” of a Universal Turing Machine
can get. Only a few instructions are needed. Esoteric language nerds have even
figured out how to compute with a single instruction (a so-called OISC or “one-in-

struction set computer”).

There are irreducible requirements, though: the instruction, or instructions,
must change the environment in some way that subsequent instructions are able
to “see,” and there must be “conditional branching,” meaning that depending on
the state of the environment, either one thing or another will happen. In most
programming languages, this is expressed using “if/then” statements. When
there’s only a single instruction, it must serve both purposes, as with the SUBLEQ
language, whose only instruction is “subtract and branch if the result is less than

or equal to zero,”

Both Turing and von Neumann were keenly aware of the parallels between
computers and brains. Von Neumann's report on the EDVAC explicitly described
the machine’s basic building blocks, its “logic gates,” as electronic neurons.|22)
Whether or not that analogy held (as we'll see, it did not; neurons are more com-
plex than logic gates), his key insight was that both brains and computers are
defined not by their mechanisms, but by what they do—their function, in both

the colloquial and mathematical sense.

In real life, though, the brain is not an abstract machine, but part of the body,
and the body is part of the physical world. How can one speak in purely compu-
tational terms about the function of a living organism, when it must physically

grow and reproduce?

Although working independently, toward the end of their lives, Turing and

von Neumann both became captivated by the connection between biology and
computation.“ Turing did pioneering work in “morphogenesis,” working out
how cells could use chemical signals, which he dubbed “morphogens,” to form
complex self-organizing patterns—the key to multicellularity.44 Although com-
puters were still too primitive to carry out any detailed simulations of such sys-

tems, he showed mathematically how so-called “reaction-diffusion” equations

---

could generate spots, like those on leopards and cows, or govern the growth of

tentacles, like those of the freshwater polyp, Hydra“

Around the same time, in a 1951 paper,“®) von Neumann imagined a machine
made of standardized parts, like Lego bricks, paddling around on a reservoir
where those parts could be found bobbing on the water. The machine’s job was
to gather all of the needed parts and construct another machine like itself. Of
course, that’s exactly what a bacterium does to reproduce; in fact it’s what every

cell must do to divide, and what every mother must do to give birth.

It’s possible for a trivially simple structure, like a seed crystal, to “reproduce”
merely by acting as a template for more of the same stuff to crystallize around it.
But a complex machine—one with any internal parts, for example—can’'t serve as
its own template. And if you are a complex machine, then, on the face of it, man-
ufacturing something just as complex as you yourself are has a whiff of paradox,
like lifting yourself up by your own bootstraps. However, von Neumann showed
that it is not only possible, but straightforward, using a generalization of the Uni-

versal Turing Machine.

He envisioned a “machine A” that would read a tape containing sequential assem-
bly instructions based on a limited catalog of parts, and carry them out, step by
step. Then a “machine B” would copy the tape—assuming the tape itself was also
made of available parts. If instructions for building machines A and B are them-

selves encoded on the tape, then voila—you would have a replicator.2°!

Instructions for building any additional non-reproductive machinery could also
be encoded on the tape, so it would even be possible for a replicator to build some-
thing more complex than itself.“ A seed, or a fertilized egg, illustrates the point.
Even more fundamentally, encoding the instructions to build oneself in a form
that is itself replicated (the tape) is the key to open-ended evolvability, meaning
the ability for evolution to select for an arbitrary design change, and for that

change to be inherited by the next generation.

Remarkably, von Neumann described these requirements for an evolvable, self-
replicating machine before the discovery of DNA’s structure and function.)
Nonetheless, he got it exactly right. For life on Earth, DNA is the tape; DNA poly-

---

merase, which copies DNA, is “machine B”; and ribosomes, which build proteins
by following the sequentially encoded instructions on DNA, are “machine A.” Ri-
bosomes and DNA polymerase are made of proteins whose sequences are, in turn,
encoded in our DNA and manufactured by ribosomes. That is how life lifts itself

up by its own bootstraps.

Life as Computation

Although this is seldom fully appreciated, von Neumann's insight established

a profound link between life and computation. Remember, machines A and B are
Turing Machines. They must execute instructions that affect their environment,
and those instructions must run in a loop, starting at the beginning and finishing
at the end. That requires branching, such as “if the next instruction is the codon
CGA then add an arginine to the protein under construction,” and “if the next
instruction is UAG then STOP.” It’s not a metaphor to call DNA a “program”—that

is literally the case.

Of course, there are meaningful differences between biological computing and
the kind of digital computing done by the ENIAC or your smartphone. DNA is
subtle and multilayered, including phenomena like epigenetics and gene proxim-
ity effects. Cellular DNA is nowhere near the whole story, either. Our bodies con-
tain (and continually swap) countless bacteria and viruses, each running their

own code.

Biological computing is “massively parallel,” decentralized, and noisy. Your cells
have somewhere in the neighborhood of three hundred quintillion ribosomes, all
working at the same time. Each of these exquisitely complex floating protein fac-
tories is, in effect, a tiny computer—albeit a stochastic one, meaning not entirely
predictable. The movements of hinged components, the capture and release of
smaller molecules, and the manipulation of chemical bonds are all individually
random, reversible, and inexact, driven this way and that by constant thermal
buffeting. Only a statistical asymmetry favors one direction over another, with
clever origami moves tending to “lock in” certain steps such that a next step be-

comes likely to happen. This differs greatly from the operation of logic gates ina

---

computer, which are irreversible“ and designed to be ninety-nine point many-

nines percent reliable and reproducible.

Biological computing is computing, nonetheless. And its use of randomness is

a feature, not a bug. In fact, many classic algorithms in computer science also
require randomness (albeit for different reasons), which may explain why Turing
insisted that the Ferranti Mark I, an early computer he helped to design in 1951,
include a random number instruction.) Randomness is thus a small but impor-
tant conceptual extension to the original Turing Machine, though any computer
can simulate it by calculating deterministic but random-looking or “pseudoran-

dom” numbers.

Parallelism, too, is increasingly fundamental to computing today. Modern AI,

for instance, depends on both massive parallelism and randomness—as in the
parallelized “stochastic gradient descent” (SGD) algorithm, used for training most
of today’s neural nets, the “temperature” setting used in chatbots to introduce a
degree of randomness into their output, and the parallelism of Graphics Process-

ing Units (GPUs), which power most AI in data centers.

Traditional digital computing, which relies on the centralized, sequential
execution of instructions, was a product of technological constraints. The first
computers needed to carry out long calculations using as few parts as possible.
Originally, those parts were flaky, expensive vacuum tubes, which had a ten-
dency to burn out and needed frequent replacement by hand. The natural design,
then, was a minimal “Central Processing Unit” (CPU) operating on sequences of
bits ferried back and forth from an external memory. This has come to be known

as the “von Neumann architecture.”

Turing and von Neumann were both aware that computing could be done by
other means, though. Turing's model of morphogenesis was a biologically in-
spired form of massively parallel, distributed computation. So was his earlier
concept of an “unorganized machine,” a randomly connected neural net modeled
after an infant’s brain.“*! These were visions of what computing without a cen-

tral processor could look like—and what it does look like, in living systems.

---

Von Neumann also began exploring massively parallel approaches to computa-
tion as far back as the 1940s. In discussions with Polish mathematician Stanislaw
Ulam at Los Alamos, he conceived the idea of “cellular automata,” pixel-like grids
of simple computational units, all obeying the same rule, and all altering their
states simultaneously by communicating only with their immediate neighbors.
With characteristic bravura, von Neumann went so far as to design, on paper, the
key components of a self-reproducing cellular automaton, including a horizontal
line of cells comprising a “tape” and blocks of cellular “circuitry” implementing

machines A and B.

Designing a cellular automaton is far harder than ordinary programming,
because every cell or “pixel” is simultaneously altering its own state and its envi-
ronment. When that kind of parallelism operates on many scales at once, and is
combined with randomness and subtle feedback effects, as in biological compu-

tation, it becomes even harder to reason about, “program,” or “debug.”

Nonetheless, we should keep in mind what these two pioneers understood so
clearly: computing doesn't have to be done with a central processor, logic gates,
binary arithmetic, or sequential programs. One can compute in an infinite vari-
ety of ways. Turing and his successors have shown that they are all equivalent,

one of the greatest accomplishments of theoretical computer science.

This “platform independence” or “multiple realizability” means that any
computer can emulate any other one. If the computers are of different designs,
though, the emulation mayruns...1...0...W...1... y. For instance, von Neu-
mann’s self-reproducing cellular automaton has never been physically built—
though that would be fun to see! It was only emulated for the first time in 1994,
nearly half a century after he designed it.2&

---

It couldn't have happened much earlier. A serial computer requires serious pro-
cessing power to loop through the automaton’s 6,329 cells over the sixty-three
billion time steps required for the automaton to complete its reproductive cycle.
Onscreen, it worked as advertised: a pixelated two-dimensional Rube Goldberg
machine, squatting astride a 145,315 cell-long instruction tape trailing off to
the right, pumping information out of the tape and reaching out with a “writing
arm” to slowly print a working clone of itself just above and to the right of the

original.

It's similarly inefficient for a serial computer to emulate a parallel neural net-
work, heir to Turing’s “unorganized machine.” Consequently, running big neural
nets like those in Transformer-based chatbots has only recently become practi-
cal, thanks to ongoing progress in the miniaturization, speed, and parallelism of

digital computers.

In 2020, my colleague Alex Mordvintsev devised a clever combination of modern
neural nets, Turing’s morphogenesis, and von Neumann's cellular automata.
Alex’s creation, the “neural cellular automaton” (NCA), replaces the simple per-
pixel rule of a classic cellular automaton with a neural net. This net, capable of
sensing and affecting a few values representing local morphogen concentrations,
can be trained to “grow” any desired pattern or image, not just zebra stripes or

leopard spots.

---

Real cells don’t literally have neural nets inside them, but they do run highly
evolved, nonlinear, and purposive “programs” to decide on the actions they will
take in the world, given external stimulus and an internal state. NCAs offera
general way to model the range of possible behaviors of cells whose actions don't

involve movement, but only changes of state (here, represented as color) and the

absorption or release of chemicals.

The first NCA Alex showed me was of a lizard emoji, which could regenerate not
only its tail, but also its limbs and head! It was a powerful demonstration of how
complex multicellular life can “think locally” yet “act globally,” even when each
cell (or pixel) is running the same program—just as each of your cells is running

the same DNA.

This was our first foray into the field known today as “artificial life” or “ALife.”

Artificial Life
Von Neumann’s work on self-reproducing automata shows us that, in a uni-
verse whose physical laws do not allow for computation, it would be impossible

for life to evolve. Luckily, the physics of our universe do allow for computation, as

proven by the fact that we can build computers—and that we're here at all.

Now we're in a position to ask: in a universe capable of computation, how often
will life arise? Clearly, it happened here. Was it a miracle, an inevitability, or

somewhere in between?

---

A few collaborators and I set out to explore this question in late 2023.C% Our first
experiments used an esoteric programming language invented thirty years ear-
lier by a Swiss physics student and amateur juggler, Urban Miiller. I'm afraid he
called this language ... Brainfuck. Please direct all naming feedback his way.

However, the shoe fits; it is a beast to program in. Here, for instance, is a Brainfuck

program that prints “helloworld”—and good luck making any sense of it:

++tt+t[—>t+ttt4<]>—-[>[++4++>]+4+4+4[<]>—]>> >>> 4+.<<,.6-.ct44 > t4+4,>,2>-,

The upside of Brainfuck is its utter minimalism. It’s not quite a single-instruction
language, like SUBLEQ, but as you can see, it includes only a handful of oper-
ations. Like a Turing Machine, it specifies a read/write head that can step left
(the “<” instruction) or right (the “>” instruction) along a tape. The “+” and “-”
instructions increment and decrement the byte at the current position on the
tape. The “,” and “.” instructions input a byte from the console, or output a byte
to it (you can count ten “.” instructions in the code above, one to print each letter
of “helloworld”). Finally, the “[{” and “]” instructions implement looping: “[” will
skip forward to its matching “]” if the byte at the current position is zero, and “]"

will jump back to its matching “[” if the byte is nonzero. That’s it!

It's hard to believe that Brainfuck could be used to fully implement, say, the
Windows operating system, but it is “Turing complete.” Here that means: given
enough time and memory (that is, a long enough tape), it can emulate any other

computer and compute anything that can be computed.

In our version, which we call bff, there’s a “soup” containing thousands of tapes,
each of which includes both code and data. This is key: in “classic” Brainfuck,

the code is separate from the tape, whereas in bff, we wanted the code to be able
to modify itself. That can only happen if the code itself is on the tape, as Turing

originally envisioned.

Bff tapes are of fixed length—64 bytes, about the same length as the cryptic
“helloworld” program above. They start off filled with random bytes. Then, they
interact at random, over and over. In an interaction, two randomly selected tapes
are stuck end to end, and this combined 128 byte-long tape is run, potentially
modifying itself. The 64 byte-long halves are then pulled back apart and re-

---

turned to the soup. Once in a while, a byte value is randomized, as cosmic rays do

to DNA.

Since bff has only seven instructions (represented by the characters “<>+-,[]”)
and there are 256 possible byte values, following random initialization only
7/256, or 2.7 percent, of the bytes in a given tape will contain valid instructions;
any non-instructions are simply skipped over. Thus, at first, not much comes
of interactions between tapes. Once in a while, a valid instruction will modify a
byte, and this modification will persist in the soup. On average, though, only a
couple of computational operations take place per interaction, and usually they
have no effect. In other words, while any kind of computation is theoretically
possible in this toy universe, precious little actually takes place—at first. Random
mutation may alter a byte here and there. Even when a valid instruction causes a

byte to change, though, the alteration is arbitrary and purposeless.

But after millions of interactions, something magical happens: the tapes begin to
reproduce! As they spawn copies of themselves and each other, randomness gives
way to intricate order. The suddenness of this change resembles a “phase transi-
tion” in matter, as between gas and liquid, or liquid and solid. Indeed, the initial
disorder of the soup is very much like that of randomly whizzing gas molecules.
Hence random, non-functional code has been called “Turing gas”;'*") however, in
bff, it “condenses” into functioning code, which is something far more complex

than a solid or a liquid.

We could call it “computronium,”! since when the phase transition occurs,
the amount of computation taking place skyrockets—remember, reproduction
requires computation. Two of Brainfuck’s seven instructions (“{” and “]”) are
dedicated to conditional branching, and define loops in the code. Reproduction
requires at least one such loop (“copy bytes until done”), causing the number of

instructions executed in an interaction to climb into the thousands.

---

16,000

14,000
12,000
[=
& 10,000
.o)
& 8,000
8
a. 6,000
4,000
2,000
0
0 5 10 15 20 25 30
interactions (millions)
Ww
he
eae
2
£
§

0 5 10 15 20 25 30
interactions (millions)

The code is no longer random, but obviously purposive, in the sense that its func-
tion can be analyzed and reverse-engineered. An unlucky mutation can break it,
rendering it unable to reproduce. Over time, the code evolves clever strategies to

increase its robustness to such damage.

This emergence of function and purpose is just like what we see in organic life at
every scale; so we can talk about the function of the circulatory system, a kidney,
or a mitochondrion, and how they can “fail”—even though nobody designed

these systems.

---

We reproduced our basic result with a variety of other programming languages
and environments. Alex (of neural cellular automata renown) created another
beautiful mashup, this time between cellular automata and bff. Each of a
200x200 array of “pixels” contains a program tape, and interactions occur only
between neighboring tapes on the grid. In a nod to our nerdy childhoods, the
tapes are interpreted as instructions for the iconic Zilog Z80 microprocessor,
launched in 1976 and used in many 8-bit computers over the years (including
the Sinclair ZX Spectrum, Osborne 1, and TRS-80). Here, too, complex replicators
soon emerge from random interactions, evolving and spreading across the grid in

successive waves.

Our simulations suggest that, in general, life arises spontaneously whenever
conditions permit. Those conditions seem minimal: little more than an environ-

ment capable of supporting computation, some randomness, and enough time.
Let's pause and take stock of why this is so remarkable.

On an intuitive level, one does not expect function or purposiveness to emerge
spontaneously. To be sure, we've known for a long time that a modest degree of
order can emerge from initially random conditions; for instance, the lapping of
waves can approximately sort the sand on a beach, creating a gradient from fine
to coarse. But if we were to begin with sand on a beach subject to random wave
action, and came back after a few hours to find a poem written there, or the sand
grains fused into a complex electronic circuit, we would assume someone was

messing with us.

The extreme improbability of complex order arising spontaneously is generally
understood to follow from thermodynamics, the branch of physics concerned
with the statistical behavior of matter subject to random thermal fluctuations—
that is, of all matter, since above absolute zero, everything is subject to such ran-
domness. Matter subject to random forces is supposed to become more random,
not less. Yet by growing, reproducing, evolving, and indeed by existing at all, life

seems to violate this principle.

The violation is only apparent, for life requires an input of free energy, allowing

the forces of entropy to be kept at bay. Still, the seemingly spontaneous emer-

---

gence and “complexification” of living systems has appeared to be, if not strictly
disallowed by physical laws, at least unexplained by them. That’s why the great
physicist Erwin Schrédinger (1887-1961) wrote, in an influential little book he
published in 1944 entitled What Is Life?,

[Living matter, while not eluding the “laws of physics” as established up to
date, is likely to involve “other laws of physics” hitherto unknown, which,
however, once they have been revealed, will form just as integral a part of

this science as the former.)

Thermodynamics

Before turning to those “other laws of physics,” it’s helpful to take a closer look

at the original ones, and especially the Second Law of thermodynamics.

These are deep waters. While the fundamental ideas date back to the ground-
breaking work of nineteenth-century mathematical physicist Ludwig Boltzmann
(1844-1906), we can understand their essence without math. Nonetheless,
Boltzmann’s conceptually challenging ideas flummoxed many of his fellow sci-
entists, and the implications of his work continue to stir controversy even today.
Much has been made of Einstein turning our everyday notions of space and time
inside-out with his theory of relativity, developed in its initial form in 1905—
just a year before Boltzmann, struggling with bipolar disorder, ended his own life.
Arguably, though, Boltzmann's earlier ideas disrupt our intuitions about time,
cause, and effect even more radically than Einstein's theory of relativity." Let's

dive in.

The Second Law of thermodynamics holds that any closed system will rise in
entropy over time, becoming increasingly disordered. A hand-powered lawn
mower, for example, starts off as a beautifully polished machine with sharp he-
lical blades, round wheels, and toothed gears, all coupled together on smoothly
rotating bearings. If left out in the elements, the bearings will seize up, the blades
will dull, and oxidation will set in. After enough time, only a heap of rust will

remain.

---

Similarly, if you were to take a dead bacterium (which, though a lot smaller, is far
more complicated than a push mower) and drop it into a beaker of water, its cell
membrane would eventually degrade, its various parts would spill out, and after
a while only simple molecules would remain, dispersed uniformly throughout
the beaker.

The Second Law gives time its arrow, because the fundamental laws of physics
in our universe are very nearly time-reversible.\*»! Strange, but true: Newton's
equations (classical dynamics), Maxwell's equations (electromagnetism),
Schrédinger’s equations (quantum physics), Einstein’s equations (special and
general relativity)—all of these physical laws would work the same way if time
ran in reverse. The difference between past and future evaporates when we look
only at the mathematics of dynamical laws, or only at an individual microscopic
event in the universe. The distinction between past and future, or cause and
effect, only comes into view when we zoom out from that microscopic world of

individual events and consider instead their statistics.

Here's a common undergraduate thought experiment to illustrate this point in
the case of Newtonian dynamics. Imagine video footage of balls on a billiard
table, all in random positions and moving in random directions. They will collide
with one another and with the bumpers at the edge of the table, bouncing off at
new angles. If we (unrealistically) assume frictionless motion and fully elastic
collisions (i.e., balls don’t slow down as they roll, and none of the collision en-
ergy is dissipated as heat), this would go on forever. The summed momenta and
summed energies of the balls will remain constant—and it will be impossible to
tell whether you're watching the video forward or in reverse. In such a universe,

causality has no meaning, because nothing distinguishes causes from effects.

If the initial conditions were random, then the positions of the balls will continue
to be randomly distributed over the table’s surface as they all bounce around,
transferring some of their energy to each other with every collision. It would be
astronomically unlikely for the balls to all bunch up in one spot. Their velocities,
too, will be randomly distributed, both in direction and magnitude, so it would
also be astronomically unlikely for them to, for instance, suddenly all be moving

precisely parallel to the table’s edges. Complete disorder, in other words, is a sta-

---

ble equilibrium.‘! In the presence of any thermal noise (that is, random pertur-

bation), it is the only stable equilibrium.

Suppose, though, that the near-impossible happens. You see fifteen of the balls
converge into a perfect, stock-still triangular grid, each ball just touching its
neighbors, while the cue ball, having absorbed all of the combined kinetic energy
of the other fifteen, whizzes away from the triangle. Aha! Now, we know that
we're watching a pool break—and we know that we’re watching it in reverse. The
arrow of time has been established. Along with it, we have causation: the triangle

broke because it was hit by the cue ball.

Theoretically, nothing prevents the exact series of collisions from happening that
would result in all of the energy being transferred to a single ball while leaving
the others arrayed in a perfect triangle; but statistically, it’s vanishingly unlikely
for such an ordered state to arise out of disorder—unless, perhaps, some master-

mind set the balls in motion just so.

Although key thermodynamic concepts were not developed until the nineteenth
century, an Enlightenment-era belief in a God who set the universe in motion
just so arises intuitively from the apparent impossibility of order arising sponta-
neously out of disorder.“ In a mechanical, billiard-table universe where the laws
of physics are inviolable and the laws of statistics seem to inexorably degrade any
pre-existing order over time, it seems absurd that anything as complicated as

life could arise spontaneously without some supernatural agent acting as “prime
mover.” Only a God with exquisite foresight could have “initialized” the Big Bang
such that, in the Earth’s oceans billions of years ago, simple organic molecules
floating around apparently at random could coalesce into a working bacterium
—an improbability many, many orders of magnitude less likely than fifteen out
of sixteen whizzing billiard balls spontaneously coalescing into an unmoving

triangle.

The billiard ball universe I've just described may seem abstract or arbitrary,

but nineteenth-century theorists like Boltzmann had become interested in this
problem for the most practical of reasons: it was the physics behind steam power,
hence the entire Industrial Revolution.!°*! Engineering had preceded theory, as it

often does.

---

Thomas Newcomen (1664-1729), an English inventor and Baptist lay preacher,
devised the first practical fuel-burning engine in 1712. It was based on a heating-
and-cooling cycle. First, steam from a boiler was allowed to flow into a cylindri-
cal chamber, raising a piston; then, the steam valve closed, and a second valve
opened, injecting a jet of cold water, causing the steam to condense and pull the
piston back down. As the piston rose and fell, it rocked a giant beam back and
forth, which, in Newcomen’s original design, was used to pump water out of
flooded mines (which, in turn, supplied the coal these engines would soon be

consuming so voraciously).

Scottish inventor and entrepreneur James Watt (1736-1819) greatly improved
the steam-engine design in 1776, making it a practical replacement for human
and animal power across a wide range of applications. This was when the Indus-
trial Revolution really got underway; for the first time, human-made machines
began to metabolize on a large scale, “eating” complex organic molecules to per-

form mechanical work.

Soon, far more energy would be flowing through this artificial metabolism than
through the Krebs cycle in our own bodies.!°"! It was, in the broad sense I’ve
been using in this book, a major evolutionary transition: a symbiogenetic event
between humans and machines, like earlier symbioses between humans and
draft animals. Machine metabolism allowed human society to explode from its
pre-industrial scale (about one billion people in 1800, most of whom lived in
extreme poverty) to its scale today (eight billion, most of whom no longer live in
poverty). In the process, we’ve become nearly as dependent on machines for

our continued existence as they are on us.

However, even as coal-powered engines transformed the Victorian landscape—
both figuratively and literally, for the pollution was dire—nobody understood
them at a deep level. What was heat, and how could it be converted into phys-
ical work? For a time, the leading theory held that heat was a kind of invisible,
weightless fluid, “caloric,” that could flow spookily into and through other

matter.

By combining Newtonian physics, statistical calculations, and experimental

tests, Boltzmann and his colleagues figured out what was really going on. Their

---

conceptual setup was a three-dimensional version of the billiard table, in which
the balls were gas molecules whizzing around in a pressurized chamber, bounc-

ing off its walls. Calculating the average effect of all the bouncing led to the

Ideal Gas Law, which established theoretical relationships between the pressure,
volume, and temperature of a gas. The theory closely matched observations by

experimentalists and engineers.“

Volume is straightforward (that’s just the size of the chamber), but the idea that
pressure is the aggregate force on the chamber’s walls as molecules bounce off
them, and that temperature is the average kinetic energy“! of those whizzing
molecules, was a profound insight. There was no need for any mysterious
“caloric” fluid; heat was just motion on a microscopic scale. And the tendency to-
ward a random distribution of molecular positions and momenta explains why,
if you open a valve between two chambers containing gas at different pressures

and/or temperatures, those pressures and temperatures will quickly equalize.

Before moving beyond classical thermodynamics, let's add a bit more realism to
our billiard-ball universe. We know that balls bouncing around a billiard table
don’t actually go on bouncing forever. They encounter friction, slowing down

as they roll. And when they bounce off each other, the collisions are slightly “in-
elastic,” meaning that after the collision, they’re moving a bit slower than before.

After a little while, they stop rolling.

How can that be? At a microscopic level, the laws of physics are reversible.
Momentum is supposed to be conserved. And the amount of matter and energy
also remains constant, whether we run time forward or in reverse. That's the First

Law of thermodynamics!

Zooming in will reveal that, on a real billiard table, balls aren't the smallest ele-
ments that bump against one other. Each billiard ball consists of lots of vibrating
molecules bound together. Collisions between these individual molecules are
what really cause the balls to bounce off each other—or, for that matter, cause

a ball to roll across the felt rather than falling right through it.!/! In each case,
momentum is transferred between molecules. Every time this happens, the dis-

tribution of molecular momenta becomes a bit more random, that is, a bit less

---

correlated with which ball the molecule happens to be in, or indeed whether it is

in a ball at all, or in the felt underneath.

In the most random distribution of molecular velocities, there would be no more
correlation between the velocities of two molecules in one ball than in the veloc-
ities of molecules in different balls. Every ball would be imperceptibly jiggling in
place, with each of its constituent molecules contributing minutely to the dance.
We call that random jiggling “heat.” When all correlated motion has been con-

verted into uniformly distributed heat, we've reached a stable equilibrium.

While the balls are still rolling, the correlations between the velocities of their
molecules are by no means all equal; the distribution is far from random. This is
not a stable equilibrium. Hence, the inevitability of friction and the inelasticity of
collisions are statistical phenomena—just more symptoms of the inexorable Sec-

ond Law.

Going forward, then, let’s imagine once more that the billiard balls are indivisible
particles, not bound collections of molecules. In that case, all collisions would
have to be elastic, all motion frictionless, and disordered, randomly colliding

balls would be the equilibrium.

Once a system has reached equilibrium, it will stay that way forever—an end
state Lord Kelvin called “heat death.”\) This seemingly trivial observation has
some profound consequences. First, the arrow of time will lose its meaning; any
two consecutive moments A, B could just as likely have been ordered B, A. Noth-

ing, therefore, can be said to be a cause, versus an effect.

Relatedly, no work can be done. If the system were out of equilibrium—for
instance, if all of the whizzing balls were on one side of the billiard table—then
we could put a movable barrier down between the empty and occupied sides,
attached to a loaded crankshaft. As they bounce around, the balls would then
nudge the barrier, doing work. What I’ve just described is, of course, a piston, like

that of a steam engine.

But if the balls were equally likely to be anywhere, then no matter how fast they
whizz and bounce, there’s nowhere to put the barrier that would result in any net

force. The piston wouldn’t move because it would be buffeted equally from all

---

sides. This idea can be generalized: work can only be done by a system in disequi-
librium, for instance, when the pressure or temperature is high in one place, and
low in another. That’s why Newcomen’s engine needed both hot steam and cold

water.

I've already used the term free energy, but now we can define it. The free energy
of a system is the amount of work it can be made to do. Far from equilibrium,
when the entropy is low, much of the kinetic energy in the billiard balls is “free”;
it can be used to move pistons, raise weights, produce electric currents, carry out
computations, or drive metabolic processes. But at equilibrium, the entropy is
maximized, and the free energy is zero. This insight into the relationship between

energy, entropy, and work lies at the heart of thermodynamics—and life.

Dynamic Stability

Recall that life seemed deeply weird to Schrodinger because living things
appear to violate the Second Law. If the bacterium we drop into a beaker of water
is alive rather than dead, and free energy is available in a form the bacterium can
use, and the water contains simple molecules suitable for building more bacteria,
then over time we will see the very opposite of an increase in disorder. After a
while, the beaker will be full of bacteria, reproducing, cooperating, and compet-

ing with each other.

The bacteria will even be evolving. If the beaker is sufficiently large—the size of
a planet, for instance—and we wait a few billion years, then eventually beings as
complicated as us may be in there, along with cities, advanced technologies, and

perhaps plans to colonize a nearby beaker.

None of these processes can occur without free energy. For us, it comes primarily
from the sun. Thermodynamics tells us that even if the Second Law appears to be
violated locally, it still holds when we zoom out. Order created in one place comes
at the expense of increased disorder elsewhere. Hence, pollution, the finite life-

time of the sun, and the eventual heat death of the universe.

What concerns us here isn’t this big picture, but its apparent local violations,

and the way they seem to become increasingly transgressive over time. The

---

puzzle isn’t only that bacteria exist, but that as time passes, life on Earth seems
to become more complex: from prokaryotes to eukaryotes; from eukaryotes to
multicellular animals; from simple multicellular animals to ones with nervous
systems; from brainy animals to complex societies; from horses and plows to

space travel and Al.

Is there any general principle behind that complexification process, a kind of
“however” or “yes, and” to the dismal Second Law? And could it account not only

for evolution and complexification, but also for abiogenesis?

Yes, and yes. Bff can offer us a highly simplified model system for understanding
that principle, just as an idealized billiard table gives us a model for understand-

ing basic thermodynamics.

Replicators arise in bff because an entity that reproduces is more “dynamically
stable” than one that doesn't. In other words, if we start with one tape that can
reproduce and one that can’t, then at some later time we're likely to find many
copies of the one that can reproduce, but we’re unlikely to find the other at all, be-

cause it will have been degraded by noise or overwritten.

Addy Pross, a professor emeritus of chemistry at Ben Gurion University of the
Negev, describes the same phenomenon using the bulkier phrase “dynamic ki-
netic stability” (DKS).\”*' I'll drop “kinetic,” since the idea also applies far beyond
Pross'’s field of “chemical kinetics” (describing the rates at which chemical reac-
tions take place). In bff, for example, dynamic stability can just as well apply to

programs or program fragments.

As Pross points out, a population of replicating molecules can be more stable
than even the hardiest of passive materials. A passive object may be fragile, like

a soap bubble, or robust, like a stone sculpture. The sculpture might endure for
longer, but, in the end, it’s still ephemeral. Every encounter it has with anything
else in the world will cause its composition or structure to degrade, its individual
identity to blur. For a sculpture, it’s all downhill. That’s the Second Law at work,

as usual.

A self-reproducing molecule—like the DNA inside a living bacterium—is another

matter. It is thermodynamically fragile, especially if we consider its identity to

---

consist not only of a general structure but of a long sequence of specific nucleo-
tides. However, its pattern is not just robust, but “antifragile.”“ As long as DNA
is able to reproduce—an inherently dynamic process—that pattern can last, es-
sentially, forever. A bit of environmental stress or adversity can even help DNA

maintain or improve its functionality.” This is how order overcomes disorder.

In fact, Darwinian selection is equivalent to the Second Law, once we expand our
notion of stability to include populations of replicators. Through a thermody-
namic lens, Darwin's central observation was that a more effective replicator is

more stable than a less effective one. As Pross puts it,

[MJatter |...] tends to become transformed |...] from less stable to more
stable forms. [...] [T]hat is what chemical kinetics and thermodynamics

is all about [...]. And what is the central law that governs such trans-
formations? The Second Law. [...] In both [the static and kinetic] worlds
chemical systems tend to become transformed into more stable ones [...}—
thermodynamic stability in the “regular” chemical world, dynamic kinetic

stability in the replicator world.“

As a chemist, Pross is sensitive to the close relationships between energy, entropy,
and stability, whether static or dynamic. However, he does not explicitly make a

connection to the theory of computing.

It now seems clear that by unifying thermodynamics with the theory of com-
putation, we should be able to understand life as the predictable outcome of a
statistical process, rather than regarding it uneasily as technically permitted, yet
mysterious. Our artificial life experiments demonstrate that, when computation
is possible, it will be a “dynamical attractor,” since replicating entities are more
dynamically stable than non-replicating ones; and, as von Neumann showed,

replicators are inherently computational.

Bff has no concept of energy, but in our universe, replicators require an energy
source. This is because, in general, computation involves irreversible steps—oth-
erwise known as causes and effects—and thus, computing consumes free energy.

That's why the chips in our computers draw power and generate heat when they

---

run. (And why my computer heats up when it runs bff.) Life must draw power

and generate heat for the same reason: it is inherently computational.

Complexification

When we pick a tape out of the bff soup after millions of interactions, once
replicators have taken over, we often see a level of complexity in the program on
that tape that seems unnecessarily—even implausibly—high. A working repli-
cator could consist of just a handful of instructions in a single loop, requiring a
couple of hundred operations to run. Instead, we often see instructions filling up
a majority of the 64 bytes, multiple and complex nested loops, and thousands of

operations per interaction,

Where did all this complexity come from? It certainly doesn’t look like the result
of simple Darwinian selection operating on the random text generated by a
proverbial million monkeys typing on a million typewriters.!” In fact, such com-
plexity emerges even with zero random mutation—that is, given only the initial
randomness in the soup, which works out to fewer bytes than the text of this
book. Hardly a million monkeys—and far too few random bytes to contain more

than a few consecutive instructions, let alone a whole working program.

The answer recalls Lynn Margulis's great insight: the central role of symbiosis in
evolution, rather than random mutation and selection. When we look carefully
at the quiescent period in the bff soup before tapes begin replicating, we notice

a steady rise in the amount of computation taking place. We are observing the
rapid emergence of imperfect replicators—very short bits of code that, in one way
or another, have some nonzero probability of generating more code. Even if the
code produced is not like the original, it’s still code, and only code can produce

more code; non-code can’t produce anything!

Thus, a selection process, wherein code begets code, is at work from the very
beginning. This inherently creative, self-catalyzing process is far more important
than random mutation in generating novelty. When bits of proliferating code
combine to form a replicator, it’s a symbiotic event: by working together, these

bits of code generate more code than they could separately, and the code they

---

generate will in turn produce more code that does the same, eventually leading to

whole-tape replication and an exponential takeoff.

A closer look at the bff soup prior to the exponential takeoff reveals distinct
phases of “pre-life,” which might have had close analogs during abiogenesis on
Earth. In the first phase, individual instructions occasionally generate another
individual instruction, but this is more akin to a simple chemical reaction than
to any real computation; the instructions are not acting as part of any larger

program.

In the second phase, we begin to see instructions in particular positions, or in
particular combinations, that are likelier to lead to copies of themselves than one
would expect by random chance, albeit often in indirect ways. “Autocatalytic
sets” start to form: cycles of dynamical interactions that mutually reinforce each
other. These, too, can arise spontaneously in the chemical world, and have long

been theorized to have driven abiogenesis.=!

At this point, with autocatalytic fragments of code proliferating and colliding, a
leap becomes possible that brings us beyond the world of digital chemistry and
into the world of real computation: the emergence of the first true replicators.
These are no longer mere autocatalytic sets, but short programs that copy them-

selves, or each other, using looped instructions.

With this leap to computation comes an enormous upgrade in evolvability,
because now, any change made to a program that does not break its copy loop will
be heritable. Thus, classical Darwinian selection can kick in, allowing adaptation
to a changing environment or speciation for occupying diverse niches. If we in-
sist on making a distinction between non-life and life, this might be a reasonable

place to draw that line.

However, these earliest replicating programs are unlikely to cleanly copy a whole
tape. Often, they only copy short stretches of tape, which may get pasted into
arbitrary locations, yielding unpredictable results. As these scrappy, fragmentary
replicators proliferate, the bff soup enters a chaotic phase. Despite the churn, the
tapes have not, at this point, resolved into any obvious structure. To the naked

eye, they still look like random junk, although the rising amount of computation

---

taking place (as measured both by the average number of operations per interac-

tion and the density of instructions per tape) suggests that something is afoot.

Tracking the provenance of every byte in the soup, starting from random ini-
tialization, can make sense of the apparent chaos. At first, almost every byte of
every tape remains whatever it was at initialization time; if we draw a line from
each byte’s current position on a tape to its original source position, the lines will
all extend back to time zero in parallel, like the warp threads of aloom. Once in

a while, a byte will change, cutting a thread, or get copied, pulling it across the
other threads diagonally.

e

io

fenemet ons Thos ands
Innencee sere JT Inad
inteeact ous Felli oe
r .
bs

feanew ron there andy

as

b y a Ww 4 Se 4D

Fr ;
yu a: FI
ie f 4
2 * Fs
sis : as
q 4 4 “da
3 3 a =

i :

as

» : " e F . po . " ;

° » uw wb a se a a uw au a “a s> “ ° uw w hn «l » wt b w Po] w 4 tw 4b
hye tyne are yo

With the rise of scrappy replicating programs, all remaining dependencies on
the past are quickly cut as replicators copy over each other in a frenzy of creative
destruction. Any given byte might get copied hundreds of times to a series of
different tape locations, in the process wiping out whatever had previously been
there. Shortly afterward, all of those copies might get wiped out in turn by some
other more efficiently replicating fragment. Soon, every byte’s history becomes
very brief in time, yet complex in space—a short-lived snarl of sideways jumps.

The loom becomes all weft, and no warp.

Are these scrappy replicators competing or cooperating? Both. Replicators that
can’t keep up are wiped out, along with any non-replicating bytes. Surviving

replicators, on the other hand, continually form chimeras,®4 recombining with

---

other replicators (or even copies of themselves) to become more effective still.
These are, once more, symbiogenetic events: sub-entities merging to forma

larger, more capable super-entity.

This chaotic phase is such a potent crucible for directed evolution that it gener-
ally doesn't last long. It rapidly produces a robust whole-tape replicator, which
then takes off exponentially, resulting in the dramatic transition to the organized
structures (and large amounts of computation) that are bff’s most obvious fea-

ture. At this point, artificial life seems to spontaneously emerge.

But as we can now appreciate, there’s nothing spontaneous about it. Replicators
had been present all along, and each larger replicator is composed of smaller ones

—an inverted tree of life, consisting of mergers over time rather than splits.

However, evolution’s creative work is not done yet. After the takeoff of a fully
functional tape replicator, we often see yet further symbiotic events. From a clas-
sical Darwinian standpoint, this seems puzzling, since further evolution seems
superfluous once whole tapes are replicating reliably. How could “fitness” possi-
bly improve further, once a tape copies itself in its entirety every time it interacts

with another tape?

We must consider that since the instructions for whole-tape replication don't
occupy all 64 bytes, there’s extra space on the tape that could be dedicated to ...
anything. That's the point of von Neumann-style replication—it allows for open-
ended evolution precisely because the tape can contain additional information,

beyond the code needed for replication itself.{=2)

Any extra replicated bytes could, of course, be random—just passive, purposeless
information cargo hitchhiking from one generation to the next. But if these bytes
contain instructions, those instructions can run. And if they can run, they can
replicate themselves, too. Thus, the symbiogenetic process can continue to oper-
ate, creating additional replicators within an already replicating tape. Sometimes
these sub-replicators even produce multiple copies of themselves in a single

interaction.

Sub-replicators can interact with their host in many ways. They can “kill” the

host by damaging its replication code, which is generally catastrophic for the sub-

---

replicator, as it thereby destroys the environment within which it can run. Sub-
replicators can be neutral, leaving the host’s replication machinery alone. Or, they
can be symbiotic, for instance by conferring resistance to mutational damage via
redundant copying of the host's code. The overall tendency is toward symbiosis,

since that is the most dynamically stable.

Over time, code colonizes a large proportion of the 64 bytes. Code is more dynam-
ically stable than non-code, and its dynamic stability increases through symbio-
sis with yet more code—in particular, when code fragments find ways to work in

functional tandem.

In a way, symbiosis is the very essence of functionality. When we talk about a
kidney’s function only making sense in context, we mean that it is in symbiosis
with other functions—like those of the liver (breaking ammonia down into urea),
the heart (pumping blood), and so on. Each of these functions is purposive pre-
cisely because its inputs are the outputs of others, its outputs are inputs to others,

and thus they form a network of dynamically stable cycles.

The same is true of larger, planetary-scale interrelationships. The “purpose” of
plants, from the perspective of animal life, is to produce oxygen and sugar, which
we breathe and eat. The “purpose” of animals, from a plant’s perspective, is to
turn the oxygen back into carbon dioxide, and provide compost and pollination.
Our growing understanding of life as a self-reinforcing dynamical process boils
down not to things, but to networks of mutually beneficial relationships. At every

scale, life is an ecology of functions.

Because functions can be expressed computationally, we could even say that life
is code. Individual computational instructions are the irreducible quanta of life
—the minimal replicating set of entities, however immaterial and abstract they
may seem, that come together to form bigger, more stable, and more complex

replicators, in ever-ascending symbiotic cascades.

In the toy universe of bff, the seven special characters “<>+-,[]" are the elemen-
tary instructions. On the primordial sea floor, geothermally-driven chemical
reactions that could catalyze further chemical reactions likely played the same

role. Under other conditions, on another planet, or in another universe, many

---

different elementary interactions could do the same—as long as they are Tur-
ing complete, enabling them to make the leap from autocatalytic sets to true

replication.

Virality

Although bffis only a toy universe, it can serve as a simplified model for life
and evolution, just as a Newtonian billiard-ball universe can serve as a simplified
model for the thermodynamics of ideal gases. As we've seen, some of bff’s predic-

tions are quite different from those of classical Darwinian theory:

1. Bff suggests that symbiogenesis is a more important driver of evolu-
tionary innovation than random mutation.

2. Since symbiogenesis must involve combinations of pre-existing
dynamically stable entities, we should expect complex replicating en-
tities to emerge after (and be made of) simpler ones.

3. As aresult, zooming in on sub-replicators within a larger replicator

should allow us to peer back in evolutionary time.=4!

These phenomena should sound familiar! They’re all consistent with Lynn
Margulis’s observations, which flew in the face of twentieth-century biological

orthodoxy, but are now, if not mainstream, at least gaining respectability.
But wait, there’s more:

4. Due to the instability of the imperfect replicators leading up to the first
true replicator, we should expect this first true replicator to be a histor-
ical “event horizon,” becoming the template for what follows and eras-

ing independent traces of what came before.

We see this on Earth too. Although the first chemical steps toward proto-life may
still be taking place in environments like black smokers, we don't see the missing
links. Where are the kinds of imperfect replicators that fused together to form
the simplest life forms today?

We likely don’t see them on their own because, as in bff, their instability made
them ephemeral, quickly displaced or absorbed by the first stably replicating
cell—which might already have been recognizably kin to today’s bacteria and

---

archaea. (Evolutionary biologists call this the “Last Universal Common Ancestor”
or LUCA.) Still, we can assume that many of the component parts of the most an-
cient surviving life forms—like the reverse Krebs cycle and RNA replication—are

fossilized fragments of earlier imperfect replicators.
In the same vein:

5. Evolved code should not only include instructions for replicating itself
as a whole, but also be rife with sub-sequences that contain instruc-
tions for independently replicating themselves.

6. If symbiosis among these parts generated the novelty driving the
evolution of the whole, we should see evidence in the genome of many
“broken” or incomplete sub-replicators.

7. Code that evolved through such hierarchical symbiotic replication
should also contain many sequences that are repetitive, or are copies of

other parts.

We can find all of these features in our own genetic code—and they don’t cor-
respond to what we would expect to see if our genomes had evolved primarily

through mutation and selection.

When the first complete human genome sequence was published in 2000, some
surprises were in store.!**! One was the astonishingly high proportion of so-called
“junk DNA” that doesn’t code for proteins: about ninety-eight percent. How did

it get there? Is it actually doing anything? We now understand that some of this
“junk” is involved in gene regulation, but most is still of unknown or uncertain
function. Close inspection reveals, though, that much of our code, whether

“junk” or otherwise, is ... viral.

---

Protein-coding [——— LINEs
genes | —_ SINEs
20.5

13.1

\

LTR retro-
—— transposons

DNA
transposons

Introns

Simple
sequence repeats

Miscellaneous | |________. Segmental
unique |__ Miscellaneous duplications

sequences heterochromatin

The reproductive cycle of viruses is an often-told story. When traveling between
cells, a virus looks like a bit of DNA or RNA packaged into a protein “envelope”
capable of binding to a target cell and injecting its genetic payload. Once inside
the cell, the viral code hijacks cellular resources to begin replicating, both copying
its genetic material and manufacturing its envelope proteins. These assemble
into more viruses. Maniacally cranking out viral proteins, the cell may eventually

burst, releasing a flood of virus particles to repeat the cycle.

“Retroviruses” like HIV (the Human Immunodeficiency Virus, which causes
AIDS) include additional “reverse transcription” machinery for permanently
incorporating their genetic material into the cell’s DNA. This makes them a lot
harder for the host to clear. The key enzyme, “reverse transcriptase,” wasn't char-
acterized until 1970,*! but Barbara McClintock (1902-1992), working at Cold
Spring Harbor Lab on Long Island, had made an earlier discovery that turned out
to be closely related.

While studying the genetics of maize plants in the late 1940s and early '50s, Mc-
Clintock found mobile segments of DNA that seemed to be able to cut and paste
themselves into different locations on the genome, producing differently mottled
color patterns in corn kernels.“*! Although many of her colleagues were initially
skeptical about these “transposons” or “jumping genes,” McClintock eventually
won the Nobel Prize for her work.

---

A much wider zoo of “transposable elements” has since been discovered, some

of which don’t just “cut and paste,” but “copy and paste” themselves; they are, in
effect, replicators within our DNA. In fact, some of them are fully fledged retro-
viruses, including instructions not only for splicing their code into a host cell's
genome, but also for manufacturing envelope proteins, allowing that code to ven-

ture out into the world in search of other cells to infect.

Retroviruses are unsettlingly ... intimate. HIV specifically targets immune cells,
but if a retrovirus infects an egg or sperm cell, it can insert its code into an organ-
ism’s germ line, becoming a permanent part not only of that cell, but of an entire
species. In a 2006 publication in the prestigious journal Nature, researchers at
the University of Queensland in Australia reported catching a retrovirus in this
act of becoming “endogenous” for the first time.!"4 An epidemic of leukemia in
koalas had first been traced to a retrovirus, then this retrovirus was found to have
invaded the koala germ line over the previous century, causing the disease to be-

come heritable.
Does this mean the end of koalas? Probably not.

The human genome is rife with signs that the same process has taken place many
times in the history of our own species. At least eight percent of our genome con-
sists of endogenized retroviruses, the remnants of such retroviral invasions.!“2!
Remember, eight percent is several times more DNA than codes for our “own”

genes!

We usually think of viruses as mere disease agents, opportunistically parasitizing
our cells to reproduce, since they have no reproductive machinery of their own.
The reality may be very different, though. As many of us know from our recent
experience with COVID,“"! viruses (and pathogens in general) tend to evolve into
forms less lethal to their hosts over time, for obvious reasons—a dead host isa
dead end for the pathogen, too. There’s mounting evidence that the relationship
between virus and host can go even further, to become symbiotic. Retroviral code
in our genome, for instance, has become fundamental to the formation of the pla-

centa, the immune system, cell differentiation, and brain function.2

---

Moreover, endogenous retroviruses are only the tip of an even larger iceberg.
Nearly half of our genome consists of transposable elements of one kind or
another. Some were probably once retroviruses, or vice versa. Fully sequenced
genomes are often rife with lengthy stretches of highly repetitive sequences,
from long and complex to mere alternations of two or three symbols—evidence

of sub-replicators running amok.

Our genomes, in other words, are not only reproduced as a whole, but include
working reproductive sub-sequences at many scales. Some are new and can

still cause disease; others are older and may have lost the ability to make viral
envelopes or the other machinery needed to become infectious; and yet others
have integrated themselves so deeply into our own code that they are no longer
distinct. Some of this code even serves critical functions in our bodies. It’s obvi-
ous that, at least by this last stage of the process, complete symbiosis has been
established: neither the host nor the sub-replicator could survive, let alone repro-

duce, on its own.

In his 2009 book Virolution,2) author and physician Frank Ryan goes further,
arguing that viruses may have been symbionts all along. Plague viruses like HIV
don’t come from nowhere; they are species jumpers. We know that HIV was orig-
inally SIV, the Simian Immunodeficiency Virus, variants of which are endemic

to Old World primates including African green monkeys, sooty mangabeys,
mandrills, and chimpanzees. Yet many of these viruses don't sicken their original
hosts.22)

We also know that if a virus finds itself inside an organism whose physiology is
too different from that of its original host, it can’t gain purchase—a lucky thing
for you, if you've ever swallowed a mouthful of seawater, which likely contained
about a billion virus particles! (Most would have targeted single-celled marine
life.) The greatest danger seems to come from viruses adapted to a different but
closely related species. Perhaps, when it kills, such a virus is doing its job: wiping

out rivals who have invaded the original host's territory.

Viruses could, in other words, work like an out-of-body immune system. Within
our bodies, our immune systems seek out and destroy cells that are recognized

as “not-us.” Outside our bodies, “our” viruses could be similarly seeking out and

---

destroying whole animals who are recognized as “not-us.” Once a virus becomes
endemic to a new population, though—even if it initially kills many—it will

differentiate, co-adapt, and perhaps eventually go native.

One could consider bacterial pathogens through a similar lens; hence the well-
documented plagues of smallpox that European colonists brought to the Amer-
icas, decimating Native populations, and the virulent (though less deadly)
syphilis epidemic believed to have been brought back to Europe by Columbus.
Unlike bacteria, though, retroviruses don’t just take up residence in our environ-
ment or in our bodies, but fuse into our very genomes, becoming inextricably

part of us—especially when they alter the germ line.

By sheer volume, our DNA appears to be made primarily of the layered remnants
of many such past fusions. It seems clear that transposable elements and “en-
dogenous viral elements” or EVEs have done much more editing of our genome in
recent evolutionary history than mutation has.“ And they have been at this for
a long, long time. Based on the best available evidence, viruses are at least as old

as the Last Universal Common Ancestor, if not older.(22

This ongoing ecology of mobile, self-reproducing, and even infectious genes
causes the supposed “tree of life” to continue entangling with itself in the oddest
ways. Fully a quarter of the cow genome, for instance, consists of copies of the
retrotransposon BovB. BovB appears to have leapt many times between species
to create a phylogenetic tree of its own, a “bizarre parallel universe where cows
are more closely related to snakes than to elephants, and where one gecko is
more closely related to horses than to other lizards.”") These are instances of
“horizontal gene transfer” (HGT), long associated with bacteria, but clearly more

universal, 24)

Whether a bit of new DNA is acting in the moment as friend, foe, or somewhere
in between is just a matter of where on the symbiotic trajectory it falls. When
brand new, it’s unlikely to be friendly. But if it has persisted for a long time, and
especially if it has become endogenous, its dynamic stability implies that it will
have become non-lethal or even friendly due to combined evolutionary pressures
on host, invader, and “host plus invader” as a “holobiont” or symbiotically fused

entity. If some gene or other functionality in the fused code proves valuable to

---

the larger whole, that functionality will be conserved, even as the sub-replicator’s
reproductive capability degrades and eventually vanishes. Perhaps that is how

new genetic functionality arises in general.

In this light, random point mutation can even be seen as something like a min-
imal abiogenesis event, creating a tiny parasitic “life form” within the genome.
On its own, it would of course be unable to reproduce, since it possesses no in-
dependent reproductive machinery;!"*! then again, neither does a virus. So, like a
virus, a mutation can reproduce—using the host's resources, which will copy it
along with everything else. When introduced into the genome of a sophisticated
existing organism, such a tiny, random entity is unlikely to be friendly, though.
As with any larger invasion, the mutation will either damage or kill its host (and
itself, in the bargain) or achieve dynamic stability, either by being neutral or (oc-
casionally) helpful.

Hence, just as replicator thermodynamics encompasses classical thermody-
namics as a special case, evolution via symbiogenesis can encompass classical
Darwinian theory as a special case. Point mutation is unlikely to be the main
driver of evolution once life has taken off because it’s so much weaker and slower
on its own than higher-order symbiogenesis. Unlike point mutation, a chunk of
code that has already circulated, jumping around in the genome or even between
species, isn’t random. It necessarily includes real functionality. And at least in
some settings, that functionality has been under evolutionary pressure to help,
or at least not kill, its host. Evolution picks up steam over time, with major evolu-
tionary transitions becoming more frequent precisely because increasingly high

orders of symbiogenesis become possible.

Compression

When code evolves through symbiogenesis, it will develop a curious statistical
structure: parts of it will be copies (or near-copies) of other parts, and as those
parts establish symbiosis, they'll form a larger aggregate which will also copy
itself as a unit. This is reminiscent of (though not the same as) a “fractal”: a struc-

ture that resembles itself at a cascade of ever-finer scales. Let's take a short detour

---

through fractals and their relationship to biology so that we can then consider
the implications of evolution itself exhibiting certain fractal-like properties.

French-American mathematician Benoit Mandelbrot (1924-2010) is the figure
most associated with fractals, though they were first described by English mete-
orologist Lewis Fry Richardson (1881-1953). In the aftermath of World War II,
Richardson, a Quaker, had been trying to build a mathematical model to predict
the likelihood of conflicts between countries. One of the parameters in his model
was the length of their common border. He was perplexed to find, though, that
certain borders didn’t appear to have agreed-upon lengths. The Portuguese, for
instance, reported that their border with Spain was 613 miles long, but the Span-
ish claimed that it was 754 miles long. This seemed like a weirdly large discrep-

ancy for what ought to have been an easily surveyed distance!

Richardson eventually figured out what was going on: the Spanish were using

a higher-resolution map. Every twist and turn the Portuguese could see in the
Minho, Douro, and Guadiana rivers separating the countries had finer-scale
twists and turns only visible on the Spanish map. Richardson showed that, if
zooming in on any given meandering revealed more meanderings, the total
length of a “self-similar” curve like a coastline or a river can grow without limit as

one measures it with an ever-smaller ruler.)

---

10’ —

6x 10°

Coastline length (meters)

4x 10°

10! 10¢ 10°
Ruler length (meters)

“Fractal geometry” is thus very different from the Euclidean geometry we all
learned in school, where the length of a line or curve is well-defined and doesn't
blow up when you zoom in. Of course, in real life, one can’t zoom in forever, but
fractals are still important mathematical tools for understanding structures that

are self-similar over a range of scales, like rivers and coastlines.

Living organisms exhibit obvious fractal properties in certain of their structures,
such as tree branches, bronchial tubes, and circulatory systems. In structures like
these, fractal geometry over some range of scales offers an elegant design solu-
tion to a biophysical problem. For instance, blood carrying oxygen and nutrients
needs to reach every cell in the body, which means that oxygenated blood has to
be pumped through a branching network of tubes, and these tubes—which are, in
Euclidean terms, one-dimensional—have to repeatedly subdivide to “fill” three-
dimensional space. Hence, we have fractally branching (and then merging) net-

works of arteries, arterioles, capillaries, venules, and veins.

By working out the design properties of such fractal networks and their impli-
cations, theoretical physicist Geoffrey West and his collaborators at the Santa

Fe Institute have figured out many fundamental “scaling laws” in biology."

---

One of the most well-known results from this body of work explains why every
mammalian heart will beat about 1.5-2 billion times over a lifetime, whether

it belongs to an Etruscan shrew (weighing a twentieth of an ounce, and living a
year or so), or a blue whale (weighing over three hundred thousand pounds, and

living about a century).

Self-similarity in general yields “power law” scaling relationships, which look
like straight lines when plotted on logarithmic axes.!°!! Body mass, for instance,
has power-law relationships with metabolic rate, the total length of the circu-
latory system, and lifespan.“°*! Combining various power-law relationships to
calculate the number of heartbeats in a lifetime causes all the scaling variables
to cancel out beautifully, yielding the famous 1.5-2 billion beat constant. While
the theory is not exact (humans, for example, live somewhat longer than pre-
dicted), it does a remarkable job of parsimoniously explaining a wide range of

phenomena.

Is life in general a kind of fractal, then? No. A rhyme by British mathematician

Augustus De Morgan is often invoked in describing fractals:

Great fleas have little fleas upon their backs to bite ‘em,
And little fleas have lesser fleas, and so ad infinitum.U2

The poem is funny precisely because it is absurd: unlike an idealized fractal
coastline, living systems are, in general, profoundly dissimilar across scales Ol
While there are rare instances of the kind De Morgan describes—such as hyper-
parasitoid wasps, tiny parasites that lay their eggs inside bigger wasps—one does

not generally zoom in on a flea to discover a smaller flea, let alone ad infinitum.

Indeed, even coastlines are best characterized, in real life, as “multifractals”:
systems with repetitive structure at every scale, but variability across scales.22)
As aresult, their power laws may also vary. For instance, zooming in twofold at
one level of magnification, where the ruggedness is especially pronounced, might
cause the apparent length to scale up by 2!>=2.83, while zooming in twofold at a
magnification where the coastline appears smoother might only cause the appar-
ent length to scale up by 2!16*2.24. Every bump has bumps on it, but the bumps

at one scale are shaped differently from the bumps at another.!!°°!

---

Na5,r =
dslog 5/

N=6, r=
d=log6/

Ne7, re
d*logT/

745 J
OPS
Bates

Similarly, although genomes are always replicated, and are made of other
genomes that are themselves replicated, every whole is different from its parts,
just as an integrated circuit is different from a transistor. How, then, would one

go about quantifying this multifractal-like property in a genome?

The answer is closely related to data compression. Consider bff. In its initial state,
the tapes consist of random bytes; there's no repetitive structure. If we were
reading through the tapes one byte at a time, the next byte would have an equal
probability of assuming any value, from O to 255, independent of any of the pre-
vious bytes. Therefore, the sequence is entirely unpredictable, which means that
if you were to try compressing the soup with file compression software, like ZIP,
the compressor wouldn't be able to squeeze the file size at all. (This is, harkening

back to thermodynamics, a working definition of a completely disordered state.)

Data are redundant—that is, compressible—precisely to the degree that they are
predictable, or, equivalently, exhibit order. Compression algorithms like those

in ZIP work by looking for patterns already encountered in the data stream and
exploiting those patterns to encode subsequent data using as few bits as possible.
The usual trick is to incrementally build a dictionary or “phrase book” out of the
source material, and to substitute sections of the text for pointers into this dic-

tionary whenever the pointer can be encoded in fewer bits than the original text.

---

The dictionary is, in effect, a predictive model, and since the compressor builds
that model incrementally as it compresses, the decompressor is able to incremen-

tally reconstruct an identical copy of the model as it decompresses.

Absent any prior knowledge about how to model a long sequence, describing it in
terms of previously encountered parts of itself is a good strategy. The full text of
this book ZIPs down to about thirty-five percent of its original size as a raw text
string—since some letters occur more often than others, many words repeat, and

those words often combine into stock phrases.241

When bff undergoes its sharp transition to whole-tape replication, the tapes
suddenly become highly compressible; they squeeze down to just five percent of
their original size. Interestingly, many regions of the human genome are highly
compressible too. These data streams compress so well because, at any given
point in the sequence, one can often make a pretty good guess as to what the next
letter will be, simply by looking for the longest previous sequence that matches

the current context.

Such matches arise due to replication. In the human genome, we’re not talking
about replication at the level of the individual, but, rather, at the level of trans-
posable elements (or their fossil remnants) within our genome. Similarly, even

a single bff tape is highly compressible, because it formed through a symbiotic
fusion of smaller replicators ... and these replicators are themselves likely to be
either copies of each other or related, having formed out of yet smaller imperfect

replicators ... which are themselves either copies or related.

Like fractals, sequences of symbols constructed by repeatedly copying sub-
sequences of all lengths exhibit power-law scaling—in this case, between the
lengths of repeated sequences and their frequency. For instance, a replicated se-
quence twice the length of another might be found half as often—which is pretty
often! (These statistics would be dramatically different for random sequences,
where increasing the sequence length would cause a much faster exponential
decline in expected frequency.*)) Sequences constructed according to a fixed
self-copying rule are, in a sense, infinitely compressible, for they contain only as
much information as it would take to write down the recipe, no matter how long

the sequence.

---

By contrast, in a complex replicating system like bff—let alone the gnome—

the way any particular set of replicating sub-sequences combine to form a larger
replicating sequence will always be specific. It will depend on the functional par-
ticulars of how those parts come together to make a working whole. Therefore,
each such combination adds novelty or information. However, that information
will be much less than would be needed to specify an arbitrary symbol sequence

of the same length.

When we look for this property in bff and in human genome data, that’s just
what we find! Not only do both compress very well; they also compress better
and better the longer the stream of data gets. For instance, a single bff tape com-
presses somewhat, but the whole soup compresses better, and as the size of the
soup grows, the compression ratio continues to improve—though no matter how

much has already been seen, the remainder is never fully predictable.

Similarly, while a single stretch of a human genome already compresses well, the
whole genome compresses better. In the statistical context of many other human
genomes, so much of the information in your genome is redundant that it could
be compressed to a file size small enough to send as an email attachment.|!2"! The
pattern continues if we zoom yet farther out to consider genomes across species.
Hence the famous statistic that the human genome is ninety-eight percent iden-
tical to the chimpanzee genome ... and sixty percent similar to that of the fruit
fly!

While common ancestry alone can explain many of the similarities across
species (though not all, as BovB illustrates), such classical Darwinian arguments
can’t explain why the genome of a single individual is also so repetitive. That
only makes sense when we begin to consider genomes to be made out of smaller

genomes.

DNA and bff tapes, in other words, are both systems that evolve through what we
could call “multifractal symbiosis.” Our genomes are aggregates of cooperating
replicators, all the way down. That’s why they are so compressible. But it’s also
why wonderful new kinds of complexity emerge at every scale—and therefore

why, in biology, we can always learn something new by zooming in or out.

---

Embodiment

There is a profound yet subtle relationship between the multifractal properties

of our bodies and the multifractal properties of the genome.

The relationship is subtle because the genetic code is by no means a one-to-one
blueprint explicitly representing the body’s final shape. One might imagine, for
instance, that because a snake has hundreds of ribs, it might have a stretch of
DNA coding for a vertebra and rib pair that might have replicated itself a few
hundred times in the snake’s genome. Could snakes be the result of a retrotrans-

poson coding for ribs run wild, like BovB?

Not exactly. So-called “Hox” genes, shared widely among animals, control overall
body plan, and they “execute” their program using a combination of gene regu-
lation and the kind of distributed computation Turing described in his work on
morphogenesis. During embryonic development, ribs begin as a self-organized
standing wave in the concentrations of chemical morphogens—the same kind of
process that gives cows their spots and tigers their stripes. Whereas patterns in
skin coloration merely involve varying pigmentation, though, the developmental

program for a rib involves many subsequent morphogenetic steps.

This mechanism is vastly more powerful, general, and evolvable than merely

replicating some “build a rib” code. It reuses code, just as any decent programmer
would: invoking the same “build a rib” function a hundred times instead of copy-
ing and pasting it a hundred times. Thus, tweaking rib flexibility or curvature in-

volves making one change, not a hundred.

Evolution can produce real programs that reuse code because life is computa-
tional. Remember that if you're a replicator of the kind von Neumann described,
you need to contain instructions for building yourself, including a machine B to
copy those instructions, and a machine A, the “universal constructor,” to follow
them. The universal constructor is the engine not only of reproduction, but also
of growth, development, healing, and maintenance. It created your circulatory
system and skin during embryonic development; it also heals your skin and

replaces the torn capillaries underneath when you get a cut. As long as you are

---

alive, your body will continuously construct and reconstruct itself. The code

never stops running.

And since a universal constructor is a kind of Universal Turing Machine, its
computations, or equivalently mathematical functions, are inherently “compo-
sitional”: complex functions (or programs) can be made of sub-functions, which
can in turn be made of sub-sub functions ... until, at bottom, everything could be

expressed in terms of the elementary instructions of a Turing Machine.

Functions can even be made out of themselves. In computer science, this is known
as “recursion.” The Fibonacci sequence, for example—1, 1, 2, 3, 5,8, 13,21,andso
on, where each number is the sum of the previous two—is most easily expressed
as the recursive function f(n)=f(n-1)+f(m-2) for numbers greater than 1, with
f(0)=f(1)=1. We find Fibonacci numbers in biology all the time, as in the spiral
pattern of a pine cone, the head of a sunflower, and the chambers of a nautilus.
This is a clue that recursive computation takes place in the construction of pine

trees, sunflowers, and nautiluses.|112)

The smoking gun, though, is the growth of self-similar structures in the body.
Compositionality and recursion are what allow genetic code to build a many-
tiered fractal like the circulatory system. Code for building ribs or nautilus
segments could, in theory, just be copied a couple hundred times, but that’s not
possible for arteries, veins, or capillaries, where the number of segments and
branches becomes astronomically large. The blood vessel branching code must
get reused. And with relatively minor tweaks, it must be possible for the param-
eters of that code to be adjusted so that the branching stops at the appropriate
size for a shrew, or goes on to construct something the size of a blue whale, since

shrews and whales are, in the grand scheme of things, close relatives.

From an evolutionary perspective, compositionality implies a hierarchical
network of symbiotic relationships. The bacteria that became mitochondria

and the archaea that engulfed them each started with the code they needed to
reproduce themselves. When they merged into a eukaryote, they still needed to
retain the instructions for their own reproduction, but they also needed to evolve
additional functionality for mutual regulation. When eukaryotes became mul-

ticellular, the same process needed to happen again; our cells still know how to

---

reproduce individually, and, indeed, cellular reproduction is a fundamental oper-

ation involved in the larger-scale growth and reproduction of a whole animal.

What is true of evolution is also true of an individual organism's develop-
ment.|!1!! Blood vessels, for instance, aren’t just Euclidean line segments, but
tubes made of layers of smooth muscle cells. Each of those cells contains a com-
plement of organelles, and each mitochondrion in each of those cells contains its
own membranes and loop of bacterial DNA. A living organism is a compositional
structure par excellence. It could only be built computationally, through the com-
position of many functions. And life could only have evolved as the hierarchical

composition of those functions—that is, through symbiogenesis.

Daisyworld

All definitions of life are controversial, most seem to require caveats or excep-
tions, and none has advanced our understanding of biology. Frustrated with this
state of affairs, biochemist Andrew Ellington has gone so far as to assert that
“there is no such thing as life. Life is not a meaningful scientific term. It is a term

for poets, not scientists,”"1244)

Ellington’s position may sound extreme, but it’s more defensible than the dog-

matic definition in many biology textbooks: that living organisms have “the abil-
ity to eat, metabolize, excrete, breathe, move, grow, reproduce, and be responsive
to external stimuli.”’! By this definition, viruses aren't alive, which might seem

reasonable. But neither are mules or worker bees, since they are sterile!

Or consider a leaner definition popular among astrobiologists: “life is a self-sus-
taining chemical system capable of Darwinian evolution.”!4) Better, but by this
definition, parasites are not alive, since they aren’t self-sustaining. Then again, is
any life form truly self-sustaining? (Not if it eats.) How can a “self” be meaning-
fully circumscribed? And while life on Earth is based on chemistry, should we re-

ally insist on this as a requirement? Functionalism would argue otherwise.

So, here's my own attempt:

---

Life is self-modifying computronium arising from selection for dynamic
stability; it evolves through the symbiotic composition of simpler dynami-
cally stable entities.

Notice that my definition doesn’t stipulate any specific function. However, in
defining life computationally, it is functional. And in a world where the Second
Law holds, dynamic stability implies that those functions must include some
combination of self-construction, self-repair, or reproduction. All of these are
computations that require code to be able to read and write code, hence the “self-
modifying” qualifier.

“Computronium” is generally understood to be a phase of matter, but the “mat-
ter” here could be anything that can support computation, including bytes in bff
or pixels in a cellular automaton. Furthermore, unlike gases, liquids, or solids,
which are essentially uniform at macroscopic scales, the phase of matter asso-
ciated with life is necessarily lumpy. One reason is that a uniform material can't
carry out general computation; computronium must, at its finest scale, contain

distinct interacting components.

There's a deeper reason, too. Dynamic stability implies the existence of discrete
units—a self, or a population of selves—for without some model of a self or selves
it would be impossible to say what is stable. And since life composes itself symbi-
otically, there are “whats” at multiple scales—in our case, from molecules to mi-
tochondria, cells, whole organisms, and beyond. Studying each “what” requires

zooming in or out to focus on the dynamic stability of a different kind of entity.

At the most zoomed-out scale, life consists of a single “lump”; for us, that would
be the Earth. Is it, too, alive? Physicist and astrobiologist Sara Walker argues that
itis not, precisely because it’s a singleton. Walker believes that the Earth will only
become alive if and when we colonize another planet, thereby “reproducing.”
My definition of life doesn’t require reproduction, but it does require dynamic

stability; can that even be defined for a singleton?

It can, in a sense first formalized in the 1970s and'80s by the independent
scientist James Lovelock, together with Lynn Margulis and others. Their “Gaia hy-

pothesis,” named after the Greek Earth-goddess, is based on the observation that

---

our planet as a whole is homeostatic. Negative feedback loops actively maintain
various biosphere parameters within ranges friendly to life (though many mech-
anisms, like the one regulating the sea’s salinity, are still poorly understood).
Earth's temperature, for instance, has oscillated within a relatively narrow band
for hundreds of millions of years, even though the Sun has grown hotter over
time. Earth’s temperature remains stable enough for life because it actively

warms and cools itself, and it warms and cools itself because it is alive.

The mechanism whereby such self-regulation arises is no mystery, and indeed
boils down to Darwinian selection for dynamic stability. A simulation of a highly
simplified Earth-like planet Lovelock called “Daisy world” illustrates how this
works.\1+°! Daisyworld has only two species: black daisies and white daisies, both
of which have reproductive rates that depend on temperature—a sweet spot at

a balmy 72.5°F, declining gradually to zero if the heat is below 41°F or above
104°F. Black daisies warm the planetary surface by absorbing sunlight, while
white daisies cool it by reflecting sunlight. Careful mathematical analysis shows
that black and white daisy populations will dynamically adjust to regulate the
mean surface temperature, keeping it close to the sweet spot over a factor of two
in solar luminosity—a remarkable range, which, on a lifeless planet, would yield

temperatures ranging from 32°F-140°F.

---

AREA C4)

C}

TEMP CBEG.

SOLAR LUMINOSITY

While the detailed analysis is complicated, even for a simple two-species ecology,
the mechanism behind this homeostatic tendency is generic. Roughly speaking,
it holds whenever there exist species whose populations both depend on the
environment and have an effect on that environment. Some homeostasis occurs
even with just a single species (in Daisyworld, either black or white daisies), but
homeostasis is more robust with multiple species that can, like opposable mus-

cles, perturb the environment in one direction or another.

So, in my view, a planet like Daisyworld or Earth is indeed alive, for it not only
contains computational life forms (and therefore does a lot of computation in
the aggregate), but it also self-modifies to achieve dynamic stability. Daisyworld
shows, in other words, how evolution can still operate with a population size of
one. The key is modularity: its parts are also alive, and can themselves undergo

evolutionary selection.

Aspen forests offer a useful parallel. Aspen trees send out horizontal roots that
can sprout a trunk and grow into another tree. Or is it another trunk of the same
tree? “Pando,” in Sevier County, Utah, is a quaking aspen covering more thana

hundred acres and estimated to weigh over thirteen million pounds. Although

---

each of its forty-seven thousand or so trees (trunks? stems?) have finite lifespans,
the whole forest can be understood as a single, immortal organism that—if it
were confined to a fertile valley surrounded by impassable mountains—might

never reproduce.

Although an aspen forest’s genetics are locked in—since every apparent tree is

a clone—Darwinian selection still takes place, in that trunks in favorable places
will flourish and reproduce, while those in unfavorable places won't. Individual
trees can’t move, but the forest can—an example of an “emergent capability.” As
the valley’s climate shifts, the whole forest then will go on the march, creeping
up and down the mountainsides to maintain homeostasis. It is thus entirely rea-
sonable to call both the trees and the forest alive, just as it’s reasonable to call both

you and your individual cells alive. So, too, the Earth as a whole.

However, this doesn’t imply that the Earth is “smarter than” the sum of its parts,
or that it is conscious, just because we individually are, and we are part of it. In
fact the social intelligence hypothesis, which we’ll explore in chapter 5, suggests
that our consciousness arose as a result of social interaction. Our planet has no

other living planets to socialize with.14)

The Earth is intelligent only to the degree that the models implicit in its feedback
loops have kept it alive under gradually changing conditions for billions of years
—a slow, vegetative kind of intelligence with limited predictive power. Although
now techno-humanity is starting to model both the Earth and the heavens, keep-
ing telescopic “eyes” open for stray asteroids and radio “ears” cocked for alien
transmissions. No dice ... yet. But arguably our planet is rapidly becoming more
intelligent and animal-ish, able to sense remotely and make long-range predic-
tions, poised to respond proactively to threats and opportunities, should they
arise—and assuming we can get our act together and re-establish a planetary

homeostasis that includes humanity and technology.

Elan Vital

If life is computational, then are human-engineered (that is, “artificial”) com-
puters alive? They are certainly purposive, or we couldn't talk about them being

broken or buggy. But hardware and software are, in general, unable to reproduce,

---

grow, heal, or evolve on their own, because engineers learned long ago that self-
modifying code (like bff, or DNA) is hard to understand and debug.“ Thus,
phones don’t make baby phones, or (alas) heal from their frequent injuries. Apps

don't write new versions of themselves.

And yet: there are more phones in the world this year than last year, and their
cracked screens do often get repaired; apps acquire new features, become ob-
solete, and eventually reach end-of-life, replaced by new ones; and AI models
improve from month to month. Electronic components and computer code also
exhibit the same kind of compositionality we’ve seen in bff and DNA. It certainly
looks as if technology is reproducing and evolving!!!" Debating its aliveness is

thus a bit like the debate over whether viruses or parasites are alive.

If we zoom back out, putting technology and humans in the frame together,

we can see that this larger, symbiotic “us” is certainly reproducing, growing,
and evolving.U2°) The emergence of technology, and the mutually beneficial—

if sometimes fraught—relationship between people and tech is nothing more or
less than our own most recent major evolutionary transition. Technology, then,
is not distinct from nature or biology, but merely its most recent evolutionary

development.

And what about that age-old inanimate stuff—rocks and rivers, mountains and
beaches, clouds and storms? Water molecules in themselves are clearly not ca-
pable of general computation. Yet in the context of the hydrologic cycle, clouds,
rainstorms, and rivers certainly serve critical ecological functions, and are pro-
foundly shaped by life. Likewise, our planet's metal and sand are shaped into
steam engines and computer chips, just as calcium we ingest turns into bones
and ionic currents. All of these materials and structures comprise parts of a
grand network of Gaian interdependency. Why do we draw boundaries around
certain networks of functions and insist that they are “alive,” while asserting the

surrounding functions are not?

This way lies vitalism, a view espoused in various forms by a long line of philoso-
phers from Posidonius of Apameia (circa 135-51 BCE, and undoubtedly reflecting
a much older tradition) to Henri Bergson (1859-1941). Some modern thinkers,

too, defend the vitalist position, such as Jane Bennett:

---

The quarantines of matter and life encourage us to ignore the vitality of
matter and the lively powers of material formations [...]. By vitality I mean
the capacity of things—edibles, commodities, storms, metals—not only

to impede or block the will and designs of humans but also to act as quasi
agents or forces with trajectories [...] or tendencies of their own. [... Our]
analyses of political events might change if we gave the force of things

more due. 124)

We resist such ideas because we tend to reserve the notion of agency only for our-
selves. The idea of agency in a molecule or a storm, let alone an abstraction like
money, seems especially far-fetched. We also tend to think in terms of a hierarchy
in which “we” (for whatever value of “we”) are at the top, and agency must surely
diminish for anything “lower’”—a view reminiscent of the medieval Great Chain
of Being.!422! When we (hesitantly) extend “agency” to the nonhuman, we tend
to do so only for things that act obviously, individually, and on fast timescales,
rather than in the aggregate and on slower, more evolutionary ones. It might be

time to re-examine these ideas more holistically.

My purpose here is not to follow in Bennett’s footsteps—though I do find her
project worth taking seriously. Language is, necessarily, imprecise, no matter
what definitions we pick.“4) This doesn’t mean that words are useless, though.
When our language can become more rigorous and scientifically grounded, and
when we use it to describe consistent patterns uniting a wide range of observa-

tions, we can start to see through ideological thickets.

I hope I have explained both clearly and rigorously how the phenomena that
give rise to the complexifying dynamics of life apply much more broadly than to
the entities we normally think of as “alive” or “agential.” Accordingly, we could
expand our definitions of these existing words, or adopt new ones, or do a bit of

each. Personally, I would find some broadening of the old everyday words helpful.

That would hardly break new ground. Many traditional, nominally “prescientific”
worldviews embrace notions of aliveness, agency, and even personhood that are
far broader than the modern Western ones. This seems a likely case of convergent
evolution in languages and ideas, motivated by the common need among tradi-

tional societies to take symbiosis seriously to secure their own survival, and to

---

flourish. Taking a broader view is practical as much as it is spiritual: encouraging
richer modeling of agency in “nature” enhances a society’s dynamic stability,

since all things in “nature,” ourselves included, are so mutually interdependent.

Thus it can be useful to take the view of an animal, plant, or river at times, even if
they can’t take ours, the better to care for them—and for ourselves. The same goes
for the Earth as a whole. That, ultimately, is the best reason to consider adopting,
or at least adapting, a more inclusive view of the animate. Potawatomi writer and
biologist Robin Wall Kimmerer makes this case eloquently in her book Braiding
Sweetgrass. U2)

In agreeing with Kimmerer, I am not encouraging superstition. When scientists
castigate animist beliefs as superstitious, they typically appeal to the materialist
discoveries of the Enlightenment, which show that the atoms that make up our
bodies are no different from the atoms that make up rocks or air. This is true.
Atoms are atoms; they all obey the same rules. Hence, the Enlightenment model

of a clockwork universe, governed by dynamical laws.

Yet as Schrédinger pointed out in 1944, our understanding of these laws—which
he played such a central role in developing—remains incomplete. The laws as
they stand do not account for the computationally complex, dynamically sta-
ble, symbiotic phenomena that comprise so much of our experience on Earth—
indeed, without which there would be no such thing as experience at all. There

would be no life, or purpose, or minds, or agency.

As we both embrace scientific rigor and start to figure out those “other laws
of physics’ hitherto unknown,”/22! we should perhaps be less surprised to find
the shoe on the other foot. What the poet Dylan Thomas called “the force that
through the green fuse drives the flower”+® drives all atoms, not just the ones

we presume to be alive.

---

# Chapter 2

2. Survival

Being in Time

I hope I have now convinced you that life is inherently computational, though
we've only scratched the surface of what it actually computes. The minimal
functionality for a dynamically stable life form is, of course, replication, or, more
precisely, self-construction. Open-ended evolution requires a von Neumann con-
structor, which is necessarily also a full-fledged Turing Machine. The constructor
makes it possible to build complex and recursive structures like a tree’s branches

or an animal's circulatory system.

But the environments in which construction and replication take place look
nothing like the pristine grid worlds of von Neumann's cellular automata. The
real world is messy, ever-changing, intrusive. To maintain any kind of integrity
in such a world, a computational system needs a protective boundary.24 Yet the
boundary can't be absolute, because life can never be self-sufficient: computation

requires energy, and self-construction requires matter.

Outputs are necessary, too, because neither computation nor growth can be
perfectly efficient. Computation generates heat, which has to go somewhere.
And not every atom that enters a living system can become a functional part

of it. Since matter and energy can’t be created or destroyed, an organism must
therefore shed matter (excretion) and energy (waste heat). Like a vortex, lifeisa

dynamical pattern that can only exist in the flux of a larger environment.

The sort of computation we call “intelligence” thus arises because of this need
for life to interact with its surroundings. Those surroundings invariably include
other life forms, opening the door to higher levels of symbiosis, as will be dis-
cussed later in the book. Here, though, we'll explore intelligence at its most basic:

in single-player mode.

Imagine a simple, single-celled life form—say, a bacterium. Its cell membrane
separates a “self,” on the inside, from the outside world. But, as mentioned, the

separation can’t be total. Studded with pores and ion pumps, able to ingest nutri-

---

ents and excrete wastes, cellular membranes are selectively permeable to matter

and energy—just like our bodies.

That also makes them permeable to information, because matter and energy
aren't generic. A potassium ion isn't interchangeable with a calcium ion, anda
red photon isn’t the same as an ultraviolet one. These inputs will have different
effects on the organism. Thus, every input is also, necessarily, a kind of sensor.
Given the value of sensory information for an organism’s survival, some inputs
have evolved to be primarily informational. A receptor may “taste” a molecule
without actually pulling it through the membrane, for example. The point is to

gather information.

To process that information, a bacterium has something like a “brain.”“! It
consists of a dynamical network of interacting genes and proteins that are both
affected by sensory data and can control cellular processes and behaviors. This
biochemical “brain” also receives inputs from within the cell, such as metabolic
status and available energy, allowing internal states like “hunger” to modulate

behavior.

Some bacteria can swim, using a corkscrew-like bundle of motorized filaments
called a “flagellum”—though steering, in the usual sense, is impossible. Due

to the simplicity of the bacterial body plan, the irrelevance of gravity, and the
molecular buffeting that characterizes life in water at such small scales, the cell
can’t distinguish left from right, or up from down. When swimming, it can only
“run,” rotating its flagella clockwise to propel itself forward, or “tumble,” running
some of its flagellar motors in reverse and causing the cell as a whole to spin

chaotically, randomizing its orientation.

---

Aclassic series of studies by biophysicist Howard Berg and colleagues in the

1970s shows how, simply by tumbling more often when food concentration is
dropping and less often when it’s rising, bacteria on average swim toward places
with higher food concentration—a behavior known as “chemotaxis.”“22! They
can use the same approach to swim toward warmth (“thermotaxis”) or, for pho-

tosensitive bacteria, toward light (“phototaxis”).

Not that a bacterium can directly measure concentration, temperature, or light
level, let alone differences in these properties along its microscopic body length.
It's just too small. Relative to every relevant feature of the world it lives in, the
bacterium is point-like; one could almost say that it exists only in time, not in
space. That is, it experiences life as a sequence of events, and anything it might
learn or observe about its spatial environment can only be inferred from that

event sequence.

These events are all discrete, or “digital,” even when they relate to continuous
physical quantities, such as chemical concentration—because at bacterial scale,
chemicals are only sensed one molecule at a time, as they dock and undock with
receptors on the cell membrane. Photon absorption and temperature-dependent

chemical events are quantized too.

While these discrete events are individually random, the ambient concentration,

temperature, or illumination determine the rate at which they occur. Hence,

---

a nominally continuous variable like concentration can only be estimated by
counting such molecular docking events within a time window, effectively calcu-
lating a moving average. If the bacterium is swimming, and concentration varies
over space, then a statistical tradeoff must be made in the estimation process.
Counting for longer allows concentration to be estimated more accurately, but at
the cost of washing out changes over time (or equivalently, over space). Bacteria
are smart about this tradeoff, adapting their concentration estimation strategy to

the situation {2

Let’s explore how the estimation process works in more detail.

Batting Average

From a bacterium’s perspective, chemical concentration is a running estimate
of the likelihood of future encounters with a molecule given a history of past
encounters with it. In more technical language, if we call the sequence of molec-
ular encounter events X, then the concentration is a time-varying estimate of the

probability of X, which can be written as P(X).

If this mathematical notation takes you out of your comfort zone, let me try to

make it up to you by offering an analogous situation from outside mine: baseball.

Here’s my naive understanding of the most famous statistic in sports, the batting
average. Every time a baseball player is at the plate, they may either succeed,
which we could represent as a one, or fail, which we could represent as a zero.
Success often involves hitting the ball, but apparently certain ways of hitting it
don’t count, and other apparent failures, such as the “sacrifice fly,” are actually
not? (If hadn't furtively brought a sci-fi novel to the one baseball game my
American relatives dragged me to when we moved to the US, I might have learned
these things earlier.) Anyway ... over time, a player’s batting history can be repre-
sented as a string of ones and zeros, with a single bit produced every time they’re
at bat. The proportion of ones—in other words, the average value of all those ones

and zeroes—is a player’s batting average.

---

We can study the data more closely, because baseball nerds have put the complete
batting histories of Major League Baseball (MLB) players online, going back many

decades.

Consider Henry “Hank” Aaron, widely held to be one of the greatest players of

all time. During a long career in the Major Leagues, from 1954 to 1976, Aaron
stepped up to the plate over twelve thousand times, and 30.5 percent of the time,
he successfully hit the ball and got on base, or better. This “.305” average is con-

sidered awesome.

No player’s performance is constant over time, though. It’s easy to see this by
calculating batting averages for individual seasons (spanning six months every
year, from April through September). Now, we can see that over the first few years
of Aaron's career, his batting average went up, peaking at over .350 in 1959. Like

anything else, baseball has a learning curve.

<i ch aie ey

FX ft a \

a 234 { ‘. \4 Gag

4 ‘ ‘ esata! | ice ea \| cas} ota kl | 4

ase] / J mal "i er Av 4 Lait |

oa ‘ A da Vy \| ay ry aN I, |

é. osky Vays ’ iC ‘ i! \\

2 oa \ vi 2.46 Ula

i

ra S oul ' “ae !

mS GD STEW 55 GOS we OUPAS mS DS TST

But alas, bodies age, and small injuries accumulate. His performance declined,
first gradually, then more sharply; by the end of his career he was batting below
.250. By that point he was going up to bat only half as often—no doubt, because
the manager was keeping a close eye on batting averages, and as Aaron's declined,

he was increasingly sidelined.

We've gone from considering career averages to six-month season averages, but
nothing prevents us from averaging over shorter windows—three months, two

months, or even single months. This finer-grained analysis brings new informa-

---

tion into view, up to a point. Using three-month windows, we can see that Aaron
reached his career peak just a few years before retiring, averaging an amazing
.378 between July and September of 1973. (He finished that year with 713 home
runs, just one behind the world record set in 1935 by Babe Ruth. Thousands of
letters to Aaron poured in, some from fans, others filled with hate and death
threats, from those appalled at the prospect of a Black man breaking baseball’s

most sacred record.)

Still, over time, not only had Aaron’s season average declined; his performance
had also become more uneven. So while the highs remained high, they were
interspersed with lower and more unpredictable lows. Hence a short averaging
window that would have been highly predictive early in Aaron’s career would

have shed less light on the future later on.

Part of the effect is simply due to lack of data. When we average over shorter
intervals, or Aaron goes to bat less often, the estimate becomes noisier because
there are fewer bits to average. In the limit, if our window shrank all the way toa
single at-bat, the “average” could only assume two values, 0.000 or 1.000, making
it useless as a predictor of future performance. Clearly, then, there’s an ideal size
of averaging window, large enough to accumulate decent statistics but small
enough to register changes over time. The ideal window size will depend not only
on the rate of at-bats, but also on how often a hit occurs and on how consistent

the player is.

All of this is to say: if X is a sequence of discrete events in the past, whether hits
for a baseball player or food-molecule encounters for a bacterium, P(X) smooths
those discrete events into a continuously varying average rate using an appro-
priately sized averaging window—which is also an estimate of the likelihood of
encountering such an event in the immediate future. Although this quantity is

a description of the past, it’s a predictive model. If no events have occurred for

a while, the likelihood is low; if a flurry of events just started, the likelihood is
high; if the rate has been increasing, then a good estimate will be higher than the
historical average, and if the rate has been decreasing, a good estimate will be
lower.24

---

So, are batting averages “real”? It’s obvious that Hank Aaron’s batting average
wasn’t a measurement of some physical quantity out in the world, or in his body
or mind—though neither was it unconstrained by the physics of balls and bats,
the psychology of pitchers, or the physiology of aging bodies. It didn’t have any
one true value, either, in that it could be estimated in many ways, and on many
timescales—though some estimates are better than others, in the sense of being
more predictive. Despite their fuzziness, though, batting averages matter to play-

ers, managers, and fans alike, because they both predict and affect the future.

The same applies to the kind of statistical measurements that matter to bacteria.
Like billiard balls, molecules are discrete objects, subject to microscopic physical
laws that don't in any way involve or require macroscopic concepts like “concen-
tration” or “temperature.” But if a bacterium needs to predict its likelihood of
encountering food, it must estimate concentration based on recorded events, not

unlike baseball hits.

As described in chapter 1, Boltzmann's development of thermodynamics—the
Ideal Gas Law, for instance—defines quantities like pressure, temperature, and
concentration using mathematical models and approximations of the same kind.
These, too, involve counting molecules or events within a time window or spatial

box.

Instruments like thermometers or pH strips do the same using an experimental
apparatus rather than theory. So does a digital camera, by counting the photons
absorbed by each pixel. In short, just like batting averages, variables like bright-
ness, temperature, pH, and concentration rely on models: ways of predicting fu-

ture phenomena using past statistics.

(No) Things in Themselves

We can either conclude that properties like temperature are not “real”—a path
that ultimately leads to the solipsistic denial that anything is “real”—or we can

reappraise what it means for something to be real.

Outside pure math, “reality” can seldom be fully pinned down. We've seen how

a concept like “temperature” falls apart when we ask about how hot or colda

---

medium is as its pressure or density drops toward zero, where averaging is no
longer reliable. So, if we're asked a question like “What is the temperature of
outer space?” we should counter with more questions to answer meaningfully.
Is this about calculating how hot a satellite's solar panel will get? (Answer: it
depends entirely on which way it’s pointed relative to the closest star, and on
the shadows of any nearby moons or planets.) Is it about determining how com-
fortable your hand will feel if exposed to outer space? (Answer: don't doit.) Fora
bacterium adapted to a watery medium, these simply aren’t relevant questions.

One might as well ask a person, “How does a neutron star taste?”

Like taste, temperature is not a “thing in itself.""=41 It doesn’t pre-exist somehow
in an unobserved universe. It is, rather, an observer-dependent model whose
usefulness, from the observer's viewpoint, depends on its behaviorally relevant
predictive power. This is true not only of temperature, but of all the macroscopic
phenomena we care about and describe using language, like “musical note,”

“chair,” “bacterium,” or “person.”

It may even be true of phenomena like “an electron,” but here we run into limits
in our understanding of the universe’s fundamental laws. “Electron” may merely
be the name we assign to a certain kind of propagating disturbance in a quantum
field, or it may have some more fundamentally “digital” nature that physicists in-
vestigating the subbasement of reality could one day discover.24! And are quan-
tum fields themselves “real”? Who knows?

Whether electrons, photons, quarks, and the various associated elementary
forces are “real” and are observer-independent “things in themselves,” higher-
order objects or features like temperature, pressure, chairs and tables, bacteria
and people seem, at first blush, to be mere ideas, or “epiphenomena.” The unob-
served universe doesn’t care about such ideas; after all, the continued existence of
a chair doesn’t depend on whether someone is around to conceive of that bunch
of atoms as “chair.” Atoms everywhere are governed by the unthinking laws of
physics,“24)

The mathematician John Conway's “Game of Life” offers a useful illustration. It’s
not really a game, in that there are no players, no score, no winning or losing. It’s

just a set of rules that describe, given the state of the game board, what its next

---

state will be. (This should sound familiar. Conway’s Life is, in fact, the most fa-

mous example of a cellular automaton, though von Neumann didn't live to see it.)
The rules are simple:

1. Like pixels or graph paper, the world consists of a grid of square
cells.i25)

2. Each cell can be “alive” or “dead.” We can visualize these states by col-
oring them black (alive) or white (dead).

3. At every time step, the state of each cell is determined by the state of
that cell and its eight neighbors during the previous time step.

4. If the cell is alive, then it stays alive only if it has either two or three live
neighbors.

5. If the cell is dead, then it springs to life if it has exactly three live

neighbors.

Under these rules, an entirely dead board will remain dead forever; that is a so-
called “fixed point” or “steady-state solution.” As you can easily confirm with pen
and paper, a 2*2 block of live cells on an otherwise dead board is also a steady

state.

Conway and others have discovered that Life's simple “physics” can produce
many interesting higher-level phenomena, too. For instance, certain config-
urations of five live neighboring cells form a stable four-state cyclic pattern

that appears to move diagonally through space, called a “glider.” A more complex
configuration of cells forms a “glider gun,” in which a piston-like reciprocating

mechanism pumps out an endless stream of gliders.

---

-

In the Game of Life, one can build a lot of complex machines using a few simple
ingredients like gliders and glider guns. In fact, it has been proven that, like

von Neumann’s original cellular automata, Life is Turing complete; despite its
simplicity, an enterprising engineer can create a general-purpose computer in
Life.l'*°! (In a particularly striking feat of recursive nerddom, the computations
required to simulate Life have even been programmed in Life! This has to be
seen to be believed.) It follows that the seemingly trivial universe of Life could
carry out arbitrarily complex computations, including, perhaps, a simulation of

our entire universe.)

Once a system can compute, its underlying physics become irrelevant to that
computation—remember that, per Turing, all computers are equivalent. There-
fore it's just as valid to say that the computation doesn’t care about the physics as
to say that the physics doesn’t care about the computation. This will matter to us
later on, as it allows us to understand functionality in a living (or intelligent) sys-

tem without needing to understand its underlying mechanism.

A die-hard physicist, though, can justifiably insist that neither gliders nor any

of the infinitely complex things one can build in Life are “real” or “things in
themselves,” in the sense that the rules of Life don’t involve any such objects.
There are only dead and live cells, and the elementary rules for determining their
next states. These facts, and these facts alone, comprise Life's “Theory of Every-

thing.”2*! Anything further is in the eye of the beholder.

---

As beholders, though, we can certainly see gliders. They appear to be real enough.
What do we mean by this? We mean that, if we recognize a glider configuration,
we can immediately predict what will happen next: it will cycle through four
states and move diagonally until it encounters an obstacle! If the glider were
the only thing on an otherwise empty, infinite board, we could, with a single
glance, predict every future state of the entire board, for all time. Compared to
brute-force computation of the future state of every cell on the board, the effort

saved is ... well, infinite.

We could say, then, that gliders are real only and precisely because, as a concept
or model, they are useful for predicting the future whenever the glider pattern
arises. Recognizing and understanding gliders allows simulation without simu-

lation.

Furthermore, the glider pattern is highly relevant in the Life universe, because the
pattern is so simple that it tends to arise spontaneously. Meaning: if we imagine
Life being played out on a large board where cells occasionally flip at random,
gliders will form frequently. And when they do, we will immediately be able to
predict their future trajectory—until and unless they are disrupted by noise, or

by running into something.

Anthropic Principle

From a mathematician’s point of view, patterns like the glider and glider gun are
special in that they correspond to “limit cycles”—generalizations of the idea of
steady states (like the 2x2 block) to endlessly repeating loops of states. According
to quantum field theory, the patterns we call “electrons,” “photons,” and “quarks”
are much like gliders: stable (though oscillating) solutions to underlying field
equations that don’t explicitly define such objects. This, too, should sound famil-

iar: we've just encountered dynamic stability again.

Seen this way, gliders and elementary particles are simply the earliest steps in an
evolutionary process, according to the maxim that whatever persists exists (and

conversely, whatever is too dynamically unstable to persist ... doesn’t).

---

Evolution doesn’t have to stop there. If eight gliders collide in just the right way,
they will “react” to form a glider gun.““4! And not only is a glider gun stable; it
also creates more gliders! Glider guns and a few other simple objects that can
arise through glider collisions are the basic ingredients for building a Turing

Machine.

Could Conway’s Life lead to abiogenesis, just as bff does? In our universe, that
route involved primordial fields coalescing into elementary particles, electrons
and protons coalescing into hydrogen atoms, the condensation of stars, the cre-
ation of increasingly heavy atoms through fusion, the formation of planets, and

the subsequent events described at the beginning of chapter 1.

This may offer a solution to the age-old puzzle of why our universe seems to be so
finely tuned for complex life to arise. As physicist Stephen Hawking wrote inA
Brief History of Time, “The laws of science [...] contain many fundamental num-
bers, like the size of the electric charge of the electron and the ratio of the masses
of the proton and the electron. [...] The remarkable fact is that the values of these
numbers seem to have been very finely adjusted to make possible the develop-

ment of life.”-4*4!

For Hawking, and many others in the physics community, our very existence is
thus evidence that many universes exist, for if there were only one, its compati-
bility with life would be a miracle ... and physicists don’t believe in miracles. In a
“multiverse” where the laws of physics vary between universes, the observation
that our universe seems finely tuned to support our existence would simply be
due to an observer bias known as the “anthropic principle”: of course the universe
we happen to observe is finely tuned for life, because nobody could be around to
observe the vastly greater number of sterile universes. It would be as absurd to
claim that we're “lucky” to live in this universe as it would be to claim that we're
lucky to live here on Earth and not on Mars, or inside the Sun, or in interstellar
space—in short, in any of the vast number of places in the cosmos inhospitable to

life,

This so-called “weak anthropic principle” is certainly correct. There are no poor
“unlucky” people on Mars because no people are on Mars, period. It is, however,

quite a leap to go from a puzzling observation about the life-friendly fine-tuning

---

of physical laws to the “strong anthropic principle,” holding that any and all con-
ceivable laws of physics must hold somewhere. Physicists should be uncomfort-
able with miracles, but many are equally uncomfortable with a multiverse where

any and all laws exist. Is this really required to account for our own existence?

A more economical explanation is that the fundamental rules of our universe,
like those of bff and Conway’s Life, allow for computation—evidently a much
lower bar than allowing for life as we know it.*4! Multiple universes may or may
not exist, but, either way, perhaps ours is not so special. Given a noise source, the
simple logic of dynamic stability will select for stable entities, which can then
start to combine into progressively higher-order dynamically stable entities:
quarks into nucleons, electrons and nucleons into atoms, atoms into molecules,
and so on. Entities like these can be understood as “proto-replicators,” subject to
the tendency toward increasing complexification and computation described in

chapter 1.

If the rules had been different, the “proto-replicators” would be different, and
life’s software would have ended up on a different computational substrate.
Perhaps quarks and electrons weren't the only viable option. Indeed, even with
the same rules, each evolutionary stage offers an expanding menu of possibilities.
DNA isn't the only possible information carrier, nor are amino acids the only pos-
sible “Lego bricks” for protein-like molecules. There’s certainly no reason all life
on Earth should rely exclusively on right-handed sugars, as opposed to their mir-
ror-image versions, the left-handed sugars. Regardless of such “just so” choices,

the end result would be the same: replication, computation, and life.

Darwin may have been right in yet another way, then, when he wrote of abiogen-
esis that “one might as well think of origin of matter.” He was being facetious, but

—why not? Matter might have evolved too.

The Umwelt Within

In describing Conway’s Life, we've allowed ourselves a third-person, God's-eye
view of a toy universe. But let’s now return to the bacterium living in our own
world, pointlike relative to its vast watery environment, yet, on the inside, full of

complex molecular machinery; technically brainless, but not unintelligent.

---

We've seen that the bacterial “brain” implements an adaptive algorithm for esti-
mating chemical concentration as it swims, and it seems natural to call this mea-
surement “purposive,” since it certainly looks like the goal is to eat and to avoid
toxins—in short, to survive. I've argued that the very notion of “concentration”
is something the bacterium appears to construct in the service of that purpose;
chemical concentration is, to use pioneering biologist Jakob von Uexkull’s word,

part of the bacterium’s umwelt: its “universe of the meaningful.”-**!

Later, we'll explore how the powerful social aspects of predictive models affect
the future, but, for now, let’s stick to single-player mode. It’s not hard to see why a
bacterium would care about its “batting average,” the rate at which it encounters

molecules it can eat.

How much that rate can vary, and how low it can go, will of course depend on
how depleted its reserves are. That’s why part of the bacterium’s umwelt is also its
internal state; let's call that state H, for “hidden.” In general, H includes a “comfort
zone,” surrounded by a “danger zone”; beyond the danger zone lies death. In the
simplest case, if we suppose that H represents the amount of available food in-
side the cell, estimating the “health-o-meter” P(H) will look like the same kind of
smoothing process as that used to estimate P(X), but now based on discrete inter-

nal metabolic events H rather than measurements of the external environment X.

An organism’s “job #1” is to keep its internal estimate of P(H) in the comfort zone:
this is “homeostasis.” The bacterium does this via actions, which we could also
represent as a set of discrete motor events O (for “output”). These actions may be
visible from outside—such as reversing the flagella to tumble—or they may be
internal, such as turning on or off a gene or metabolic pathway.“ Either way,
homeostasis involves performing actions O given external observations X that
maintain H within the comfort zone. This is intelligence in its most rudimentary

form.

It’s common to suppose that something like “reinforcement learning” is at work
here, allowing the organism to learn to perform any needed actions based on
feedback that can be positive (“feeling more comfortable”) or negative (“feeling
less comfortable”). However, the whole idea of grounding the emergence of intel-

ligence in reinforcement learning—or supervised learning of any kind—implies

---

an oracle that can administer rewards and punishments, or give correct answers.
Where did this oracle come from? How did it become intelligent? Maybe there is

no such oracle!

It's simpler and more general to think about the evolution of intelligent behavior
as arising from “unsupervised” learning (or, as it’s sometimes called now, self-
supervised learning“““) of the combined or “joint” probability P(X,H,O). Bacterial
populations that learn this joint probability distribution will not only “know”
how to estimate nutrient concentration and their own internal state, but also,
within some operating envelope, “know” what the consequences would be of act-

ing in various ways under different internal and external circumstances.

Critically, this joint distribution is a prediction of self as well as environment—
and of the consequences for oneself of various possible actions. The joint distri-

bution includes all of the below “knowledge”:

How to tell if you're hungry;
How to measure food concentration;
How your next actions are likely to affect future food concentration; and

How much less hungry you will be when you get that food.

Thus, the joint distribution contains everything one might want to “know” about

how to behave to stay alive—at least, with respect to food.\‘*%)

Going forward, I'll drop the scare quotes around “know” and “knowledge.” I’ve
used quotes for two reasons. One reason is deep, and the other less so. The deep
reason has to do with the distinction between a passive, abstract model and a real
agent, whose predictions include actions that it takes and that determine the fu-

ture. I'll discuss this in more detail shortly.

But first, let's dispense with the shallower reason for the scare quotes: the distinc-
tion many cognitive scientists draw between knowledge and competence. The
phrase “competence without comprehension” has often been used to describe
the way an agent can act as if it has knowledge without, apparently, having that
knowledge.**! Never mind bacteria; human baseball players or race-car drivers
have amazing physical intuition in their domain of expertise, yet most baseball

players wouldn't be able to explain or reason about parabolic trajectories in gen-

---

eral, and most race car drivers don’t know the equations for friction or centripetal

force. So, do they “know” physics, or not?

This sounds like a more profound question than it really is. Math, physics, and,
for that matter, the ability to explain things using language are all skills or com-
petencies in their own right; none of them follows from learning how to swing
bats, catch balls, or drive race cars—or vice versa. Plenty of nerds know physics
well enough, but are so clueless about sports that they may need to look up what
“batting average” means on Wikipedia. (Thank you, Wikipedia.) And of course
symbolic math and language are far out of reach for an agent with the very lim-
ited computational capacity of a bacterium, even when such an agent’s learned

competencies approach mathematical perfection in some practical domain.

As we'll see when we explore large language models in chapter 8, symbolic skills
and capabilities, like language and math, can also be fully represented as joint
probability distributions—albeit enormous, complicated ones. Most of us who
both know physics and have an intuitive understanding of how to drive or swing
a bat don’t connect the two domains much, but, for some people, mathematical
thinking and those physical intuitions might be closely associated, just as the
sound of a voice and the motion of a speaker's lips are; either way, it’s all in the big

overall joint distribution P(X,H,O).

Latent Variables

Learning P(X,H,O) efficiently—that is, successfully representing it without
exhaustively memorizing the probability of every individual combination of
circumstance, state, and action—requires data compression. Without such
compression, the size of the model, even for a simple organism like a bacterium,
would be unwieldy; learning the model would therefore be very hard, and storing

it or evaluating it would be expensive.

As we've seen, data compression involves finding patterns in data and factoring
them out. For symbolic data, which are usually compressed “losslessly” by algo-
rithms like those used for ZIPping files, such patterns generally take the form of
repeated sequences. When the data are instead continuous and the compression

is “lossy,” like that of MP3 audio or a JPEG image, finding those patterns allows

---

irrelevant details to be ignored, exposing a smaller number of meaningful “latent

variables,”"25l

For the bacterium, the concentrations of molecules that bind to receptors are
important latent variables. To see why, imagine the bacterium has one hundred
receptors that bind to some chemical of interest, like aspartate (for E. coli, that’s a
“yum"), Each receptor can be occupied or unoccupied by an aspartate molecule.
Let’s suppose (I’m just making up numbers here) that occupancy is measured in
millionths of a second, and the bacterium encounters between zero and a thou-
sand aspartate molecules per second as it swims. Since the state of each receptor
can be thought of as a binary digit, O for unoccupied and 1 for occupied, these
hundred receptors produce a raw information stream that amounts to a hundred
million bits of information per second. That’s a lot of bits per second, around ten

times what it takes to transmit 4K video,2!

Luckily for a bacterium’s little brain, the overwhelming majority of this infor-
mation is either useless or redundant. Since the cell is so small and there are no
meaningful concentration differences along its length, it doesn't matter which
receptors are occupied—the receptors are “symmetric,” making any meaning ex-
tractable from them “invariant” to this symmetry. So we might as well just add all
of these bits together.

Even when added up, the total is almost sure to be either O or 1 at any given time,
because the occupancy time is short and the concentration is low. That means
we're already down to a mere one million bits per second. Then, when we con-
sider that the exact timing of the docking events doesn’t matter—meaning that
there is “local time symmetry,” or invariance to the precise timing of the docking
events—we realize that we can just add up all of the ones each second, giving us

concentration as an average occupancy rate over a one-second time window.

So, we're back to averaging over a time window, as for calculating a batting av-
erage. That single number per second, which can be represented with only a few
bits, accounts for the great majority of the real information coming in through
those hundred receptors, though a little more information can be squeezed out by

making the averaging window adaptive, as mentioned earlier.

---

Evolution will have honed in on something close to this compression scheme,
because it sieves the useful information out and discards everything else. Such
compression makes the overall distribution P(X,H,O) learnable, because the
patterns relating X to H and O can only be generalized if the welter of irrelevant
detail in X has been cleared away. In the language of information theory, the use-

ful parts of X are the “signal,” while the discarded parts are the “noise.”

Remember, this signal is useful precisely because it’s a continuous estimate of the
likelihood of a future docking event—though note that this continuous estimate
is itself represented as discrete, stochastic signaling events within the cell, so

in calling it a continuous number, we're doing some modeling of the model. But
we're getting ahead of ourselves. More importantly, we've arrived at a practical
definition of chemical concentration simply by thinking about what is relevant
to the bacterium’'s future given its past. Concentration is real because it’s predic-
tive, just as the temperature of an oven is real for you because knowing it will
allow you to predict whether your food will cook in there, or your finger will burn

if you touch it.

Hunger is much the same. Just as the exact sequence of molecular encounters
that led to a given estimate of the concentration is irrelevant, the exact sequence
of energy-consuming actions that led to a depleted energy state is irrelevant;
what matters is that death will occur without more food. Hence hunger is “real”
in exactly the same sense—and for the same reason—that concentration is “real”:
both are useful latent variables for efficiently modeling P(X,H,O). That one of
these latent variables is an estimate of conditions outside the cell, while the other
is an estimate of conditions inside the cell, will become interesting as we consider
social relationships between cells. But for our solitary bacterium making its way

in the world, there is no difference.

Modeling

So far, I've argued that modeling a single joint-probability distribution,
P(X,H,O), is enough to establish the reality of both regular features of the external

world (like temperature, concentration, and brightness) and of the internal life of

---

an organism (like hunger). I haven't explained how such models arise, or why or-

ganisms with models appear to be purposive.

I've also been deliberately vague about the word model, shifting its usage back
and forth between noun and verb. As a noun, we often think of a model as
something disembodied, perhaps an algorithm or set of equations represented

in abstract form. A one-dimensional linear model, for example, can be written
f(x)=wx, and is fully specified by the single number w.**! The billions of parame-
ters in a large machine-learned model are no different—they just take much more
space to write down. As a verb, “modeling” may mean learning or approximating
w (or, equivalently, billions of parameters, often expressed as a giant matrix of
“weights” w, between artificial “neurons” i andj) from training data; or it might
mean evaluating the resulting model, that is, actually calculating f(x) for a given

x.

A living organism is clearly more verb than noun; “verb-ness” or, to use a more
resonant term, “agency,” is precisely what distinguishes living things from dead
things. Living things do stuff of their own accord; nonliving things don’t.

A bunch of parameters, printed out on a giant ream of paper and shoved into a
closet never to be seen again, are certainly not a living thing. They are just inert
matter ... dead information. (Much like the reams of DNA still coiled inside the
cells of an animal after it has died.) Even to call those numbers information may
be overstating the case, since if no reader exists—no active process making use
of those printed numbers to do something—they might as well be gibberish, or
blank. It would make no difference. And information is, as the anthropologist
and philosopher Gregory Bateson memorably put it, “a difference that makes a

difference.”24!

The noun and verb senses of model differ from each other in much the same way
a mathematician’s definition of the word function differs from that of a practical
programmer. For a mathematician, a function is an abstraction; it could be un-
knowable in practice (like the oddness or evenness of the number of pennies in
circulation at any given moment) or even fundamentally non-computable (like
whether an arbitrary mathematical statement is correct!+*2)), Interesting as they

may be in theory, for a programmer, such “functions” are nonsense. Program-

---

mers only care about functions that can be implemented by running actual code

that can function, or that, if buggy, fail to function.

Relatedly, remember that the O in P(X,H,O) stands for “output.” Life must act (yet
another word for “function”). A living thing is a process, not a printout or a math-
ematical abstraction; so these actions have to be taken—or the process is discon-

nected from the world, and, causally speaking, the model may as well not exist.

In the so-called “autoregressive sequence prediction” setting used by many un-
supervised AI models today, the action with maximum probability according to
P(X,H,O) is generally taken. At the next moment in time, the action taken, along
with any new observations of X and H, becomes part of the past, and the model
is evaluated again. Hence every action depends not only on past observations,
but also on past actions. An organism is therefore modeling itself jointly with the
environment, and, in so doing, is carrying out agential or “verb-ish” modeling. It’s

running its own program in a continuous loop.

I’ve expressed the program as a probability distribution rather than in the more
obvious way a programmer might, as a deterministic function mapping input to
output, o=/(x,h), for two reasons.*4) First, as we've seen, biological computing

is stochastic, so actions need to be thought about in terms of probabilities, not
certainties. That’s true of AI models too; with nonzero temperature, as generally
used in chatbots, the action taken is drawn from a probability distribution, rather
than being fully determined by the inputs. Second, those actions are not just out-

puts, but also inputs at the next moment in time.

A “strange loop” is at work here.|!2"! Because the model is joint, all senses are
active: not only do actions taken depend on interior and exterior percepts, but all
percepts also depend on actions. In our chemotaxis example, for instance, any
perceived change in nutrient concentration, and its interpretation, will depend
on whether the bacterium is swimming forward or tumbling in place—which
itself depends on perceived nutrient concentration. Further, the model is always
modeling itself, in the sense that it predicts its own future states and actions in
addition to predicting its environment. We could even say that it predicts its own

predictions, in a kind of infinite regress.

---

Life is a hall of mirrors.

Learning by Evolving

The active modeling described above seems to leave no room for learning—
only for doing, or, in mathematical language, function evaluation.!*"! But where
does the function constantly being evaluated, P(X,H,O), come from in the first
place? This question sounds a lot like the puzzle of abiogenesis, and that’s no

coincidence.

As far back as 1948, Turing realized that evolution could be understood as a trial-
and-error learning process.>" It may seem crude and inefficient, but it is the
necessary bootstrap to any more sophisticated kind of learning. Everything that
learns either learned to learn by evolving, or was designed by entities (so far,

human) who themselves learned to learn by evolving.2“°)

Suppose we have a world in which bacteria have already somehow arisen; and
that, if they survive to do so, they can reproduce, in the process “cloning” their
P(X,H,O) models to pass on to daughter cells. We are assuming, in other words,
that P(X,H,O) is encoded genetically. After all, if P(X,H,O) is a computable func-
tion, it can be implemented with code, and since the bacterium is a “self-repro-
ducing automaton” as von Neumann described, it already comes with a Universal
Turing Machine in the box. The bacterium’s computing resources will be limited,
and certain functions will be easier to express on that biological platform than

others, but any kind of computation is theoretically possible!

By virtue of being genetically encoded, the code is also open-endedly evolvable.
Not only can it improve via tedious, old-fashioned, million-monkeys-on-a-
million-typewriters point mutation; it can improve far more efficiently through
symbiosis, as described in chapter 1. Maybe, then, evolution, in its full self-modi-

fying glory, isn’t such a slow learning algorithm.U&!

So, what makes for a “fitter” P(X,H,O)? In short, one that is more dynamically sta-

ble. As a first approximation:

® Ifa high probability is assigned to being dead, that is, to H going beyond the

“danger zone” and into the “dead zone,” then, in a self-fulfilling way, the

---

model will predict—and take—actions that result in its own death. How-
ever, a fitter model will not suicide.“ It will assign the highest probabili-
ties to the “comfort zone,” with declining probabilities outside this zone.

© If the model isn’t accurate, consistent, or suitably general—failing to predict
death, or to account for the relationships between actions and states, or
its own future actions, including under novel conditions—then it will be
less fit than a model that is accurate, consistent, and general, hence good at
avoiding states leading to death.

@ If signals are available, whether internal (H) or external (X), that can help
with the above predictions, then a model able to avail itself of these signals
will be fitter than a model lacking them.

® Since modeling (the verb) is computationally costly (hence energetically
costly), a smaller, leaner model that predicts the future just as well as a big-
ger one will win, because it will starve less often and leave more resources
available for reproduction.

@ Asa bonus, model compression tends to go hand-in-hand with generality,
meaning that, all things being equal, a leaner model is also more likely to

continue to perform well under novel conditions.%!

In a resource-constrained environment, then, organisms with incrementally bet-
ter P(X,H,O) models will outcompete those with worse models, and, over many

generations, the modeling will become very good indeed.

Cause by Effect

The term good, applied to a model, can be interpreted in multiple ways. For data
scientists, a “good” model usually means one with a low error rate on held-out
test data, or that otherwise performs well on some predefined task. This measure
of goodness applies to a model (the noun), as opposed to a dynamic agent that
models (the verb). Measuring goodness does involve computational evaluation—
that is, resetting the model and bringing it “to life” very briefly, and many times,
computing its response to test stimuli. But generally no notion of time or agency
exists in such an artificial setting, and “goodness” is whatever the data scientist

says it is. This is the highly artificial setting of “supervised learning.”

---

On the other hand, a model that is “good” in evolutionary terms is one that works,
or at least works well enough, meaning that it effectively predicts the future. In
doing so agentially, it tends to bring that future about: a self-fulfilling paradox of
backward causality.

The apparent paradox arises because causes are supposed to precede their effects.

How could it ever be right to say that something happens because of its effect?

Yet colloquially, we do this all the time. Suppose, for instance, that I’m talking
with a friend at the coffee shop, then glance at the clock, jump up, and race out
the door, my coffee unfinished. A busybody at the next table wonders why I’m
madly careening off on my bike. My friend says, “Oh, it’s just because he’s running

late to the office again.”

This is an utterly unremarkable exchange ... but if you think about it, quite a
strange use of the word “because.” If a boulder is careening down a hillside, about
to squash a parked car, and someone asks why the boulder is doing that, there
might be all kinds of answers. Maybe a landslide occurred higher up, or it broke
off a cliff. We don't say it’s careening down the hill because there's a parked car
down at the bottom. The causes are uphill, in the past, and effects are downhill, in

the future.

In this light, an effect preceding its own cause seems nonsensical. Yet when it
comes to bacteria, people, and everything in between, the future, or a wishful
model of it (one in which you are safe, warm, well-fed, caffeinated, and make it to
the the office just in time), seems to influence the events leading up to it, rather
than those events inexorably determining the future.“ In fact, evolutionarily
speaking, only creatures with models that successfully predict their own future

even have a future!

Of course none of this happens in violation of the laws of physics—but, like life
itself (per Schrédinger), it certainly looks suspicious. In a deterministic universe,
how coulda “plan” or “intention” possibly affect what will just happen? (If you're
thinking that this sounds a lot like the paradox of free will: yes, it does. We'll get
to that in chapter 6.)

---

The answer comes from that strange loop inherent to autoregressive sequence
modeling. We've seen why the evolution of life implies the evolution of a “suffi-
ciently good” P(X,H,O) model. That model gives rise to actions in the world, but
the world also gives rise to the model. While the model can only have learned
from the past, it is a model because it can predict the future. When that predic-
tion informs its actions, we get something that looks like backward causality. The
more powerful the model—or, we could say, the more “intelligent”—the more

pronounced this effect will be.

Cognitive scientist Terrence Deacon calls systems exhibiting apparent backward

causality “entensional.”““! We could equally call them “agential,” “purposive,” or,
in a broad sense, “alive.”\!°°! Hence for the boulder rolling downhill, the car at the
bottom could only enter into the “why” of things if someone or something rolled

that boulder on purpose.

At this point, we've considered two senses in which a model can be called “good.”
For a data scientist, a model is “good” to the degree that it scores well on a test.

For a living organism, a model is “good” to the degree that it successfully predicts
the future—of the world, of the self, and of the effects of one’s actions on self and

world.

A third sense of “good,” connecting these two, is normative, as opposed to
descriptive: a model is good if it keeps the organism alive, because being alive

is good, and being dead is bad. Notice that this normative quality arises in the
evolutionary setting without anything like reinforcement learning, wherein an
external oracle or teacher metes out rewards and punishments. In fact, “punish-
ment” of an individual organism under Darwinian conditions is impossible, since
the only negative feedback is death, which will prevent any subsequent learning!
Rather, a taste for aliveness emerges from something like a tautology: dead things
don’t model; alive things do; their models successfully predict their own alive-

ness; ergo, it is “good.”

Goodness and Truth

While death itself is nothingness, states adjacent to death will be aversive to

any creature that has evolved with death acting as what physicists call an “ab-

---

sorbing boundary condition.” Being averse to death, in other words, is how not to
die. Aversion results in actions that are likely to move the creature away from a
“bad” state and toward a better one more conducive to survival. This normative
judgment, and the response to it, are the same for a bacterium swimming away
from a toxic chemical, a beetle fleeing a stomping foot, a rabbit evading a wolf, or

a human refugee escaping a civil war.

As we'll explore in chapter 4, animals need to internalize this kind of normative
signaling the moment they become multicellular. They do so using ancient neu-
romodulatory chemicals like dopamine and serotonin, which first evolved in flat-
worms and remain the basis of our own most elemental feelings, such as desire
and satiety. With our big brains and complex cultures, human ideas about what
is “good” or “bad” have become manyfold and nuanced, but they all trace back to

these evolutionary fundamentals.

An account of modeling in general as normative, foundational to life, and
arising from computation in living systems troubles some still-influential ideas
in Western philosophy. One is David Hume's “is/ought” distinction,““4 which
seeks to distinguish descriptive from normative statements. Hume privileged
description, which was a progressive idea at the time. He held that descriptive
statements ought to take precedence over normative judgments—and precede
them, or we wouldn't find it so irritating when people express opinions about
topics they don’t understand. For Hume, facts (“is” statements) are universal,

while opinions (“ought” statements) are merely personal.

While intuitive, the is/ought dichotomy falls apart when we realize that models
are not just inert matrices of numbers or Platonic ideas floating around ina
sterile universe. Models are functions computed by living beings; they arguably
define living beings. As such, they are always purposive, inherent to an active
observer. Observers are not disinterested parties. Every “is” has an ineradicable
“oughtness” about it. Our umwelten are what they are for good reasons—the
wavelengths we see or don't, the categories we distinguish or don’t, the variables

we deem salient or not.

Summing up:

---

1) All knowledge or understanding of the world is observer-dependent;
2) “Accurate” is best thought of as “useful for predicting the future”; and

3) “Useful” can be read as “good for someone.”

Philosophical “idealists” like Immanuel Kant (1724-1804) have made similar
arguments, as have more recent postmodern philosophers and critical theorists,
who profess to be skeptical about the very possibility of observer-independent
“is” statements. They are right, in a way, but their solipsism isn’t warranted.

We can mostly agree on a shared or “objective” reality because we all live in the
same universe. Within-species, our umwelten, and thus our models—especially
of the more physical aspects of the world around us—are all virtually identical,

statistically speaking. Merely by being alive and interacting with one another, we

(mostly) agree to agree.

---

The rarity of instances like The Dress, an internet phenomenon that went viral
in 2015, is telling. Some people perceive it as white and gold, others as blue and
black. This enigmatic photo is only ambiguous because it was taken under weird
lighting conditions; confronted with the actual article of clothing, everyone
agrees that it’s really ... whichever it is, Ican never remember. How we perceive

it turns out to depend largely on our prior expectations with respect to lighting.

Early risers see white and gold, while night owls (like me) see blue and black.|+°5!

¢
(A

Even between species, both a common biological toolkit and interlocking
umwelten tend to reinforce a consensus reality. Our interests, hence our models,
are all entangled, whether cooperatively or adversarially. Indeed, it can be hard to
tell the difference. A rabbit that fails to effectively recognize and distinguish be-
tween fellow rabbits and wolves is not long for this world. Nor is a wolf who can't
recognize dinner. Over evolutionary time, through this apparently adversarial
interaction, wolves and rabbits have cooperated to mutually shape each other’s

highly capable bodies and sophisticated world models.

The science-fiction writer Philip K. Dick once wrote, “Reality is that which, when

you stop believing in it, doesn’t go away."4°2! While an entity may ignore or var-

---

iously interpret many of its input signals, failure to understand the relationship
between those signals and its own future existence will result in future non-
existence. At a minimum, then, facts are models that work well enough not to kill

you.

Consensus is easier to achieve for X than for H. Two agents who (perhaps by
virtue of both being human) have similar sensory apparatus, similar survival
imperatives, share a common language, and are looking at the same dress, will in

an overwhelming majority of cases agree on its color.

On the other hand, a hidden state H by definition is not directly accessible to

an other. 1 can say that I’m hungry or tired or feel sad, but ... you'll just have to
take my word for it. Or not. Under certain circumstances, it can be important for
hidden states to remain hidden. Hence we become anxious when neuroscientists
develop methods to “read out” hidden states in our brains, or social media com-

panies seek to use algorithmic wizardry to infer our innermost desires U“)

Are Feelings Real?

The most rudimentary kinds of feelings are little more than physical signals:
hunger, cold, heat, thirst. For any organism that seeks to stay alive—that is, for
anything that is alive, as remaining so requires constant work—gauges and me-
ters like these matter. Is it time to sweat, or to shiver? Pick the wrong answer, and

your model might not be around to make any more janky predictions tomorrow.

For a bacterium, such gauges are chemical measurements, just like environ-
mental variables; they’re simply assessing conditions on the inside of the cell
membrane rather than the outside. That implies solving the same kind of com-
putational problem as for an external measurement. Finding the correlation
between a raw signal (like molecular docking and undocking events) and an
estimated property (like concentration, or hunger) requires a learned, and likely
adaptive, model. As organisms get more complex, both the signaling mechanism

and the model required to infer a variable like “hunger” become more complex.

Consider pain. In his 2023 book The Experience Machine: How Our Minds Predict
and Shape Reality, philosopher Andy Clark—whose take on the larger subject

---

of brains as predictors I agree with—describes a number of telling ways our pain
models can malfunction. Amputees, for instance, can experience phantom limb
pain. Similarly, many people live with chronic pain disorders, often beginning
with an acute injury or illness but persisting long after the physical damage has
healed.

On the other hand, many of us are familiar with receiving injuries, sometimes
serious, that don’t hurt at first—the pain only comes later, if at all, and some-
times seems to depend on our higher-level awareness of the injury. To cite one
gruesome example: in early 2005, a construction worker in Colorado experienced
what he perceived as a bruising blow from a recoiling nail gun at a job site. Six
days later, he visited the dentist, complaining of a mild toothache; he had been
icing it and taking Advil. An x-ray revealed that he had fired a four inch nail
through the roof of his mouth and into his brain. He recovered well following
surgery to remove the nail, but this tabloid story doesn’t inspire me to take on

more handyman stuff around the house“!

There's an opposite phenomenon too, in which intense pain accompanies a
mistaken perception of injury. Consider another story about an unfortunate
encounter between a construction worker and a nail, as reported in the British
Medical Journal in 1995.24! This worker jumped from some scaffolding onto a
plank, failing to notice the seven-inch nail projecting up from it, which pierced
clean through his boot, coming out the top. In agony, the construction worker
was dosed with fentanyl and midazolam. But in the emergency room, when the
doctors pulled out the nail and removed the boot, they found that the nail had

passed harmlessly between his toes.

---

As Andy Clark puts it, “Such effects seem much less surprising once we accept
that [...] ‘raw’ sensory evidence is [...] never experienced. |...] [RJesponses of the
‘pain receptors’ (known as nociceptors) are not what we feel when we're gripped
by asharp pain. Instead, those responses are simply one source of evidence [...].
That’s why we can genuinely feel pain even when nociceptor activity is absent.
We can also fail to feel pain even when intense nociceptor activity is present [...].
What we feel [...] reflects a process of unconscious inference [...] about [...] the

events causing our sensory stimulations,”74

Clark’s point is general: it’s not just about pain, but about the nature of reality,
both external and internal, and how that “reality” is made. Beyond Hume's
“js/ought” distinction, Classical and Enlightenment dogma that reality can be
cleanly separated from psychology is mistaken. The second construction worker
was not faking pain, any more than the first construction worker was pretending

not to be in much pain.

Neither Clark nor I would claim that reality doesn’t exist. Rather, we are using “re-
ality” to describe a purposive model with a high degree of social consensus and
good predictive power. We call the first construction worker’s belief that he was
uninjured “false” because that belief would not have predicted the dramatic x-ray,
or the urgent need for surgery. We call the second construction worker’s belief in
his injury “false” because his belief would have predicted that, when the doctors
removed his boot, they would find a bloody wound. When there was no such
wound, everyone realized that their model needed updating; and, as a bonus, the

man’s pain went away.

Unfortunately, it doesn’t always work so neatly. For people with chronic pain,
knowing that nothing is “wrong” doesn’t bring relief—just as for people with
arachnophobia, conscious knowledge that a pet tarantula is tame doesn’t make

the dread of touching that giant hairy spider go away.

---

# Interlude

Interlude: The Prehistory of Computing

Computing may be fundamental to life, intelligence, and everything, but its
history is tortuous, full of false starts and misunderstandings. To better under-
stand our conceptions and misconceptions about computing, we'll need to begin
well before Turing and von Neumann, connecting their work to its roots in math-
ematics, industrial engineering, and neuroscience. We’ll also need to take stock of

the social context surrounding its development.

This will be a short and curated, rather than definitive or comprehensive,
account. Its goal is to reassess our received wisdom about what computing is (or
isn’t), and its relationship to brains and minds, labor, intelligence, and “rational-
ity.”

Our prehistory of computing begins”! during the European Enlightenment,
with Gottfried Wilhelm Leibniz (1646-1716), the co-inventor of calculus, among
many other achievements. His “stepped reckoning machine” was the first me-
chanical calculator that could perform all four basic arithmetic operations, but

this was only a baby step in his far more ambitious agenda.4/4!

---

7

.

hb. a4 >

ma. »am waive a oe & &
Se at om aaa

At age twenty, Leibniz asserted that one day, we'd be able to formulate and
answer any question—not just in math, but in politics, economics, philosophy,
even in ethics or religion—using pure logic: “If controversies were to arise, there
would be no more need of disputation between two philosophers than between
two accountants. For it would suffice to take their pencils in their hands, to sit

down with their slates and say to each other [...]: Let us calculate [calculemus]."-2)

In imagining that accountants—human computers, really—could work out the
right answer to any question once properly formulated, Leibniz presumed the
existence of universal truth, both factual and normative: a Platonic world of pure,
timeless, and axiomatically correct ideas. He only needed to devise—or discover
—a formal language for expressing any proposition symbolically (he called this a
characteristica universalis, or “universal notation”), and an algebra for manipulat-

ing such propositions (a calculus ratiocinator or “calculus for reasoning”).\75) The

---

existence of God, the right of the Habsburgs to rule Austria, and the legitimacy of
same-sex marriage could all boil down to logical proofs, just like the value of pi.
And, if so, a descendant of the reckoning machine could eventually compute such

proofs mechanically.

This grand idea died a slow death over centuries, though, in a sense, the entire
field of computer science grew out of its moldering remains, like a sapling out of
a nurse log. Remember that the theoretical foundations of computing were laid
by Turing in his attempt to solve the Entscheidungsproblem in the 1930s—the
problem of finding a general algorithm for deciding on the truth value of a math-
ematical statement.“ This was Leibniz’s problem, albeit restricted to math.
The bad news: even in that purely abstract, formal domain, Turing proved that
no such algorithm existed. The good news: in the process, he invented (or discov-

ered) universal computation.

Although Leibniz worked on many other problems throughout his long career,
he never gave up on the quest for a universal symbolic language. It was his Holy
Grail. In a New Year's letter to the Duke of Brunswick in 1697, Leibniz excitedly
explained some progress toward this goal: numbers could be represented in
binary, using only the digits 0 and 1.*"! The letter sketched a design for a medal-
lion to commemorate this insight featuring an image of divine creation, noting
that it would be “difficult to find a better illustration of this secret in nature or
philosophy [...] that God made everything from nothing.”

---

AU VW. ANT APRs NM YOO AVI.

Because it was both a minimal representation for numbers and a natural notation
for yes/no logic, binary seemed the obvious basis for Leibniz's characteristica
universalis. George Boole (1815-1864), the self-taught nineteenth-century math-
ematician who formalized the Boolean logic at the heart of virtually all digital
computing, independently arrived at the same conclusion more than a century

later,U8U

In practice, though, the earliest “human computers” didn’t use any special nota-
tion or work out the answers to weighty questions on slates; in short, they didn't
resemble Leibniz's philosopher-accountants. They were out-of-work hairdressers
employed by a civil engineer, Gaspard de Prony (1755-1839), to crank out books
of logarithmic and trigonometric function tables for land surveyors to use after
the French Revolution."! (The hairdressers were out of work because many of
their former customers, Ancien Régime aristocrats, were losing their towering
hairdos, along with their heads, to the guillotine. Survivors, rich and poor alike,
were wisely opting to keep their hair short and plain.*2!) These hairdressers
may not have known higher math, but they were used to working carefully and

methodically. They had no trouble performing the elementary operations into

which each calculation had been decomposed: addition and subtraction.“*

---

Prony framed his project in industrial terms, boasting that division of labor
allowed him to “manufacture logarithms as easily as one manufactures pins.”
The reference to pin manufacture came straight out of Adam Smith's The Wealth
of Nations, the founding document of industrial capitalism.U*! Leibniz had
complained that “it is beneath the dignity of excellent men to waste their time in
calculation when any peasant could do the work just as accurately with the aid
of a machine.”*5! Although Prony’s hairdressers were not (yet) using machines,
they were organized to work like one.U24l And, of course, machines had already

been invented for adding and subtracting.

Pliste 185 The Pin Factory I

———

tel dpe At

Prony’s project greatly impressed Charles Babbage (1791-1871), designer of the
first general-purpose computer, the “Analytical Engine,” in the 1830s. Entirely
mechanical, the Analytical Engine would have been steam-powered and would
likely have taken about three seconds to perform an addition—far slower than

any electronic computer, but still faster than doing it by hand.2%!

Although known today as a hapless inventor too far ahead of his time (neither the

Analytical Engine nor its more modest predecessor, the “Difference Engine,” were

---

built in his lifetime), Babbage was no idle dreamer. He was in fact one of the In-
dustrial Revolution’s great architects and theorists; his most important book, On
the Economy of Machinery and Manufactures, was all about factory automation.
It was full of down-to-Earth engineering and entrepreneurial advice, gleaned

through close observation and obsessively backed up with productivity data.

v

---

Steampunk computing engines are just one (uncharacteristically speculative)
idea among many in Babbage’s book. He introduced automatic computing ina
chapter about the division of labor, noting: “The proceeding of M. Prony, in [his]
celebrated system of calculation, much resembles that of a skilful person about
to construct a cotton or silk mill, or any similar establishment.”= In short, like
Prony, Babbage sought to “manufacture logarithms.” Mechanical calculation was

simply a means to automate the jobs of Prony’s hairdressers.

The parallel Babbage drew to textile mills is telling, for his other great inspiration
was the Jacquard loom, patented by Joseph Marie Jacquard in 1804. Jacquard’s
machine made the mass reproduction of complex patterned fabrics possible

by encoding their designs as holes punched into a sequence of cards. Similar
punched cards were to be the data input and storage mechanism for the Analyti-

cal Engine.=

eh ll

Ir t i MW k :

In 1833, Baroness Anne Byron, an educational reformer and philanthropist, took
her seventeen-year-old daughter Ada, the future Countess of Lovelace (1815-
1852), to a soirée at Babbage’s house.!**) As Lady Byron wrote soon afterward,
“We both went to see the thinking machine (for such it seems) last Monday.

It raised several No.’s to the 2nd and 3rd powers, and extracted the root ofa

---

quadratic equation. [...] There was a sublimity of the views thus opened of the
ultimate results of intellectual power.” They had witnessed a demonstration of a
working prototype of the Difference Engine—as sophisticated a computer as any-

one then alive would ever see in operation. U2!

Despite her youth, Ada Lovelace (as she is usually called today) understood the
far-reaching implications of the machine. Over the following years, she became
Babbage’s intellectual collaborator as the incomplete Difference Engine gave way
to grander (and even less complete) plans for its fully programmable successor,
the Analytical Engine.

af Ce ere at
Ur Le QM QW )

~ ff he Te

fej te . rs fs)

i Tht wt Set

a ey aH, om rma, oat te wy ae, is) ved oe g
e's (SCI es ey

as navn Nane "ant Se? Na? aie Li a")
3

th il Hi i ul he i Ib
efi ia { ‘

In 1842, Lovelace translated a lecture on the Analytical Engine given by Italian

military engineer Luigi Menabrea, appending to it a series of notes far lengthier
and more insightful than the lecture itself. Note G includes the first published
computer program for the Analytical Engine—hence the first published program,
period. It calculated Bernoulli number sequences, which turn up often in math-
ematical analysis. As Lovelace famously wrote, “The Analytical Engine weaves
algebraic patterns, just as the Jacquard-loom weaves flowers and leaves.”“** This
observation was even sharper than it first appears, for she likely understood that

the algebraic patterns in real flowers and leaves are themselves woven compu-

---

tationally, producing the mathematical regularities of petals, veins, leaves, and
branches discussed in chapter 1.424

To what degree, though, should one think of a computer as a mere “loom” for the
mass production of mathematical tables? Babbage’s computing engines included
a beautiful design for a printer capable of creating stereotype plates of whole
finished pages. But there is a notable difference between the labor involved in
printing tables (or manufacturing pins, or weaving cloth) and actually calculating
those tables: the former kind of labor is physical, while the latter is mental.

This suggests a functional (not just metaphorical) analogy between computers
and brains. The analogy has been used liberally by journalists over the years; for
instance, in 1946, the Surrey Comet described Turing’s Automatic Computing
Engine (ACE) as an “Electric Brain to be Made at Teddington.”“*») When the long-
delayed ACE was finally completed in 1950, the newspapers once again referred
to it as an “electric brain,” “electronic brain,” or ‘brain’ machine.”24! We tend to
dismiss such headlines as old-timey clickbait, but this glosses over the genuine
insight behind Lady Byron's characterization of the Difference Engine as a “think-

ing machine.”

---

——— —_

F gat wma banane ONE Pl eT L veer wens ead. Aes pes ower i]
me * Ure ren of ee LE ee ian eres aoe DAW Mew Merny wnt Ah ttm bch toate Bin?
nae lhe Po etchant i 5 = ype ia ais Noe
a_i A 4
¥ ¥ r
QR abt yet amie nuecinoae ~=DALLY POST
“ yy CALCULATOR ne Wee

wir Meowty'e Woke i Minis AT LACEINE aby Se
ome prim ca Sips Sever “Towa wares | do Sieh) i |

on i os Py stay tm meat
ay es st DEUTER S) OT
Cea

Eacwiny Parctctt etal

Nowadays, we prefer terms like “information processing” to avoid the baggage

of consciousness and subjective experience implied by words like “thinking”

and “mental,” but we should keep in mind that, to a committed industrialist like
Babbage, subjectivity simply wasn't relevant. As far as we know, he didn't give the
question of “what it was like to be” a mechanical computer a moment’s thought;
then again, neither did he trouble himself with “what it was like to be” a human
computer. Factory work was purely functional, operating at a level of abstraction
above the individual—hence the substitutability of workers on a production line.
As Babbage put it, “[D]ivision of labor can be applied with equal success to mental

as to mechanical operations.”-22

Lady Byron was excited by the “sublimity of the views thus opened of the
ultimate results of intellectual power,” but, for others, the idea of machines
doing mental labor sparked an early glimmer of the unease some feel about AI
today. In 1832, a year before Lovelace and Babbage met, the London Literary
Gazette had referred to Babbage, perhaps only half in jest, as a “logarithmetical

Frankenstein.”24! Information work may not have been a significant sector of

---

the labor market yet, but the prospect of machines thinking still induced a certain

agitation.

Just how far could a mechanical monster’s mental functions advance? According
to Menabrea, the Italian engineer, “The [Analytical Engine] is not a thinking
being but simply an automaton which acts according to the laws imposed

on it.” Lovelace agreed, writing in her Note G, “The Analytical Engine has no
pretensions whatever to originate anything. It can [only] do whatever we know
how to order it to perform.”-"! This zombie-like picture recalls the golem of me-
dieval Jewish folklore: a clay figure animated by a powerful rabbi using magical
incantations—that is, code. The golem may follow commands, but without un-

derstanding or discernment.

George Boole may have thought otherwise. Recall that, like Leibniz, Boole be-
lieved in binary logic as a universal calculus for reasoning. Boole went further,
asserting that it is the way the mind reasons; hence the title of his great treatise,
An Investigation of the Laws of Thought, published to wide acclaim in 1854,222!
Presumably, he meant that understanding and discernment were themselves
products of logic, for while Boole was religious, he (again, like Leibniz) thought
of logic and rationality as inherently divine.“° The human soul was a “rational
soul,” and our subjectivity followed from, rather than existing in spite of, our

rationality.

In the beginning, this neuroscientific aspect of Boole’s thesis remained largely
unacknowledged. A notable exception was Boole's friend and colleague Augustus
De Morgan (author of the “Great fleas have little fleas” rhyme in chapter 1), who
had himself been working on the foundations of logic.““"! The Victorian intelli-
gentsia was a small world: De Morgan was also Ada Lovelace’s mathematics tutor,

and had taught her calculus and the Bernoulli numbers.

Unlike her contemporaries, though, Lovelace was not content to choose between
logic-based brains, on one hand, and mystical non-explanations of mental pro-
cesses, on the other. In an 1844 letter to a friend—a decade prior to Boole’s Laws
of Thought—Lovelace wrote, “I have my hopes |...] of one day getting cerebral phe-

nomena such that I can put them into mathematical equations; in short a law or

---

laws, for the mutual actions of the molecules of brain [...]. The grand difficulty is
in the practical experiments.”

Lovelace undoubtedly knew about the sensational experiments of Luigi Galvani
(1737-1798). Galvani had discovered that the application of electrical current to
the nerves of freshly killed frogs caused their legs to twitch. Galvani’s nephew,
Giovanni Aldini (1762-1834), carried on the work, legitimizing his studies with
claims—not wholly implausible—that “galvanic” shocks could sometimes revive
the drowned and treat the mentally ill. Twentieth-century defibrillation paddles

and electroconvulsive shock therapy are heirs to these early experiments.

Still, Aldini appears to have been more of a showman than a scientist. In 1803, he
rushed the hanged body of convict George Foster from London's Newgate Prison
to the Royal College of Surgeons for an anatomical demonstration.““ According
to the lurid (and wildly popular) Newgate Calendar, “On the first application of
[electricity] to the face, the jaws of the deceased criminal began to quiver, and the
adjoining muscles were horribly contorted, and one eye was actually opened. In
the subsequent part of the process the right hand was raised and clenched, and
the legs and thighs were set in motion.”4""' The beadle of the Surgeons’ Company

reportedly died of fright soon after returning home.

---

Mary Shelley’s Frankenstein'2°>! was probably inspired by this account. Perhaps
likewise inspired, Lovelace wrote, underlining words with her customary enthu-
siasm: “I must be a most skillful practical manipulator in experimental tests; &
that, on materials difficult to deal with; viz: the brain, blood, & nerves, of animals.
[... Njone of the physiologists have yet got on the right tack; I can’t think why.

[...] It does not appear to me that cerebral matter need be more unmanageable to
mathematicians than sidereal & planetary matters & movements, if they would
but inspect it from the right point of view. I hope to bequeath to the generations a

culus e Nervous em."/205)

In drawing a parallel between neural activity and Newtonian laws of motion,
Lovelace implied that cerebral “calculus” would not be founded on abstract logic
like that of Boole and the Analytical Engine, but rather should be grounded in ex-

periment, and, in this, she was indeed on the right tack.

Unfortunately, Lovelace’s health, always fragile, soon worsened. She began taking
opiates for chronic pain, and died a few years later, at age thirty-six, of uterine
cancer. We will never know what she might have achieved as a neurophysiologist

or as the first computational neuroscientist.

---

When real experiments with nerve tissue finally got underway, they at first
seemed to confirm the “digital” intuitions of Leibniz and Boole. In the 1920s,
pioneering English neuroscientist Edgar Adrian was electrically recording “all-
or-nothing” action potentials, or “spikes,” in the sensory neurons of dissected
frogs at his lab at Cambridge.!2°"! Adrian’s colleague and predecessor, Keith Lucas,
had already established that impulses in motor-nerve fibers were similarly all-or-
nothing.2°2!

With neural inputs and outputs thus seemingly binary electrical signals, the
idea that the brain is a logic machine carrying out a kind of calculus ratiocinator
gained powerful support. In particular, if every neuron has inputs corresponding
to Boolean ones and zeros, and produces a Boolean output in response, it’s a logic
gate—that is, a Boolean operator.“ And, if so, the activity of the brain as a whole

would amount to a vast logical calculation.

Two pivotal figures in modern neuroscience, Warren McCulloch and Walter Pitts,
brought these ideas together in a legendary 1943 paper, “A Logical Calculus of the
Ideas Immanent in Nervous Activity.” It seemed to be the realization, ninety-nine

years after Lovelace’s letter, of her envisioned “Calculus of the Nervous System”:

To psychology, [...] specification of the [neural] net would contribute all
that could be achieved in that field—even if the analysis were pushed to
the ultimate psychic units or ‘psychons,’ for a psychon can be no less than
the activity of a single neuron. [...] The ‘all-or-none’ law of these activities,
and the conformity of their relations to those of the logic of propositions,
insure that the relations of psychons are those of the two-valued logic of
propositions. Thus in psychology [...] the fundamental relations are those
of two-valued logic. 242!

This paper was at once an end, a beginning, and a turning point—but not in

any way its authors could have foreseen. As an engineering manifesto, it proved
highly influential. John von Neumann read McCulloch and Pitts’s 1943 paper as

a blueprint for how to perform general-purpose computation using electronic
logic gates in place of biological neurons (as mentioned in chapter 1). In the right
configurations, these gates—first made using vacuum tubes, and later transistors

—could implement a Universal Turing Machine, and could therefore compute

---

anything. The Boolean architecture was more minimal and elegant than that of
the Analytical Engine and its successors, which relied on complex mechanical

components and used base-ten arithmetic./4:4

One can think, then, of digital computers as Universal Turing Machines built of
hand-crafted neural networks of McCulloch-Pitts-type neurons. The symbols
used today to represent logic gates are cribbed directly from the graphical rep-
resentations McCulloch and Pitts drew of “pyramidal neurons” (which were, as
the name implies, pyramid-shaped). We still draw a little circle at the tip of the
pyramid for logical negation (turning an AND gate into NOT-AND or NAND, an
OR into a NOT-OR or NOR, etc.). Originally, that circle represented an inhibitory
synapse, which McCulloch and Pitts believed to implement the NOT operator.\**4!

N,(t).=.N,(t—1).~N,(t—1)

Despite its powerful influence on computer engineering, as a neuroscientific
theory, the 1943 McCulloch-Pitts paper was a false start. It marked the endpoint
and high-water mark of the notion that individual neurons work by carrying out
logical operations. Postwar neuroscientists quickly established that while all-or-
none voltage spikes are indeed a key signaling mechanism in the brain, they don't

correspond to logical propositions, and neurons don’t work like logic gates.!242)

Larger-scale electrical fields and oscillations matter too; neither is electrical
signaling the whole story. A wealth of neurotransmitters and neuromodulatory
chemicals operate at a variety of scales, from local signaling with specialized
“neuropeptides”*:4) to hormones secreted into the bloodstream that affect the

entire body. These play major roles in our mental states, emotions, and drives.

---

The emerging picture remains computational, but more in the spirit of Turing’s
models for morphogenesis and “unorganized” neural networks rather than any-

thing like a calculus ratiocinator.

Turing understood this, as he made clear in a 1951 BBC Radio address.244! He
agreed with Lovelace’s assertion that writing a program in the usual way could
only produce a predefined golem-like result—indeed, traditional programming
involves writing code whose function is fully understood by the programmer in
advance, foreclosing any possibility for subsequent machine behavior we could
reasonably call “creative” or “intelligent.” However, the universality of comput-
ing makes it possible to implement any computable model of neural function,
including Lovelace’s “calculus of the nervous system,” on any Universal Turing
Machine. Thus, Turing said, “it will follow that our digital computer, suitably pro-

grammed, will behave like a brain.”

Although, like Turing, neuroscientists understood long ago that the brain is nota
classical logic machine, the message took a long time to sink in among computer
scientists and AI researchers. Recall that, throughout the twentieth century,
repeated attempts at hand-writing algorithms to carry out the most basic of
everyday tasks, like image and speech recognition, robotic control and common-
sense reasoning, had failed utterly, bringing on the AI winters mentioned in the

introduction. 212

For many decades, then, computers were able to perform logic-based tasks that
had been deemed purely “mechanical” with superhuman speed, yet seemed un-
able to get anywhere at everyday “human” tasks. They failed even at tasks that
many other animals with much smaller brains find easy. It began to seem that,
despite Turing’s ideas about universal computation, computers might have little

to do with either biology or brains after all.“!7

The popular culture of AI throughout the twentieth century navigated this
apparent mismatch between brains and computers by imagining that when—or
if—AI finally arrived, it would be stellar at “rational” thinking and logic but poor
at human emotion, creativity, or common sense. HAL 9000,2:4) or Data from Star

Trek, are prime examples.\2!2!

---

The message was: computers can perform rote calculations today, and may
eventually exceed humans at “book smarts” too, but, being golem-like, they aren't
remotely like us; the human spirit is neither logical nor rational. We can't be re-

duced to mere computation.

This trope seems especially irresistible to Hollywood, resurfacing over and over
in franchises like The Terminator, Robocop, and The Matrix. If Boole was an En-
lightenment thinker living in the Romantic period, Hollywood remains full of

closet Romantics living in a Postmodern era.

What attracts us to this kind of human exceptionalism? Partly, the question
answers itself; of course we like thinking of ourselves as fundamentally different,
better in some non-quantifiable way, possessing some je ne sais quoi that will
remain forever out of reach of the encroaching “other.” Nationalities and ethnic

groups play this identitarian game all the time.

Beyond the obvious, though, the “incomputably human” narrative is comfort-
ing because the Industrial Revolution established a computational hierarchy
wherein the soulless, rote, mechanical stuff is done at the lowest tier of the org
chart of its time—first by calculating women, then by the machines that re-
placed them—so that upper class gentlemen-scholars could be freed for the more
varied, creative, and intellectual pursuits they deemed worthy of being called

“intelligent.”229)

As historian of science Jessica Riskin puts it, “Not only has our understanding of
what constitutes intelligence changed according to what we have been able to
make machines do but, simultaneously, our understanding of what machines
can do has altered according to what we have taken intelligence to be. [...] [T]he
first experiments in automation were devoted to determining its uppermost lim-

its, which simultaneously meant identifying the lowest limits of humanity.”224

Today we not only face the problem that those limits have continued to shift, but
also that they have stubbornly refused to fall into the right sequence, according
to our class-based preconceptions. It’s easier nowadays to imagine a doctor re-
placed by an AI model than a nurse. We probably won't have AI plumbers anytime

soon, but AI physicists (at the very least AI physics research assistants) may ar-

---

rive imminently. When large language models can read and summarize complex

arguments, write essays and poems, create software, and so on, there ceases to be
any obvious hierarchy of information tasks where a computer can only substitute
for the work of the poorly paid or uneducated. Als are no longer, as Leibniz would

have it, “artificial peasants” manufacturing logarithms.

Neither is Al the purely book-smart supernerd envisioned by twentieth-century
media. Real AI isn’t necessarily overly logical; in fact, its failures at solving logic
puzzles, or even simple arithmetic problems, featured prominently in AI critique
during the early 2020s. Now, not acting enough like a computer is interpreted as a

lack of intelligence!

As an engineering discipline, too, modern ATI is disruptive; it has little to do with
the programming languages, data structures, and paradigms that were the main-
stay of computer engineering departments a scant few years ago. AI models may
run on Universal Turing Machines, but they aren't algorithms in any classical
sense. Instead, they tackle the problem of modeling probability distributions di-
rectly from data.

So where did the new approach to computing and AI come from? As it turns out,
it has been here all along, just not in the mainstream. Understanding this alter-
native vision, and its relationships with other disciplines, requires following a
different path from that of Leibniz, Boole, and traditional computer science—one
that, inspired by living systems, conceived of computation less in terms of logic

than in terms of learning and prediction.

This was the path of cybernetics, an idea developed as far back as the 1940s, in
wartime, and already falling into disrepute by the ’60s.

---

# Chapter 3

3. Cybernetics

Love and War

We have seen how even simple life forms, like bacteria, evolve to predict their
environment, their internal states, and their actions. Both normativity (good ver-
sus bad) and basic feelings (like hunger, satiety, and pain) arise as consequences
of prediction. However, the discussion so far has been framed in terms of a single-
player game: how a “self” can evolve to enhance its dynamic stability in a world
that is, if not hostile, at least indifferent. The food molecules a bacterium chases
during chemotaxis are not running away; nor are chemorepellent molecules ac-
tive aggressors. Chemotactic bacteria are modeling molecular concentration, but
those small molecules they’re modeling (probably) aren’t modeling the bacteria

in turn.

When it comes to wolves and rabbits, though, multiple agents are at work model-
ing each other—whether in skittish alarm (the rabbit) or with murderous intent
(the wolf). Big-brained animals like us (and wolves, and rabbits) have detailed
models of themselves, too, as well as of kith and kin—hopefully, with neither skit-
tish alarm nor murderous intent. Such rich social, subjective, and “intersubjec-
tive” experiences seem far removed from the simple machinery of bff programs
or bacteria, Yet I will argue that minds like ours are a natural consequence of the
same evolutionary dynamics. In particular, minds arise when modeling other

minds becomes important.

The need for such modeling goes a long way back. It relates to two major evo-
lutionary transitions: the emergence of sexual reproduction, likely about two
billion years ago, and of hunting, which became prevalent during the Cambrian

explosion, 538.8 million years ago.

Because sexual reproduction is so ancient, first arising among our distant single-
celled ancestors, its origins remain obscure. Sex may have been an integral part
of the eukaryotic revolution, two billion years ago.!224! Since eukaryotes are the

canonical instance of symbiogenesis, it seems fitting that sex is itself symbiotic:

---

the female and male forms of a species depend on each other to reproduce, mutu-
ally benefitting through faster evolutionary learning.2*) (Hence, under most cir-
cumstances and all other factors being equal, a sexually reproducing species will

outcompete one that reproduces asexually, even though each individual member

of the asexual species faces fewer barriers to reproduction.)

For our purposes, though, sexual reproduction is relevant because it requires

an organism to recognize one of its own, and, usually, to distinguish male from
female and modulate its behavior accordingly. This is a big deal: when reproduc-
tion requires sex-selective cooperation or competition, others of the same species
(and subtle differences between individuals) become an obligate part of one’s

umwelt.

Now, let's fast-forward a billion and a half years. While many aspects of the

ancient fossil record remain controversial, there is broad consensus that pre-
Cambrian life was dominated by soft-bodied organisms with a wide range of
body plans and symmetries, from tubular to quilted to more amorphous. We

can only guess how those ancient Ediacarans moved, but it seems likely that the

---

behavioral boundary between plants and animals would have seemed indistinct,
with many organisms either drifting on ocean currents or anchored to rocks,
their fronds or appendages waving languidly in search of nutrients. Nervous

systems during this period, when present at all, may have looked much like the

distributed nerve nets of Hydra or comb jellies.!=*)

Then, the Cambrian explosion occurred: a sudden great diversity of marine crea-
tures with protruding eyes, armored plates, fearsome claws, and sharp teeth. It’s
impossible not to imagine them moving quickly and actively, hunting, escaping,
killing and being killed. An arms race ensued, featuring a cascade of innovations
and counter-innovations in the arts of attack and defense. For the first time,

complex, centralized nervous systems would have been required to intelligently
coordinate rapid, perceptually guided, purposive movement.\“22 The (one-sided)

joys of predation had been discovered.

In light of the earlier discussion of thermodynamics and its relationship to
dynamic stability, it’s worth pausing to spell out the Darwinian motive for preda-

tion, even though it may seem intuitively obvious. Why do we eat, anyway?

---

Recall that life requires computation to reproduce (per chapter 1) and to respond
to changes in its environment or internal state (per chapter 2). Computation, in
turn, requires free energy—though recall also that this term is deceptive. Energy
can neither be created nor destroyed; we don’t “use it up.”224l Free energy really

means a source of order, or low entropy.

Recall that in thermodynamics, the classic low-entropy system is a pressurized
piston: a cylinder of air in which most of the gas molecules are concentrated

on one side of a partition, leaving a partial vacuum on the other side. It would
be extremely unlikely for this situation to arise spontaneously—like randomly
bouncing billiard balls suddenly forming a triangle at one end of the table—but
with the piston locked in place to prevent the gas from redistributing itself more

randomly, the pressure differential can be maintained.

This low-entropy configuration is like a loaded spring, or a cocked gun. The mo-
ment that piston is allowed to move, it will do so with force, until the pressures
on both sides equalize—that is, until entropy is again maximized. That would
“use up” the free energy, even though the total amount of actual energy in the
system (proportional to the summed squared velocities of all of the gas mole-
cules) has remained constant. When Newcomen and Watt harnessed the piston’s
movement to work a pump, or spin a loaded crankshaft, the molecules would

slow down accordingly, cooling the gas.

Now, remember that once life takes hold, it creates predictability and order; its
entropy plunges. That, too, requires work. It also means that an organism itself

is a kind of pressurized piston—or loaded spring, or cocked gun. A wonderful
source, in other words, of free energy. (The fatty bits, especially; all those deli-
cious carbon-hydrogen bonds!) Thus, predation: a life form using the order, or
“negative entropy,” stored in the body of another life form to do the work of main-

taining or increasing its own order or negative entropy.22/)

There are conflicting interests here. In the best case (for the victim), the predator
will just take a harmless little nip or sip—that’s how fleas, ticks, flies, and mos-
quitoes work. We still resent them; grooming behaviors among primates, and the
swishy tails on horses, evolved to discourage such micro-predation. (And partly

in response, flies have become lightning-quick, mosquitoes have evolved to inject

---

anesthetics, and ticks have become tenacious flesh-burrowers.) As for predation
of the kind that comes in larger, life-ending bites—well, avoiding it at any cost

immediately rises to the top of any prey animal’s to-do list.

At first blush, the two great revolutions I've just described—sex and predation—
seem to have as little to do with each other as love and war. However both love
and war require that you recognize and form internal models of other living
things in the pursuit of dynamic stability. They require, in other words, effective

prediction of something that is itself a predictor.“

We'll get to love later in the book. Here, though, we’ll focus on warfare—the
original “killer app”—from a computational perspective. Let’s return briefly to

nineteenth century London.

Killer App

Babbage struggled to drum up financial backing for his Analytical Engine. The
market for Jacquard-woven textiles was obvious, but who needed industrially
mass-produced “analytical formulz”? To sell the idea of mathematical tables as
a popular commodity, he resorted to folksy examples, such as “the amount of

any number of pounds from 1 to 100 lbs. of butchers’ meat at various prices per
1b")

Price tables for the village butcher? Hardly. A moment's reflection will make it
clear that small tradesmen wouldn't have been a viable customer base for a hulk-

ing industrial machine like the Analytical Engine.

State administration, which Prony had bet on, was closer to the mark; the
information needs of bureaucratic governments were on the rise." still, it was
too early. The French government defunded Prony’s project long before it was

complete.

The real killer app was warfare. The British Army and Navy would have been
Babbage’s obvious backers, and ultimately it was their lack of investment that

doomed his enterprise.

The artillery table was already a paradigmatic product of human computation

by the turn of the nineteenth century. A new table was needed for every big gun,

---

including corrections for factors like altitude, wind, and barometric pressure.
With every major world conflict from the Napoleonic Wars (1803-1815) onward,
gunnery became increasingly important, and, with it, tabulation. And doing the

calculations by hand took a long time.

By World War I, the first fully industrialized large-scale conflict, both the Allies
and the Central Powers were making extensive use of complex tables. Artillery
fire was often planned days in advance, and its accuracy became crucial for sup-
porting infantry advances. Computation had become a bottleneck in warfare,
and, more than any other single factor, this was what finally motivated serious

investment in automatic computing between the World Wars.

As weapons production for World War II began ramping up, the University of
Pennsylvania's Moore School of Electrical Engineering hired at least two hundred
women to work on artillery tables. Their methods would have been largely famil-
iar to Babbage or Prony. But, spurred by the war effort, technology was advancing
at breakneck speed. Six of the Moore School's women were selected to become the
programmers of the ENIAC.224! This first fully general, programmable computer
had been designed to automate artillery tabulation, 424)

By the time the ENIAC became operational, in December 1945, priorities had
changed. The Germans and the Japanese had been defeated, but Cold War
brinkmanship picked up right where World War II had left off. The new com-
puter’s first substantial program was a simulation of the “Super Problem,” explor-
ing the feasibility of a hydrogen bomb.22» The math required was a lot harder
than calculating ballistic trajectories, and the machine's thousands of vacuum
tubes burned out frequently, requiring near-daily repair. This incentivized rapid
improvements in the hardware, kickstarting what would later be known as

Moore’s Law.2241

The early computers were a long way from anything we have today. It’s sobering
to consider how many years of capital-intensive incubation within the military-
industrial complex were needed before the technology had become sufficiently
cheap, reliable, and miniaturized to rouse real interest from the private sector, let

alone the village butcher.

---

IBM’s 701 mainframe, announced to the public on May 21, 1952 and originally
dubbed the “Defense Calculator,” became the first computer commercially
available in the US. There’s an apocryphal quote, usually attributed to Thomas

J. Watson Jr., IBM's president, from a stockholders meeting in 1953, to the effect
that he believed there was a worldwide market for only five computers. This isn’t
quite true; Watson really said that, when IBM had drawn up the plans for the 701
and toured them across the country to “some twenty concerns” that they thought
“could use such a machine,” they had assumed they'd only get five orders and

were astonished to get eighteen. |222!

At first, general-purpose computers were not designed to work in real time. Like
the human computers they replaced, they supported the war effort using batch
processing. Such computing was a stately, offline affair. You submitted your job,
and went to get a coffee ... or, more likely, take a nap while technicians nursed the
job along, replacing tubes, clearing punch-card-reader jams, and swapping out
spools of magnetic tape. Running on the ENIAC, bff would have taken centuries
to achieve full-tape replication. By 1952, on the IBM 701, it would still have taken

years, running nonstop, at a cost of millions of (today’s) dollars.!22%

The '50s did see some early experiments in interactive architectures. Project
Whirlwind, operational in 1951, was initially designed for flight simulation, and
later became the heart of the US Air Force’s SAGE air-defense system.2= Real-
time computing had become important due to the development of radar and re-
lated radio-signaling technologies, effectively allowing one machine to physically
detect another machine—at least one of which might be moving through space at

high speed and with lethal intent.

Identify Friend or Foe (IFF) systems soon followed, using encrypted signaling to
allow radar dots to be annotated when a bogey was “one of ours.” This in turn cre-
ated an incentive to hack an enemy’s IFF system, spoofing the “friend” signal to
sneak into enemy territory. A game of technical one-upmanship ensued, not un-

like that of the Cambrian explosion.

Still more Cambrian was the rapidly increasing speed, precision, and deadliness
of the military hardware. Jet fighters, missiles, and anti-missile defenses prolif-

erated. GPS was invented in large part to make autonomous weapons guidance

---

possible, as it was obvious that high-speed warfare would soon render keeping

a human “in the loop” impossible; the precision and response time needed were
superhuman. Even the G-forces incurred by aerial maneuvers soon began to ex-
ceed human endurance.“ Robots would need to close the sensorimotor loops of

these new weapons systems.

Behavior, Purpose, and Teleology

Thus, the field of cybernetics was born, so named in 1947 by MIT mathemati-
cian Norbert Wiener, physiologist Arturo Rosenblueth, and their colleagues..2"
Unlike batch computing, cybernetics was all about real-time feedback loops in-
volving continuous time-varying signals like position, velocity, and thrust. Early
proto-cybernetic technologies included electromechanical gun turrets and auto-
matic bomb-sighting engines used to correctly time the dropping of munitions

from a plane to hit a target, often using analog cams and gears.2%)

The cyberneticists took on the challenge of generalizing such systems to aerial
dogfighting, in which the target is not stationary." In the presence of noise and
uncertainty, such problems can be formulated using information theory, a field
where Wiener made important early contributions. Under the assumption that
the “brain” of a targeting system is linear, meaning that its outputs are weighted
sums of its inputs, he also derived elegant theoretical results in optimal filtering
and control. (Bacterial chemotaxis, described in chapter 2, can be modeled using
the same math.!2*4)) These optimal linear theories are both useful for building
weapons systems and, under many real-life conditions, can be hard to improve
on: when the goal is clear and unchanging, everything is happening very fast,

and measurements are noisy, there isn't time for nonlinearity to matter so much.

In high-speed, goal-directed, and similarly adversarial natural contexts, such as
a bat or dragonfly closing in on prey, animal brains can also carry out something
close to cybernetically optimal linear modeling.“*4) The same holds when you

reach for an object or catch a ball 2"

Balls don't actively try to escape you—at least outside the Harry Potter universe.
A moth, however, behaves like a real-life “golden snitch” when a bat is closing

in for dinner.2** It can’t fly as fast as a bat; its brain and sensory apparatus are

---

outmatched too. But it can try evasive action. The evasions must be genuinely
unpredictable, because randomness is the moth’s only cybernetic advantage. The
bat, with its much larger brain, would preempt any more coherent plan the moth
could dream up. So, while the bat applies something close to optimal prediction
tailored to the moth’s flight statistics, the moth takes advantage of its low mass
to flutter around chaotically, rendering those statistics as blurry as possible.
Instead of a smooth, predictable curve, the resulting flight pattern is a tortuous
“random walk” occupying a volume in space known affectionately as the “Wiener

sausage.” (For real.2*4!)

As you will know if you've ever tried—and failed—to catch a seemingly not-that-
fast moth, these Wiener-sausage tactics work, at least up to a point. The moth
implements them with a biological random-number generator, likely based ona
combination of mechanical instability in the wings and random neuronal activ-
ity. If you're wondering how neuronal activity can be random, keep in mind that
it always is, a little bit. The biochemical events leading to neural firing include ion
channels opening and closing in the cell membrane, and the release and capture
of synaptic vesicles containing neurotransmitters. The timing of these events is
never quite precise, because they’re contingent on the same random molecular
interactions that drive all cellular activity. If a neural circuit is wired to amplify
that noise, then, like the random-number instruction of Turing’s Ferranti Mark I

computer, the result will be a computationally usable random signal.!2*2.

Ample evidence suggests that prey species like moths use such circuits to
generate chaotic behavior; startled cockroaches, similarly, use them to scurry at
random.*4) If randomness is the low road to cybernetic unpredictability, though,
there is also a high road: becoming smarter than the entity trying to predict you,
and predicting that entity's predictions. We'll explore this brainier strategy in
chapter 5.

But first, let’s take the full measure of cybernetics—what it got right, what it

got wrong, its untimely demise, and its enduring influence. As formulated by
Wiener, cybernetics was the field we now call Artificial Intelligence, and more—it
was the hallmark of all complex systems, a grand unifying theory of the biologi-
cal, the technological, and even the sociological.!24%!

---

The simplest cybernetic system is something like a humble thermostat, a feed-
back mechanism that turns the heat (or air conditioning) on and off to maintain a
constant temperature. Warm-blooded animals, of course, do just that, and living
systems in general must use feedback to “homeostat” (that is, to regulate) their
internal state. Construed broadly, homeostasis is what being alive is all about.
The point of eating, for example, is to maintain the body's store of free energy,
and similar purposive arguments can be made for all of our primary drives. Our
secondary drives, such as the desire for praise or prestige, can in turn be formu-
lated as “instrumental” to those primary drives. Homeostasis is thus our old

friend, dynamic stability, implemented purposively.

Complex animal behaviors may seem a long way from those of a thermostat,
but consider that a truly optimal thermostat will not only switch on or off in
response to fluctuations in the temperature now, but also on the basis of its
prediction of the future. If, for instance, the sun is about to rise and start rapidly

warming your house, this ought to affect your home thermostat’s strategy.

Generalizing this observation in a 1943 essay entitled “Behavior, Purpose, and
Teleology,”!2*°! Wiener, Rosenblueth, and computer pioneer Julian Bigelow per-
fectly articulated the “predictive brain” hypothesis in cybernetic terms (though

they did not coin the word for several more years):

All purposeful [or “teleological”] behavior may be considered to require
negative feed-back [which] may be extrapolative (predictive) [...]. A cat
starting to pursue a running mouse does not run directly toward the
region where the mouse is at any given time, but moves toward an ex-
trapolated future position. [...] The cat chasing the mouse is an instance of
first-order prediction [...]. Throwing a stone at a moving target requires a
second-order prediction [...]. It is probable that limitations of [...] the central
nervous system [...] determine the complexity of predictive behavior |...].
Indeed, it is possible that [...] the discontinuity [between] humans [and]
other high mammals may lie in that the other mammals are limited to pre-
dictive behavior of a low order, whereas man may be capable potentially of

quite high orders of prediction.

---

First—,
second=, etc.

Predictive orders of
(extrapo- prediction
lative)
Feed-back
(teleo- Non-predic-
logical) tive (non-
Purposeful extrap-
olative)
Non-feed-
back (non-
i teleo-

Active logical)
[serps
Behavior ful (random)
Non
active
(passive)

The authors also pointed out that, from this behavior-focused perspective (that
is, without worrying about how the predictive computation is implemented),
purposive machines and living systems are alike, “regardless of the complexity
of [their] behavior,” adding that “examples [...] are readily found of manmade ma-

chines with behavior that transcends human behavior.”

This was true of machines even in 1943, before general-purpose computing;

it was even true in 1843, or there would have been no Industrial Revolution,
though few machines back then were teleological or purposive in the cybernetic
sense. A notable exception is the centrifugal governor, first invented by Christi-
aan Huygens in the seventeenth century, then adapted by James Watt in 1788.
Watt’s version controlled the amount of steam going into a steam engine using
a valve coupled to whirling weights driven by the engine, creating a negative (or

homeostatic) feedback loop to regulate the engine's speed.

---

In invoking teleology, Wiener and colleagues were playing with fire, both in the

philosophical and scientific communities. Materialism and reductionism had
given teleology a bad name, relegating it to a quasi-religious belief. After all, if,
given initial conditions, the (entirely knowable) dynamical laws of physics fully
determine what will take place at the next moment in time, what role could tele-

ology or purposive action possibly play?2241

Beyond stipulating goals and purposes, cybernetics posited agents that predict
the future and bring that future about—the same apparent reversal of causal-

ity we encountered in chapter 2. The cyberneticists’ insight, both trivial and
profound, was that predictive negative-feedback loops are sufficient to give an
apparatus (or organism) purposiveness ... without violating the laws of physics.
The Huygens-Watt centrifugal governor, for instance, is a simple machine whose
workings are fully described by Newtonian physics. Yet it also has a goal: it ma-
nipulates a steam engine's intake valve to regulate the engine's speed. In doing so,

it “creates” causes in order to bring about future effects.

---

The apparent paradox of backward causality resembles the apparent paradox of
an apparatus (or organism) building a copy of itself. In that case, von Neumann
realized that the solution lay in the apparatus having an internal model of its own
structure, and using that model to guide construction. Wiener and colleagues
realized that the solution to their problem lay in the apparatus having an internal

model of (part of) the world, and using that model to guide behavior.

These are flip sides of the same coin. In both cases, the models are computational;
and in both cases, their purpose is to continue to exist through time, whether by
growing, by preserving the integrity of the self, or by replicating.

Von Neumann and Wiener published their insights within a year of each other,
though, at the time, the intellectual kinship between them may not have been

fully appreciated.

Negative Feedback

Cybernetics got many things right, especially as compared with the symbolic,
programming-based approach to AI championed by Wiener’s detractors. For

starters;

® It embraced continuous values and random processes.

@ It was based on learning (that is, modeling) probability distributions,
rather than executing hand-engineered code reflecting a programmer's
intuitions.

@ It advanced the idea that agency (or purposiveness, or teleology) is funda-
mental to intelligence, and to life more broadly.!222!

® It was consistent with the neuroscientific consensus that emerged soon
after McCulloch and Pitts’s 1943 paper, when it was understood that neu-
rons do not implement propositional logic using Boolean values.

@ It focused on the continuity between intelligence and living systems more
generally, rather than imagining that intelligence is a purely logical con-
struct in the Leibnizian tradition—and therefore the exclusive province of
symbolically minded humans. As a corollary, cybernetics presumes that

bats, dragonflies, and even bacteria are also intelligent.

---

@ It emphasized the importance of behavior over mechanism, noting that the
same models could be computed in radically different ways—for instance,
in standard Turing Machine-like computers, “largely by temporal multipli-
cation of effects” given “frequencies of one million per second or more,” or
in biological systems, by “spatial multiplication,” that is, massive and non-

deterministic parallelism.

This last point may sound reminiscent of B. F. Skinner and radical behaviorism,

a school of thought that has been pilloried as brutally reductionist, or as denying
the existence of mental states./2**! A fair assessment of behaviorism would take
us too far afield, but suffice it to say: Wiener and colleagues were making a point
about the fundamentally computational nature of the brain or mind. Hence, its
multiple realizability, or platform independence, is underwritten by the univer-
sality of computation, per Church and Turing. This is the same kind of “behavior-
ism” that led Turing to formulate the Imitation Game in terms of behavior, rather

than insisting on any specific brain mechanism.

Cybernetics also got some things wrong. Its greatest flaw was in overpromising:
there was a vast gulf between Norbert Wiener’s self-promoting grandiosity and
the engineering realities of his day. The theory was so general that it was nearly
tautological, yet practical demonstrations using mid-twentieth-century tech-
nology were underwhelming. Neither was Wiener much of an engineer; he was
more at home at a blackboard than in a machine shop. An idea for a cybernetic
antiaircraft-gun controller, which he had insisted would prove crucial to the war

effort, remained vaporware.

---

In 1949, Wiener’s students at MIT cobbled together a motorized cart with wheels

driven by feedback loops involving two photocells. Wired up one way, it was
christened Palomiilla, Spanish for “moth,” and could trundle bumpily along a
corridor, more or less following a flashlight beam. Switching the wires turned it
into a light-averse “bedbug.” Cranking up the feedback gain made it oscillate with
something like Parkinsonism or intention tremor. But beyond the tight feedback
loops of missile control systems (which did what Palomilla did, marginally more

reliably2**)), real-life applications were elusive. Why were these demos so lame?

Wiener could easily write down a feedback-response function that would stand
in for the totality of an organism's behavior. He could then proceed to expand
that function formally into an infinite series of higher-order terms. He could
even derive closed-form solutions for the linear parts, given a simple goal like
playing an optimal game of chase with an opponent whose movements could be
analyzed statistically. Yet the higher-order terms remained out of reach. Explod-
ing numbers of parameters and the difficulty of characterizing higher-order goals
made it unclear how further progress could be made—especially given the feeble

computational power available.

---

Access to massive computation would not have immediately solved the problem,
either, because major conceptual gaps remained. Cyberneticists had largely swept
memory and learning under the rug, along with anything resembling individual
behavior. Lofty rhetoric aside, what cybernetics offered in practice was a cartoon
of the purely instinctual behavior of a simple organism performing a single low-

dimensional sensorimotor task in an unchanging niche. A thermostat, basically.

Real moths and bedbugs have a vastly richer behavioral repertoire than the
Palomilla. Even chemotactic bacteria do. Those pesky feedback functions were
black boxes where seemingly infinite complexity hid. In theory, more or less any
function could be approximated with a series expansion, but, in practice, it was
hard to see how anything resembling thought, perception, or action—let alone
anything like psychology or a “self”"—could arise merely by adding more terms to

the series.

Good Old-Fashioned AI or GOFAI, based on hand-written programs instead of
cybernetics, may have been cheating, but at least its canned responses could be
substantive. In one famous example, MIT professor Joseph Weizenbaum created
a chatbot called ELIZA, which, given a modest collection of grammatical rules,

could simulate a therapy session.

The year was 1964—the heyday of psychologist Carl Rogers’s “person-centered
therapy.” Rogers believed in the power of patients talking themselves through
their problems, and avoided ever passing judgment; he called this “unconditional
positive regard.” Hence, his method consisted mainly of listening empathically
and encouraging the patient to carry on. ELIZA could approximate this kind of
engagement by using heuristics to guess at key words or phrases in the dialogue
and ask followup questions about them, or, if stumped, to fall back on restate-

ment or asking a more general question.

As Weizenbaum put it, “This mode of conversation was chosen because the psy-
chiatric interview is one of the few examples of [...] communication in which one
of the participating pair is free to assume the pose of knowing almost nothing

of the real world. If, for example, one were to tell a psychiatrist ‘I went for a long

boat ride’ and he responded ‘Tell me about boats,’ one would not assume that he

---

knew nothing about boats, but that he had some purpose in so directing the [...]

conversation.”"22

In a 1966 paper, Weizenbaum reproduced an ELIZA dialogue he described as
“typical”; the machine’s responses (in caps) are accurate, though the exchange is

cherrypicked to avoid bloopers:

Men are all alike.

IN WHAT WAY?

They're always bugging us about something or other.

CAN YOU THINK OF A SPECIFIC EXAMPLE?

Well, my boyfriend made me come here.

YOUR BOYFRIEND MADE YOU COME HERE

He says I’m depressed much of the time.

I AM SORRY TO HEAR YOU ARE DEPRESSED

It’s true. lam unhappy.

DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY
I need some help, that much seems certain.

WHAT WOULD IT MEAN TO YOU IF YOU GOT SOME HELP
Perhaps I could learn to get along with my mother.

TELL ME MORE ABOUT YOUR FAMILY

...and so on 2241

It would be hard to argue that a few hundred stock responses with their blanks
filled in by echoing back user-supplied words really constitutes “intelligence.”
Still, the results looked far more impressive than anything on offer from the cy-
berneticists. And GOFAI code like ELIZA ran efficiently, even on the earliest gen-

eral-purpose computers.

Many researchers and engineers didn't care if programmed behaviors were brit-
tle; they were busy launching a trillion-dollar industry. When AI grants stopped
getting funded, they found plenty of other applications that didn't require any-
thing like cognitive flexibility. Computer science began to disentangle itself from
Al to become a discipline in its own right, while software engineering crossed the

chasm from the military-industrial complex to big business, and from there into

---

home computers. Nobody regarded their home computer as even remotely intel-
ligent or brain-like, though by 1977, it was easy enough to spend an hour or two
typing the ELIZA program into your Altair 8800, just for laughs.!22%

Meanwhile, cybernetic philosophy was going ever more meta, and was ultimately
embraced (sometimes as little more than a metaphor) by the intellectually hip in
fields as far-flung as government,“ anthropology,2™ ecology,““4 urban plan-
ning,“*4 sexology,2°4! feminism,2**! and post-structuralist critical theory.!2®)
Some cybernetically inspired period pieces still make for great reading, some

had the right idea, and some had significant impact in their own fields. But un-
like mainstream computer science, none were accompanied by much technical
progress in cybernetics itself. The concept of a “cyborg,” a cybernetically inspired
superhuman fusion of man and machine (yes, usually man), went from a serious

research priority at advanced defense labs to a comic-book trope.\4®*!

In other words, cybernetics began to look like a fad. Even by the mid-1960s, it
had largely faded as an area of active research, though the name has survived
vestigially, and somewhat randomly, in terms like “cyberspace,” “cybersecurity,”

“cybercrime,” and “cyberwarfare.”/2°4)

Cybernetics fell victim not only to overreach, but also to the systematic efforts

of its detractors.!2°*l In 1955, computer scientist John McCarthy coined the term
“Artificial Intelligence” in the proposal for a summer workshop at Dartmouth—
precisely to distinguish the new symbolic (a.k.a. GOFAI) approach from cybernet-
ics. Despite promising “a significant advance” over the two-month period, little
headway was made at the workshop proper, but its attendees, including Arthur
Samuel, Allen Newell, Herbert Simon, and Marvin Minsky, became the who's who

of Al over the next several decades. Wiener was pointedly not invited./2°2)

---

DARIMOUTH COLLEGE
Dhgertownd yf Cif eairowesier (2 yfitrewey
HANOVER WRF AMPATITRE

March,
1986

Kr, finy Solomonotf
Technical Research Geoup
1? Union Sqvere Wsat
New York, New Yorx

Dear Hey:

You tre one of the poopie
ve ahould Ike to invite to the
"Summer Research Profinet om fvtift—
aial Lnatellizanns."

Yerma: $1,200 - $900 cr
whieh will Provably | oouns aa s Pol~
lownnip and be tax “ree, plus
traveling oxpernea.

Detes: Tuns 16 to Aug. 17

Place: Hanover, M. H.
{a sool place).

Can we counts on yout

Test regards,

Stee
Jonn AcCarvhy
TMet sHA
Te he Cue hy Bare Samay tame
+. Mtoe 7 Gan Rastactee |
Jaane "is nats Seek Ore = eed
@. Selamat Me Callow
Foliar Bry x lee + Nawredl
Fo een,
Mek
Ete

It’s ironic that we continue to use the term “Artificial Intelligence,” given that

today, virtually the entire field descends from the kind of work the coiners of this
phrase sought to discredit—especially, per philosopher Hubert Dreyfus, “the per-
ceptrons proposed by the group Minsky dismisses as the early cyberneticists.”-"

These were the first artificial neural nets.

How We Know Universals

Inspired by the brain’s physical structure, pioneering American psychologist
William James (1842-1910) had envisioned something very like neural networks
as far back as 1890. In his magisterial textbook, The Principles of Psychology,4!)
James imagined that neural processes—the minutely complex “wires” evident in
stained tissue samples from the cerebral cortex—might physically embody asso-

ciations between co-occurring stimuli.

---

Shortly afterward, the great Spanish neuroanatomist Santiago Ramon y Cajal
(1852-1934) concluded that this wiring is not “reticular” (meaning continuous),
but consists of the branching outgrowths of individual neurons. Influenced by
James, Ramon y Cajal went on to suggest that the junctions between neurons,
which we now call synapses, were the sites of neuroplasticity. Associations could
be learned (or unlearned) through the selective strengthening (or weakening) of

synapses.\*"4!

The idea that mental associations are central to learned behavior has its own long
history. In 1897, Ivan Pavlov (1849-1936) published his classic experiments in
which dogs were taught to associate food with the sound of a musical triangle.

Once conditioned, they began salivating when the triangle was struck, |"2!

Learning associations is even more fundamental than behavioral experiments
like this suggest. Dogs aren't born with individual neurons that activate exclu-
sively at the taste or smell of food, the sight of a particular person, or the sound of
a triangle. Associating these multimodal events with each other is the easy part.
Without being able to learn subtle, complex associations among raw stimuli, a

dog would be unable to recognize a person or a ringing triangle at all.

---

McCulloch and Pitts formulated this problem in their 1947 paper, “How We Know
Universals: The Perception of Auditory and Visual Forms.” Their theory was
(once again) wrong, but the question posed by the paper's title is a good one: How
do we recognize categories, or “universals”? Four years after the publication of “A
Logical Calculus of the Ideas Immanent in Nervous Activity,” experiments had
convinced them that neurons were not logic gates, although they did exchange
excitatory and inhibitory signals. The researchers had also realized that one of
the hardest computational tasks facing the brain is that of achieving “perceptual

44

invariance”—the key to performing what we now call “classification,” “recogni-
tion,” or, more broadly, “generalization.” McCulloch and Pitts were trying to figure
out how anatomically plausible neural circuits in the sensory cortex might do

that.

Perceptual invariance is illustrated by an insightful short story, “Funes el memo-
rioso,” published by Jorge Luis Borges in 1942.27! In Borges’s story, a young man,
Ireneo Funes, is thrown from a horse and suffers a crippling brain injury. It leaves
him with a perfect memory yet robs him of the ability to generalize. After the ac-
cident, Funes can remember “not only every leaf of every tree of every wood, but
also every one of the times he had perceived or imagined it”; yet he is described
as “{...] almost incapable of ideas of a general, Platonic sort. Not only is it difficult
for him to comprehend that the generic symbol dog embraces so many unlike
individuals of diverse size and form; it bothers him that the dog at three fourteen
(seen from the side) should have the same name as the dog at three fifteen (seen
from the front).”

For a long time, machines fared no better. Throughout the twentieth century
and well into the twenty-first, memory technologies improved exponentially,
but perceptual invariance seemed to remain an unsolved problem. Attendees at
the Al summer workshop in 1956 made no progress, and when those who were
still alive fifty years later returned to Dartmouth for a reunion, little seemed to
have changed. A computer could, like Funes, “remember” the color of every pixel
in a two-hour movie, yet be unable to make any sense of those tens of billions of
pixels. Hence bots could easily be foiled by visual Turing Tests as simple as “click

on the images below containing a dog.”!2"*) The reconvening wizards, grizzled but

---

as opinionated as ever, were of various minds about what to try next, but they all

agreed that AI was a long way off.24

S

The year was 2006. They could not have been more wrong.

Perceptrons

The solution had lain hidden in plain sight for over a hundred years. At the turn
of the twentieth century, William James and Santiago Ramon y Cajal had already
accurately described how brains must learn associations. As experimenters fig-
ured out how to move beyond dissection and tissue staining to study the living
brain at work, a clearer view of neural information processing began coming into

focus.

In a series of papers beginning in the 1950s, neuroscientists David Hubel, Torsten
Wiesel, and a rotating cast of collaborators reported on painstaking investi-
gations of the cat and monkey visual cortex.“ While they presented visual
stimuli to animals under anesthesia, they recorded the activity of individual
neurons using tungsten electrodes. They found that the “retinal ganglion cells,”

which combine inputs from photoreceptors in the retina to create local visual

---

features, are only the first stage in a visual processing hierarchy. In the brain,
those features are in turn combined to form higher-level edge-like features by
“simple cells,” which are themselves combined to form yet higher-level features
by “complex cells,” which combine to form “hypercomplex cells”"—until eventu-

ally, the features in question may be entire objects.

Margaret Livingstone, a neuroscientist at Harvard who did postdoctoral work in
Hubel’s lab, wrote, in an obituary of him in 2013, “Studying vision is fun because
you see what you show the animal, and when you cannot figure a cell out, you
show it everything you can think of; sometimes you find surprisingly specific
things that will make a cell fire, like a bright yellow Kodak film box."22)

Hierarchical recognition is an elegant concept: any perceptual classification task,
no matter how complicated, can be built up as a combination of features, which
are themselves combinations of features—turtles all the way down. This seemed

to be the brain's approach to generalization.

In 1957, Frank Rosenblatt, a young engineer at the Cornell Aeronautical Labora-
tory, decided to build an apparatus to do what the visual cortex does. He called

it the “perceptron.” As he wrote in the introduction to his report, “[I]t should be
feasible to construct an electronic or electromechanical system which will learn
to recognize similarities or identities between patterns of optical, electrical, or
tonal information, in a manner which may be closely analogous to the perceptual

processes of a biological brain.”!2°°)

---

In a passage reminiscent of Borges, Rosenblatt noted that although “[t]he

recognition of ‘similar’ forms can be carried out, to a certain extent, by analytic
procedures on a [...] computer [...] itis hard to conceive of a general analytic
program which would [...] recognize the form of a man seen from any angle, and
in any posture or position, without actually storing a large library of reference
figures [...]. In general, identities of this sort must be learned, or acquired from ex-

perience [...].”

Rosenblatt’s “identities” were the same as McCulloch and Pitts’s “universals” a
decade earlier. Unlike McCulloch and Pitts, though, Rosenblatt created a real,

working system.

The original Mark I perceptron was a three-layer neural net. Its first layer
consisted of a 20x20 array of photocells, or “sensory units,” the second had 512
“association units,” and the final layer had eight “response units.” Each layer was
wired randomly to the next, with a motor-driven potentiometer (like the volume

knob on a radio) modulating the strength of every connection.

---

Raise
iett
asm

tet
fone

PIG. 1 — Organization of a biological brain. (Red areas indicate
active cells, responding to the letter X.)

Projection area tem
Sensory {10 some models) rar ee

FIG, 2 — Organization of a perceptron.

The response units also implemented “lateral inhibition,” a feature commonly
found in neural circuits: when one activated, it inhibited the others, which in
turn fed back inhibition to any competing association units. Using a simple learn-
ing rule that exploited this feedback, Rosenblatt got the device to distinguish

among simple shapes—a square, a circle, a triangle. It was a start.

More than a start: in retrospect, the perceptron was arguably the single most
important advance in AI in the twentieth century. Modern neural nets, especially
those most commonly used for visual recognition, are still powered by “multi-
layer perceptrons” (MLPs), although they use different learning rules and are typ-

ically much deeper—that is, they have many more than three layers.

---

If perceptrons worked—and did so by taking an approach so much more obvi-
ously brain-like than symbolic AI systems—then why did they lay fallow for so

long? Several narratives have merit:

1. Neural nets big enough to do practical work require large-scale parallel
computation, which didn’t become available to most researchers until
inexpensive GPUs (graphics processing units) began flooding the mar-
ket, around 2006.25" This is true; however, if, beginning in the 1960s,
we had begun to seriously engineer parallel neural computers, or
special-purpose hardware like the Mark I, we probably could have had
powerful MLPs by the 1980s. Engineers didn’t push much in this di-
rection because Moore’s Law advanced ceaselessly for six decades after
the invention of the transistor in 1947, shrinking their size, increasing
their maximum clock speed, and decreasing the power the needed to
operate. The industry was eager to reap the most obvious benefits—
making the whole computer smaller, faster, cheaper, and lower-power
—rather than sacrificing these benefits to increase parallelism in the
service of an unproven approach to computing.2=2

2. Large neural nets require large datasets to train, which weren't
available before the web took off. And labeled datasets, like ImageNet
(which researcher Fei-Fei Li began gathering in 2006—that year
again!), relied not only on internet-scale collections of images, but also
on online gig workers to apply labels, like “chihuahua” and “blueberry.”
All true, but let’s keep in mind that Netflix began sending subscribers
digital movies by DVD nearly a decade earlier, and a modest collec-
tion of DVDs contains far more imagery than ImageNet. There was
no shortage of pixels. We also now know that unsupervised learning
works well, rendering extensive labeling unnecessary (as will be dis-
cussed in the next chapter). This would likely have been discovered
decades earlier had neural-net research remained mainstream in the
latter half of the twentieth century.

3. Rosenblatt's original perceptron-training algorithm wasn't powerful
enough to work for complex datasets or deep neural nets; the suite

of tricks required to do so has only been perfected in recent years.

---

The most important of these tricks, though—the “backpropagation”
algorithm, allowing the weights of synapses, or “synaptic weights,” in
an arbitrarily deep neural net to be adjusted to minimize the output
error—had already been worked out by 1970, and was repeatedly rein-
vented by other researchers over the years.'2*#! Like any technology,
dedicated tinkering is required to get the details right. For many years,
there simply weren’t enough dedicated tinkerers working on it, in part
because—

4. In 1969, Marvin Minsky and an MIT collaborator, Seymour Papert,
published a highly cited book entitled Perceptrons.|“*4| Although
dedicated to Rosenblatt, the book was a hatchet job, implying that
perceptrons could never approximate a number of simple mathe-
matical functions, and therefore perceptrons were inherently far
weaker, computationally, than GOFAI algorithms. The book contained
mathematical proofs of these assertions, but the proofs only applied
to simplified two-layer models. It can be shown that with three or
more layers (as even the Mark I perceptron had) any continuous func-
tion can be approximated,/“*») as Rosenblatt himself appears to have

intuited.28"

Despite the protests of Rosenblatt and fellow travelers, the Perceptrons book was
highly effective in discouraging “connectionism,” as neural net research was
then called, for decades, diverting mainstream attention instead to the GOFAI ap-
proaches favored by Minsky, Papert, and their colleagues. In 1988, with interest
in neural nets rising once again just as we entered a final Good Old-Fashioned AI
winter, Minsky and Papert reissued Perceptrons. In a new prologue and epilogue,
the updated edition doubled down on their original critique, claiming that “little
of significance has happened in this field” and that, even by 1969, “progress had
already come to a virtual halt because of the lack of adequate basic theories.”

These claims seem bizarre, if not disingenuous. Just a year before the second edi-
tion of Perceptrons, computational neuroscientists Terry Sejnowski and Charles
Rosenberg had trained a neural net, NETtalk, to pronounce English text. They
showed not only that it could effectively master this notoriously unruly (that is,

---

non-GOFAI-friendly) problem, but that its performance exhibited many human-

like characteristics.2&4

Minsky and Papert’s objections to connectionism make some sense, though, in
light of the theoretical grounding they had been hoping AI might offer. They were
uninterested in the rapid advances taking place in computational neuroscience,
machine learning, or general function approximation. Instead, they focused on
mathematical theories of knowledge representation, manipulation, and formal
proof in the tradition of Leibniz. This required operating at the level of abstract
concepts, more like the “psychons” McCulloch and Pitts had speculated about in
1943 (but that neuroscience had shortly thereafter abandoned, failing to find any
evidence of them in the brain). Per Minsky and Papert: “perceptrons had no way
to represent the knowledge required for solving certain problems. |...] No machine
can learn to recognize X unless it possesses, at least potentially, some scheme for

representing X.”

They wanted, in other words, for knowledge to be represented logically, in terms
of clear taxonomies and semantic relationships—just as Leibniz had imagined.
And such logical representations would, they believed, need to look like Boolean,
yes-or-no variables somewhere specific in the brain. Without such “schematized”
and “localized” knowledge representations, Minsky and Papert did not believe
that higher-order rationality, including causal reasoning, self-reflection, or even
consciousness, would be possible: “[W]e expect distributed representations =")

to tend to produce systems with only limited abilities to reflect accurately on
how they do what they do. Thinking about thinking, we maintain, requires the
use of representations that are localized enough that they can be dissected and
rearranged. |...] [D]istributed representations [...] must entail a heavy price; surely,

many of them must become ‘conceptual dead ends.’"22"

Unlike the book's proofs, these assertions were mere intuitions. To many, they
seemed reasonable at the time. Adherents of the GOFAI school of thought, includ-
ing many trained in linguistics (which is largely concerned with schematized
knowledge representations) continue to argue this position today, though it
seems increasingly disconnected from reality given what modern neural nets can
do, and how they do it.2%

---

Deep Learning

Training multilayer perceptrons is difficult both because of the dependencies
between layers (fiddling with a synaptic weight affects everything downstream)
and because of the dramatically increased sizes of these models. To get a sense of
this, consider that a two-layer “fully connected” perceptron classifying a 32x32
pixel image as one of ten digits already has (32«32)x 10=10,240 synapses—that
is, a synapse connecting every pixel with each of the ten output neurons. If we
add in a single additional 32x32 layer of neurons between the input layer and the
output layer, we now have (32*32)x(32*32) + (32x32)x10=1,058,816 synapses.
Each of these synaptic weights is a model parameter that must be learned from
data, and, roughly speaking, fitting a hundred times more parameters requires a

hundred times more data.!224)

Over time, though, researchers found ways around these problems. The story of
modern “deep learning” is just the story of these tricks accumulating over time,
with compounding gains and accelerating progress as the field finally attracted
serious time and investment. Here are a few representative advances. A complete

list would be much longer:!222)

1. Sparse connectivity, dating all the way back to Rosenblatt’s perceptron,
can greatly reduce the number of weights compared to a “fully con-
nected” layer as sketched above; this makes sparse networks faster
to train and more reliable. In the 1980s, Yann LeCun, John Denker,
and Sara Solla, then at Bell Labs, figured out how to prune unneeded
weights in a more principled way.224)

2. Deep learning itself is a form of sparse connectivity, when you con-
sider that a truly fully connected neural network wouldn't have layers
at all; every neuron would be connected to every other neuron. Ina
multilayer perceptron, though, a neuron is only connected to neurons
in the previous layer and the next layer. Hence, the deeper a network
is, the sparser its connectivity compared to a fully connected network

with the same number of neurons. In the mid-2010s, researchers

---

pushed this form of sparsity to extremes, exploring architectures with
up to a thousand layers.)

3. “Convolutional layers,” first conceived by AI researcher Kunihiko
Fukushima and further developed by LeCun and collaborators,\222!
implement yet another form of sparse connectivity by wiring a neuron
only to a small neighborhood of neurons in the previous layer, rather
than to all of them; furthermore, an entire “channel” of neurons share
acommon weight pattern within this local area, making the number
of parameters to train far smaller than the number of connections.

4. The backpropagation algorithm, as mentioned earlier, allows mini-
mization of an error, or “loss function,” to happen reliably through
many layers of neurons. It involves using calculus to compute the total
downstream effect of fiddling with any given synaptic weight. Virtu-
ally all machine learning today uses backpropagation.

5. The “softmax” function,“ applied to a layer of neurons, implements
something analogous to lateral inhibition, picking out the maximum
activation and enhancing it while suppressing competing neurons,
while forcing the layer’s total activity to sum to one. Softmax was
originally used only for the output layer of classifier nets, which are
trained to be “one-hot” (a single neuron on, all the others off), How-
ever, the suppression of competing activations isn't complete (hence
the “soft”), allowing learning through backpropagation to work.

6. “Max pooling” can discard unneeded resolution, for instance
reducing a 3232 layer of features to a 1616 layer by picking only the
largest values within each 2*2 region to pass on. This works because
the presence of complex features is often more important than their
precise location.

7. Datasets can be “augmented”2°") by shifting, stretching, and rotating
training examples, then using these distorted copies as additional
training data. This helps strengthen the neural net’s perceptual

invariance.

It’s significant that researchers working at the intersection of computer science

and neuroscience pioneered many of these techniques. In recent years, this con-

---

fluence of disciplines has been called “NeuroAlI,” and a number of conferences

and workshops have been convened under that banner.

While the name is new, the phenomenon is not.\222! From the beginning, machine
learning and neuroscience have been continuous with one another, as we've seen.
For many years, the scientific value of this interdisciplinary work was greater
than its technological value, so it was often referred to as “computational neu-
roscience.” With the technological side now ascendant, it’s unsurprising to see
the ordering reversed with “NeuroAl.” But the conference attendees are largely
the same. And while no practical machine-learning trick faithfully models any
specific process or circuit in the brain, many of the tricks are clearly biologically

inspired, just as the original perceptron was.4™!

Using such tricks in combination, researchers fully solved handwritten single-
digit visual recognition in the 1990s," and moved on to increasingly difficult
visual-recognition problems over the following two decades: objects, clothes,
places, plants and animals, natural scenes, faces, and ultimately nearly every-
thing one might encounter while browsing through the photos on a phone.)
Although they were developed mostly for the visual modality, convolutional nets
also work well in many other domains, from auditory recognition“ to weather
prediction.2°! surprisingly, they even work for classifying text,22) but we'll hold

off on exploring neural nets for language until chapter 8.

Closing the Loop

Before moving on, let’s consider neural networks through the cybernetic lens.
On one hand, the perceptron did generate discrete symbolic output—per Rosen-
blatt’s 1957 report, “inhibitory feedback connections guarantee that only one re-
sponse out of a mutually exclusive set can be triggered at one time.... [Response]
units thus [act] like a multi-stable flip-flop.”““*! (In modern neural nets, softmax

layers serve the same purpose.)

Still, GOFAI partisans like Minsky and Papert understood that Rosenblatt was
working squarely within the cybernetic tradition, and, indeed, the response layer
and learning rule only approximated digital logic in the output through the use

of analog negative-feedback loops. The system learned by example, and relied

---

on this analog quality to do so. Neural representations within the network were
distributed and continuous, not localized or symbolic. Synaptic weights were
continuous, and the perceptron as a whole evaluated a nonlinear continuous

function specified by those weights.

Rosenblatt's perceptron made use of randomness too, both in the wiring and in
the learning process: “The penalty that we pay for the use of statistical principles
in the design of the system is a probability that we may get a wrong response in
any particular case....”22"| The perceptron worked precisely because it was far

from the world of cleanly represented knowledge and exact logical inference.

Let’s boil down the main advance Rosenblatt and his successors made over
Wiener: while Wiener’s “black box functions” were expressed in terms of “series
expansions,” the function evaluated by a perceptron is instead specified by a
hierarchy of synaptic weights. A series expansion is a weighted sum of increas-
ingly high-order mathematical terms, typically truncated after only a few terms.
For the kinds of simple cybernetic systems Wiener and colleagues were able to
build (like thermostats, or, eventually, antiaircraft-fire controllers), a single term,
representing a linear approximation, might suffice. Not so for a multilayer per-

ceptron capable of achieving visual perceptual invariance.

The problem isn’t theoretical, but practical. At bottom, a function is a function.
Both neural nets and series expansions are “universal function approximators,”
meaning that either one can approximate any function.22"! However, Wiener’s
more formal approach would have required vast numbers of parameters to go
beyond the linear or first-order regime. Realistic nonlinearities (say, for object
classification) couldn't, in practice, be learned from a limited number of training
examples. By dispensing with this kind of math and simply wiring together
simplified neurons in multiple layers, Rosenblatt had stumbled onto a far more
learnable way of representing the kinds of functions needed to transform images,
sounds, and other natural stimuli into invariant classifications. One could at-
tribute that to luck, intuition, or both, but, at some level, something like it had to

work, or our brains would all be like that of poor Funes, el memorioso.

Why perceptrons are so “learnable” relative to more traditional function approx-

imators is not yet fully understood.“ Recent analyses suggest that it may have

---

to do with a “compositional prior,” meaning a bias“!"! toward learning functions
that can be defined in terms of a hierarchical composition of simpler functions.
This kind of prior appears to be useful for all sorts of cognitive tasks and gener-
alizations, not just vision.“ (Intriguingly, the symbiogenetic view of evolution
described in chapter 1 can also be understood as a learning algorithm that favors

hierarchical compositions of functions.)

Although the perceptron is cybernetic in spirit, it doesn’t qualify as a complete
cybernetic system, at least not as usually deployed. An image classifier has no ob-

vious agency. It doesn’t act, it just is, like any other mathematical function.

One notable exception, though, is a 2016 paper from researchers at Nvidia: “End
to End Learning for Self-Driving Cars,”!214) describing the DAVE-2 system (suc-
cessor to DAVE, an earlier “DARPA Autonomous Vehicle”). The authors trained a
convolutional neural net to “map raw pixels from a single front-facing camera
directly to steering commands.”“"4) Their abstract continues, “This end-to-end
approach proved surprisingly powerful. With minimum training data from
humans the system learns to drive in traffic on local roads with or without lane
markings and on highways. It also operates in areas with unclear visual guidance

such as in parking lots and on unpaved roads.”

---

Output: vehicle control

Fully-connected layer
Fully-connected layer
Fully-connected layer

Convolutional
feature map
64@1x18

Convolutional
feature map
64@3x20

Convolutional
feature map
48@5x22

Convolutional
feature map
36@14x47

Convolutional
feature map
24@31x98

Normalized
input planes
3@66x200

Input planes
3@66x200

DAVE-2 appears to be a remarkably pure realization of Wiener’s cybernetic vision,
courtesy of the universal function-approximating power of a convolutional net.
One can think of it as a much more sophisticated version of the Palomiila, with
real eyes instead of photocells and twenty-seven million synapses in place of a
couple of vacuum tubes. (For rough comparison, a honeybee probably has about a
billion synapses and a mouse has about a trillion, though biological synapses are

not interchangeable with model parameters.)

The nonlinearity of DAVE-2’s learned function allows for rich, contextually
dependent behavior without explicit “if/then/else” logic; lane markings, guard
rails, and other cars influence driving in all the ways one would hope. Although
the network's only output is a steering wheel angle, if we were to perform “neuro-
science” on this network after training, we would undoubtedly find neurons that
respond specifically and selectively to all such objects, much like the visual-sys-

tem neurons Livingstone recorded from during her work in Hubel’s lab.

---

This picture is still missing important elements, though. Notably, the input to
the convolutional net is only a single frame of video, and the output only controls
steering, not gas or brakes. It involves no prediction of the future. Since the net-
work is run at thirty frames per second, vehicle speed is kept steady by a human
copilot, and steering is forced to be reasonably smooth by mechanical inertia,

the system undoubtedly feels dynamic, but the learned model has no dynamics.
Nothing like planning or memory is possible here, only instantaneous reflex-like
response, fully determined by prior offline training. Neither is the model model-
ing itself in any way; its umwelt is purely external, just a view of the road at that

moment in time.

Rosenblatt’s original (and cybernetically informed) vision was considerably
broader. He emphasized that what we now simply call the “perceptron” was in
fact only a “momentary stimulus photoperceptron, [...] the most elementary
device which could be built to demonstrate the general principles of this type

of system.” Not only could other sensory modalities also be imagined, but “tem-
poral pattern perceptrons” would also have the ability to “remember temporal
sequences of events, rather than transient momentary images, such as would be

obtained from a collection of isolated frames cut from a strip of movie film.”24

Most of this remained on the drawing board, but, tellingly, even the Mark I mo-
mentary stimulus photoperceptron had been implemented as a physical device
with real dynamics, able to learn by adjusting its parameters based on feedback
at any time. Today's neural nets generally don’t share this property. Even if they
act as controllers in a feedback loop, as in a self-driving car, they do not alter
themselves in a feedback loop during operation, the way we do. Instead, they are
trained offline on static data using batch processing, much the way ENIAC and
the other early computers crunched away on big problems overnight (or for many

nights).

Thus, the field we call “machine learning” still doesn’t generally produce systems
that learn, but only systems that act. It may be hard to consider something “alive”
if nothing it experiences can durably affect it, and, for many, calling something

“intelligent” may also be hard if it can’t learn from those experiences,2+*! In these

---

crucial respects, we're still working toward the ambitious vision laid out by

Wiener, Rosenblatt, and the other early cyberneticists in the 1940s and 'S5Os.

---

# Chapter 4

4. Learning

Unkneading

It's time to explore the inner workings of deep neural nets in more detail.

Consider a perceptron trained to recognize bananas on sight, in all their varia-
tions and orientations, against any background. Normally this would involve a
final one-hot layer in the neural net containing a “banana neuron”; since we need
at least two neurons for such an output layer, let's also assume a “not-banana
neuron” lights up in response to everything else. Supervised training of this
model would involve curating many images of either bananas or something else,
each labeled with a single bit specifying which of the two neurons should acti-

vate. By the end of the training, we'd have a banana detector,“

Recall from chapter 3 that in a convolutional net, higher-order features emerge
hierarchically as combinations of lower-level features. As activations propagate
to higher layers in the network, the features represented become increasingly in-

variant—that is, more semantically meaningful.

I think of the process as a bit like kneading dough. Every layer of a neural net
works its input data, turning it like a ball of dough in a certain direction and then
pressing it down, flattening it as if against a countertop. Then the next layer

does the same. Understanding how and why this “data kneading” accomplishes
anything will require deeper insight into how the successive layers of a neural net
transform the information flowing through them. Let’s work backward from the

output layer.

Suppose that the penultimate layer, just before the one with two neurons, has
128 neurons. In this layer, input images are said to be “embedded” in 128 dimen-
sions. One can think of the activations of those neurons as the coordinates of a

point in a 128-dimensional “embedding space.”

It's a bit mind-bending to think about high-dimensional spaces, since we live in
only three dimensions, so let’s develop a bit of intuition. Specifying a point on

a 2D surface requires two numbers—such as x and y on a graph, or latitude and

---

longitude on a map. Specifying a point in 3D space requires three numbers; ina
rectangular room, for instance, it could be x and y coordinates on the floor, and
a height above the floor, z. So why not 128 numbers specifying a point in 128 di-

mensions? It’s like 3D, only ... more. Just pretend it’s 3D. (Everyone does, secretly.)

None of the 128 neurons in the embedding layer is itself a banana neuron—or
there would be no need for an additional output layer. Still, most of the banana
recognition work must already have happened by this point, since the output
neuron just receives a weighted average of those 128 neural activations. The
weights associated with the banana neuron's 128 inputs can be thought of asa
“vector,” or direction, in the 128-dimensional embedding space. Remember that
every image corresponds to a point in this embedding space. The farther out
along the “banana direction” such a point lies, the stronger the input to the ba-

nana neuron; so we can think of the vector as pointing “bananaward,”*+4)

Alternatively, we could imagine a “hyperplane” at right angles to the banana vec-
tor. In 3D: think of the hyperplane as an ordinary plane, a big flat sheet of paper.
The “bananaward vector” can be visualized as an arrow coming straight out of
that sheet. Since the arrow points toward banana-ness, it follows that we ought
to be able to slide the sheet of paper along the arrow until the points representing
banana images all lie on the far side, while the non-banana points are on the near
side. The hyperplane thus defines a “banananess threshold.” The banana neuron
will light up only when the level of banananess exceeds this threshold; otherwise,

thanks to lateral inhibition, the “no banana” neuron will light up instead.

---

This “thresholding” transforms an embedding space that would otherwise be
continuous into a categorical yes or no. A banana is either there or it isn’t. More
precisely, if a banana is detected, that detection is invariant to whether the im-
age’s banananess was just over the threshold or far over it.2!*) Conversely, if the
“no banana” neuron is activated, it doesn’t matter whether the banananess was

just under the threshold, or far under it.

In summary, the transformation from the penultimate layer to the output layer
consists of two steps. First, each output neuron is looking for a pattern in the
previous layer (such as banananess), then the neuron applies a threshold to make
that pattern detection more invariant. These are like the two kneading steps: ro-
tating the ball of dough into a certain orientation, then pressing it down against
a hard surface.

The same basic steps take place in every earlier layer of a deep neural net, too,
All neurons calculate a weighted sum of activations in the previous layer. And
although softmax is typically only used for the output layer, all neurons (artificial

or otherwise) involve some form of thresholding or “nonlinearity.”

One of the most commonly used nonlinearities is ReLU, which stands for “Rec-

tified Linear Unit”; such a neuron has zero response if the weighted sum of its

---

inputs is less than zero, and otherwise has activation equal to that weighted sum.
Like softmax (which, recall, approximates lateral inhibition in real neurons),
ReLU is inspired by basic neuroscience. Real neurons either fire action potentials
or don’t. Their firing rate is thus either zero or positive; a neuron can’t have a
negative response. ReLU is pretty much the simplest nonlinear alteration one can
make to the linear “identity function” /(x)=x to avoid negative output in an artifi-

cial neuron.

—2 -1 0 1 2

Nonlinearities like ReLU are essential to deep learning; without them, there

would be little point in making a neural net more than one layer deep. A weighted
sum of weighted sums is just another weighted sum.2!"! However, with a non-
linearity, not only can successive layers no longer be replaced by an equivalent
single layer, but, as mentioned in the previous chapter, virtually any function can

be approximated, given enough neurons,|22"!

More intuitively, nonlinearities like ReLU implement a limited form of invari-
ance. Every layer in a deep neural net is doing the same as the output layer:
looking for a pattern in the previous layer and lighting up if it’s present. Single-
neuron pattern detection is rudimentary, consisting as it does only of a weighted
average—a form of recognition sometimes called “template matching.” Still, a
neuron with a nonlinearity like ReLU turns the presence or absence of a pattern
into an approximate “yes” or “no.” This allows the next layer to operate on higher-

level, more abstract, and more invariant patterns.

To lean into the dough analogy a bit further, template matching, or taking a
weighted average of the neural activations in a layer, is something like rotating

the dough ball into a particular orientation. In fact, mathematically, it pretty

---

much is a rotation—just imagine rotating the embedding space so that the
hyperplane is horizontal, like a countertop.424! Applying the nonlinearity then

squishes the data down.

Without that squishing step, no useful work would get done by repeating the
process—we would just be rotating the dough ball first this way, then that way,
then the other way, which is equivalent to a single overall rotation. The squish
between every rotation is what transforms the dough. There is no single rotation
and squish that will produce the same result as a hundred consecutive rotations
and squishes: the dough develops gluten, the network gets better at recognizing

bananas.

The key difference is that when we knead dough, our rotations and squishes are
random. We may have started with flour, water, and salt, but, by the end, these
random operations have produced a uniform, glutinous output. Through the
magic of machine learning, though, a trained neural network can do the opposite,
starting with a “pixel dough” in which images of all kinds are swirled together,
then progressively unswirling them until they’re cleanly separated by category.
It’s as if, by orienting the dough just so before pressing it down each time, you
could “unknead” it until you're left with a big pile of flour, a little pile of salt, anda
puddle of water.

Transfer

If we were to lop off the final softmax layer of our banana detector, its new
output would be a 128-dimensional point in the embedding space of the previous
layer. Given many varied input images, what kind of patterns would those points

make?

It's possible to visualize such patterns, although we must use mathematical
tricks to reduce many dimensions down to something we can easily plot, in 3D

or 2D. Many research papers have used such visualizations over the years, though
the most striking one I've seen was made by a Turkish-American artist, Refik

Anadol.

---

Already an established artist, Refik got his start in AI art with the Artists +
Machine Intelligence (AMI) program my team and I founded in 2016, at the dawn
of generative AI. He has since become famous. One of his first large-scale AI art
commissions, Archive Dreaming, was a 2017 collaboration with SALT, an art and
research institution based in Istanbul. SALT houses a major archive of photo-
graphs, architectural drawings, maps, posters, correspondence, and ephemera
dating from the last century of the Ottoman Empire to the present, and they
have been busily digitizing it. Refik used neural nets to generate embeddings for
1.7 million visual documents in the archive and created a room-size immersive
visualization that allowed one to swoop through all of these documents, each
rendered as a thumbnail hanging in the void. In that embedding space, visually
similar objects cluster together, allowing one to get a sense of the archive as if it

were a galaxy with 1.7 million stars, all arranged in space as if by a cosmic Dewey

decimal system.

Suppose Refik had used the banana-recognition net to generate his embeddings,
and the SALT archive had included a bunch of banana images. (For all I know, it
might.) We know that a hyperplane would separate those banana images cleanly
from the non-banana images; but what about other fruits, or other objects

altogether?\222)

Remember that the banana recognizer works by creating an increasingly invari-
ant hierarchy of visual features; the banana/no-banana output neurons are just

the visible tip of a submerged iceberg of features. Consider, for example, that

---

unripe and overripe bananas look very different. Therefore different ensembles
of features will likely have been combined to calculate one or more “banana of a
certain ripeness” neurons in the embedding layer, but this ripeness information
must be discarded to create the final ripeness-invariant banana neuron. The
same will be true of bananas in different orientations, or under different lighting

conditions.

These observations explain “transfer learning”: the ability to retrain a network
to do a related task, using much less labeled data than would be required to train
from scratch.!224) If we wanted our banana network to detect only ripe bananas,
for instance, it would only take a bit of tweaking of those final 128 weights to ex-

clude the unripe cases.

More dramatically, the same trick will work nearly as well to turn the banana de-

tector into an apple detector. Apples are also fruits, though red and round instead
of yellow and long. The embedding layer will already contain neurons represent-

ing apple properties that are either like or unlike banana properties. Thus, apples

could easily be detected simply by adding an apple neuron to the output layer

alongside the banana neuron.

We could even learn the weights for that apple neuron from a lone exemplar, by
setting them based on the activations of the embedding layer in response to a sin-
gle apple image.“ (An average based on a few apples would be better, but a sin-
gle one will do.) The network will subsequently recognize “another of those.”\222!
This is more or less what we do in adulthood when we learn about an unfamiliar
object category from a single exposure. It’s called “one-shot learning,” and can be

thought of as a special case of transfer learning.

The success of transfer and one-shot learning suggests that training a banana
detector mostly involves getting it to learn how to see generically—that is, devel-
oping a general sense of perceptual invariance in the visual world. This involves
learning the correlations between pixels in images, regardless of how those im-

ages are labeled.

---

Is it necessary, then, to start with a banana detector at all? More to the point, do
we really need to label a gajillion images with the banana/not banana bit to learn

generic visual invariance?

We don’t. A neural network can learn how to see without any labeling. This sim-

ply means relying on unsupervised learning rather than supervised learning.

One popular unsupervised method, known as “masking,” involves blacking out
random parts of the images and requiring the network to fill in, or “inpaint,” the
blacked-out parts as accurately as possible. Any neural net that can do this well,

for a large and varied set of images, will certainly have learned pixel correlations.

Notice that this is very much like predicting blacked-out words or passages in
text—which is how large language models are trained! That’s why, in this book,

I use the terms “prediction” and “modeling” almost interchangeably. To model
data is to understand its structure, whether in space, in time, or both; hence, to be
able to guess unseen parts of the data, whether those are masked or occluded in
the present, or belong to the future (in which case the term “prediction” is most

apt), or even took place, unobserved, in the past.

If a neural network has learned to successfully inpaint (or “predict”) missing
pixels in a corpus of training images, that implies it has also learned how to rec-
ognize everything represented in those images—apples, fire hydrants, Siamese
cats—not just bananas. It will know how to distinguish figure from ground, it
will understand depth of field, it will recognize colors, and it will be able to distin-
guish ripe from unripe fruit. The evidence: if the network was trained on banana
images, and you test it by blacking out half of a previously unseen banana image,
it should convincingly fill in the other half. Moreover, the ripeness of the filled-in
half should match the ripeness of the visible half.

This raises some interesting questions, both practical and scientific. On the
practical side, all sorts of knowledge may be latent in a neural net trained with
unsupervised machine learning, but how would we read it out? That is, how
could one turn this pixel inpainting model into an actual Siamese cat detector,

banana detector, or fruit-ripeness detector?

---

We might also wonder about the relationship between unsupervised learning
and neuroscience. It’s nice to get rid of all that banana/not banana labeling, but
blacking out random regions of a sheaf of arbitrary images and training the
model to fill them in still seems like a highly artificial task. What does this have to

do with how learning works in brains?

Green Screen

The limitations of transfer learning, and the parallel limitations of our own
brains, are revealing. If the banana network had been trained entirely on photos
taken in supermarkets and we then tried to use it to recognize individual faces, it
would do a poor job, because the transformations leading to the embedding layer
would not include learned representations of the needed features. Even if super-
market shoppers had been visible among the “not banana” images, the relevant
details of their faces might get discarded early in the network, because those de-
tails are irrelevant to banana detection—if it’s any kind of face, it’s not a banana,

end of story.

A similar effect explains why people who grew up in a racially homogenous
environment tend to be so poor at distinguishing individuals of other races. We
learn our face embeddings young, and they are exquisitely sensitive—but only
within the statistical distribution we have learned from. Hence the all-too-com-
mon sayings, usually considered racist, that all people of a “foreign” race “look
alike.”22*) Yet in a very literal sense, if our brains weren't exposed to “foreign”
faces as children, then, for us, it’s true. As adults, the best we can do is to under-
stand the limitation and work on it (ongoing improvement is possible). Less
excusably, the same problem is evident in convolutional nets trained to recognize

faces based on inadequately diverse datasets.|224l

The same phenomenon holds for recognizing phonemes. In Japanese, for exam-
ple, there are no separate “r” and “1” phonemes, making it hard for adult native
speakers to distinguish between the English words “rock” and “lock.” Studies dat-
ing back to the 1980s and’90s show that, from the moment an infant's brain is
exposed to language—and long before learning to speak—the brain's neural net-

works begin to learn meaningful invariant representations of speech sounds.22"

---

While these invariant representations constrain what the baby can hear (and
later, say), they are essential “scaffolding” for learning higher-order concepts. In
particular, babies can learn new words efficiently only once they have developed
a rich lower-level representation of the necessary speech sounds. Japanese adults
learning English can, over time, improve their ability to discriminate “r” from “1,”
but it’s much more of a slog than learning a new word in Japanese, since learning
a new low-level representation doesn’t benefit from any of that developmental
scaffolding.

Learning, then—whether supervised or not—is mostly a matter of “representa-
tion learning”—that is, learning how to embed. Using a combination of theory
and machine learning experiments, physicist and AI researcher Brice Ménard and
colleagues have demonstrated that representation learning in multilayer percep-

trons is universal, regardless of how they’re trained.2*2!

One could even say that learning is also learning to learn. That is, once a suitable
generic embedding or representation has been learned, associating a label witha

specific point or region in the embedding space becomes trivial.

So, although our brains take a long while to learn how to see the world and how to
hear language, once we have these representations down, we become adept one-
shot learners. If you are shown a kiwi for the first time, you'll henceforth imme-
diately be able to recognize that furry little fruit. A perceptron trained on general
vision tasks can do the same, with the addition of a kiwi neuron to the output
layer trained in one shot. That's so much easier than labeling lots of kiwi (and

not-kiwi) images and training on them from scratch.

If a perceptron is trained to inpaint pixels rather than detect bananas, its high-
level layers will be general embeddings, equally good at representing bananas,
faces, cats, kiwis, and anything else in the (unlabeled) training data. Moreover,
there will be neurons specifying the ripeness of fruits, the features of faces, and
the breeds of cats. When the image is of a cat, its eye color will be guessed if need
be, for instance if we've blacked it out—otherwise, those pixels could not be filled
in. It follows that latent eye-color knowledge is also present if the cat happens to

be facing away from the camera.

---

You can see how powerful unsupervised learning is. That’s why, in recent years,
researchers have been shifting away from the old supervised approach. Not only
are the large numbers of labels we used to rely on unnecessary; they may actually
impede learning, since training a model only on a particular classification task
can allow the learned representations to get away with being less robust. More-
over, the very fact of labeling is bound to introduce additional errors and biases,

and is also labor intensive—at best, boring, and at worst, exploitative.424

The hourglass-shaped “masked autoencoder” is now a common way to construct
an unsupervised perceptron-style model.!2*4! Starting from a “retinal” input layer
of, for example, 512512 color pixels, a sequence of progressively narrower lay-
ers culminates in a bottleneck—say, 128 values—which then expands back into
an output layer of the same shape as the input. The input omits masked pixels,

which may amount to seventy-five percent of the total, while the output recon-

structs (or “hallucinates”) the whole image.

---

A masked autoencoder might appear unimpressive. If you picture it as a machine
with a digital camera connected to the input layer and a display connected to

the output layer, it seems to behave like an ordinary viewfinder. You feed ina
512*512-pixel image of a Siamese cat, and out comes ... a 512*512-pixel image

of the same cat, indistinguishable at a glance from the input.

The masking capability adds magic, though. In addition to the three color chan-
nels (red, green, and blue), masked autoencoders use a binary masking channel to
tell the network which pixels to use as input, and which to inpaint. Suppose you
dipped your hand in a special color of green paint that will be interpreted as that
mask—as in the “green screening” technique in Hollywood, where live actors are
recorded against a solid-green background in the studio, then the footage is com-
posited into a computer-generated environment. Here, you'd wave your green-
painted hand in front of the camera, and the autoencoder would do its best to
inpaint those pixels. On the viewfinder, anything that shade of green would be in-
visible, as if the autoencoder had perfect x-ray vision and could see right through

your hand—even if you were to cover a large portion of the visual field.

Of course, that inpainted content is a hallucination. If the area you cover up is
small, or is entirely predictable from the surrounding context, the reconstruction
will seem flawless. But in general, it won’t be. If your hand is partly occluding the
cat’s body, there’s no way for the model to know the arrangement of every hidden
strand of fur, so those details will be made up. And if you cover everything except
acorner of blue sky, the reconstructed scene might have little in common with

what’s actually there.

The first half of the neural network begins with an input image and, layer by
layer, narrows to 128 values at the bottleneck. It looks just like a supervised clas-
sifier stripped of its output layer, which suggests that the bottleneck acts like an

embedding—and indeed it does.

We can also interpret the bottleneck layer as a form of image compression (as
described in chapters 1 and 2). Compression is, in a deep sense, closely related to
language. It extracts the meaning from a signal, its semantic essence, from which
the original can be reconstructed, at least statistically. If you can see just enough

of the cat's body to know it's a Siamese, then this knowledge suffices to imagine

---

what its head will look like, where its eyes will be, and that those eyes will be blue.
The strands of fur might all lie in different places in the reconstruction, but if it’s
done convincingly, a judge confronted with the original and the reconstruction

wouldn't be able to guess which is which. The details would vary, but the seman-

tic content would be the same.

Grandmother Cell

Our visual cortex is not so unlike a perceptron, but it doesn’t get trained by
reconstructing arbitrary collections of partially masked static images. Instead,
our brain is exposed to a continual stream of “video” from our eyes, broken up by
eye movements, called saccades, that we make approximately five times a second.
The brain also controls those saccades, along with the orientation of our heads

and the position of our bodies, so the stream isn't passive, but actively generated.

Still, masked-autoencoder training isn’t as far from our experience as it may
seem. The retinal fovea, where we can resolve enough detail to read, is barely big
enough to make out a handful of printed words. Even that region is noisy and
jittery. The wider visual field is much lower in resolution and crisscrossed with

blood vessels.4! This certainly differs from our impression of what we see.

A dramatic series of experiments using eye tracking done in several labs between
the 1970s and the '90s illustrates this.224 A subject sits in front of a display
showing a grid of letters. Wherever the viewer's eyes are looking, the display
shows stable underlying text, but everywhere else, the letters are randomized.

To an onlooker, the entire screen looks like an illegible jumble. But, if the window
of clear text is a mere eighteen characters wide—about three characters to the
left of the fixation point and fifteen to the right, in a language like English that is
read from left to right—then to the subject, the whole page of text looks clear and
steady. This is what neuroscientists mean when they say we “hallucinate” the

world into existence based on the sketchiest of signals.

From the moment we open our eyes, soon after birth, and begin swiveling them
around using our “exterior ocular muscles,” we're putting our visual systems
through an unsupervised training regimen much like that of a masked autoen-

coder. With every saccade, we have the opportunity to test whether or nota

---

previously unresolved part of the environment looks as we had predicted or “in-

painted” it in our heads, and to improve our model accordingly.

After a while, we learn to saccade to the spots that matter the most, and where
our uncertainty is highest—was that a tiger nosing through the underbrush?—
thereby constantly pinning our reconstruction to reality. Of course, the moment
we saccade away, uncertainty in that spot begins to grow again, reminiscent of

the way an unobserved particle begins to blur in quantum mechanics.

Vision is not the raw stream of sensory input from our eyes. Rather, that input
stream acts like an error-correction signal. Vision—what we actually see—is a
reconstruction of the world around us, an actively maintained and constrained

hallucination.

Using nothing but prediction, then, we will rapidly learn a powerful unsuper-
vised model of our visual environment. It will include sparse neural represen-
tations that have just the kinds of high-level semantic meanings that masked
autoencoders learn, that Hubel and Wiesel recorded in the cat visual cortex, and

that have even been recorded from the brains of awake humans.222)

Iintroduced the concept of sparsity in chapter 3 to describe connectivity in neu-
ral networks, both artificial and biological. In a sparse network, neurons are only
connected to a small subset of the other neurons in the net; unless the network
as a whole is very small, this constraint is essential for efficient learning—and, in
a real brain, it is physically impossible for every pair of neurons to be connected.
The whole field of deep learning can be understood as an exploration of sparse
neural architectures, starting with the separation of neurons into multiple dis-

tinct layers.

The idea of sparsity can extend from connectivity to activity.22* In a neural
network with sparse activity, only a small subset of neurons will be active (that
is, have nonzero activation) at any given time. This, too, is a physical requirement
for biological brains, because a neuron burns serious energy when it fires. (That's
why epileptic episodes, in which overexcited populations of neurons start to fire
continuously, can't go on for too long, and can lead to brain damage as energy re-

serves deplete and toxic byproducts build up.)

---

Even without such physical constraints, sparse activity appears to arise naturally
in trained neural networks.“24 In the final layer of a classification network, the
reason is clear: softmax forces the output layer’s total activity to sum to one,
while supervised classification encourages a one-hot distribution, with the activ-

ity dominated by a single neuron—an extreme form of sparsity.

Less obviously, activation sparsity emerges in earlier layers too. Nonlinearities
like the ReLU function naturally lead to sparsity, since they replace what would
otherwise be negative activity with zero activity, and the resulting “quietness”
in one layer spreads through subsequent layers. But in a more profound sense,
sparse activity comes with the increasing specificity of every neuron's response

as the network learns.222!

Your cortex doesn't have any single “banana” neuron. However, the idea that we
might have unique neurons in our brains corresponding to highly specific per-
cepts or memories has a long history. The term “grandmother cell” was coined
in 1967, somewhat cheekily, to refer to a hypothetical neuron that activates only
in response to one’s grandmother.24! Margaret Livingstone’s recollection of a
cat visual neuron that, after an extensive search, was found to respond only toa
yellow Kodak film box can be interpreted as evidence of something resembling
a grandmother cell. A famous 2005 Nature paper, “Invariant Visual Represen-
tation by Single Neurons in the Human Brain,”=“"! documented a neuron ina
human subject that seemed to respond only to Jennifer Aniston ... and another
neuron that responded only to Jennifer Aniston and Brad Pitt together!““ The
researchers also found a Pamela Anderson neuron, which responded specifically
not only to pictures of Anderson (including a caricature of her), but also to her

name written out—and not to any other name or string of letters they could find.

As suggestive as these findings are, remember that no supervised-learning
process was forcing a (hypothetical) one-hot layer somewhere in your brain to
activate a single “banana” or “grandmother” or “Pamela Anderson” neuron, to the
exclusion of all else. Such single points of failure would make your brain far too
fragile. Would you suddenly be unable to recognize your grandmother if “her”
neuron died one day, or just failed to fire? And if you're using up neurons on such

granular concepts as Jennifer and Brad together, do you risk running out?

---

No: in a sparse distributed code, which is learned by a set of high-level neurons
(analogous to the embedding layer) with neither supervision nor centralization,
a whole set of neurons in your brain lights up in response to your grandmother,
or a banana, or a specific movie-star couple. Even if only one in ten thousand
light up, that’s still nearly ten million neurons. Soif a few of those remain silent,
it probably won't matter. (And, while the code is sparse, it's not too sparse, or a
neuroscientist poking around in someone's brain while showing them pictures
would never get lucky enough to find a Pamela neuron, let alone also a Jen neu-

ron, and even a Jen and Brad neuron.)

As a bonus, sparse distributed representations are vastly more efficient than a
one-hot code. With 128 neurons, a one-hot code can only represent 128 things.
In a sparse code that involves, say, sixteen of them lighting up at a time, there are
about ninety-three quintillion possibilities.!244) With larger numbers of neurons,
the available combinations are virtually limitless, even accounting for plenty of

redundancy.

Final Causes

Let’s now switch from a perception-centric to a motor-centric perspective. In
doing so, we will be moving farther away from perceptrons and closer to real

critters.

Suppose a neuroscientist records from neurons somewhere along the complex
pathway from an animal's visual cortex to its exterior ocular muscles, postu-
lating, quite reasonably, that these spike trains (that is, sequences of action
potentials) issue motor commands for eye movement. How could the neurosci-
entist “decode” this command stream? The answer, of course, is to simultane-
ously measure eye movement and build a model (these days, probably using an
artificial neural net) that, given the spike trains, can predict eye movement. If it
works reasonably well, voila—an eye-movement command-stream decoder, and

thereby proof that what is being recorded is a command stream!

However, what the neuroscientist has actually created could equally be inter-

preted as an artificial brain region that—if the predictive-brain hypothesis is

---

right—performs exactly the same kind of prediction task that every other brain

region performs! The “decoding” will “work” reasonably well, to the extent that

1) most of the information used by downstream neurons to carry out their
prediction is captured by the recording,

2) the timescale is fast enough to allow feedback loops to be ignored,

3) the neuroscientist’s model is sufficiently powerful to proxy the down-
stream brain region, and

4) the downstream region isn’t actively trying to evade prediction via dynami-

cal instability and randomness (per chapter 3).

In short, given the feedback loops present everywhere in the brain, the “com-
mand stream” interpretation is arbitrary. If various brain regions are trying to

predict each other, no inherent hierarchy determines which one is giving orders.

Neuroscientists and AI researchers may find this counterintuitive; we need a bit
of neuroanatomy to understand why. Neurons have a cell body located near the
“dendrites” that receives inputs, and a long process, the “axon”—I've previously
called these connections “wiring”—sending neural spike trains to other neurons
(or muscles) elsewhere in the brain or body. Those wires can be really long. For in-
stance, the axon of a motor neuron with a cell body in the lumbar region of your
spinal cord can extend all the way to the tip of your big toe, a distance in excess of

three feet. (In blue whales, axons can be thirty feet long!)

It's tempting to imagine neurons as little people, doing their “thinking” near the
body or “head” and deciding what signal to send out along their axonal “tail” toa
downstream target. Using philosophical language, one could say that we think of
the head as the “agent” and the tail as the “patient,” meaning the passive recipient

of the agent’s actions.!2*!

The idea that the target could be in charge seems odd, given where the decision
about when to spike appears to be made and the direction in which that spiking

signal appears to travel. But, in a sense, the tail wags the dog.

An example will help illustrate why. Imagine a theater has fifty free seats that
become available five minutes before a show starts, at eight o'clock sharp. The

usher is given a counter. At 7:55, she starts pressing its button every time some-

---

one walks in so that she can close the doors when the counter reaches fifty, or at

eight o'clock, whichever comes first. It’s a popular show, so at 7:57 the doors close.

Why did the doors close? One answer, corresponding to what Aristotle called the
“efficient cause,” is that the fiftieth person walked through the door. Another,
deeper answer, corresponding to what Aristotle called the “final cause,” is that

the theater had reached capacity. These “whys” differ in where they locate agency.

If we were alien researchers studying the theater, we would notice that a particu-
lar person walked through, triggering a click, causing the usher to close the doors,
and could easily mistake that fiftieth theatergoer for the agent that made the

doors close. The aliens would, in other words, observe a “command stream,” with

the commands issuing from the theatergoer to the usher.

But, of course, none of the theatergoers exhibited agency here. The fiftieth the-
atergoer might not even have noticed that he was the last one to make it in, and
certainly would not think of himself as having closed the door. To understand
where the agency really lies, we need to zoom out and look at the whole system
from a functional or purposive point of view, and this requires understanding
events farther back in time—the causes of the causes—as well as more abstract

concepts like theater capacity and the usher’s job description.

As every kid knows who has asked an increasingly annoyed adult “why” after
every attempt at an explanation, there really is no such thing as a final final
cause. It is meaningful, though, to distinguish between a mechanistic or “how-

like” why and a purposive, agential, “final cause” why.

Here’s one way to tell the difference: when an event has a final cause, disrupting
the causal chain leading up to it will (when possible, and within limits) not per-
manently disrupt the event, but merely force it to be achieved by other means
—which implies an intelligent agent at work, doing that “causal rerouting.” For
instance, if the theater-observing alien is meddlesome and takes away the clicker,
the usher will shrug and use some other method to count people as they come in,

perhaps with marks on paper or a mental tally.

Similarly, if one of your muscle cells is working hard and there isn’t enough

oxygen available to meet the energetic demand with aerobic respiration, it will

---

switch to anaerobic metabolism, a different set of chemical pathways that can
liberate free energy without oxygen. Agents are adaptive and resourceful, even

when they are individual muscle cells!

Hence it’s meaningful to answer the question “why do our cells need oxygen?”
with the final cause answer, “because it’s used to obtain free energy.”2*4! Oxygen
is needed for the aerobic means to that end, and obtaining free energy is a critical
cellular function that must be achieved one way or another. (Unfortunately, in
our cells, an oxygen debt is incurred via the anaerobic route, so you can’t remain

anaerobic for long, and you'll pant for a while after the vigorous exercise stops.)

Now let's return to the nervous system. Neural circuits are functional too, and,

in complex nervous systems, their functions are learned. Learning requires
signals relating activity to its downstream effects to flow backward, from target
to source; hence the “backpropagation” algorithm for training artificial neural
nets. As will be discussed in chapter 7, real brains are unlikely to implement the
backpropagation algorithm, but whatever algorithm they use must involve infor-
mation about “downstream” effects somehow making its way back “upstream”
to the neural machinery that caused those effects, so that the machinery can

be modified accordingly. In this sense, learning is the very essence of backward

causality.

Neuroscientists often don't directly observe learning taking place in electro-
physiological experiments, because it’s slower than real-time electrical activity.
It's also not nearly as well-understood. We figured out how neurons spike in the
1950s, but are still arguing about how they modify their inputs and parameters
to learn when to spike. Hence, our understanding of the slower aspects of nervous
systems exhibiting backward causality lags far behind our understanding of the

mechanisms underlying their rapid, forward causality.

More abstractly, we tend to notice only efficient causes, and not the final causes,
just as an alien watching the theater fill up would have missed the earlier inter-
action when the theater manager gave the usher a clicker and directions about

when to close the doors.

---

Sometimes final causes get ignored for another, related reason: they smell of
teleology. Indeed, the whole idea of a final cause only makes sense in the context
of purposive behavior. But as we've seen, biological (and more broadly “enten-
sional”) systems are characterized by purposes. We can only understand them

functionally, which means embracing Aristotle’s final causes.

Meathead

This brings up an unsettling question: to what degree is the brain really “in
charge” of the rest of the body?

Since learning determines what each neuron does—which signals it responds to
and which it ignores—a neural cell body with a long axon projecting to a different
brain region doesn’t only live to serve the region near the cell body. It’s also an
outpost, a listening station, whose learned function involves serving the commu-

nity of neurons at the far end of the axon.

This is most obvious for the neurons in our sensory periphery, which we can
think of as being in contact with our environment. Pressure and temperature
sensors in our skin relay their signals to “somatosensory” cortex; light-sensitive
cells in our retinas send information to the visual cortex; and vibration-sensitive
hair cells in our inner ears send information to the auditory cortex.4*! These

cells are clearly information-gathering outposts.

You probably wouldn't say that a sensor on your fingertip is the “boss” sending
commands to drive your behavior, but, rather, that it's one of many inputs in-
forming your behavior. Under certain circumstances, though—such as touching
a hot stove—it would be hard to argue that these sensory neurons aren’t bossing
you. Your interests as an organism are best served by the fastest possible reaction
time, pushing initiation of this action as close to the source of the signal as possi-
ble. So your brain doesn’t decide, but is merely informed about what you did after

the fact.

What about the muscular end of things? This is where the usual “brain in charge”
picture seems least in question. The idea of our brain being in charge of our mus-

cles seems obvious, while the idea of our muscles being in charge of our brain

---

sounds, on the face of it, absurd. As everybody knows, brains are smart and mus-

cles are dumb; otherwise, “meathead” might be a synonym for “genius.”

Indeed, on their own, muscles are seemingly passive. That’s why, if you get a
nasty knock on the head, you will fall down. While you’re unconscious, your
muscles will go limp and do nothing. Your body will be like a marionette with its

strings cut.

Or will it? Despite its intuitive appeal, this view may be too one-sided. Consider
your heart, gut, and blood vessels—they’re muscles too. Luckily, they don’t stop
contracting when you're unconscious or asleep. The heart can continue to beat

rhythmically for quite a while, even when disconnected from the brain.

Indeed, the earliest motile life forms, dating back at least to the Ediacaran (635-
538.8 million years ago, just prior to the Cambrian), didn’t have centralized ner-
vous systems at all, but they certainly had muscular coordination. Muscles are
useful even for the simplest “sessile” animals—those anchored to rocks on the
seafloor—as they allow rhythmic pumping movements to filter seawater over
or through their bodies to sieve out nutrients. Jellyfish perform such rhythmic

pumping while free-floating, enabling them to swim.

Coordinated oscillation can occur at larger scales and among more complex
organisms, too. Giant swarms of certain firefly species, for example, can glow in
near-unison, creating an otherworldly Christmas light spectacle.“*4 Both the
synchrony of a firefly swarm and the speed with which they can get into sync
depend on the ability of the fireflies to see each other. They're able to coordinate
quickly—and stay coordinated—because they can see not only their immediate
neighbors, but also the glow of more distant fireflies, halfway across a clear-
ing. 224

Whether the oscillators are individual muscle cells or whole fireflies, coordi-
nation requires a flow of information, but it need not involve any centralized
control. We can think of what the individual units are doing as a minimal kind of
local prediction, or pattern completion. Each unit aligns the frequency and phase
(i.e., timing) of its oscillation with that of its neighbors. At the most basic level,

coordinated movement is what makes many entities into one.

---

“Phase synchronization” is the way the heart works too. Peristalsis—the coor-
dinated toothpaste tube-squeezing maneuver that moves food along the gut—
similarly relies on a traveling wave of contraction. Decentralized coordination
among muscle cells in organs like the heart and gut, and in animals like jellyfish
and Hydra, is partially achieved via “gap junctions”: channels that couple two
neighboring cells, causing electrical activity in one to propagate directly into
the other. However, fast and efficient synchronization of muscular contraction
requires longer-range connectivity. The decentralized nerve nets of jellyfish and
Hydra provide such long-distance connectivity, just as the visual systems of fire-

flies allow them to coordinate across that forest clearing.

In fact, some of the earliest neural nets appear not to be made of distinct neurons
at all. The “subepithelial nerve net” of the comb jelly, an ancient branch of animal
life dating back to the Ediacaran, consists of a fused or “syncytial” network of
nerve fibers, effectively serving as an undirected, organism-wide highway for

long-distance information transmission.“=* Perhaps these earliest neural nets

---

are best thought of as providing extended internal sensory systems for muscle

cells, allowing them to contract in synchrony with faraway neighbors.2“!

How and why, then, did organisms with diffuse neural nets evolve centralized
brains? A likely answer: sensing the external environment is helpful for muscle

cells too.

Food, of course, is an all-important environmental signal. And pretty much ev-
erything that is alive pulls away from noxious stimuli, just as our hands do from
a hot stove—in general, using a fast, local feedback circuit. Chemical receptors
—implementing chemosensing, or what we call “taste”—are in turn the oldest
and most ubiquitous environmental sensors, capable of detecting both yum and
yuck. Recall that even bacteria have such sensors, since in a watery medium and

at the smallest scales, floating molecules are the environment.

Now, consider the saliency of such receptors for an animal that can both propel
itself forward and turn via rhythmic muscular contraction—something worm-
like, for instance. While a coral polyp lives anchored to one spot and must make
the best of whatever washes over it, a crawling worm continually makes deci-
sions that will determine its future environment, hence its survival prospects. In

this respect, it resembles a swimming bacterium.

Unlike a bacterium, though, a worm is long and bilaterally symmetric, or
“bilaterian,” rather than tiny and cylindrically symmetric. As a result, it can

steer left or right, not just run or tumble—an innovation critical to life on land.
As philosopher and naturalist Peter Godfrey-Smith has pointed out, “In the sea,
animals have various body plans. On land, all animals are bilaterian. There are no
terrestrial jellyfish."“=2

Receptors at the front end of a bilaterian are especially important, because
they're the first to detect an encounter with anything tasty or aversive. That is,
unlike a coral, a bilaterian moves through the world in a particular direction, so it
has a leading end. And unlike the point-like bacterium, space and time are mean-
ingfully correlated; one could say the front end of a worm lives in its future, while

its rear end lives in its past. Muscles throughout the body will need to know about

---

the future, and the ones on the right and the left will want to behave differently

in order to turn away from noxious things and toward food.

Thus, a symbiotic partnership emerged between muscle cells and their non-
motile, spatially extended cousins, nerve cells. The usual way of thinking about
this partnership holds that the neurons took control of the muscle cells, but

I've argued that it may be equally valid to think of early neurons as information
conduits, or even as sensory outposts, to serve muscle cells. Initially, neurons
allowed improved long-range coordination across the body. But by wiring up
preferentially to the leading end of the animal, muscles could also respond to any

important changes in chemical concentrations up there.

Among bilaterians, those responses needed to be differentiated from the start,
not only by stimulus type, but also by stimulus and muscle location. A “yum” to
the right, or a “yuck” to the left, should cause the muscles on the right side, but
not the left, to contract. It’s not so easy for a diffuse neural net to convey such spa-

tially differentiated signals.

So, as muscles all over the body began to wire up selectively to the front end of the
animal, the resulting knot of spatially organized neurons resulted in “cephaliza-

tion”: the first glimmers of a brain in the head.

Neuromodulators

In addition to growing simple brains to support immediate perceptual input,
bilaterians immediately faced a need to modulate their behaviors on timescales
longer than the activations of individual neurons or muscles. Even chemotactic
bacteria need to compute a “batting average,” adding up, or integrating, what
they sense over a long period to decide whether the food level in the environment
is going up (in which case they should keep swimming), or down (in which case
they should tumble and change direction), Bilaterians needed to turn this inte-
grated chemical signal around the head into an internal chemical signal within

the body, so that the signal could be sensed by other neurons.

Early bilaterians did this via neuromodulators, chemical signals that accumulate

and reabsorb gradually, affecting entire populations of neurons at a time. In

---

terms familiar from chapter 2, we can think of these neuromodulators as hidden-
state variables (H) with long timescales—not permanent, but longer-lasting than

any momentary input (X), or action (0).

Dopamine and serotonin, neuromodulators that remain crucial to our brains
today, date back to these earliest bilaterian nervous systems.=!/ The “nearby
food sensors” in a worm’s head release dopamine, triggering feeding behavior,
which looks like nonstop turning to exploit the local environment—just like the
increased rate of tumbling that causes a bacterium to stick around and feed. We
can understand dopamine, then, as turning the “food-outside” signal into a time-
averaged internal signal. When high, it lets the worm’s muscles know that they
should keep turning the animal in place to continue eating whatever delicious

thing is in the immediate vicinity.

While dopamine has sometimes been interpreted as a “pleasure” signal, this isn’t
quite right. It's true that being in food will presumably make the animal happier
than not having any food, but, often, dopamine is better interpreted as a predic-

tive error signal, even in this very simple setting.

If you are a worm—or any living being—you need to predict the presence of food
in your future environment. So you'll be “happy” when you are swimming toward

food, meaning the food level at your leading end is rising.

The most apt feeling to associate with dopamine is probably anticipation. This
seems consistent with the subjective reports of human patients who, in a series
of ethically dubious experiments during the 1960s, were wired up to directly
stimulate dopamine production deep in their own brains. One patient, while
mashing the dopamine button, explained that “it was as if he were building up
to a sexual orgasm. He reported that he was unable to achieve the orgastic end
point, however, explaining that his frequent, sometimes frantic, pushing of the
button was an attempt to reach the end point. This futile effort was frustrating at

times and described by him on these occasions as a ‘nervous feeling.’""422)

---

On the other hand, when the dopamine-producing neurons of rats are destroyed,

the rats become passive and starve to death, even if food is “literally under their
noses.”4** If food is placed into their mouths, they eat it with evident pleasure,
but no matter how hungry they get, without dopamine, they aren’t spurred to

action.

Now, put yourself back in the worm’s place. If you realize your prediction of
future food is being violated by a decline in the ambient food near your head, you
will want to turn. The turn, even if random (as with a bacterial tumble), will re-
orient you toward a direction where the food level might once again go up—and
if that doesn’t work, just keep turning until it does. In an area of peak food, every
direction leads to a decline, so the animal will continue turning (or tumbling) in

place, which is, as it happens, the optimal food-exploitation strategy.

Serotonin neurons serve the converse function. They sense food in the animal's
throat rather than in the environment. As serotonin builds up over time, the

message becomes: “enough, I'm satiated.” The effect of dopamine will be quelled,

---

along with the impulse to move at all. Postprandial torpor will set in, the better to
digest.

Thus, we can crudely characterize dopamine and serotonin as the chemicals asso-
ciated with “wanting” (dopamine) and “getting” (serotonin). The word “crudely”
is important to emphasize here, though. Both serotonin and dopamine serve
complex and only partly understood functions in animals with big brains. =
Decreased dopamine levels, for instance, have not only been implicated in “not
wanting,” but also in lack of “vigor,” or drive to exert effort for a reward—which
isn't quite the same. Are hungry, dopamine-deprived rats not eating due to a lack

of desire, a lack of vigor, or both? These remain open questions.2=

In early bilaterians, though, dopamine and serotonin affected behavior more
straightforwardly, by providing smoothed averages, accessible to other neurons,
approximating food expected and food eaten. Neurons that were not in direct
contact with either the outside world or the throat could then modulate signals

sent to the muscles appropriately.

This developmental stage appears to be preserved in Acoela, an ancient order of
small marine worms that diverged from other animals more than 550 million
years ago. With simple body plans, Acoela have no gut and no circulatory or respi-
ratory systems. They move (either swimming or crawling between sand grains on
the sea bottom) by means of “cilia,” little hair-like projections covering their exte-

rior, whose movements are locally controlled.

In addition to a distributed nerve net, Acoela have a sort of “brain cap,” an aggre-
gation of neurons at the front end, coinciding with sensors, including a simple
eye.254) They can use complex repertoires of sensory-guided behavior to actively
hunt, modulated by dopamine and serotonin.'22" Yet the “brain” seems not to

be highly organized. If one of these worms is cut in half, then, like the neurally
decentralized Hydra, each half can regenerate into a whole animal. Signaling
molecules exchanged among the muscle cells appear to orchestrate the pattern-

ing and re-generation process, 32)

---

Bootstrapping

Animals with simple distributed nerve nets, like Hydra, show little evidence of
learning in any form that a behavioral experimentalist would recognize, though
every cell does continually regulate its own biophysics to ensure that it remains
responsive to whatever signals it receives—a form of local learning.=*") This is
consistent with the idea that these earliest nerve nets serve only secondarily for
sensing the environment, having first evolved to help muscles coordinate coher-

ent movement.

Rudimentary behavioral learning arises the moment anything like a brain ap-
pears, because, at this point, neurons in the head must begin jointly adapting to
changing conditions in the outside world. Every connection or potential connec-
tion between one neuron and another offers a parameter—a degree of coupling—
that can be modulated to suit the circumstances, even if the “wiring diagram” is

genetically preprogrammed or random.

To see why, let’s take the neuron’s point of view, and imagine that it is simply
trying to do the same thing any living thing does: predict and bring about its own
continued existence.“ Some aspects of this prediction will certainly have been
built in by evolution. For example, if dopamine is a proxy for food nearby, the
neuron will try to predict (and thereby bring about) the presence of dopamine,
because prolonged absence of dopamine implies that the whole animal will starve
—bringing an end to this one neuron, along with all of its cellular clones. Even a
humble cell has plenty of needs and wants beyond food, but without food, there

is no future.

Therefore, if the neuron is not itself dopamine-emitting, but its activity
somehow influences dopamine in the future, it will try to activate at times that
increase future dopamine. Aside from neuromodulators like dopamine, the
neuron’s inputs come either from other neurons or, if it’s a sensory neuron, from
an external source, such as light or taste. It can activate spontaneously, or in re-
sponse to any combination of these inputs, depending on its internal parameters

and degree of coupling with neighboring neurons. Presumably, at least one of its

---

goals thus becomes fiddling with its parameters such that, when the neuron fires,

future dopamine is maximized.

I've just described a basic reinforcement learning algorithm, where dopamine
is the reward signal. As brains became more complicated, though, they began
to build more sophisticated models of future reward, and, accordingly, in ver-
tebrates, dopamine appears to have been repurposed to power something ap-
proximating a more sophisticated reinforcement learning algorithm: “temporal

difference” or “TD” learning.

TD learning works by continually predicting expected reward and updating this
predictive model based on actual reward. The method was invented (or, arguably,
discovered) by Richard Sutton while he was still a grad student working toward
his PhD in psychology at UMass Amherst in the 1980s. Sutton aimed to turn
existing mathematical models of Pavlovian conditioning"! into a machine-
learning algorithm. The problem was, as he put it, that of “learning to predict, that
is, of using past experience with an incompletely known system to predict its fu-

ture behavior.”2@1

In standard reinforcement learning, such predictions are goal-directed. The
point is to reap a reward—like getting food or winning a board game. However,
the “credit assignment problem” makes this difficult: a long chain of actions and
observations might lead to the ultimate reward, but creating a direct association
between action and reward can only enable an agent to learn the last step in this

chain.

As Sutton put it, “whereas conventional prediction-learning methods assign
credit by means of the difference between predicted and actual outcomes, [TD
learning] methods assign credit by means of the difference between temporally
successive predictions.”“*4) By using the change in estimated future reward as a
learning signal, it becomes possible to say whether a given action is good (hence
should be reinforced) or bad (hence should be penalized) before the game is lost or

won, or the food is eaten.

This may sound circular, since if we already had an accurate model of the ex-

pected reward for every action, we wouldn’t need to learn anything further; why

---

not just take the action with the highest expected reward? As in many statistical
algorithms, though, by separating the problem into alternating steps based on
distinct models, it’s possible for these models to take turns improving each other,
an approach known as “bootstrapping”—after that old saying about the impossi-
bility of lifting oneself up by one’s own bootstraps. Here, though, it is possible.

In the TD learning context the two models are often described as the “actor” and
the “critic”; in modern implementations, the actor’s model is called a “policy
function” and the critic’s model, for estimating expected reward, is the “value
function.” These functions are usually implemented using neural nets. The critic
learns by comparing its predictions with actual rewards, which are obtained by
performing the moves dictated by the actor, while the actor improves by learning

how to perform moves that maximize expected reward according to the critic.

ATD learning system eventually figures out how to perform well, even if both the
actor and critic are initially entirely naive, making random decisions—provided
that the problem isn’t too hard, and that random moves occasionally produce a
reward. Hence an experiment in the 1990s applying TD learning to backgammon
worked beautifully,~** although applying the same method to complex games
failed, at least initially.

Beyond Reward

Around the same time, at the University of Fribourg’s Institute of Physiology,
Wolfram Schultz’s lab had been studying the relationship between motor func-
tion and Parkinson’s disease, which was known to compromise movement via
dopamine depletion.“* In a typical experiment, Schultz and colleagues would
record from single dopamine-releasing neurons in the brains of macaques while
they performed simple motor tasks, which they needed to learn via Pavlovian
conditioning.2*" A thirsty monkey, for instance, might need to learn which

of two levers to pull in response to a flashing light to get a sip of juice. The re-

searchers made the following observations:

1. Dopamine neurons normally spike at a moderate background rate.
2. When the monkeys first stumbled upon an action producing the sug-
ary drink, the spiking rate of these dopamine neurons rose.

---

3. Once the monkeys figured out the association between the visual cue
and the reward, extra dopamine was no longer released when the treat
came, but was released earlier, when the visual cue was presented.
This coincided with the monkeys licking their lips, akin to the saliva-
tion of Pavlov’s dogs.

4. If, following the visual cue, the treat was withheld, then activity of the
dopamine neurons subsequently decreased—that is, they went quiet
relative to their background rate.

Do dopamine neurons report an error
in the prediction of reward?

No prediction
Reward occurs

Reward predicted
Reward occurs

Reward predicted
No reward occurs

1) ,¢bar mee
ne one Sige g

ti

When Peter Dayan and Read Montague, then postdocs in Terry Sejnowski's lab
at the Salk Institute in San Diego, saw these results from Schultz's group, they
realized that dopamine was acting precisely like a temporal-difference learning
signal.!2°") This is the signal whereby the brain's “critic” tells the “actor”: please
reinforce whatever behavior you're doing now, because I predict it will leadtoa

future reward. Long sequences of actions that ultimately lead to a reward can be

---

learned this way, with the TD learning signal shifting earlier and earlier in the se-

quence as the learning progresses.

The repurposing of dopamine from a simple reward signal to something like

a temporal-difference reinforcement-learning signal might follow naturally
from the growth of brain structures both “upstream” and “downstream” of
the dopamine-releasing neurons. Remember that even among the earliest bi-
laterians, dopamine no longer represents food, but nearby food. In this sense,
dopamine is already a prediction of food, not a food reward in itself. Predicting

dopamine is thus a prediction of a prediction of food.

A predictive symbiosis between neural areas upstream and downstream of
dopamine will therefore result in the upstream areas being able to make higher-
order predictions (hence longer-range forecasts), thus acting as an increasingly
sophisticated critic or value function. Meanwhile, the downstream parts become
an increasingly sophisticated actor, or policy function, smart enough to learn

how to make better moves using these longer-range forecasts.

This may help to explain the approximate fit between the TD learning paradigm
and at least one major role played by dopamine in the brains of vertebrates.2**)
Like many primal feelings, “something good is within reach” is a simple, useful
signal that a worm can infer directly from smell, and a larger-brained animal
like us can infer through a much more complex cognitive process. That is a use-
ful signal for many parts of the brain, since they are all invested in producing
good outcomes for the organism as a whole; hence dopamine signaling has been
conserved for hundreds of millions of years, and its role has remained, if not the

same, at least recognizable throughout those eons.

Still, we should be careful not to interpret these experimental findings about
dopamine as proof that the brain implements TD learning as Sutton formulated.
That can’t be the whole story. For one, we have ample evidence that humans,

and likely many other animals, are even more powerful learners than the TD
algorithm is. Advanced board games we have no trouble playing, for instance, are
beyond the reach of TD learning. Additionally, as I hinted earlier, recent experi-
ments suggest that dopamine encodes information well beyond that of a TD error
signal.b®!

---

None of this should surprise us. Brain regions that symbiotically predict their
environment and each other are not restricted to implementing simple learning
algorithms, or communicating using cleanly definable mathematical variables,
any more than human emotional expression is limited to a single dimension or
natural language is restricted to logical grammar. Like every other approach to
machine learning described in this book, TD learning is an elegant conceptual
simplification that sheds light, but does not illuminate every corner. It is neither

a complete nor an exact representation of what the brain does.

In 2016, DeepMind’s AlphaGo model made headlines by achieving a major
milestone in AI history. This program, based on a more elaborate descendant of
TD learning (which we'll explore in chapter 5), defeated reigning Go champion
Lee Sedol in four out of five games.“ The news came amid reports of machine
learning besting humans at a rapidly lengthening list of tasks previously consid-

ered “safely” beyond Al's capabilities. 24!

epMing
This Move was feallyereative ancd-beautiful.

-

TF Gorcgte Cemcshtons
Despite this impressive showing, neurophilosopher Patricia Churchland pointed
out fundamental limitations in the AI paradigm at the time relative to what real
organisms with real brains do. In response to AlphaGo's victory, Churchland
wrote an essay entitled “Motivations and Drives are Computationally Messy,”2!

noting:

---

The success of [artificial neural nets like AlphaGo] notwithstanding |...
their] behavior is a far cry from what a rat or a human can do [...]. Main-
taining homeostasis often involves competing values and competing
opportunities, as well as trade-offs and priorities[...]: should I mate or hide
from a predator, should I eat or mate, should I fight or flee or hide, should
I back down in this fight or soldier on [...]. The underlying neural circuitry
for essentially all of these decisions is understood if at all, then only in the

barest outline. And they do involve some sense of “self” [...].

It’s true. A pure reinforcement-learning approach, no matter how fancy the
algorithm, cannot account for realistic animal behavior, because real animals—
including us—are not optimizing for any one thing (except, maybe, when we're
playing championship-level Go). However, “real AI” may be simpler than Church-

land—or any of us—imagined in 2016.

Close mathematical relationships exist among the various known machine-
learning methods,/2/! and ongoing theoretical work will likely unify them fur-
ther. While this remains an active research area, I believe that a unified theory of
learning will ultimately encompass evolution, brains, and, as special cases, estab-

lished ML methods. Such a unification would:

—

. Frame the central problem as active prediction of the future given the

past;

2. Not distinguish between learning and evaluation or inference, but
instead recognize that prediction must occur over all timescales;2!

3. Synthesize prediction with an extended theory of thermodynamics in
the spirit of dynamic stability, as sketched for bacteria in chapter 2;2!
and

4. Explain how mutual prediction between agents can lead to collective,

nonzero-sum outcomes.

A unified theory would illuminate the deep relationships between computing,
machine learning, neuroscience, evolution, and thermodynamics. Such a the-
ory is still incomplete, but this book offers a glimpse of what it may look like,
predicated on a hypothesis about what nature does at every scale, from cells (and

below) to societies: unsupervised sequence prediction.

---

Predicted sequences involve continued existence. If they did not, then the
organisms that made those (self-sabotaging) predictions wouldn't still be here.
Moreover, as we'll soon explore, when entities that can sense each other begin to
mutually predict each other, it becomes easy for them to enter into a symbiotic
partnership in which their joint future existence is more secure than their indi-

vidual existences.

Let’s call this view “dynamically stable symbiotic prediction.” What would it
imply about the brain? Unlike TD learning or any form of pure reinforcement
learning, symbiotic prediction does not imply that animals optimize any single
reward, whether food or dopamine. On the contrary, such single-mindedness
would not be conducive to either mutualism or survival in the real world, hence
it would not be dynamically stable. Per Churchland, “Maintaining homeostasis
often involves competing values and competing opportunities, as well as trade-
offs and priorities.” This is even truer in social settings. There are many ways to
be alive in this world, but all of them must involve continuing to exist in the fu-

ture, and existence requires ongoing relationships.

Let’s pull these threads together and summarize: as evolution built on the design
of simple Acoela-like bilaterians, additional neurons appeared in heads. This hap-
pened because neurons are themselves replicators, and, like all replicators, they
will colonize any favorable niche,“ in particular when that neural proliferation
symbiotically helps the whole organism. Once this brain-knot began to grow,
more complex neural networks developed, capable of handling more sophisti-
cated sensory modalities, like hearing and camera-style vision. With help from
neuromodulatory signals like dopamine, such brains were also able to predict
increasingly subtle patterns relevant to the whole organism over ever-longer

timescales.

Thus animals acquired the computational power to develop behaviorally relevant
models of other complex animals, resulting in the kinds of early “social intelli-

gence explosions” evident in the Cambrian period.

---

# Chapter 5

5. Other Minds

Forking Paths

We're finally ready to begin tackling the big questions posed in the introduc-
tion: the nature of general intelligence, the “hard problem” of consciousness, and

the thorny issue of free will.

Let’s begin with free will, picking up where chapter 3 left off, with Nvidia's
DAVE-2 self-driving car. Our goal will be to understand what we mean when we
call a model's actions “willed.” Recall that DAVE-2 was nothing but a convolu-
tional neural net whose input was a front-facing camera and whose output was
a steering-wheel position. It was the purest and simplest approach to cybernetic

self-driving. But is it capable of choice?

More concretely, what happens when such a “reflex-based” car arrives at a T-
junction? A generic, pretrained model operating without any larger context can’t
react sensibly. When we’re driving, these are the moments when we might make
decisions based on higher-order goals. At other times, we're on “autopilot” our-
selves: the goal is merely to stay in our lane, follow the rules of the road, and avoid
collisions with other vehicles, pedestrians, or animals. If we’ve established habit-
ual routes, say to and from work, we might also make a lot of turns on autopilot.
Those are instances when our inner “autopilot model” is not generic, but specific

to our own lived experience.

DAVE-2, however, is only trained to perform the generic autopilot task. To gather
the dataset, human drivers navigated a wide variety of routes on many different
roads, and excluded from the training data the brief intervals when they were
changing lanes or making turns. During live road tests, the human driver inter-

vened to perform these maneuvers manually.

What would the car do if kept on autopilot at a T-junction? Presumably, it would
choose the straightest way. At an exactly symmetric T-junction, one would hope
that the model itself is just a tad asymmetric, causing it to break the tie somehow.

A perfectly symmetrical model would be unable to break the tie, hence would be

---

forced to generate the only non-tiebreaking output: steering straight ahead and

running off the road. (Remember, DAVE-2 doesn't control the gas or brakes.)

This unfortunate situation illustrates the old saying about the perfect being the
enemy of the good. It also recalls “Buridan’s ass,” often framed as a philosophical
paradox in discussions of free will. In the parable, the ass (or donkey, though the
other definition applies too) is midway between two equally sized piles of hay,

and, being unable to decide which to eat, starves to death.2/J

Avoiding this “metastable” situation is easy enough. All it requires is a random

variable, a bit of noise in the system, to break any near-ties.

In real life, though, Buridan’s ass only rears its poor muddled head infrequently,
because few decisions we make are truly arbitrary, fully symmetric, or context-
less. We don't need to make random turns at T-junctions since, when we're driv-
ing, we're usually trying to get somewhere. More broadly, questions about choice,
decisions, and free will only make sense when we consider an agent with its

own history, acting in time and in context. That's why we don’t generally count

generic reflex actions as willed.

DeepMind’s AlphaGo contest with Lee Sedol took place in 2016, the same year
Nvidia’s DAVE-2 self-driving-car paper was published. Go is exceedingly complex,
with many more possible moves at any point in the game than chess—a vast

and intricate garden of forking paths. For this reason, it had resisted the brute-
force search or heuristic approaches that had produced grandmaster-level chess
programs many years earlier, as well as naive temporal difference reinforcement

learning.

At bottom, DeepMind’s trick was the same as Nvidia's: replacing hand-written
code with a learned convolutional neural net. AlphaGo's system design was con-
siderably more complex, though, not only involving separate policy and value
networks trained through reinforcement, but also incorporating traditional
methods, like a randomized or “Monte Carlo” tree search through possible fu-
ture moves.!*/4/ In this sense, it was a hybrid between deep learning and GOFAI,
though subsequent models—AlphaZero,2™) MuZero2="_moved progressively

toward a purer deep-learning approach, removing the remaining handcrafted

---

heuristics while further improving performance. MuZero is general enough to

play any game, not just Go.

DeepMind has always aimed to solve artificial general intelligence through an
agential approach. Gameplay runs deep in the organization’s culture. Its founder,
Demis Hassabis, was a chess prodigy and an expert at many other games. (In
2024, he won the Nobel Prize, along with John Jumper and University of Wash-
ington researcher David Baker, for AlphaFold, which applies deep learning to
solving the longstanding problem of predicting a protein's structure from its
amino-acid sequence.) Prior to DeepMind, Hassabis designed video games, and
even founded his own gaming company. DeepMind’s first highly visible success,
in 2013, involved combining reinforcement learning with convolutional neural

nets to play Atari games.2241

The company’s bet that gaming could provide a controlled arena for developing
general Al has certainly yielded impressive and important advances. Go com-
mentators studying AlphaGo’s games lauded the system for “exhibiting creative
and brilliant skills and contributing to the game's progress."284)

However, beyond the limitation Churchland pointed out**2/—its single-minded-
ness—AlphaGo was very different from the brain in another important way: it

did not exist in time. It had no dynamics or internal state.

Children of Time

Like the self-driving-car model, neither AlphaGo nor its successors maintain
any explicit memory of its prior “thoughts” or plans.22*! True, the system works
out its next move by thinking as many steps ahead as possible, making it a stretch
to call that extended evaluation a “reflex action.” However, once the move is

made, it’s groundhog day—the next turn, it considers the board afresh.

AlphaGo makes no attempt to model its opponent's psychology, nor does it learn
on the fly; thus, it can’t individuate. Neither can it have any sense of a “self” act-
ing in the world. All it models is that world itself and the possible paths through
it, annotated (courtesy of the value network) with each path’s goodness or

badness.

---

For a board game like Go or chess, none of these design choices are necessarily
shortcomings. According to game theory (as formalized by none other than John
von Neumann,22! who had his fingers in many pies), the optimal next move de-
pends neither on history, nor on the opponent, nor on any internal state, but only
on the state of the board and the rules of the game—to which both players have
full access. And the opponent should be presumed to always play optimally. To do
otherwise would risk falling prey to a wily antagonist, who might lull an oppo-
nent by playing dumb, then take the gloves off at an opportune moment.224

You may wonder how AlphaGo could pull off a complex, multi-turn strategy—
which it certainly can—without a self or memory. But given a clear view of the
future's forking paths at every turn, there’s no need to remember. All possible
strategies are visible at all times, including the continuation of whatever strategy
seemed best on the previous turn. If it’s still the best option after the opponent's

move, then so be it.

While elegant in its way, this approach can be wasteful, in that it often involves
rediscovering the same strategy, turn after turn. Occasionally, catastrophic (and

quite nonhuman) failures occur, since the model's view of the future is not per-

---

fect, but, as with all Monte Carlo methods, stochastic. The model might make an
unusual move due to glimpsing a brilliant but distant outcome down the line, but
later fail to spot that same opportunity, even if it’s still in play, and foreclose on it

with a wrong move. Out of sight, out of mind.“*2

Portia spiders offer an illuminating contrast to this kind of “statelessness.” Al-
though only a centimeter or less in size, they have been called “eight-legged cats”
due to their unusually intelligent hunting behaviors.**! They're odd-looking,
with a slow, choppy, robot-like gait—until they pounce. Unlike other spiders, Por-
tia have a pair of large, forward-looking camera-type eyes with high resolution
over a narrow field of view, well adapted to nuanced visual discrimination. Their
favorite meal is other spiders, typically web-weavers, which may be twice their
size. Portia can control the behavior of prey by spoofing web vibration signals;
they learn which signals generate the desired response for each species through
trial and error. In the lab, they can even learn how to fake out species they would

never encounter in the wild.

They plan their attacks slowly and carefully. With tiny brains and telephoto eyes

that need to scan around to resolve the environment, it seems likely that they sac-

rifice much of the parallelism of animals with bigger brains (a topic we’ll return

---

to in chapter 8). Once they have worked out a strategy, though, they can execute
it virtuosically, leaping from twig to twig, abseiling down silk threads, and land-
ing on their target from above, behind, or frontally, depending on what is safest
under the circumstances (for oftentimes, the spider or insect they’re stalking is
perfectly capable of eating them if the tables turn). Perhaps most impressively,
Portia routinely reach their prey via indirect routes, including detours of up to
an hour during which they may move away from their goal, breaking line of

sight.2*2! Impressive stuff!

Principal eye (from above) Pon
Comeal lens Bye tube Second Jens 1.000 Cae s
a te
3 LoOD ai ttt) we
5 a Se e*
i 100 eu o* ov
| ‘iain seer eeweeee ue oo wieeeeeenes
”
ODI.
cs
Prod
we @
000i ering er reny Serry ering —errsiem
0.10 Loo 10.00 100.00 1000.00 10000.00
Body height (mm)

I've offered this detailed account because it illustrates—and builds on—a number

of Churchland’s observations:

© Portia isn’t playing any one game against any single opponent. Eventually it
must eat if it is to survive, but it gets to choose with whom to engage, and
when; it can always back off and try something else, or “soldier on.”

@ The “game board” is not equally visible to all players. In its totality, it isn’t
visible to any player. Portia must build up and incrementally update a men-
tal model of the world in order to make decisions.

® This model must include not only the externally visible world, but the inter-
nal states of hunter and prey alike. Knowing its own state allows Portia to
assess how hungry (or desperate) it is, how strong or weak it feels, whether
hunting should take precedence over mating or resting, and so on.

® Modeling the mental state of its prey is also essential. Are they aroused?
Have they realized I’m stalking them? If so, how well have I been localized?

By timing its movement on a victim's web to coincide with wind gusts,

---

Portia may work to remain “vibrationally invisible”; or, by strumming the
web, it may attempt to create the illusion of a trapped bug. The trickster
must constantly assess: are my tricks working? Is this getting the reaction I

want?

None of these tricks or capabilities are fundamentally out of reach for artificial
neural nets; after all, each capability can be expressed in terms of functions, and
neural nets are universal function approximators. Such capabilities will not,
however, emerge on their own in a system like DAVE-2 or AlphaGo, due both to
the constraints of the setup (autopilot or board game) and the structural limita-
tions of a stateless classifier—even one that makes very clever decisions in the

moment by evaluating many possible futures.

Sphexish

Given Portia’s alien lifestyle, physiology, umwelt, and brain limitations, it takes a
leap of imagination to understand what it's like to be a jumping spider, though it
is fun (and maybe fruitful) to make the attempt.22"! My own sense is that Portia,
cats, and humans on the hunt all share not only the ability to assess and plan an
attack (or defend against one), but also to experience doubt, uncertainty, fear,
and triumph. I expect that such feelings and experiences would emerge naturally
from the evolution of predation, as described in chapter 3, just as hunger emerges

naturally from the need to eat, as described in chapter 2.

But it seems so subjective to assert that another mind is experiencing something
familiar from one’s own experience. How can one really know? We will soon ex-

plore how such claims can be assessed more rigorously, as predictive hypotheses.

For now, though, let's stick to a more ethological perspective. Ethology concerns
itself with animal behavior, studied using lab experiments and analyzed in the
context of neurophysiology, function, and evolution. Through the ethological
lens, we can simply ask the same questions about feelings and internal states we
would ask about physical features, like the differently adapted beaks of Darwin's
finches. Why would that feeling arise and be preserved by evolution? How is it
useful? What would happen if it were absent? This lets us fend off charges of an-

thropocentrism and defer “philosophical zombie” questions a little longer.

---

Free will, as a desire or imperative, seems easy enough to understand from an
ethological perspective. No animal likes being trapped, humans included; that's
why imprisonment is a form of punishment, even if our bodily needs are met.
Remember, the whole point of having a brain is to be able to act in the world,
choosing among alternative futures in order to enhance our dynamic stability—

that is, to stay alive, and to continue to be able to make choices in the future.

When others restrict our ability to make choices, it doesn’t feel good, just as
gnawing hunger doesn't feel good. The confinement of our possible futures ren-
ders us increasingly helpless, like a king being chased into a corner of the chess

board in the endgame.

Go offers an even purer expression of this idea. Although the stones don’t actually
move once laid down, their “liberties” are the number of adjacent unfilled board
positions where they “could” hypothetically move, and stones only remain “alive”
as long as they have at least one liberty. Death, then, whether in a game or in real
life, represents the ultimate exhaustion of one’s ability to choose. It's the pinched-

off end of our Wiener sausage.424!

Mutual prediction is the key to sociality and cooperation, but, in a predatory con-
text, as the early cyberneticists understood, prediction can also be adversarial. A
predator will try to predict prey right into its stomach. Prey will try to predict the
predator's moves, and escape. Each is trying to preserve its own liberties, poten-
tially at the cost of the opponent's. Each will therefore try to predict the other’s

predictions, ad infinitum.

As we'll discuss in more detail in chapter 7, when mutual prediction is cooper-
ative, it must also be imperfect, for cognitive cooperation involves a division of
labor. That means each party brings cognitive resources or inputs to the table
that the others lack. If one of the cooperating parties is always perfectly pre-
dictable to any of the others, that would imply that the predicted party doesn’t
bring anything unique to the table, and is therefore a third wheel.

So, whether in a cooperative or adversarial context, being perfectly predictable
is bad news. In a way, it’s even a form of imprisonment. Ted Chiang mordantly

explores the psychological consequences in his short story “What's Expected

---

of Us.”/224! A device called the Predictor, consisting of nothing but a button and

a light, appears on the market. The light always flashes green one second before
the button is pressed. Millions of Predictors are sold, and, at first, people treat the
device as a novelty, showing it to their friends and trying to fool it. When the
implications sink in, though—that the Predictor can’t be fooled—free will is re-

vealed to be an illusion, and people despair, eventually losing their will to live.

Real-life predictors aren’t single-button devices, of course, but other minds, like
that of a cat pursuing its prey. And one way to become highly predictable is to run
out of voluntary moves, like a cornered rat. But if one’s behavior looks determin-
istic from the outside—if it can be perfectly predicted by an observer—then, from

an adversarial perspective, that is equivalent to being cornered.

When an agent becomes perfectly predictable to an observer, it makes the agent
no longer register as agential to that observer. Cognitive scientist Douglas Hofs-
tadter has described this property as “sphexishness,” by reference to the golden
digger wasp Sphex ichneumoneus.“>+! Hofstadter was drawing on observations

by French entomologist Jean-Henri Fabre (1823-1915), who has been hailed as
the founding father of ethology.“2 Although generally a keen and sympathetic
observer of animal behavior, Fabre took a dim view of cognition in insects, claim-

ing they exhibit a “machine-like obstinacy.”“"*!

---

He noticed that when the time comes for Sphex to lay eggs, she constructs a bur-

row and seeks out a cricket to nourish her future hatchlings. Instead of eating the
cricket herself, she paralyzes it with a sting, brings it to the burrow entrance, goes
in to see that all is well, then drags the cricket in, lays the eggs alongside the body,
seals the burrow, and flies off. This elaborate performance certainly looks purpo-

sive—and it is.

But then, Fabre noticed that if the cricket is moved by a few inches after the wasp
has gone into the burrow to check that all is well, Sphex will re-emerge and move
the cricket back into position, then go back into the burrow to check that all is
well again! He described repeating this process dozens of times. By moving the
paralyzed cricket every time the wasp went into the nest, Fabre was able to get

her stuck in an endless loop."

One interpretation of this little parable: it’s easy to be fooled into thinking that a
behavior is intelligent or agential when in fact it’s just a running program. That
would beg the question, though: what else could it be? In some sense we are all

“Just running programs.”

A better take is to recognize, first, that Sphex’s nest preparation behavior is

genetically determined, hence the intelligence manifested by the program isa

---

product of evolution, not of in-the-moment reasoning by the individual wasp.
The individual wasp appears to be, like DAVE-2, running on autopilot, at least
with respect to nesting behavior. This seems reasonable, given the wasp’s small
brain and two-month adult lifespan. It has no time to learn the ropes, and nobody
to learn them from, so it has to know how to reproduce and care for its young

“right out of the box.”

Perhaps more interesting, though, is our own response to observing sphexish
behavior. When we see the elaborate preparations the wasp makes for her brood,
we think she’s smart and agential. Then, when we see that the behavior is pre-
scripted, we “realize” that she's just a machine, an “it,” and any impression of
intelligence or willed action vanishes. But the difference is in our own minds, not

that of the wasp.

Alan Turing arrived at a similar conclusion: “From the outside, [...] a thing could
look intelligent as long as one had not yet found out all its rules of behavior. Ac-
cordingly, for a machine to seem intelligent, at least some details of its internal

workings must remain unknown.”222

In the case of Sphex, this realization comes about due to our reverse-engineering
of the script and “hacking” it to create an infinite loop. We come to believe the
wasp has no intelligence or agency precisely because we can now predict its ac-
tions perfectly. What we really mean by “it’s just following a script” is that we, on
the outside, know what the script is, and don’t even need to interact with the ani-

mal to predict what it will do next.

As a fellow computational being, how can you escape the same pickle—how do

you keep from becoming a robotic “it” to a clever observer? Here are three ways:

1. As described for moth flight in chapter 3, simply using a random vari-
able can keep your behavior fresh and surprising even if you're not so
smart. In an adversarial setting, this strategy still works if your oppo-
nent is smart enough to see right through you (that is, if your internal
state is transparent, or can be fully modeled by an outside observer).
It even works if you are entirely generic and incapable of individual

learning, meaning that your behavioral repertoire is fully genetically

---

programmed, and you are “just like” every other member of your
species./22*! Randomness is equally valuable in cooperative contexts,
such as for foraging insect colonies, where it ensures that even near-
identical individuals will diverge to explore different parts of their

environment.

nN

. The ability to learn allows your responses to be more unique, and
allows your behavioral repertoire to scale up far beyond what can
be encoded in your genome. By storing in your brain learnings and
behaviors based on past experiences, you become vastly more complex
on the inside—and all of this complexity is a hidden state, invisible to
a stranger. In a competitive setting, such lifelong learning makes you
harder to predict. In a cooperative setting, it allows individually differ-
entiated skills and expertise to develop, greatly expanding the oppor-
tunities for cognitive division of labor.
3. If you are able to model others effectively, including others who are
modeling you back, then in an adversarial situation, you can outfox
them by going meta. Modeling others is also essential to the cognitive
division of labor, as it allows you to know who knows what you don't
know. Psychological studies suggest that we humans are so adept at
keeping track of socially distributed knowledge that we tend to har-
bor greatly exaggerated beliefs about how much we personally know,
when a good deal of our “knowledge” really consists of knowing whom
to ask.222)

Wasps might not bother with any of these strategies when it comes to nest
preparation because cricket-moving tricksters have never exerted evolutionary
pressure on making this specific behavior unpredictable. Predator/prey inter-
actions are a different story. It’s unlikely that Sphex would behave so sphexishly

while hunting the cricket it brings to its nest, or evading a predator of its own.

The last trick on the list—modeling your modeler—requires being very smart
indeed. Roughly speaking, you need to be as smart as whomever you're modeling,
or more so, and you need to be able to imagine how you (and the world in general)

appear from their point of view.

---

Does the small brain size of an arthropod preclude this trick? Apparently not.
When Portia spiders show an awareness of what their adversary does and doesn't
know, and learn to actively manipulate that opponent’s world model, they are op-

erating at this higher cognitive level.

Matryoshka Dolls

Among human children, this so-called “theory of mind” or ability to “mental-
ize” (I'll use the terms interchangeably) takes quite a while to develop fully. The
classic experimental setup for probing it is the Sally-Anne Test, popularized in

1985 by psychologists Simon Baron-Cohen, Alan Leslie, and Uta Frith.“

The experimenters put on a little chamber drama for their young subjects using
two dolls, Sally and Anne. Sally has a covered basket, and Anne has a box witha
lid, Sally puts her marble in her basket, then goes out for a walk. While she's gone,

Anne slips the marble out of Sally’s basket and into her own box, closing the lid.

Later, with Anne out of the picture, Sally returns.

During the skit, the children are asked four questions:

1. The Naming Question, a warm-up, asks them which doll is which; it

establishes basic understanding of the scenario.

---

2. On Sally’s return, the Belief Question is: “Where will Sally look for her
marble?”

3. This is followed up with the Reality Question: “Where is the marble
really?”

4. ... andthe Memory Question: “Where was the marble in the begin-
ning?”

Even babies (by the time they can talk a little) are able to say who is who and
understand where the marble is throughout the skit, although it’s stashed out of
sight; hence questions 1, 3, and 4 are all fairly easy. However, until somewhere
between two anda half and four years of age, children tend to get the Belief
Question wrong.““"! They probably aren’t able to model the minds of others well

enough to knowingly attribute false beliefs to them.

Psychologists tend to be very particular about which kinds of agents they believe
could, even hypothetically, exhibit theory of mind, in part because of the baggage
implied by language like “knowingly attribute.” Many reserve the term for hu-
mans only, though other great apes have also been shown to pass the Sally-Anne
Test, with suitable modifications.“°! However, from a functional perspective,
theory of mind is exactly what is required to lie or deceive, as Portia does (and as

many other animals do),!*22)

Exhibiting this cognitive capacity implies not only an ability to simulate other
minds, but also to model counterfactual (“what if”) universes. In the Sally-

Anne Test, there is a real-life universe, in which the marble is in the box. There

is the universe in Sally’s head, in which the marble is in the basket. Each of these
universes also contains agents, like Sally and Anne, who in turn contain model
universes in their virtual heads. The Anne in the universe in Sally’s mind, for in-
stance, also believes that the marble is in the basket. Of course Sally and Anne are
mere dolls; they only exist within the minds of the experimenter and the subject.
The experimenter and subject are in turn abstract people I am describing to you,
dear reader. Nesting dolls, universes within universes, in an endless recursion. It’s

a dizzying prospect.

As adults, though, we negotiate such recursive mentalization all the time

without a second thought. Reading a novel like Jane Eyre involves regularly en-

---

tertaining fourth-, fifth-, and sixth-order theories of mind, as we wonder what
Charlotte Bronté expects us to believe about what Jane believes Mr. Rochester
must think Jane thinks about Mr. Rochester's feelings about Blanche. Exercising
this mentalizing faculty seems to have been the main pastime of the nineteenth-
century English upper classes. (Writing popular novels about it added yet an-
other layer of indirection, at times ironic.)

But theory of mind is far more than just a valuable skill for navigating hidden
barbs and avoiding faux pas at teatime. There is good evidence that it is the very

stuff of intelligence; it is, thus, at the heart of this book’s main argument.
We have arrived at that heart. My contention is that theory of mind:

®@ Powers the “intelligence explosions” observed in our own lineage, the ho-
minins, and in other brainy species;

@ Gives us the ability to entertain counterfactual “what-ifs”;

® Motivates, and is enhanced by, the development of language;

@ Allows us to make purposive decisions beyond “autopilot mode”;

@ Underwrites free will;

@ Operates both in social networks and within individual brains;

@ Results automatically from symbioses among predictors; and

@ Is the origin and mechanism of consciousness.

In a sense, theory of mind is mind.

Intelligence Explosion
These are big claims. Let’s begin with the more established ones.

In the 1970s, Dian Fossey, the world’s leading expert on gorilla behavior, invited
British neuropsychologist Nicholas Humphrey to spend a few months at her re-
search station in the Virunga Mountains of Rwanda. Reflecting later on what he
had seen, Humphrey wrote, “[O}f all the animals in the forest the gorillas seemed
to lead much the simplest existence—food abundant and easy to harvest (pro-
vided they knew where to find it), few if any predators (provided they knew how
to avoid them) ... little to do in fact (and little done) but eat, sleep and play. And

the same is arguably true for natural man.”“4°)

---

These observations flew in the face of the usual explanation for evolving high

intelligence—that it's all about being a brilliant hunter, or otherwise “winning”
at playing a brutal, Hobbesian game of survival in a tough environment. But if
not to hunt (or evade hunters), why bother with intelligence? Couldn't one live
the easy life of a gorilla without incurring the high cost of a big brain? The fossil
record suggests not: primate brains in many lineages, including those of gorillas

and humans, haven't shrunk over time, but, rather, have grown dramatically.

Humphrey’s explanation: “[T]he life of the great apes and man [...] depend{[s]
critically on the possession of wide factual knowledge of practical technique and
the nature of the habitat. Such knowledge can only be acquired in the context of
a social community [...] which provides both a medium for the cultural transmis-
sion of information and a protective environment in which individual learning

Tel
05

can occur. [...][T]he chief role of creative intellect is to hold society together.”—

There are now many variations on this basic theory—some, like Humphrey,
emphasizing cooperation and division of labor, others competition and Machi-
avellian politics.“°° These correspond fairly well to the “love” versus “war” expla-

nations for the emergence of intelligence generally, as described in chapter 3.

---

In the 1990s, evolutionary psychologist Robin Dunbar and colleagues used com-
parative brain-size measurements across species to advance the closely related
“social brain hypothesis,” which holds that the rapid increases in brain size evi-
dent in hominins and cetaceans (whales and dolphins), among others, arise from

mentalizing one-upmanship.422)

~.
CS Homo sapiens
pic, Neandertalensis
x S

KS) Homo erectus

1000 ce
Homo habilis
~| Australopithecus
Anthropoia Yricanus 500 ce

ape
Millions of years ayo -4 3 2-10

Underpinning all of these related hypotheses is the observation that, among
highly social animals like us, theory of mind is a powerfully adaptive trait. Being
better able to get inside others’ heads increases the odds of finding a mate, build-
ing coalitions, securing resources from friends and family, getting help raising
young,“"! avoiding violence (or being on the winning side of it), climbing in
prestige, and amassing fans or followers. So, unsurprisingly, people with better
theory of mind tend to live longer and have greater reproductive success.“ That

means Darwinian selection will be at work.

Strong theory of mind is correlated with both larger numbers of friends and
larger brains, particularly in brain areas associated with mentalizing—above all,
the frontal cortex.“"! Thus, startlingly, we can see evidence of the evolutionary

pressure on social intelligence even among modern humans.

---

My guess is that the extra cortical volume of highly social people is dedicated

not only to general mentalizing skills, but also to rich learned representations
—we could even call them simulations—of their many specific family members,
friends, colleagues, and acquaintances.“ After all, mentalizing requires not just
imagining another person in the abstract, but modeling their particular life ex-
perience, what they know and don't know, their quirks and values, the ways they
express themselves—in short, everything that comprises a personality, outlook,
and umwelt. You probably bring such knowledge to bear effortlessly to play out
hypothetical social situations in your head, drawing on a cast of hundreds of peo-

ple you know.

This task is even harder than it appears at first glance, because there are infinite
reflections in the social hall of mirrors: all of those people are themselves model-
ing others, including you. And, of course, their models of you include models of
them, and of others. These relationships are important, because they powerfully
affect behavior. Who shared their meat with whom after the last hunt, and in
front of whom? Who is sleeping with whom? Who is gossiping about it, and who

doesn’t know? Who is beefing with whom, and over what (or whom)?

Even if your model of second-order relationships (i.e., who is friends with whom,
and what you know about those interactions) is not as rich as your model of
first-order relationships (your friends), the sheer number of higher-order terms
in your model explodes. If you have twenty classmates who all know each other
(and you), then you need to keep track not only of your twenty relationships with
them, but of all of their relationships with each other and with you, which is an-
other 20x 20=400 pieces of information. Third-order relationships climb into the

thousands.

The numbers get truly mind-boggling when you consider that our acquaintances
can easily number in the hundreds; family, school, and work environments tend
to involve cohorts of people who all know each other; and our theories of mind
can go up to sixth order, or beyond.\*!4! You can imagine, then, that even if many
corners are cut, the amount of brain volume needed to do social modeling might
grow both as a function of your number of friends and as a function of your abil-

ity to model higher-order relationships.

---

Indeed, when Dunbar and colleagues set out to find the relationship between
the brain sizes and the social-group sizes of brainy animals, they found that

as troop size increases, the amount of brain volume dedicated to the cortex

also increases“4) Mentalizing order, which Dunbar refers to as “intentionality
level,” appears to be limited by cortical volume; behavioral studies suggest that
monkeys can only operate at level one, while nonhuman apes have level-two in-
tentionality. By extrapolation, archaic humans and Neanderthals may only have
been able to achieve level-four intentionality, which is at “the lower end of the
normal distribution for modern human adults, and at about the same intellec-
tual level as young teenagers.”“!“! Finally, the slope of the relationship between
cortical volume and troop size is considerably steeper for apes than for monkeys,
consistent with the idea that modeling higher levels of intentionality requires a

greater investment of cognitive resources per troop member.

As brain size increases, so
does group size. Human group
size as predicted by Dunbar's
model comes out to about 150.

1,000

Poveverrererer ey prrerererererrcrirererirterrrircrircrirritiricy far) | Humans
100

Monkeys @
e 8

Average social group size
—
So

1x 2x 3x 4x Sx 6x

Size of neocortex relative to rest of brain

Findings relating brain size to social group size, and social group size to Dar-
winian fitness, are themselves a hall of mirrors, revealing a profound self-similar-
ity—and feedback loop—between brains and social groups. If you have a slightly

larger brain than your friends and family, and are able to model more relation-

---

ships more reliably, you will have a Darwinian advantage, so on average will have
slightly more descendants than those who are less socially adept. But that means
that your descendants will themselves become harder to model socially; that is,

everyone else’s model of them must now be more complex, including higher-level
intentionality and more relationships. And remember, everybody is trying to pre-

dict everybody else, but not be fully predictable themselves!

So it’s an arms race, not unlike that of the Cambrian explosion—though (usually)
friendlier. Everyone is getting a bigger brain to model everyone else, and every-
one else is getting harder to model at the same time, because ... well, their brains
are getting bigger. A social intelligence explosion ensues: a rapid (by evolutionary

standards) increase in brain volume in your species.

When social modeling becomes such an important component of everyone's life,
the effect on individual incentives is dramatic. Lone operators, like leopards, are
content to fend for themselves; their umwelt consists mainly of their territory
and their prey, while other leopards are, most of the time, unwelcome intruders.
For a modern human, though, being cast out or excluded from the community
becomes a severe punishment—or even a death sentence. Our world consists
largely of other people, and most of us would be unable to survive at all without

continual mutual aid.

At the same time, sociality is a fraught business. We try to “win” at modeling oth-
ers without being fully modeled ourselves; we compete for mating opportunities
and for attention; we strive for dominance and prestige. These dynamics once

again illustrate how competition and cooperation can be interwoven to such a de-

gree that it can be hard to tell which is which.

Selection pressure also operates at the level of social groups. If one group sports
slightly bigger brains and greater social prowess, the group itself can grow larger,
and will thus tend to outcompete the smaller (and smaller-brained) group. Such

may have been the fate of certain of our now-extinct hominin kin.

Societies have a kind of collective intelligence, and a rich body of workin social
anthropology tells us that collective intelligence exhibits a scaling law not unlike
that of individual brains. Theory of mind, incidentally, is important both for

---

effective teaching and effective learning, which implies that it enhances cultural
evolution at the group level too." So, bigger societies can create and evolve
more complex technologies, and thereby develop greater adaptability and re-
silience.“““ Greater scale, in other words, can support greater intelligence, and
greater intelligence improves dynamic stability, both at the individual level and
at the group level.

Crew of Eight

It’s hard not to wonder whether this recursive pattern applies at finer scales, too.
Could our brains be “societies” of neural circuits that have evolved to model each
other and thereby create the larger collective intelligence we call a “brain”? Neu-
roscientists and AI researchers have advanced such theories many times over the

years, offering a range of supporting evidence.14J

For one, the cerebral cortex has a modular or repetitive structure, consisting of

a honeycomb of “cortical columns”—though these columns don't have distinct
borders, which has led to endless debate about their exact definition and granu-
larity.“44! Therefore, when I use the term “cortical column,” please take it with a
grain of salt; I will interchangeably use even vaguer language like “small piece of

cortex” or “part of the brain.”

Despite these ambiguities, we know that the basic “cortical circuit” is much the
same in different regions of the cortex. When we distinguish between “auditory
cortex” and “visual cortex,” for instance, the difference seems to be mostly about
where each gets its inputs.“+2! In one famous experiment, the optic nerves of
baby ferrets were rerouted surgically to their auditory cortex, and these animals
nonetheless developed the ability to see. Moreover, the characteristically pat-
terned neural mapping of oriented visual features Hubel and Wiesel discovered
in the visual cortex developed in the ferrets’ repurposed “auditory” cortex, albeit
more sloppily.“22) There’s evidence that the human brain can rewire in simi-
larly dramatic ways: blind people can learn to see using their hearing via “click
sonar,”|*24 and can even acquire a limited form of vision via spatially patterned

tongue stimulation.““4!

---

Perhaps generic modularity is precisely what made the intelligence explosion
possible: just as DNA could easily evolve to replicate more vertebrae and ribs to
produce snakes (per chapter 1), the genomes of animals undergoing intelligence
explosions could respond to individual and group selection pressure by replicat-
ing more cortical columns. Thus, evolution could progressively expand the corti-
cal sheet without needing to invent anything fundamentally new. In the biggest-
brained animals, like dolphins and humans, expansion progressed to the point of
scrunching up the cortex into dense folds, giving our brains their characteristic
furrowed appearance, We manage to cram about a quarter of a square meter of

cortical area into our skulls.

Given this, one might even consider the cortex itself to be more like a population
than a single entity: a “colony” of cortical columns that have managed to replicate
inside our skulls in larger and larger numbers through increased cooperation
among themselves. The greater intelligence they give us adds to our individual
fitness, which in turn allows us to form larger societies, which increases dynamic

stability all round.

You might find it disconcerting to think of your cortex as a colony of entities,
rather than as one unified entity, “yourself.” Remember, though, that at some
level, life always works this way. Our cells harbor colonies of mitochondria, and
our bodies consist of colonies of cells. All of these small entities are intelligent
in their own right, as any living thing needs to be in order to survive when sur-

rounded by other similar entities in a dynamic environment.

I think the reason we find intelligent cortical columns uncanny is that their
umwelt, the domain in which they are intelligent, overlaps with “our” umwelt—
unlike, say, a white blood cell, which, while obviously alive and active, inhabits
a microscopic inner world utterly alien to us. Cortical columns, by contrast, un-
derstand colors and shapes, people and places, stories and emotions. Our under-

standing is their understanding. And that is weird.

Indulge me in a speculative digression about everyone's favorite “alien intelli-
gence”: the octopus.!*24 Octopuses have always seemed like a bit of a fly in the
ointment, as far as the social-intelligence hypothesis is concerned. Unlike other

very smart animals on Earth, they're notoriously cranky and individualistic.

---

They don’t tend to hang out with each other, and usually only meet to mate—a

fraught encounter that may end in violence or even cannibalism.@4

While they are brilliant lifelong learners, they don’t live long enough to raise
their young, hence lack the ability to accumulate cultural knowledge. If they did,
it seems entirely possible that our planet’s seas would teem with octopus cities,
and perhaps even octopus-made computing machines (which would undoubt-
edly use an octal, or base eight, numbering system—a much better engineering

choice than our own base ten).

If octopuses are so antisocial, and intelligence is a social phenomenon, why are
they so smart? One could dodge the question and note that sociality doesn't
just involve conspecifics (i.e., others of your own species), nor is it necessarily
friendly. With omnivorous appetites and a total lack of body armor, the octopus
must rely on its wits to model and predict everything it wants to either hunt or
escape from; it seems likely that highly developed theory of mind, vulnerability

to predators, and flexible hunting strategies all coevolved.\422)

Amore fun possibility, though, is suggested by considering the other ways octo-
puses are so different from other big-brained animals, including us. The octopus’s
“brain” is highly decentralized, likely due to the high cost of long-distance com-
munication in the nervous systems of molluscs. Our own long-distance nerve
fibers are coated with fatty myelin sheaths, which greatly speed up and lower

the energetic cost of transmitting electrical impulses.!*2*! Mollusc nerve fibers
lack myelin sheaths, though. Transmitting fast impulses in unmyelinated nerves
requires dramatically increasing the diameter of the axon, which explains why
squids have a “giant axon”—a single nerve fiber up to 1.5 millimeters in diameter!
—running the length of their body. This giant axon allows for a rapid, coordi-
nated escape response.“ But obviously, for an animal with many neurons
powering complex behaviors, there isn’t room (or the energetic budget) for many
such giant axons, so a great majority of neural processing needs to be local. That
probably explains why three fifths of an octopus’s neurons are in the arms, rather
than in the head.

While cephalopods are bilaterian like us, their bodies are far more modular than

any land animal, exhibiting many additional near-symmetries. In the octopus,

---

over two hundred suckers are arranged in beautiful patterns along each of eight
arms, with chained neural networks surrounding each sucker. Individual suckers
are prehensile, almost like a pair of opposed fingers, and endowed with far richer
local sensory input than our hands, including touch and taste receptors, chro-
matophores for colorful skin displays, and even photoreceptors for light sensing.
A lot of tasting, moving, color-changing, reacting, deciding, predicting, and even

reasoning seems to occur under local control.

Hence the octopus's modularity is not just structural, but functional. Each sucker
is smart. Each arm, too, is intelligent, able to respond to stimuli with complex
movements without the involvement of the central brain.“ Arms recognize
each other directly as they move, avoiding self-entanglement without requiring
any central representation of the animal's geometry,“ which—given the wild
range of geometries possible for such a squishy animal with so many degrees of
freedom—would be an extraordinary challenge for any brain.“ The arms can
even communicate with each other directly via a ring of ganglia that encircle the
“shoulders,” with additional direct connections between alternating arms; these

routes bypass the brain entirely.2

There's more. Octopuses occasionally need to bite off an injured arm, an act
known as “autotomy.”“24! They may even do so to distract a predator, leaving one
writhing appendage behind while the other seven, along with the head, escape.
(At this point, as a smartass on Reddit observes, we would have a septopus.) In at
least one squid species, “attack autotomy” has been observed as well: a severed
arm attacks a predator while the rest of the animal escapes.“22! Following auto-

tomy, a new arm will regrow. For octopuses, the process takes about 130 days.

Perhaps, then, the octopus is best thought of as a tightly knit community of eight
arms, sharing among themselves a common pair of eyes. In fact, the bulk of the
central “brain” consists of a pair of optic lobes; we could think of these lobes com-
pressing visual information in service to the arms, rather than being “the boss,”
or even, in any meaningful sense, “the octopus.” In this light, attack autotomy in
the squid (whose nervous system is similarly organized) may not be so different

from the kamikaze tactics of a bee defending the hive.

---

Could the intelligence explosion that resulted in the octopus have been driven by
predictive social modeling—theory of mind, in effect—among its eight arms? As
absurd as this sounds, I think it’s plausible. Octopus arms are individually smart,
but communication among them is limited, due both to the high latency and low
bandwidth of unmyelinated nerve fibers. Centralized control under these con-

straints is impossible.

Yet the octopus’s arms must work together seamlessly to swim, hunt, escape
aquarium tanks, and so on; to do so, they must model each other. We know that
people can work closely together to perform such tasks with only a little commu-
nication; consider an elite military unit, or a hunting party, exchanging subtle
signs while stalking their quarry. Even intellectual tasks, like solving escape-
room puzzles or competing in Math Olympiads, involve such teamwork. Lan-

guage is a very low bandwidth medium, yet we still manage.

Accounts of small, extremely high-performing teams invariably emphasize both
the unity of purpose that can be achieved and the need for each team member

to infer what the others are up to based on minimal cues: that is, high-fidelity
mutual prediction, or mentalizing. When this happens in competitive rowing,
it’s called “swing”: “It only happens when all eight oarsmen are rowing in such
perfect unison that no single action by any one is out of sync with those of all the
others. [...] Each minute action [...] must be mirrored exactly by each oarsman,
from one end of the boat to the other. [...] Only then will it feel as ifthe boatisa

part of each of them, moving as if on its own.”""24

Homunculus

How different are we from the octopus, really? We have fast, myelinated nerves
that allow for greater physical centralization of our brain in our heads, but if what
I've suggested is correct—that our brains can be thought of as symbiotic colonies
of cortical columns modeling each other—then the difference may be more of
degree than of kind. This is unsettling, because we tend to have a strong sense of

ourselves as a unified “I.”

Much intuitive (and supernatural) thinking over the ages has presumed this

indivisible self, located somewhere in the body. Presumably it’s in the brain

---

somewhere. That’s why we can imagine getting a “full body transplant” but not
a “brain transplant.” A common term for this “something in the brain” is a “ho-
munculus,” literally, a “little man” somewhere in there, pulling the strings. In

many religious traditions, the immortal soul plays this homuncular role.

René Descartes (1596-1650) thought about the problem from a neuroanatomical
point of view. An influential champion of “mechanical philosophy,” or what we
now call physics, Descartes held that the body and brain must be mechanical, or
machine-like, since we seem to be made of the same stuff as the rest of the physi-
cal universe. Further, human anatomy has much in common with other animals’
anatomy, and human behavior has much in common with other animals’ behav-
ior: the “passions” of hunger and sexual attraction, reflexes to flinch if burned,
and so on. Hence Descartes coined the term “béte-machine,” or “animal-machine,”

to describe the mechanically based physiology of animal and human bodies.

Still, Descartes needed some way to reconcile mechanical philosophy with his
Christian faith.“2*) The Church held that we have immortal souls while other
animals do not, and the Enlightenment emphasized the divine gift of human
rationality; other animals certainly didn’t seem to be writing philosophical trea-
tises. Borrowing from Aristotle, Descartes found an elegant solution: identifying
rationality itself with the soul. The twist was that a soul-brain interface of some

kind would be needed for the immaterial soul to puppet the material body.

To theorize how this might work, Descartes again borrowed from the classical
world, this time a medical authority. Galen (roughly 130-210 CE) believed the
cerebral ventricles were filled with “psychic pneuma,” a volatile, vaporous sub-
stance that he described as “the first instrument of the soul.”4 Riffing on this
idea, Descartes imagined the body to be, literally, a hydraulic machine powered
by psychic pneuma: “When a rational soul is present in this machine it will have
its principal seat in the brain and will reside there like the fountaineer, who must
be stationed at the tanks to which the fountain’s pipes return if he wants to initi-

ate, impede, or [...] alter their movements.”24

Clever! But where was this “fountaineer”? Descartes concluded that it must reside
in the pineal gland, a small, pinecone-shaped structure near the center of the

brain. For one thing, it’s near the cerebral ventricles, the supposed “tanks” or

---

reservoirs of psychic pneuma. More importantly, the pineal gland is one of the
few discrete structures located along the brain’s midline—meaning we have only
one of them. Being indivisible, surely the soul couldn't reside in a pair of struc-

tures on both the left and right sides of the brain!

Spoiler alert: the pineal gland’s main job is melatonin production. It helps regu-

late the circadian rhythm. It is not the seat of the soul.

Descartes’s mistake was more fundamental than picking the wrong gland. Some
neuroscientists are still seeking an elusive brain region, circuit, or type of neuron
where our consciousness might reside. It’s certainly true that not all brain re-
gions are created equal; the severity of a stroke depends critically on which struc-
tures it knocks out. However, I think that attempting to pin down the location of
a homunculus, soul, or “self” within the brain is like trying to locate where the

“swing” is in a crewed boat.

This isn't to say that either phenomenon is unreal or illusory. Swing is perfectly
real, as those who have experienced it can attest. But it is a verb, not a thing;
distributed, not localized; a dynamic process in time, not a static condition; and
relational, not individual. There is nothing supernatural about it, but neither is it

physical, or even objective. It’s functional. It results in higher performance of the

---

boat, and so has tangible effects in the world. But it is also subjective, experienced
by each of the eight members of the crew in relation to the others, and to the

whole.

Imagine replacing one of the crew members in the boat with a robot. Not the
dumb kind we have in factories today, but one capable of pulling the oars likea
person, hearing, seeing, touching, and using haptic and audiovisual cues to com-
municate with the rest of the crew. Could such a “cyborg crew” achieve swing? I
think the answer is a clear “yes,” and, in fact, given the sophistication of today’s
AI models, any remaining impediment has mainly to do with deficiencies in bat-

teries and motors—bodies, not “brains.”

This thought experiment is a boat-crew version of one posed by philosophers
David Chalmers and Susan Schneider that we could call the “brain of The-
seus,”\*25! by reference to Plutarch’s much older “ship of Theseus” thought experi-
ment (to stick with the boating theme a little longer). Theseus, the mythical king
and founder of Athens, has a legendary ship that is preserved by the Athenians
for generations. It undergoes innumerable repairs over the years to keep it in good
order. The question is: once every timber has been replaced, is it still the ship of

Theseus?

Now that we understand something about cellular biochemistry, we know that
the question applies literally to us, too, as most of the cells in our bodies turn over
many times throughout our lives, and, even in the longest-lived neurons, every
atom will get swapped out over time. If we want to assert the continuity of our
own identity, we need to acknowledge that a “self” is, like swing, a dynamical and

computational process, not a specific set of atoms. And the same is true of a ship!

Let’s follow Chalmers and Schneider in considering the “ship of Theseus” ques-
tion for the brain, now with a cyborg twist, as for the rowing crew. Imagine that a
single neuron in your brain is replaced by a computer model of that neuron. Once
more, the greatest problems here are technological, not conceptual. Thanks to
those mid-century experiments on the squid giant axon (and a great deal of work
since), we have excellent computational models of individual neurons, at least

with respect to their fast dynamics.

---

A complete neuron-machine interface is a much taller order. It would require not
only coupling a computer to all pre- and post-synaptic neurons, but also the abil-
ity to sense and emit a variety of neuromodulatory chemicals. This is well beyond
us today. But let’s set practicalities aside. The question is: if one of your neurons

were replaced by a “robot neuron,” would you notice?

Of course you wouldn't, because the brain is robust to anything going awry with
any single neuron. But what if we repeated the procedure for a billion of your

neurons? Or half of them? Or all of them?

The question is unsettling, because it highlights the difficulty we have in coming
to grips with a dynamic, process-oriented, computational, distributed, and
relationship-centric view of the “self.” We are still Cartesian enough in our think-
ing to wonder whether—per Schneider's description of a hypothetical surgeon
replacing your biological neurons with silicon-based ones—“your consciousness
would gradually diminish as your neurons are replaced, sort of like when you
turn down the volume on your music player. At some point [...] your conscious-
ness just fades out.” Or perhaps, “your consciousness would remain the same
until at some point, it abruptly ends. In both cases, the result is the same: The

lights go out.”

These ideas are—I have no words to put this gently—silly (and I think Schneider
and Chalmers both agree). In physical and computational terms, a neuron has

an inside and an outside, and if the insides were scooped out and replaced with
different machinery that performed the same function—which is to say, resulted
in identical interactions as seen from the outside—then none of the larger func-
tions in which this neuron plays a part will be affected. Per the Church-Turing
thesis, these functions could be computed in many equivalent ways, and using
many different computational substrates. That is true at every level of the nested

set of relationships, or functions, that we call “life” or “intelligence.”

Illusion and Reality

Philosopher of mind Daniel Dennett believed that consciousness and the self
are illusions; we're robots made of robots made of robots, so, per Dennett, there

is no real “there there,” other than as a convenience of speech.“*"! Similarly, for

---

philosopher-neuroscientists Sam Harris and Robert Sapolsky,‘**“! free will is an il-

lusion because minds are products of inexorable physical processes.

We are indeed robots made of robots made of robots, and minds are indeed based
on physical processes. However, my own sense is that “illusion” isn’t necessarily a
helpful word here, because it implies an incorrect assumption, or at best a polite
fiction. While nobody has suggested that we dispense with this “fiction” alto-
gether, Sapolsky comes close to running off that cliff when he asserts that, since
minds are physical and free will is illusory, notions like criminal justice, prizes,

praise, blame, and moral responsibility are all invalid and should be abandoned.

In Sapolsky’s defense, it is worthwhile to ask tough questions about our received
notions of justice, reward, and responsibility, especially when confronted with
alternatives that seem more humane, fairer, or lead to better outcomes. It's less
productive to become nihilistic because “it’s all an illusion.” That kind of nihilism
could also lead us to conclude that tables and chairs aren't “real,”“"! because they,

too, are mere collections of atoms.

Chapter 2 offers a more pragmatic take on reality, familiar from physics as well as
real life: “reality” is our name for a model with good predictive power. Or rather,
a suite of models. We will always need many, because every model has a limited
domain of validity. It would be awesome to discover the physicists’ holy grail, a
“Theory of Everything” unifying quantum fields and gravity. But it would tell
you nothing about whether your aunt will like the cake you're baking for her,
your friend will take your shift at the café, or your kid will get along with the
neighbor's kid. In fact, unless you’re one of a handful of rarefied physicists, it will

inform precisely nothing in your life.

Good questions to ask about a model, then, are: Does it agree with observations?
Does it make any testable predictions? Who cares about it? What function does
it serve? Where does it break down? Do we have a better candidate model? Some-
times we do have a better candidate, but, as with general relativity, it may be dis-
turbing or challenge deep-seated intuitions. Newtonian physics, which we finda
lot more intuitive, follows from general relativity, but only as an approximation
valid in our everyday world, where spacetime is reasonably flat and objects move

far slower than the speed of light.

---

That’s not to say that classical physics is an “illusion”; rather, the more general
theory illuminates a wider area. Einstein’s theory shows us when the Newtonian
approximation holds, when it doesn’t, and why. It resolves apparent contra-
dictions, like the incompatibility of Newtonian physics with a constant speed

of light. In this sense, general relativity actually bolsters the narrower classical
theory by reassuring us that the seeming paradoxes aren't cause for concern, and
by showing us why, when, and to what degree we can rely on familiar approxima-

tions.

Free will; the unitary, indivisible “self”; and interaction with other unitary
“selves” in the world are the common-sense axioms underpinning something
like a Newtonian model of social life. Theory of mind is that model. It’s our folk
theory—literally. It’s what we use when we predict our aunt’s tastes, our friend's
willingness to help, or our kid’s friendships. While powerful and useful in every-
day life, theory of mind is also confounding, even paradoxical, when we try to
reconcile it with the physical universe; hence the trouble Descartes got us into. In
the following discussion, we'll flesh out a more general theory that will help us

better understand our folk theory—and how it arises, and its conceptual limits.

But let's keep in mind just how powerful that folk theory is. Will Aunt Millie like
my cake? For a physicist, making such a prediction may seem like weak tea com-
pared with the extraordinarily precise, quantitative predictions we expect from

physical theories. But it’s not so.

---

# Chapter 6

6. Many Worlds

Au Revoir

Consider the scenario at the end of Richard Linklater’s indie film Before
Sunrise.“*2) Young backpackers Jesse and Céline meet on a train traveling from
Budapest to Vienna. Arriving in the evening and low on funds, they decide to
spend the night wandering the city together before their onward connections the
following day—Jesse will catch a flight back to the US, while Céline is returning to
university in Paris. Sparks fly, of course (I mean, it’s Julie Delpy and Ethan Hawke;

they are clever, charming, and... well, hot).

The next morning, they’re back at the train station, but they haven't shared
contact information. Here, you have to cast your mind back to 1995, when ro-
mance was still analog: no cell phones, no social media. They had agreed that this
would be a one-night thing. But as Céline’s train is about to leave, in an anguished
rush of words, the maybe-lovers realize that they badly want to see each other
again after all. So they decide to meet right there, at the same place, in exactly six

months.

---

Six months from this morning, or from last night? asks Céline.

From six o'clock last night, when their train arrived, says Jesse. It’s June seven-

teenth, so it will be ... December sixteenth, on track nine.

---

They say goodbye, which Céline amends to a hopeful “au revoir.”

Now, let’s take off the love goggles and think about this as physicists. Given
accurate measurements, dynamical laws allow us to predict the orbits of planets
and moons, gravitationally bound and hurtling through the near-vacuum of
outer space, far into the future. Those laws of motion are quite simple. Even here,
though, prediction has inherent limits, because when three or more bodies are
interacting gravitationally, chaos rears its head. If two trajectories differ by some
small amount, then, over time, this difference grows exponentially. In the Solar
system, luckily for us, the exponential divergence is slow, with a characteristic

time of millions of years.)

So much for celestial bodies; what about earthly ones? If we think about the
predictability of Céline and Jesse as physical systems, we quickly realize we're
sunk. They are not isolated from the rest of the world by hard vacuum, but are

in continual rough-and-tumble contact with it. And virtually every interaction
within their bodies and with their surroundings is strongly nonlinear. The math
is impossible. Not to mention that after six months of breathing, eating, and per-
forming other bodily functions, we won't even be talking about the same atoms.
It's not straightforward even to specify what exactly we mean by “Céline” and

“Jesse.”

Worse, as described earlier, their evolutionary origins have conspired to make
them unpredictable. It’s not just a matter of maintaining a facade of romantic
mystery. Operating like this is essential to any living system that seeks to remain
responsive to its environment. The signals exchanged between Jesse and Céline
on that platform amounted to a few seconds of faint pressure waves in the air
that were picked up by their eardrums, amplified by their middle ears, and con-
verted into action potentials by hair cells in their cochleas. For that faint signal
to have any macroscopic consequence relies on a cascade of physical systems that
are all tuned to be on the edge of chaos, which is to say, exquisitely sensitive to

perturbation—starting with the ear itself.)

Hence, the electrical activity of a few neurons in their brains could tip the be-

havior of their entire bodies (and everything those bodies interact with) toward

---

radically diverging futures. Céline and Jesse are walking, talking instances of the

butterfly effect—one of the movie's main themes.“

And yet. In the days before cell phones, we used to make plans like this all the
time, and they often worked out“! How could that be, in light of its seeming
physical impossibility?

Or, more accurately, extreme improbability. Based on physical modeling alone,
we could work backward to conclude that it would be possible for the watery,
ever-changing bag of molecules known as “Jesse” to once again be at the platform
of track nine in exactly six months, but given exponential divergence (or, seen
backward, exponential convergence), it would also be possible for him to be in

Kathmandu, or anywhere else.

A hidebound determinist might argue: yes, but if we knew the exact position
and velocity of every particle in the universe, then we could in theory run the
(unbelievably complex) calculations forward in time, exponential divergences be
damned, and just see whether the lovers meet again or not—just as we can calcu-
late the orbits of the planets at some future time, given enough decimal places of

precision and enough computing power.

Here’s the trouble: even in theory, such precision would be impossible. Exponen-
tial divergence means that over some constant amount of time, an extra deci-
mal place of precision would be needed to keep the prediction accurate within
some tolerance. Suppose that for the system we call “Céline,” that interval is one
second.““7! Well before a minute has elapsed, an accurate prediction would then
require knowing the starting positions of all of Céline’s elementary particles with
a precision finer than the Planck length, which is about 1.6«10°?> meters. But
that can’t be. Quantum physics tells us that the Planck length is a hard limit on
our ability to localize anything.

As mentioned near the beginning of this book, we don’t understand how the
universe works at that absurdly tiny scale. Some physicists imagine a kind of
churning spacetime foam. What we know for certain, based on elegant experi-

ments, is that randomness bubbles up into our universe at this scale—and it’s real

---

randomness, not some deterministic mechanism involving unseen or “hidden”

variables 4)

This means no deterministic physical theory exists that could predict with cer-
tainty where the lovers will be in six months. Ignoring practical impossibilities,
even if we were to run a full simulation of the universe many times, with initial
conditions perfectly matched to the present and with quantum randomness
injected to sample possible trajectories, the positions of the particles associated
with Céline and Jesse will rapidly diverge. Hence any physics-based model will be

inherently myopic; the future blurs as we try to peer into it.

Fascinatingly, it blurs much faster for living systems than for nonliving ones.
One could even characterize intelligent life as that which cloaks its own future

in indeterminacy, pushing back against physical prediction.“ The mechanism
it uses to pull off this trick is dynamical instability, which can work as a noise
amplifier. And the universe provides us with a faint but inexhaustible source of
noise to amplify. At coarse scales, it looks like thermal noise, or Brownian motion;
at much smaller scales, the ultimate noise source underwriting that randomness
is quantum mechanical. Living things eke out their elbow room by using such

noise—along with inputs from their environment—to make decisions.“

While physical theories fail to predict the behavior of living systems, we havea

much more effective predictive model: our old friend, theory of mind.

Will What You Will

Céline and Jesse are not just watery bags of molecules, but agents whose entire
evolutionary raison d’étre is to model themselves and each other. That is both

what it means for them to have free will, and for them to be able to predict each
other’s behavior six months hence—far beyond anything physical determinism

could achieve in a world with quantum uncertainty.

Amplifying random numbers seems like a dubious basis for either of these

claims. If you were to, for instance, attempt to foil determinism in your dating
life by scrolling through Tinder and flipping a coin to decide whether to swipe
left or right, that would hardly be a satisfactory basis for claiming that you are

---

exercising free will. It would also render your actions wholly unpredictable, both

to yourself and to your (perhaps bemused) prospective dates.“

Free will involves combining theory of mind, randomness, dynamical instability,

and selection:

1. Theory of mind can be used not only to model others, but to model
oneself. We've already encountered this at second order, and beyond
(“what Jane believes Mr. Rochester must think Jane thinks”). There's
no reason this same faculty can’t work reflexively: “what Jesse thinks
Jesse thinks.” Or, in a less navel-gazey way, “what Jesse imagines he
will see, think, and do in a few minutes, when it’s time to catch a bus
to the airport,” or “what future Jesse will do in five months or so: book
a plane ticket.” Planning for one’s own future is necessarily a theory-
of-mind exercise—a way to cooperate with your future self. Or, to turn
it around, without theory of mind it would not be possible to “time-
travel” and imagine what you will experience and do under circum-
stances other than the present.

2. To time-travel, or to imagine how any pretend scenario might play out,
you must be able to draw random numbers in your head, in much the
same way the physical universe must constantly draw random num-
bers to resolve the blurry cone of possible futures into a specific one.
Daydreaming is a kind of random walk through modeled associations
or predictions, but so is planning; planning is just more directed.

3. Dynamical instability (the butterfly effect) in neural circuitry makes
choosing a potential future possible, for the same reason that dy-
namical instability makes it possible for a cockroach to scurry either
left or right in advance of a shoe (as described in chapter 3). For the
cockroach, the butterfly effect allows behavior to be unpredictable,
when driven by the faintest whisper of a random variable. Interest-
ingly, though, dynamical instability is also necessary for behavior to
be predictably influenced by an external stimulus—as when you turn
left or right based on a faint whisper in your ear saying “go left” or “go
right.” Free will, too, relies on this dynamical instability, for you need

to be able to whisper to yourself, “imagine doing X,” then “imagine in-

---

stead doing Y,” and, eventually, “do Z.”(*4l In other words, being able to
control your own behavior requires being able to amplify faint inter-
nal signals.

4. Finally, selection, powered by theory of mind, allows one to favor cer-
tain possible futures, and cut off or stop exploring other ones, much
the way AlphaGo's value network prunes its Monte Carlo tree search.
If Jesse knows that by getting to the plane on time he will feel melan-
choly but be safely en route home, and that missing the plane will
leave him stranded, alone, anxious, and broke, then there’s no need to
plan the latter scenario in detail; best to just figure out, instead, what
steps he will take to get to the plane on time. When we talk colloquially
about “rational” behavior, this is generally what we mean. Notice that
the branching character of possible futures allows one to justify—
and at times even legitimately make—decisions using logic. However,
contra Leibniz, this logical aspect of decision-making, when present at
all, is computationally trivial compared to the acts of imagination in-

volved in mentally simulating worlds and people, including yourself.

So, theory of mind lets us build a network of solid tracks along which our minds
can venture far into an otherwise marshy future. Dynamical instability, like a
lubricant, lets us glide anywhere along those tracks, free to go either way at any
fork with the gentlest of nudges. Randomness provides those nudges, letting us
wander prospectively into multiple futures. And selection prunes the network to
allow efficient long-range planning. You may notice that this looks a lot like a fast

version of evolution taking place in imaginary worlds!

When pruning occurs in advance and after lengthy exploration, we callita
deliberative decision. When it occurs just in time, because we've kept multiple
paths open until the last possible moment, or we’ve changed our minds, or an
unforeseen opportunity arises, we call it a snap decision. If you've been able
to competently exercise theory of mind about your “self” to guide a decision,
whether deliberative or spur-of-the-moment, you can meaningfully be said to

have exercised free will.

---

There's no dualism or supernatural “fountaineer” in this account. Nonetheless,
calling a decision freely willed seems justified given an everyday understanding
of what that means. There is a “you” who made this decision; you are not acting
reflexively, but modeling a self, sampling multiple alternatives, and making a
choice based on how those alternatives appeal to that modeled self. In other
words, the “you” here is not just a brain, but a modeled self: a functional entity,

not merely a physical one.

Free will is compromised when these conditions are compromised. For instance,
if your choice landscape is too constrained to offer meaningful alternatives, then
you aren't free, as anyone who has ever been in prison, in a refugee camp, or in
an endless immigration queue at the airport can attest. If an act is reflexive, it’s
not freely willed either. If your model of yourself is unreliable due to immaturity,
incapacity, intoxication, or mental illness, then your free will is also impaired.
The same holds if your predictive model of the world or of others is broken, for
instance, due to delusional beliefs. These ideas are familiar from legal theory,

ethics, or plain common sense.

Endless debates and ongoing reassessments (rightly) abound about what consti-
tutes impairment, freedom, or choice. For instance, when someone without any
criminal history suddenly commits a horrible crime, and a brain scan reveals a
fast-growing tumor, this may be exculpatory. Before brain-imaging techniques,
we wouldn’t have known.!*+! However, not everybody who does something
reprehensible has the equivalent of a tumor, especially when that somebody was
perfectly able to think through the options and model the perspectives of others.
There's nothing spooky about choice, impairment, responsibility, or culpability.
Every human society acknowledges these concepts, though they vary in their

norms and in where they draw lines.

Some free will “compatibilists” acknowledge the social utility of concepts like free
will, but believe that they are, at bottom, illusions, either because physics alone
suffices to explain everything, or because, as Schopenhauer observed, a person
can do what they will, but not will what they will.“ I hope I have explained why
physics does not explain everything, or, practically speaking, much of anything,

when it comes to predicting each other—or ourselves.

---

As for Schopenhauer’s maxim: the first clause trumps the second. It’s true that,
when you evaluate choices, you're applying a value judgment; its particularities,
from valuing honesty above loyalty to finding blue cheese gross, are part of what
makes you you, and not someone else. You can't choose to wake up as a different
person one day, but you can decide that you're going to try the blue cheese with
an open mind, despite the ick. Your decision need not be due to some other, over-
riding value. It could be a reasoned decision, or just a case of “what the hell, I'll

give it a go.”

Once you realize how yummy blue cheese is, your future judgments will change.
So, as you author (and revise) the story of your own life, you can change who

you are, thus willing what you will will.“°*! We even understand something now
about the mechanics of that process. It’s called “in-context learning,” and will be

discussed in chapter 8.

The account I've just given of free will“ includes the self-referential features

of what we generally call “consciousness.” Immediate feelings or experiences,
such as pain, pleasure, fear, or, for animals that can see the color red, “redness”
don’t require these fancy features. Chapter 2 describes how basic feelings arise

as a matter of course in any self-predicting modeler that has evolved to persist
through time. Most of us can tell red from green because it’s a useful spectral
distinction for spotting ripe berries or blood, which are helpful things to know
about. That’s no mystery, and lots of other animals—including insects—can
experience “redness” too, for similar reasons. Many can also experience “ultravio-
letness” and other sensations unfamiliar to us, because for them, those signals are

behaviorally relevant.“°41

Amore sophisticated mind can support more complex internal states, including
simulated worlds, counterfactuals, and prospective futures. Such minds evolve
via social-intelligence explosions, which implies that much of the complexity in
those simulations concerns other minds—what they know, what they experience,

how they will act or react.

A “self” is inherent to any social modeling if carried out to second order, because
those others you’re modeling are ... modeling you back. If they're conspecifics,

then they are also very similar to you; for instance, as a chimp, it requires only a

---

little imagination to see the world through the eyes of another chimp. When your
social brain has evolved to this point, it’s no great leap to stare into the mirror,
physical or mental, and consider yourself as a being, both in the future (which is
essential for long-range planning) and in the present.“ The infinite regress of

your “Mind’s I” in that mirror gives you the vertiginous experience of self Douglas

Hofstadter calls a “strange loop.”22)

What It Is Like to Be

Consciousness is not that complicated! So why do we struggle so much with it—

of 460}

what makes it a “hard problem"—“ for philosophers?

Since “hardness” is subjective, a cross-cultural perspective is helpful.\4°4! As it
turns out, philosophers in the modern European tradition are far from the norm;
they are, to use evolutionary anthropologist Joseph Henrich’s term, WEIRD:
Western, Educated, Industrialized, Rich, Democratic.“ Let’s step outside this

bubble, which is, both historically and psychologically, a minority.

Human cultures are near-unanimous in their belief in souls, though the details

of what constitutes a soul and where it resides in the body (or at times outside

---

it) vary.*®2! Belief in the ensoulment of animals is commonplace, as is a belief in
souls, great or small, residing elsewhere in nature. Chapter 1 offered a bottom-
up account of animism, emphasizing the blurriness of the boundary between the
living and the nonliving from the standpoint of dynamic stability and function-

alism.

Let’s now take the human perspective, or, more generically, the perspective of a
social animal that has undergone an intelligence explosion and is endowed with
a highly developed theory of mind. For such a being, souls are just about the most
behaviorally relevant things one can imagine—more so than numbers, clouds, or
ripe berries. For social animals, other minds are the umwelt. So of course we distin-
guish between “somebody home” and “nobody home.” Many human languages

mark that distinction grammatically, as English does with “who” versus “what.”

Even so, cultures are far from being in agreement about what falls into each cate-
gory. In Potawatomi, almost everything is a “who,” until or unless it is harvested
for human use.!*4! Under Roman law, on the other hand, human slaves were
instrumenta, like tools or equipment.“ In both cases, the distinction is made on
the basis of whether theory of mind is being exercised. A Potawatomi considers
the perspective of a “bear person,” a “tree person,” and so on, until the moment

of harvest—which is traditionally accompanied by a prayer of thanks—after
which that perspective ceases to be, in the harvester’s mind. For Romans, the very
definition of slavery lay in the slave's loss of agency, such that for the master, the

slave’s point of view didn't need to be taken into account.

These represent cultural ideals, of course. In reality, we humans, regardless of
cultural background, are probably more alike than we let on. Some Romans un-
doubtedly had reciprocal relationships with their slaves, and some Potawatomi
herb-gatherers are probably guilty of skipping their ceremonial thanks if no-
body’s watching. Conversely, we may all profess not to believe there’s “anybody
home" in a kid's stuffed animal, but as Tracy Gleason, a professor of psychology,
has written about her much younger sister’s threadbare stuffed rabbit, that’s not
how many of us behave: “I know his brain is polyester fill and his feelings are not

his but my own, and yet his [...] eyes see through me and call me on my hypocrisy.

---

I could no more walk past Murray as he lies in an uncomfortable position than I

could ignore my sister’s pleas to play with her or the cat’s meows for food.”

WEIRD beliefs about what counts as a “who” are particular. Then again, any such
beliefs are particular. What seems to distinguish WEIRD beliefs from those of
traditional societies is their single-mindedness—literally. Philosophical debates
about consciousness in the West focus heavily on the inner life of an individual:
per Descartes, “Cogito, ergo sum,” meaning “I think, therefore I am.” That packs a

lot of “I” for such a short sentence.

Centuries of introspective discourse have carried on about qualia and “phenome-
nal consciousness” while ignoring the fundamentally social and relational nature
of theory of mind, and the way consciousness arises precisely when we model
ourselves the way we model others. For example, in her book Conscious, Annaka

Harris writes,

Surprisingly, our consciousness [...] doesn’t appear to be involved in much
of our own behavior, apart from bearing witness to it [...]. [Flew (if any) of
our behaviors need consciousness in order to be carried out. |...] However,
in my own musings, I have stumbled into what might be an interesting ex-
ception: consciousness seems to play a role in behavior when we think and
talk about the mystery of consciousness. [...] How could an unconscious robot
(or a philosophical zombie) contemplate conscious experience itself with-

out having it in the first place?t*4)

Consciousness certainly does come in handy when thinking about conscious-
ness. But unless we're chronic navel-gazers, we don’t spend much time thinking
about our own experiences and thoughts in the moment. When we are on our
own and on autopilot (as we often are when we’re on our own), we tend to just
act. Life would be exhausting otherwise. But in a social setting, we must con-
stantly think about our relationships, how we're coming across, and the experi-

ences of others; this modeling deeply informs how we act.

And it is sometimes useful to be able to actively model, and thus manipulate,
your own attention. Consider meditation, or simply allowing yourself to fall

asleep when you're keyed up after a busy day—acknowledging, then dismissing

---

intrusive thoughts; scanning your body; relaxing your muscles from head to feet.
Your attention is like a spotlight, and controlling it requires you to pay attention

to your attention.

According to neuroscientist Michael Graziano’s “Attention Schema Theo-

ry” (AST), consciousness is an illusion arising from this modeling of one’s own
attention.“““! Graziano invokes ventriloquism to illustrate the point. When a
skilled ventriloquist throws their voice into a puppet, manipulating its gaze and
moving its jaw along with the words, we experience a powerful impression of the
puppet as a person. In modeling that puppet’s attention, we have conjured into
existence a modeler, or soul: a being whose attention that is. If the puppet turns
toward us and begins to speak, we enter into that recursive social loop, modeling
it attending to us attending to it, and so on. The punchline is that we are all pup-

pets; we just happen to pull our own strings.

I agree with Graziano'’s account, though I would quibble with his use of the term
“illusion” to describe consciousness or personhood. If chairs aren't illusory, then
neither are people. Attention is a real enough sort of computation, useful for pre-
dictive modeling. And in a world of sophisticated predictive modelers, including
oneself, attention is worth modeling in its own right. It’s reasonable, then, to
define a being, a soul, or a “who” as that which can pay attention—and can model

that attention.

Weird

Taking seriously the perspective of intelligence as relational implies something
far more mind-bending than merely acknowledging the social origins of con-
sciousness, It implies that relationships themselves are the building blocks of
reality. There is no God’s-eye “view from nowhere” in a relationship graph. In fact

there isn't even a God’s-eye view of what the nodes in the graph are.

Let’s first take Tracy Gleason’s perspective. Murray the rabbit is a node in her
social graph, albeit one that she is of two minds about (a phrase that, as we'll see,

might have an almost literal interpretation).

---

But does Murray have a perspective? We (mostly) believe not, and can back the
“nobody home” belief with all sorts of scientific evidence, like the fact that his
little head is stuffed with polyester. Insisting that computation is happening in
there, that he has muscles and a nervous system, and that he is about to jump
up and dash into the closet would all be poor predictions, both anatomically and
behaviorally.

For a slightly less clear-cut case, consider Furby, a furry robotic toy released

in 1998. When placed in an “uncomfortable” upside-down position, the robot
squirms and makes unhappy noises. These simple electronic behaviors make it
powerfully aversive to hold Furby upside-down for too long, even if, like Gleason,

we can’t rationalize our own behavior.!22)

Or take the case of Graziano's ventriloquist. It’s true that a puppet, no matter
how convincingly imbued with personality, has a head as empty as Murray's. Its
ears can’t hear and its eyes are painted on. However, the puppeteer can see, hear,
and think just fine. Moreover, she can use her theory of mind and acting skills to
immerse herself in the puppet’s perspective, creating a character with its own
relationships—whether to the audience, to other puppets, or to the puppeteer.
Are puppets really people, though? If they were, wouldn’t we be more concerned

when Punch and Judy pummel each other?

More broadly, when is accounting for another's perspective possible and war-
ranted, and why? How should these perspectives be imagined and weighted
against one another? We have arguments all the time about the really difficult
judgments: how do we weigh the interests and perspectives of chimpanzees and
bonobos, or of octopuses, or even of octopus arms? What about the potential per-
spectives and interests of embryos and fetuses at various stages of development?
Or of people in comas with profound brain damage? In these cases and many
more, reasonable people disagree, and while advances in neuroscience may offer
additional insight, no magical scientific measurement will come to our rescue

and tell us what is “right.”

Still, it’s not hopeless to imagine the inner life of another being. On the contrary

—we’re good at this. It’s what we have evolved to do. However, all we have are our

---

models and our ability to mentalize—to see through the eyes of (some) others,

some of the time, with greater or lesser predictive accuracy.

Recall how categorical modeling works for an inanimate concrete category, like
“bed.” There is nothing mysterious or ineffable about the existence of beds in the
world; you probably sleep on one, most nights, and don’t wonder about its onto-

logical status. You can easily recognize one on sight, or, if you're blind, by touch.

But this doesn’t mean that every person has the same definition of “bed.” In the
European Middle Ages, rushes strewn on the floor comprised “bed” for most peo-
ple. In Japan, tatami mats may be beds. A futon can be a sofa or a bed, and it may
“be” one or the other simply by virtue of whether you are lying down on it. In
other words, our models of “bed,” which work something like multilayer percep-

trons (as described in chapter 3), vary by person and by context.

Although this is easy to understand, it’s not a triviality: per the interlude at the
end of chapter 2, it already deals a death blow to the Leibnizian ideal of relying
on impartial logic to make universal truth statements about beds or pretty much
any other object. We have already left the notion of “objective” reality behind.

Here’s the weightier implication: it’s just as impossible to assert objectivity about
animate categories, like “person” or “conscious.” This idea has been far harder for

me to accept.

The difficulty is partly of WEIRD origin. One of the most famous documents lay-
ing out the tenets of the WEIRD worldview says, right at the top, “We hold these
truths to be self-evident, that all men are created equal, that they are endowed by
their Creator with certain unalienable Rights, that among these are Life, Liberty
and the pursuit of Happiness.”““"! These were great ideas, and they represented

important social and political innovations in the eighteenth century.

However, the use of the word “men” suggests that these truths are not so time-
lessly and universally self-evident. We would not use the same word today. And
it was no grammatical quirk. The authors of the Declaration of Independence (all
men) didn’t believe that women, let alone non-European people, were “created

equal” to themselves or endowed with the same “unalienable Rights.”

---

Clearly, then, the legal understanding of personhood changed significantly
between 1776 and 1948, when the Universal Declaration of Human Rights ex-
tended “inherent dignity and [...] equal and inalienable rights” to “all members of
the human family [...] without distinction of any kind, such as race, colour, sex,
language, religion, political or other opinion, national or social origin, property,
birth or other status.”424

Excellent progress. However, that these are statements of evolving political intent
rather than of self-evident, universally agreed-upon fact is once again obvious,
given that the Declaration was partly a response to the Holocaust, which had

been brought to an end by the Allied victory in Europe just three years earlier.

Universality and “self-evidentness” are WEIRD mind tricks.*/“! They assert that
something is so unquestionably the case that there is no author, no point of view
—other than, perhaps, that of God the Creator. In reality, of course, there are
specific authors, and they are expressing their point of view and their political
will, But unlike the proclamations of kings, the WEIRD approach adds a layer of
indirection and anonymity, an appeal to “universal law.” It asserts a kind of New-
tonian physics of personhood, stipulating “who counts as a who” in terms that do

their best to deny any role for subjectivity.

This is entirely in the spirit of the Enlightenment. It goes along with the stan-
dardization of weights and measures, the establishment of reliable “railroad
time,” the development of latitude and longitude as a global coordinate system,
and, most of all, the formulation of physical laws with universal applicability,
from celestial motion to the pendulums of clocks. These, too, were important
advances, both intellectually and practically. They made it possible for people,
goods, and information to flow worldwide, underpinning much of the wealth,

knowledge, and global culture we now take for granted.

However, general relativity tells us that this global frame of reference is only an
approximation. What the passenger on a train regards as one meter is a tiny bit
less for someone watching from the station. When you stand on the ground, a

second passes a tiny bit more slowly for your feet than for your head.

---

Similarly, we know that, no matter how vigorously we assert the timeless
universality of human rights and dignities, precepts of moral conduct or ethics,
these are neither timeless nor universal; we have had to continually argue about
them, fight for them, and change our conceptions of them over time. Historical
documents, from religious texts to political manifestos, reveal their cultural
contingency, variability, and ongoing evolution. It would be nonsensical to assert
that we have, at just this moment in history, reached the end of the line, and
have achieved either the final word or a universal consensus. And this includes
not only questions of how to behave toward a “who,” but who or what counts as a

“who,” and indeed whether that is best thought of as a binary category.

Entanglement

Like Alice in Wonderland, we are about to go down the rabbit hole. Our rabbit
hole is quantum mechanical weirdness, and what it tells us about the nature of

reality and our models of it.

To be clear, this is not in any way an appeal to the pseudoscience of “quantum
consciousness,” or the idea that the brain is a quantum computer—a position
with no mainstream scientific support.“”! As far as we know, no cognitive func-
tions rely on quantum phenomena. Nonetheless, we have seen why quantum
mechanics matters in discussing the mind, despite its remoteness from our
everyday experience: it establishes sharp limits on the predictability of living
organisms (which is relevant to determinism debates), and it provides an inex-

haustible source of randomness for minds to “harvest” as they exercise free will.

We'll now delve deeper into post-classical physics, because it can also help us
better grasp what it means to adopt the kind of relationship-centric perspective
required to understand mutual modeling and conscious experience. Keep in
mind that this is more than a metaphor. Modern physics offers our best guide
to how the universe works at a fundamental level; it is our Newtonian or folk
physics that we should handle with caution, even—or especially—when we rely

on it as a metaphor. So... down we go.

One of the least intuitive ideas in quantum mechanics is that of superposition,

which holds that a physical system can be in multiple states at once. This is

---

certainly true of single particles. Putting a very faint photon source and photo-
graphic film on opposite sides of a barrier with two slits, for example, produces
dots on the film as one would expect, yet their distribution reveals an interfer-
ence pattern with multiple peaks and troughs, as if each photon had passed,
wave-like, through both slits at once before turning back into a particle to expose
the film. If one of the slits is closed, the interference pattern disappears. Likewise,
the interference pattern disappears if the experimenter adds any measuring
apparatus to determine which slit the photon passes through! The double-slit ex-

periment has also been done with electrons, and even with large molecules,.4“!

In 1935, Erwin Schrédinger devised a famous thought experiment to highlight
the bizarreness of this phenomenon. It goes like this. A cat is in a box, along with
an apparatus. The apparatus contains a Geiger counter that will register the nu-
clear decay of a single atom in a radioactive sample. We know that nuclear decay
is a truly random quantum event. The source and detector could be calibrated so
that such a decay event has a fifty-percent chance of occurring within an hour. If
the event occurs, a mechanism will open a draught of sleeping potion, and the cat
will fall asleep. Otherwise, she will remain awake. (In keeping with modern lab
ethics and my fondness for cats, I’m adopting physicist Carlo Rovelli’s modifica-
tion to Schrédinger’s original protocol, in which the “sleeping potion” was need-
lessly lethal.47!)

We know that, when we open the box after an hour, we will see either a sleeping
cat or an awake cat. But was the cat already asleep or awake just before we opened

the box? Or was she ... both?

Originally, Schrédinger’s cat was meant to critique the so-called “Copenhagen
interpretation” of quantum mechanics advanced by Werner Heisenberg and col-
leagues. In this interpretation, a physical system is in a superposition of all possi-
ble states until it is measured, at which point its “wave function” collapses into an
unambiguous state. Everything behaves, in other words, like a fuzzy probability
wave while your back is turned, but becomes a particle the moment you peek, like

the exposed dots on the film in the double-slit experiment.

While the Copenhagen interpretation is consistent with a century’s worth of

experimental findings, it's deeply troubling, because it appears to privilege the

---

observer or experimenter. After all, we, too, are just quantum wave functions;
why should our observation of a particle in the lab collapse its wave function,
while it can get up to all sorts of spooky business—including “quantum entangle-
ment” with any number of other wave functions—when we're not looking? It all
seems a bit Twilight Zone. And lest we believe it only applies at scales so invisibly
small as to be irrelevant, researchers have succeeded in putting millimeter-sized
objects in the lab into quantum superpositions, if they are suitably isolated from
their surroundings—which in practice has meant cooling them to extremely low

temperatures. +!)

The practicalities of making a box well enough isolated for a whole cat inside to
remain in superposition (and not frozen solid with liquid helium) aren't straight-
forward; it’s a lot harder than preventing the sound of a meow from getting

out. Still, in theory, it’s possible. If we succeeded in isolating the box thoroughly
enough, then after an hour, the cat would be both sleeping and not—until we
opened the box. At that point, we would collapse her wave function, and she

would be just one or the other: asleep or awake.

As with the ambiguities about objects and subjects described earlier, what makes
Schrédinger's thought experiment so disturbing is that what's inside the box is
not just a loop of superconducting wire, as in experiments that have actually
been done, but a cat. What is it like to be simultaneously awake and asleep? Hold
on—isn’t the cat an observer too, inadvertently running a lab experiment of her
own, inside the box? If so, wouldn't she collapse the apparatus’s wave function by
either observing or not observing the unstoppering of the potion? But then, why
would that not be true within the apparatus itself—isn’t every part of it “observ-
ing” whatever it’s in contact with? Does an “observer” have to be conscious for col-

lapse to occur?

There is no universal agreement on any of these questions within the physics
community; that’s why we're still talking about Schrédinger’s cat nearly a cen-
tury later. Quantum mechanics continues to be subject to myriad interpretations,
most of which add some further postulate or assumption to the known equations
to force them to make more intuitive sense. Partisans of each interpretation make

different claims about the cat: perhaps she’s too big to be in superposition, but a

---

flea on the cat could be; or perhaps the cat exists in an infinite number of parallel

universes, awake in some and asleep in others.

A particularly straightforward interpretation championed by Carlo Rovelli (the
physicist who likes cats) is “relational quantum mechanics” or ROM. It adds
nothing to the equations, but instead asks us to take them at face value—with

a reminder that any observations made during an experiment are always made
from a point of view. Just as in the theory of relativity, there is no privileged “view
from nowhere.” According to Einstein's relativity, lengths and durations depend
on one’s perspective. According to Rovelli’s RQM, events themselves depend on

one’s perspective.

From her own point of view, the cat can’t be simultaneously asleep and awake,
any more than we, outside the box, can be. Nobody ever gets to observe some-
thing in superposition, including oneself. However, from an experimenter’s
perspective outside the box—f all interactions between inside and outside are
prevented—the cat is indeed in a superposition of asleep and awake ... right up

until the box is opened.

In this view, time itself doesn’t work the way we imagine. The theory of relativity
already confounds certain of our intuitions about time, such as a global par-
titioning of events into those that took place in the past, those that are taking
place now, and those that will (or may) take place in the future. According to
Einstein, the notions of past and future can only be defined locally, based on the
“light cone” of a point in spacetime, which represents the region that could have
affected it in the past and that it might influence in the future—really two cones,
their apexes converging on an infinitesimal present. Everything outside your
light cone is inaccessible, causally disconnected from you, hence neither part of

your past, present, or future.

---

In RQM, pasts and futures are even more local and relative, as they are contingent
on the particular network of prior interactions leading up to an event. Thus
RQM offers a new perspective on an especially bizarre variation of the two-slit
experiment proposed by physicist John Wheeler in 1978,“75l and confirmed
experimentally in 2007: the “delayed-choice” experiment.\+!! In this version,

an experimenter decides whether to measure which slit a particle went through
after it has already passed through the slits; yet the seemingly paradoxical result
remains: an interference pattern is observed only when no measurement takes
place. It’s as if the information about whether the experimenter will “ask” which
slit the particle went through somehow travels backward in time to determine
retroactively whether it behaved like a particle or a wave!

Yet all of this follows because the equations of quantum mechanics describe
interactions, not “things in themselves.” What we call a measurement is just an
interaction between A and B. We could say A is the experimenter, and B the object

---

being studied, but either way works. For A, B collapses; for B, A collapses. But for
C, which has not yet interacted with A or B, A and B are entangled in superposi-
tion.|28)

Subjectivity, then, exists even at the most fundamental level of description. You
can only know about something by interacting with it, and any uncertainty in-
herent in that interaction is real—for you. Between one interaction and the next,
that uncertainty grows. And the same applies reciprocally. Reality is continually
being locally and mutually constructed, interaction by interaction. We can’t ask
what “real” reality looks like, outside that network of interactions. As Rovelli
puts it: “If we imagine the totality of things, we are imagining being outside the
universe, looking at it from out there. But there is no ‘outside’ [...]. The externally
observed world does not exist; what exists are only internal perspectives on the
world which are partial and reflect one another. The world is this reciprocal re-

flection of perspectives.”

The same can be said of our psychological universe, because, like RQM, theory of

mind is purely relational. It involves one mind modeling another—and itself.

To reiterate: none of the above implies that theory of mind, consciousness, or any
mental process relies on quantum phenomena per se. However, physics is rele-
vant to our understanding of concepts like consciousness, agency, free will, and
souls because these concepts (and the difficulties we encounter in grappling with
them) have always been contingent on our folk understanding of the universe's

underlying rules.

Zombie-Free

In a dualist universe, physical laws govern ordinary matter, but spirit and the
self exist on a separate plane, presumably governed by other laws. Often, these
other laws are deemed divine or unknowable. Even so, Descartes struggled to an-
swer the hard questions raised by dualism: How could animals not have spirits,
too? How does one's spirit know what the organs of the body perceive? (And why
doesn’t the spirit have access to other bodies?) Even trickier, how does the spirit

control our body, and where is the physical locus of this control?

---

The conceptual and neuroanatomical absurdities encountered by pursuing this
line of thinking led the iconoclastic Enlightenment physician Julien Offray de

La Mettrie (1709-1751) to write L’Homme Machine (“man machine”) in 1747,
extending Descartes’s béte-machine (“animal-machine”) concept to humans and
suggesting that resorting to supernatural “other laws” to account for human cog-

nition or behavior was unnecessary.““4.

At the time, La Mettrie’s thesis was radical enough to compel him to publish his
tract anonymously, in a miniature format that could be secreted in an inner coat
pocket. The authorities burned many copies, and La Mettrie was forced to flee one

country after another, especially after he was outed.

Eventually, though, his perspective became mainstream. Today, thinkers like
Robert Sapolsky and Sam Harris articulate the same view, and both have written

bestsellers arguing the point.

In a fully deterministic Newtonian universe, everything is fated, time is
reversible, and there is no difference between cause and correlation. Blurriness
about the future or the unknown, or the existence of counterfactuals (how things
could be, as opposed to how they are), are illusory: nothing could be other than

it is, was, and will be. Without counterfactuals, blame or responsibility seem
difficult to justify, as Sapolsky points out. Consciousness and free will are at best
epiphenomena, meaning that they lack causal power—if they can be said to exist

at all.

This leads us to wonder about philosophical zombies: the same events and behav-
iors without those epiphenomena. People without souls. Why not? How would we

even know, and what would “knowing” even mean?

The quantum world—the one we actually inhabit—has very different rules, and
understanding these rules, as physically counterintuitive as they may be, helps to
resolve many of the apparent metaphysical—even spiritual—conundrums that

arise in a Newtonian universe:

@ The future is not predetermined after all, especially for living systems,

which are finely tuned to amplify noise through dynamical instability.

---

® Because life isn’t deterministic, counterfactuality—the idea that things
could or could have been otherwise—is not just an illusion.

@ Choice—though constrained by the blurry “future cone” of the physically
possible—is likewise real, and underwrites the free will of beings able to
model and select among alternative futures.

@ Our mental models of causality have real meaning and power, especially
when it comes to predicting how we and other living beings will behave—
yet we are also free to violate the expectations of others (if we choose to,
and have a good enough theory of mind to pull it off).

® We can never fully know the inner experience of others, but only model it
based on interactions.

® That said, subjective experience is also real; or, to turn it around, reality is

defined subjectively by networks of interactions.

Given all this, the idea of philosophical zombies seems incoherent. If you interact
with someone over an extended period such that your theory of mind models
them in detail, that model includes their model of you, and their model of your
model of them, and so on. If they don’t in fact have a working theory of mind of
their own, then your theory of mind will be violated in the interaction—and it
will become apparent to you that there’s “nobody home.” This really is just the

Turing Test.

One can, of course, be fooled by a social interaction; actors, for instance, can take
on a role in which they pretend to feel things they don’t, then drop the act, re-
sulting in a (possibly unpleasant) surprise. But let’s suppose that never happens.
Imagine an interaction between A and B, in which Bis different on the inside than
A imagines; B might, for instance, actually be B’, an actor who plays B and never
breaks role. Perhaps B’ is really a cold fish, and has never experienced heartbreak,
but can pretend to, pitch-perfectly. We could say, then, that A is “real,” Bis “fake,”
and B’ is the “real” B.

Here’s the problem. In this description of the situation, we have presumed some
God-like perspective that can observe every detail inside A and B, and render an
oracular judgment about the actor B’ “inside” B, But no such God-like, all-seeing,

all-judging perspective exists.

---

If we replace that third-person view with a real third person, C, we can spot the
trouble. Now, C must interact with both A and B to render judgment. This inter-
action could involve not only conversation, but also all sorts of lab tests, body
sensors, brain scans—the works. Even so, C can't consult any magic oracle to
distinguish between “real” and “fake” people, and is still just making a (more de-
tailed) model-based judgment. Theory of mind is that model.

Another judge, D, could come along, and on the basis of their own, somewhat
different model, or different interactions, or alternative instrumentation, dis-

agree with C. Whois right?

It's not that reality doesn’t exist, any more than ROM argues that the universe
doesn’t exist. The point is that reality consists of relationships, and there is no
specially privileged view, no magic oracle. Perhaps agreement becomes nearly
universal on certain kinds of judgments, especially when those judgments carry
strong predictive power. But a judgment may always remain contested, especially

when it concerns subjectivity itself.

Alters

“Dissociative identity disorder,” a controversial condition formerly known as
“multiple personality disorder,” offers a real-life example. People with dissocia-
tive identity disorder seem to have multiple other people living in their heads
—“alters,” with some combination of different personalities, different memories,
and even different-sounding voices. Encountering someone with this disorder
can be frightening, since it so dramatically violates our usual assumptions about
the indivisible unity of a person, their brain, and their “soul.” At times, it may

have been interpreted as demonic possession."

Is this condition real, or do people just fake it? If they are faking it, do they have
any choice in the matter? Could some people be unaware that they're faking it?
The psychiatric community can’t agree on any of these questions. Some believe
it’s an act, others believe it’s real, and yet others hedge their bets. I’m skeptical
that we will ever have anything like a universally convincing answer, because

I can’t imagine what shape such an answer could take, even in principle. It cer-

tainly won't take the form of a cloven pineal gland.

---

Imagine for a moment that, as neuroscience advances, it becomes possible to read
out a person's experiences and thoughts perfectly, using superconducting mag-
netometers, optogenetics, nanotechnology, or whatever else to record the activity
of every neuron in the brain.“““ That would, of course, produce a staggering
amount of data—impossible for any researcher to make sense of in raw form.
Even today’s instruments, which can easily record from hundreds of neurons, re-

quire sophisticated computational modeling for any meaningful interpretation.

How would a researcher train and test a model designed to provide total access
to a subject’s internal experience? An honest subject could give positive feedback
when the model correctly reconstructs what's in their minds and negative feed-
back when it’s wrong. Once trained, such a model could allow an experimenter
to map brain activity onto the description that subject would give—what they’re
seeing, hearing, touching, and tasting, what they’re feeling and thinking, and so
on485)

Once again, we're talking about a theory of mind. It might be an excellent one.
But ultimately, the model is just another “observer C.” Or, more accurately, the
model would provide a human experimenter C with a computational prosthetic,
a “theory of mind extender” with the ability to decode the rich brain signals in
the subject’s head that would otherwise remain hidden. That could make C a fear-

some interrogator, but it does not afford them a “view from nowhere.”

It’s unclear whether, even in principle, we could make a generic model that
would accurately read out anyone's mind, as opposed to the mind of a volunteer
for whom the model has been individually (and consensually) tuned. But I sus-
pect that even if we could travel forward in time (and into the right Black Mirror
episode) to grab such a generic theory of mind-extender gadget, then back in
time to experiment with it on various medieval saints who believed they had
witnessed miracles, we would find that some of them believed what they were
saying. Does that prove these miracles actually happened? And if they didn’t,

does it prove that the saints were mentally ill?

I don’t think we can reliably draw either of these conclusions. Virtually all of us
believe some things that many others don't, including the sincerely religious,

who comprise a large proportion of the human population, as well as committed

---

atheists. Yet few people in either camp would make the hyperbolic claim that ev-

eryone in the other camp is mentally ill.

When it comes to the truth or falsehood of alters, we're on shakier ground still.
Someone's sincerely held conviction that the Earth is flat is easily and indepen-
dently testable by anyone—and on the basis of air travel, the moon landing, and
much else, it’s as obviously false as a belief gets.“*" But a belief about subjective
experience isn’t testable by others in that way. It’s a model of a model, and if it’s
your model of your model (whether singular or plural), it's hard to see how a third

party’s contrary claim could invalidate that. It would just be another opinion.

Could one do any better in arriving at a deeper truth? I've described a “theory

of mind extender” trained with human subjects using supervised learning and
wielded by a human experimenter who must ultimately interpret the results.
Such scenarios are inherently limited by the human mind. So yes, one could, in
theory, do better. Imagine that the complete brain activity of billions of humans,
together with every detail of their environment and activity, were used to train
a gigantic unsupervised model, vastly more powerful than the human brain,
capable of “autocompleting” our every move. For such a model, all the subtlety
and complexity of the human mind might boil down to rote behavior plus some
irreducible randomness—a bit of deterministic Sphex wasp and a bit of flutter-
ing moth. Surely this model could afford us something more than “just another

opinion”!

Not really. It would not tell us whether alters are “real,” or, at least, not unless the
most cynical possible interpretation holds—that everyone who claims to have
alters is simply lying, knows it, and doesn’t bother keeping up the exhausting
act in private. (Few psychiatrists adopt this extreme view, as patients exhibiting
such behaviors are often deeply traumatized and exhibit signs of other mental
conditions.) In short, insofar as people believe things and are consistent in their
beliefs about themselves, such that those beliefs reliably inform their behaviors,

the most any model could ever tell us is just that.

Let’s now move on to territory that has been explored scientifically in rigorous

detail: the curious case of split-brain patients.

---

M-I-B

“[...] [T]he Washington freshmen came up with a mantra that their coxswain, George
Morry, chanted as they rowed. Morry shouted, “M-I-B, M-I-B, M-I-B!" over and over to
the rhythm of their stroke. The initialism stood for ‘mind in boat."241

Beginning in the mid-twentieth century, doctors began experimenting with
brain surgery as a medical treatment—including, at times, for such purported
“conditions” as being gay, or just failing to conform. Their approach was at best

cavalier, at worst abhorrent.

One of the few enduring interventions developed during this period was for

the treatment of epilepsy. During an epileptic seizure, violent electrical activity
spreads through the brain, often starting from one or more foci. Brain surgery
to cut out the diseased tissue where the electrical storms begin can be effective.
In the most intractable cases, though, a last-ditch solution is to cut through part
or all of the corpus callosum, the bridge of white matter connecting the left and
right hemispheres. This makes seizures less debilitating by preventing runaway
electrical activity from propagating between the hemispheres. Surprisingly,

the procedure often has little obvious effect on a person’s cognitive ability or

behavior.

On closer examination, though, the results are disconcerting.“*") After the
surgery, each hemisphere appears to have independent inputs, outputs, and even
thoughts. If different visual stimuli are shown to the left and right halves of the
visual field, then a verbal account from the patient will include only what was on
the right side; they appear oblivious to anything in the left visual field.“**! On the
other hand, if the patient is asked to report on their experience using their left
hand—by drawing, for instance—this hand can report the contents of the left vis-

ual field, but not the right.

---

Usually, there are enough ways in which the left and right hemispheres can stay
in sync that these inconsistencies don’t arise. The intrinsic coordination of eye
movements, for instance, generally ensures that the left and right visual fields
see the same world; the setup for split-brain vision experiments requires visual

fixation on crosshairs and careful projection of separate left and right images.

\ KEY | cHse /
7 \s fe

\o conconmessensnyebet poems
; 5

---

Creating these dissociations, though, makes it apparent that, in many ways, split-
brain patients have two minds. In one famous recorded experiment, a patient
plays “Twenty Questions” with himself to allow one half of his brain to figure
out what the other half is seeing.“"| There are even occasional reports of “hemi-
spheric rivalry” in a patient’s behavior. One hand might be buttoning up a shirt
while the other hand is busy unbuttoning it, in an apparent disagreement over a
wardrobe choice; or one arm might be hugging a spouse while the other pushes

him away.24 So, is a split-brain patient one person, or two?

First, let’s note that the split-brain findings may not be as surprising as they
seem, if we are indeed not so different from the octopus. Myelination has allowed
our neurons to consolidate more in our heads, but our brains nonetheless exhibit
extensive symmetry, not so unlike that of the octopus body. Cortical columns
appear to be repeated structures with highly local connectivity, like the nerve
ganglia surrounding each of an octopus’s suckers, and our cerebral hemispheres
are (nearly) bilaterally symmetric, like a pair of octopus arms. Communication
between the hemispheres is higher-bandwidth than between an octopus’s arms,

but it’s still limited to a narrow bridge, even in the intact human brain.

Neuroscience has also failed to locate a homunculus anywhere in the brain; there
doesn’t appear to be any single special spot where consciousness “lives.” Hence

it’s not so surprising that both hemispheres are conscious, contra Descartes.

And finally, we know that the hemispheres are innervated differently and
specialize in different functions. The visual field is divided in two by the optic
chiasm, a cross-shaped wiring complex that visual signals must pass through en
route to the left and right visual cortex at the rear of the brain, in their respective
hemispheres. We've known for a long time that the left hemisphere controls

and receives inputs from the right side of the body, while the right hemisphere
controls and receives input from the left side of the body. We've also long known
that, in most right-handed people, language is handled mainly by the left hemi-

sphere, and vice versa.

All of which is to say: if the left and right hemispheres can no longer commu-

nicate directly, then the lateralized neurons producing language can’t speak to

---

anything seen or experienced on the opposite side of the body. How could it be

otherwise?
Still, we could reasonably have hypothesized a few other outcomes:

1. The split-brain patients might never have woken up after surgery. If
consciousness in any form had required the continual communication
of specialized areas on both sides of the brain, then cutting those con-
nections could have left patients comatose or unresponsive.

2. The split-brain patients might have woken up with complete hemine-
glect and hemiplegia: consciousness of and ability to control only one
side of the body. This would imply that “you” live on only one side of
your brain, while the other is just a peripheral—a lateralized version of
the homunculus idea.

3. The split-brain patients might have been deeply cognitively disabled
when they woke up. This would have been the case if cognition were so
diffusely “holographic” that forming any clear thought or percept re-

quires every part of the brain to work in tandem.

Fortunately, for most of the patients, none of the above obtain. What we see
instead speaks to the modularity, robustness, parallelism, and “internal sociality”

of the cerebral cortex.

As I've argued, no part of the cortex is doing something fundamentally different
from any other part. Specialization arises mainly due to connectivity and some-
thing like the division of labor in a human society—that is, analogously with the
way we learn different skills and do different jobs, but are not fundamentally
different in our capacities. Local connectivity is “cheaper” than long-range con-
nectivity, so functionality is implemented as locally as possible—a design that
can be robust to failures in connectivity (as evidenced by split-brain patients) or
to regions of the cortex being knocked out, whether by injury, stroke, or some

more transient event.

Hence our cerebral hemispheres seem to be intelligences in their own right,

which are made of still more local intelligences, and so on. And of course, for

---

intelligences to work effectively with others, they must continually model each

other. It’s theories of mind, all the way down.

Perhaps the most revealing split-brain finding is not in how the abilities of the
patients are affected, but in their subjective experience. They need to work harder
at certain tasks than those of us with intact brains do, as revealed by Twenty
Questions-type scenarios that look suspiciously like two people helping each
other—or, even more frustratingly, hindering each other, such as when hands are
actively working against each other—rather than one person. It might, similarly,
be harder for a rowing crew to achieve swing if a barrier were suddenly erected
mid-boat, preventing the rowers in the front and the back from seeing or hearing
each other. They might even occasionally try to row in opposite directions. None-
theless, the left and right hemispheres of a split-brain patient are still obviously

in the same boat.

The result? Split-brain patients won't “admit” that there’s more than one person
in there. This is a particularly striking illustration of how the relational quality of
theory of mind violates our usual assumption that there's a single, objective truth
about “who is a who.” The patient still feels whole; there's just more trouble after
the surgery reaching for certain words, or performing certain tasks, especially

when one’s eyes or hands are prevented from working together “normally.”

However, to the experimenter, it seems evident that there are two minds in the
patient’s head. Indeed, to make sense of any interaction with a split-brain patient
in an experimental setting where left and right stimuli are dissociated, it’s neces-
sary to have distinct theories of mind for the left and right hemispheres—what
do they see and hear? Which hands do they control? What do they know? What
will they choose to do? To fail to take these things into account would be to flunk
the Sally-Anne Test. It's worth reflecting on the implications, even for those of us

with an intact corpus callosum.

When we say we're “of two minds” about something, could that literally be true?
It is a small miracle that we manage to make decisions and take coherent action
most of the time, despite being a tandem bike, or rowing crew, or maybe a whole

crowd, on the inside. Yet we learn such internal cooperation from birth. Unless

---

you learn how to doit asa party trick, it’s hard (without a split brain) to button

your shirt with one hand while simultaneously unbuttoning it with the other!

Still, we’re not by any means in eternal a priori agreement with ourselves—or
else that multiplicity would be redundant, and would therefore not exist, as a big
brain is a highly expensive adaptation. We only get more intelligent as the brain
scales up because every additional “local mind” brings its own skills, inputs, spe-

cializations, and, one could even say, differing opinions to the table.

Experimenters can easily engineer internal disagreements by presenting us with
forced-choice responses to conflicting stimuli that will be processed by different
parts of the cortex, The “Stroop effect” is a classic example, named after Amer-
ican psychologist John Ridley Stroop. In 1935, Stroop published a study testing
the reaction times of subjects on a simple color-recognition task. The name of

a color was printed on a card in colored ink. If the ink color conflicted with the
named color, for instance the word “red” was printed in green ink, both the error

rate and reaction time rose considerably.\“*4!

Despite the complexity of the brain, studies like these are consistent with a sim-
ple model of how we arrive at decisions: parallel populations of neurons “vote,”
with softmax-like lateral inhibition determining which ones “win.” A close
call leads to slower convergence. The fine balance of neural circuits once again
comes into play here: always close enough to firing that an eager “raised hand”
somewhere can quickly cascade into a decisive global response, yet not so overex-

citable that chaos and epilepsy ensue.

Although it’s a fine balance, room for functional variability remains. Are our neu-
ral parameters tuned for faster convergence on a decision, or for more thought-
fulness? Or for too much thoughtfulness, also known as waffling? (That’s me!) If
some cortical columns actively dissent, do they commit to a collective decision
anyway, or do they carry on grumbling? How much idle chatter do brain regions
generate when they’re not trying to drive behavior? Could they even attempt to

pursue their own agenda by “fooling” their neighbors at times?

These are interesting questions, and ones that may underlie certain systematic

personality differences between people. Carried to extremes, such differences

---

could become dysfunctions: lack of impulse control, decision paralysis, perhaps

even schizophrenia or dissociative identity disorder.

The Interpreter

One of the most telling split-brain findings is the way the language-specialized
(usually left) hemisphere assumes a role neuroscientist Michael Gazzaniga and
colleagues have dubbed “the interpreter.”“2*! It has sometimes been cited asa
counterargument to “the typical notion of free will,”““" but, more to the point,
the interpreter role reveals something important about how and why split-brain
patients tend to feel to themselves like one person, despite their (literal) cognitive

dissonance.

In one classic early study, a patient's left hemisphere was shown a chicken claw,
while the right hemisphere was shown a snow scene. The patient needed to select
associated objects with each hand, given four choices per side. As expected, each
hand chose an image associated with what its corresponding hemisphere could
see: for the left hand, a shovel (rather than a lawnmower, rake, or pickaxe), and

for the right hand, a chicken (rather than a toaster, apple, or hammer).

But now comes the twist. When asked why he had made those choices, the patient
responded without hesitation, “Oh, that’s simple. The chicken claw goes with the
chicken, and you need a shovel to clean out the chicken shed.” The language-im-

bued left brain appears to be, in other words, a fluent bullshitter.

In another example, the right hemisphere is given the instruction, “Take a walk.”
The subject stands up and begins walking. When asked why, the response might
be, “Oh, I need to get a drink.”24)

You may now be wondering: how could a split-brain patient manage to walk at
all, when that requires the coordinated activity of both legs? And how could such
a bilaterally coordinated action take place in response to a unilaterally willed

command?

In fact, split-brain patients perform coordinated activities all the time, including
tasks involving both hands. Some researchers have hypothesized elusive cross-

hemispheric nerve fibers somewhere other than the corpus callosum maintain-

---

ing some kind of minimal communication, but this has never been convincingly

shown, either behaviorally or neuroanatomically.“

It’s not necessary to reach for such an explanation, though. The whole body is
arich cross-hemispheric communication channel. Your eyes can see what your
arms and legs are doing. If one leg begins to exert pressure on the ground to stand
up, your butt can feel it. If the muscles on one side of your neck begin to tense

to turn your head, that tension is felt on the opposite side. And so on. As anyone
who has rowed crew or run a three-legged race knows, it’s possible to quickly pick
up cues and follow through on movements based purely on sensory feedback.
Gazzaniga and colleagues call this “behavioral cross-cueing”; it emphasizes the
importance of physical embodiment, the way our bodies are, in a sense, part of

our brains, as well as vice versa.

Conjoined twins Abby and Brittany Hensel vividly illustrate the phenomenon.
They have separate heads, brains, and spinal cords, but a single pair of arms

and legs, with Abby controlling one arm and leg and Brittany controlling the
other. Despite their virtually complete sensory and motor separation, the twins
are able to run, swim, play volleyball, play the piano, ride a bicycle, and drivea
car.4°"! when one of them initiates a movement, the other unconsciously and
effortlessly follows through. Not only can they complete each other’s sentences,
as close friends might be able to; they also share an email account, and have no
trouble typing email with both hands. While they maintain individual identities,
they use the “I” pronoun when they agree, as they often do, and use their names if

they disagree.

In this light, the left hemisphere’s effortlessly creative narrative “interpretation”
seems less like a special case (or like bullshit), than like what the cortex always
does: it predicts, and follows through. This involves constantly updating its the-
ory of mind, including a theory of mind for that omnipresent first-person entity
we call “I.” Such a theory-of-mind model includes simple, low-order terms to pre-
dict the immediate future, like “I’m walking, and just stepped with my left foot,
so my right foot is going to step next.” It also includes higher-order terms, like
“T've just gotten up to walk, and I’m a little thirsty, so I’m probably headed for the
kitchen to get a drink of water.”

---

If the bit of cortex doing the modeling happens to control my right foot, then its
“active inference” will involve moving that foot to “autocomplete” the walking
movement. In fact the spinal cord is perfectly capable of such low-order autocom-
pletion on its own.“ If, instead, the bit of cortex doing the modeling is the left
hemisphere’s language center and the experimenter has just asked why I’m leav-

ing the room, then autocompletion involves spinning a likely story.

Even with a corpus callosum, no part of the brain can have complete access to
every other part, so this kind of inference takes place all the time. Mutual model-

ing, including within the brain, is the very essence of intelligence.

Still, this kind of teamwork, in which our “inner selves” predict and cover for
each other, can lead to embarrassment. We're all highly invested in appearing
whole, unified, consistent, and “rational” in our social interactions with others.
Given the potentially adversarial nature of social prediction, we’re disconcerted
when someone else is able to predict us better than we can predict ourselves. Per
chapter 5, being too predictable makes us vulnerable, and feels like a violation.
It's even worse to believe that you've made a choice when you haven't, and then
to be caught out justifying that “choice” with a post-hoc rationale—a literal attack
on personal integrity.

Yet we’re ail vulnerable to such manipulation, as Swedish psychologist Petter Jo-
hansson and colleagues have demonstrated in a series of groundbreaking studies.
They first demonstrated the phenomenon they call “choice blindness” in a 2005
study entitled “Failure to Detect Mismatches between Intention and Outcome

in a Simple Decision Task.”“24! The task involved showing the subject two cards
with faces on them and asking which was more attractive. Immediately after
choosing, participants were sometimes shown their card again, and asked why
they had judged this face more attractive. However, unbeknownst to the subjects,
in three out of fifteen trials their choice was swapped using sleight of hand. The
participants were being asked to justify why they had made the choice they had

not just made.

---

Surprisingly few subjects noticed the swap. When they had been given two sec-

onds to make a judgment (which they generally affirmed was enough time), only
thirteen percent detected the ruse. Even under the friendliest possible experi-
mental conditions, when they were given unlimited time to judge, and the faces
were selected to be especially dissimilar, the figure only rose to twenty-seven
percent. Viewing time was the only condition that made any difference. The re-
spondent'’s age and sex didn’t matter. Neither did the similarity of the faces, even
though “[low-similarity] face pairs [...] bore very little resemblance to each other,

and it is hard to imagine how a choice between them could be confused.”

Perhaps most surprisingly, there was little or no statistically significant variation
between the justifications given for real or swapped choices. The researchers
certainly tried to find such differences. Using multiple human raters, they con-
sidered length of response, laughter, emotionality, specificity, the proportion of
blank responses (in which subjects couldn't say why they had made the choice),
and even whether they described their judgment in the past or present tense. The
only slight difference—maybe a telling one—was in “more dynamic self-com-
mentary” in the swapped instances, in which “participants come to reflect upon
their own choice (typically by questioning their own prior motives),” but only

five percent of respondents evinced this behavior.

---

As behavioral scientist Nick Chater has written in describing these experiments,
our left-brain “interpreter” can “argue either side of any case; it is like a helpful
lawyer, happy to defend your words or actions whatever they happen to be, ata

moment's notice,"222)

In the run-up to Sweden’s 2010 election, Johansson and colleagues tried applying
their choice blindness paradigm to politics.“ First, they asked participants
whether they intended to vote for the left-leaning or right-leaning coalition.
They then followed up with a questionnaire about respondents’ positions ona
series of wedge issues. As with the face-judgment task, the experimenters surrep-
titiously swapped some of the answers—enough to place subjects in the opposite

political camp.

When respondents were then asked to explain their manipulated responses, no
more than twenty-two percent detected the manipulations, and, once again,
justifications offered in defense of the swapped responses were just as articulate
as for the “real” ones. A full ninety-two percent of respondents accepted and
endorsed their altered surveys, and as many as forty-eight percent were subse-
quently willing to consider switching their allegiance from one coalition to the
other. This contrasted markedly with polling data, which had found only one in

ten Swedes identifying as potential swing voters.

Moreover, the effects of such interventions seem to stick. Even in the seemingly
trivial face-preference experiment, subjects whose responses were manipulated
showed an increased likelihood of expressing the altered preference later on. It

seems that once we've told ourselves (and others) a story, we try to stick with it.

Chater takes an understandably jaundiced view of these results, as one can tell
just from the title of his 2018 book, The Mind Is Flat: The Remarkable Shallowness
of the Improvising Brain: “[W]e don't justify our behaviour by consulting our men-
tal archives; rather, the process of explaining our thoughts, behavior, and actions
is a process of creation. And [...] the process of creation is so rapid and fluent that
we can easily imagine that we are reporting from our inner mental depths. [...] So
our values and beliefs are by no means as stable as we imagine. The story-spin-
ning interpreter [...] attempts to build a compelling narrative [...] by referring back

to, and transforming, memories of past behavior [...]."“24

---

It’s not unreasonable to think the “interpreter” findings unmask our “illusion” of
having a stable inner self. However, I think it's equally valid to see these results as
a peek into what it means to have a self at all, and how that selfis constantly being
constructed and revised. After all, we aren't born with predetermined personal-
ities, preferences, habits, or political allegiances. These things must accrue over
time. We are the story we tell ourselves. And this story isn’t immutable—which is
a good thing. That's what learning is for, and, paradoxically, if we were not able to
narrate and re-narrate our lives, our preferences, our choices, and ourselves, our

claim to free will would be considerably weaker.

However, this continual process of narrative self-definition may be vulnerable

to manipulation precisely because, as far as we know, no single spot in our brain
contains our political-preference database, personality module, or attractive face-
o-meter. Rather, every part of the brain may be trying to model and learn about
the other parts, and thereby to agree on—and constantly renegotiate—a “self.”

Multifractal Boundaries

Suppose some neuron in the brain receives a signal. Does it come from elsewhere
in the brain? From some other part of the body? From out there in the world?
There is no obvious way to tell. Hence the “self” has a porous boundary. This
comes in handy when using a tool, driving a car, or playing a video game—all
circumstances in which our sense of our own bodies shifts or expands to include

objects, vehicles, or even virtual worlds.22%)

This porosity is vividly illustrated by the “rubber-hand illusion,” in which a
rubber hand visible above a table is stroked with a paintbrush in tandem witha
subject’s real hand, hidden behind a partition.“ If you happen to have a lifelike
rubber hand lying around, you can try this on a friend. Before long, they will have
the strong impression that the rubber hand is theirs. (If you're feeling mean, you
can then try sticking a knife into it.) Here, correlated visual and haptic signals
from different parts of the brain appear to be, from the perspective of both of
these regions, accurate mutual predictions. That's enough to temporarily remap

one’s physical sense of self.

---

As the political experiments of Johansson and colleagues show, the manipula-
tions of others can also influence the narrative self. In this sense, the rubber-
hand illusion and the interpreter can be understood as instances of the same

phenomenon.

One's self can even temporarily merge with other selves to one degree or another,
whether in a chamber orchestra, a three-legged race, a ritual dance, team sports,
choral singing, or a political rally. One could argue that this even happens in
conversation. Such porosity may be a key ingredient enabling human society

to achieve large-scale collective intelligence, without which we would be little

different from our primate cousins.

Split-brain results, the “interpreter,” choice blindness, the rubber-hand illusion,
and many other counterintuitive consciousness-related findings ““” make sense

in light of the hypotheses about intelligence I have advanced so far:

@ Intelligence is predictive. It amounts to a kind of “autocomplete”
operation: given a history of observations, actions, and consequences, both
internal and external, it predicts the likeliest next action. Intelligence en-
hances its own dynamic stability by successfully predicting (hence bring-
ing about) its own future existence; that’s why it arose in the first place, per

chapter 2, and why it continues to evolve.

---

e Intelligence is social. Per chapters 3 and 4, much of an intelligent agent’s
umweit of observations and actions consists of other intelligent agents,
which are themselves predictors. Thus, per chapters 5 and 6 (this one),
theory of mind emerges, and, under suitable conditions, it can result in so-
cial-intelligence explosions.!2°*! Applied to oneself, higher-order theory of
mind implies self-consciousness (social modeling of the “self”), the ability
to reason about counterfactuals, and the capacity for long-range planning.
There is no God’s-eye “view from above” of intelligence; “selves” are always
modeled, and there is always a modeler—which can either be another or
the same “self.”

@ Intelligence is multifractal. Intelligences are made of smaller intelligences,
and are defined by the predictive relationships among those smaller
intelligences. These dynamically constituted interrelationships—not a
homunculus—define a “self.” “Selves” composed of larger populations of
mutual predictors form larger social units, which can themselves be more
intelligent as a result.

e Intelligence is diverse. For a “self” to be greater than its parts, the parts
need to diversify and specialize. That is, even as the intelligent parts strive
to predict each other, they must differ in their predictions; otherwise they
would not provide each other, or the whole, any benefit. Specialization
arises naturally from differences in connectivity—that is, because each
smaller intelligence receives different inputs and generates different out-
puts, both internal and external. Finally, it follows that—

@ Intelligence is symbiotic. When the dynamic stabilities of multiple intel-
ligences become correlated, they find themselves “in the same boat,” and
they will learn how to row together to further enhance their joint stability.
This is the route to symbiogenesis, as described in chapter 1: the emer-

gence of new, larger intelligences from the cooperation of smaller ones.

Pulling all of these aspects of intelligence together into a concise definition is

tricky, but here's my best effort so far:

Intelligence is the ability to model, predict, and influence one’s future; it
can evolve in relation to other intelligences to create a larger symbiotic

intelligence.

---

To highlight the duality between intelligence and life, it’s helpful to read this
alongside the definition of life I offered in chapter 1:

Life is self-modifying computronium arising from selection for dynamic
stability; it evolves through the symbiotic composition of simpler dynami-
cally stable entities.

---

# Chapter 7

7. Ourselves

Block Diagram

In an old-fashioned, block-diagram view of the brain, the blocks around the out-
side might have labels like “visual cortex,” “auditory cortex,” “motor cortex,” and
so on. Implicitly, these are presumed to work like the peripherals of a computer,
carrying out specialized processing to deal with their particular modality. (Ro-

bots, too, are usually built this way.)

Neural signals would presumably flow in the obvious direction: inward for sen-
sory modalities, outward for motor. Convolutional neural nets, whose design was
directly inspired by visual cortex, seem in keeping with this view. They are fully
feedforward, meaning their connectivity flows one way, from a “retinal” input

layer to semantically meaningful output in an embedding layer.

Those semantic embeddings, in turn, seem like the right kind of input to... what?
Something needs to go in the middle, taking in the processed sensory input, mak-
ing decisions, and generating high-level motor commands; we might as well call
this the Central Processing Unit, though the usual innocuous label is something
like “association cortex.” It’s hard to look at that block on the diagram and not
think “homunculus.” For surely, that’s where “you” live. A perceptron, which
merely turns pixels into embeddings, does not seem like a promising spot in the

diagram for locating anything akin to a “self.”

However, as the motor-first perspective laid out in chapter 4 implies, almost
everything about this block diagram and its information-processing paradigm
may be wrong. For one, I've argued that there isno homunculus. If there were,
unplugging it would surely turn the lights out. Instead, when a good portion of
the non-sensory-specific “association cortex” in the frontal lobes is destroyed
or disconnected from the rest of the brain—as happened to many victims of the
mid-twentieth-century lobotomy craze—the effects can be disconcertingly sub-

tle, just as with split-brain patients.

---

Emphasis is warranted on can be. The details of the procedure, and the nature and
extent of the ensuing damage to the brain, varied considerably. Some victims of
this brutal medical fad were killed outright by massive cerebral hemorrhage, or
rendered profoundly disabled. After her lobotomy in 1941, for instance, Rose-
mary Kennedy, President John F. Kennedy’s sister, was left unable to walk, speak
intelligibly, or use the bathroom; she required constant care throughout the rest
of her life.

Nonetheless, in 1942, star neurosurgeons Walter Freeman and James Watts
claimed that, of the two hundred lobotomies they had performed to that point,
sixty-three percent were “improved,” twenty-three percent were “unchanged,”
and only fourteen percent were “worse.”"°! Rosemary Kennedy was one of those
two hundred, and was presumably counted among the “worse.” While we must
meet with skepticism any assessment of what constituted an “improvement,” fig-
ures like these do make it clear that most lobotomized patients didn’t end up like

her. What, then, wondered Freeman and Watts, were the frontal lobes even for?

“Neurologic manifestations are surprisingly slight following prefrontal lobot-
omy, and the old concepts of the frontal lobes as concerned with the higher inte-
gration of movements have had to be revised. [...] The psychiatrist must think out
these problems and determine for himself what contribution the frontal lobes

make to normal social existence [...]."12%

Another puzzle: as described in chapter 5, cortex is highly modular. In particular,
while subtle differences exist between sensory and motor cortex, their structure
and wiring are surprisingly similar. Both are dominated by recurrent connec-

tions, or feedback—shades of Wiener’s cybernetics.

That seems especially odd for sensory areas. Perceptrons are entirely feed-
forward, and they do seem to capture something of what is going on in visual cor-
tex. The “receptive fields” of units early in a convolutional net (that is, the visual
patterns to which these model neurons are most sensitive) look uncannily like
the receptive fields of real neurons early in the visual system. The sparse, seman-
tically meaningful embeddings in the final layers of perceptrons also resemble

the activation patterns recorded from higher-level visual neurons.!

---

Observations like these have led to debates between neuroscientists and AI
researchers. Some (especially on the AI side) emphasize the functional similari-
ties between brains and deep learning. Neuroscientists, at times irritated by the

looseness of these parallels, point out the inconsistencies, including:

@ Real neurons communicate with spiking action potentials, not the continu-
ous values of artificial neural nets.

@ Neurons and synapses are vastly more complex than their cartoonish deep-
learning versions.

@ The backpropagation algorithm used to train perceptrons isn’t biologically
plausible 244)

®@ Deep learning, true to its name, often relies on dozens or even hundreds
of layers, while the brain only has a few layers. Brains would be useless
if visual stimuli needed to pass through so many cortical layers, because
neurons and synapses are so slow relative to computers; in real life, there's
often only time for sensory input to propagate through a few synapses
before it must become a motor output, driving a behavioral response. And,
of course,

@ Visual cortex, like all cortex, is dominated by feedback connections, while

perceptrons are entirely feed-forward.

The arguments have gone back and forth. Some of the objections raised by neuro-
scientists are easy to counter. For instance, the universal function-approximation
theorems mentioned in chapter 3 prove that, in principle, networks of complex
spiking neurons can be approximated by (larger) networks of highly simplified
model neurons. Researchers have also come up with versions of backpropagation
and related learning rules that are more biologically plausible, and, while we
don’t yet fully understand the neuroscience, there is evidence of such learning

rules in the brain, 22)

In 2018, machine learning researchers found that convolutional neural nets
could reliably be fooled into making bizarre misclassifications using “adversarial
stimuli,” which many at the time considered conclusive evidence that deep learn-

ing wasn't anything like biological vision.“+“ But countervailing findings in 2022

---

showed that the primate visual system could be fooled in just the same way, and

to the same degree!=!"' So, the debate continues.

Clearly, the shallowness of visual cortex and its highly recurrent connectivity
an’t be finessed—in these respects, the brain is self-evidently not like a convo-
lutional neural net (CNN). Structurally, visual cortex—in fact, all cortex—looks

more like a “recurrent neural network” (RNN).

Recurrence

As the name implies, recurrent neural networks have both forward and back-
ward connections. More formally, this means that neurons take inputs not only
from other neurons in space (i.e., a previous layer) but also in time. That is, the
output of a neuron at time step t becomes an input for neurons at time step ¢+1;

weights associated with these inputs define the recurrent part of the network's

connectivity.
@ cs
Tw z a - a -
Tu a a

@ @ ©

Keep in mind that feedforward artificial neural networks are, by definition,

both timeless and memoryless. When they evaluate an input, they do so in-
dependently of any other input; no time variable is involved. By introducing
time, RNNs extend neural computation into the dynamical realm. That’s more re-
alistic, as any physical system (including the brain) unfolds over time. The input
weight associating each neuron with its own activation in the previous time step
implements a memory mechanism in its simplest form: a degree of persistence in

neural activity.

Recurrent networks are generalizations of feedforward networks, in the sense
that any feedforward net, like a CNN, can be implemented as a recurrent net. To

see how, imagine replacing the CNN's “spatial” feedforward connections with

---

equivalent feedback connections. A CNN with one hundred layers would turn

into an equivalent RNN that runs in one hundred time steps.

Seen this way, the high proportion of recurrent connections in visual cortex
might seem less surprising; those recurrent circuits could be implementing
something like deep learning, but doing so in time rather than in space. In fact,
since every kind of sequential neural processing must happen over time, the sim-
ple remapping envisioned here amounts to little more than notational sleight of
hand.

But what about reaction time? It would hardly be a good idea for you, as, say, a
highly visual prey animal, to experience the world a hundred time steps in the
past.+*) At t=0, a tiger might just be coming into view through the bushes. At
t=8, it might have caught sight of you. At t=16, it might be tensing to pounce. By
t=80, you might already be getting eaten, so there will be no t=100!

No problem. Even when deep convolutional nets are optimized purely for accu-
racy, researchers have found it beneficial to add “skip connections” to the stan-
dard sequential information flow, allowing some activations to bypass layers!“
Moreover, while making a feedforward architecture deep is a way of improving
task performance, “early exits” can be used if the extra accuracy is unneeded—or

if reaction time matters.

After just a few CNN layers, or RNN time steps, the network can make a reason-
able guess as to whether a cat is in the picture. Since the network's accuracy isn’t
great at this point, it can be tuned to prefer false positives over false negatives and
immediately escalate the timely alert. That is indeed how we operate for highly
salient stimuli; hence, the double take. (What's that, a cat?)

A few more layers, or time steps, can accurately establish whether the cat in
question is of the small Felis domesticus kind or the potentially man-eating Pan-
thera tigris. (Whew! It's just a house cat.) It may take dozens of further layers, or
time steps, to pinpoint the breed, guess the color of the eyes, establish its mood
and likely state of mind; but in the recurrent setting, this is where we would say

“upon closer examination....” Recurrent nets, then, can implement both rapid

---

responses and the many-layered precision of CNNs, operating dynamically rather

than as static functions.

This dynamic aspect is the heart of the matter. The visual world is not a suc-
cession of uncorrelated still images, and the visual cortex is not an abstract,
timeless mathematical function. In a continuously changing and temporally cor-
related world, where one's actions (including perceptual actions, like saccades)
determine what one sees, highly recurrent architectures are to be expected and

classification is better thought of as continual prediction.

Evaluating a CNN-like function from scratch for every visual frame would be
madness; for one, it would be computationally wasteful, since, most of the time,
each frame is nearly the same as the previous one. Worse, independent frame-
by-frame processing would be incapable of reconstructing the visual world as it
actually is. Building and maintaining the “controlled hallucination” described in
chapter 4 requires integrating information over many frames. And that means
memory. It is, almost by definition, a job for a recurrent network with persistent

state.

Imagine how the visual system of a Portia spider might work. Owing to the very
narrow field of view of the spider’s high-resolution front-facing eyes, a frame-
by-frame CNN would be nearly useless; for Portia, understanding a visual scene
requires moving the eyes around dynamically and reconstructing a model of the
world over time—not unlike the way a blind person can “see” someone's face by
touch, using their fingertips, though in Portia’s case, it would be more like a single
fingertip. Large predators like birds, frogs, and mantises are the bane of Portia spi-

ders, seemingly because they are too big to recognize in time!=!")

Humans can see more at once than Portia, but not nearly as much as we believe. If
we were to experience our visual input feed in a rawer, less “hallucinated” form,
it would look something like the shaky, grainy found footage of a horror film like
The Blair Witch Project, with a flashlight beam jumping around spasmodically

to illuminate a tree branch here, a bit of a face over there, the corner of a wood-
shed, a dark something on the ground. That horror trope will give you perceptual
claustrophobia, a sense that no matter where you look, the stuff you really need

to know about is happening offscreen—to one side, or above, or behind your back.

---

Like Portia being hunted by a giant mantis, we would wish we could zoom way

out and see what the hell is going on!

If you don’t normally feel that Blair Witch sensation of near-constant panic—
and dear reader, I hope you don’t—it’s not because you can see so much more at
a time. It’s because your controlled hallucination is good enough to make you
feel that you do see everything happening “offscreen,” although you can’t. That
is, you have confidence that your continually updated prediction is accurately
modeling every behaviorally relevant feature of your environment, well beyond

the narrow cone of that jittery foveal flashlight beam.

Efference Copy

Prediction underlies intelligence at every scale. Per chapter 2, single cells like
bacteria must predict sequences of events, both internal and external, to survive.
Emerging evidence suggests that it’s also what single neurons do; their synaptic

learning rules appear to give rise to local sequence prediction. 222!

Cortical circuitry, too, appears to implement predictive sequence modeling.“
This may account for the highly recurrent architecture of cortex, whether in
perceptual, motor, or so-called “association” areas: since sequences unfold over
time, any sequence predictor must also operate in time, which requires feedback

connections.

In visual (and other perceptual) areas, sequence prediction will also involve
recognizing hierarchies of increasingly invariant features, like those of a feed-
forward CNN trained using the masked-autoencoder approach. This is because
invariant features can be thought of as predictions. If you recognize that you're
looking at a banana, for instance, you can predict that it will remain a banana in
the future, even if it rotates, you move closer or farther from it, or you look away

and then look back at it.

Now, consider what happens when multiple brain areas are connected, entangled
in mutual prediction. Actually, we already have. Several brain areas are involved

in eye movement,2" but let’s ignore the anatomical details and pretend a single

---

“eye motor region” sends signals to the small, fast-acting muscles that aim the

eyes,

First, consider the motor region in isolation. To carry out its own predictive
processing, it will need to learn the basics of controlling eye movement: how to
send signals to the muscles that result in predictable responses by the stretch
receptors in those muscles. Three angular variables define each eye's position, but
six muscles control the movement, and many individual nerve fibers innervate
each one. Our developmental programming ensures basic routing, such that
relevant sensory and motor signals wire up to neurons in the right general areas.
Still, learning oculomotor control is not trivial. When the sensorimotor loop isn't
perfectly tuned, the results may manifest as “lazy eye” or the oscillating pattern
known as “nystagmus.” Wiener would recognize these as symptoms of excessive

or insufficient negative feedback; the latter is akin to intention tremor.

Meanwhile, the visual cortex will try to predict what imagery the retinas will see
at any given time. In the service of that prediction, it will reconstruct an entire
three-dimensional world. This seems so much loftier than what the eye motor re-
gion purportedly does that we might now be tempted to return to the homuncu-
lar fallacy, but with the shoe on the other foot: imagining that the visual cortex is
the “boss” or “central processing unit” that orders the eye motor region around,

telling it where to look next, treating it as a mere “peripheral.”

But the shoes are, so to speak, on both feet. The eye motor region can and does
move the eyes around of its own accord, perhaps in response to a vestibular
input, a sound, a touch, or something else. It could even do so in response to noth-
ing. After all, we decide to do things all the time for reasons of our own, that is,
not as immediate responses to an outside stimulus. Remember that, in a distrib-
uted picture of self, these decisions could be initiated by nearly any brain region.

All of your brain regions are “you.”

Communication between the visual cortex and the eye motor region, then, does
not merely consist of a one-way stream of gaze coordinates sent from one region
to the other. It’s a two-way dialogue, communicating (in compressed form) the

most useful aspects of the state of each region to the other.

---

By most useful, I mean most helpful in predicting the future for the receiving
region. In general, rather than imagining region A sending “commands” to re-
gion B, imagine region B containing “sensory” neurons in region A, with the goal
of finding the most salient information for making its own predictions. Visual
cortex, then, will want to learn from the eye motor region about eye movements
when they occur, because that will help predict what the visual cortex “expects”
to see next. The eye motor region, in turn, will want to learn from visual cortex
where the most interesting spots in the environment are, because knowing those
will help predict where the eyes will next look. The regions are cooperating to bet-
ter predict themselves, and in the process, better predict each other. Yes, it sounds

more than a bit like theory of mind—but carried out between brain regions!

This picture makes a counterintuitive experimental prediction: that signals
specifying movement will actually be sent from motor regions to other parts of
the brain, rather than vice versa. And that is indeed the case: it’s called the “effer-

ence copy.”

In the mid-nineteenth century, pioneering German physicist and proto-neurosci-
entist Hermann von Helmholtz first suggested that something like the efference
copy must exist. He noticed that if you cover one eye, then press gently on the
other eyeball (but do this through the lid please, and gently—don’t hurt yourself
and then blame me) you will see the world appear to move. This is interesting,
because when you move your eyeball the usual way, the world seems to stay rock
steady, although the images your eyes see are anything but steady. The visual
system must therefore do something like self-motion cancellation, and this must
make use of an extremely accurate real-time eye movement signal—the efference
copy. Helmholtz reasoned that when you press your eyeball, there is no efference
copy from the eye muscles corresponding to that displacement, so the visual sys-

tem’s usual “motion cancellation” doesn’t compensate for it.

Helmholtz was right, but in 1900, Sir Charles Sherrington, an enormously
influential neuroscientist who later won the Nobel Prize, cast doubt on the effer-
ence copy idea, causing it to languish for decades.224) Having spent a significant
part of his career exploring spinal cord reflexes, the sensorimotor pathways Sher-

rington had mapped out didn’t seem to involve anything like an efference copy,

---

just stimulus, response, and feedback from stretch receptors in the muscles.!222)
Later in the twentieth century, though, as neural recording technology improved,
numerous studies found that efference copies are real and ubiquitous—not just

for eye movements, but for all motor activity, and across species,“24

But why is it called a “copy”? Perhaps because the homuncular fallacy dies hard;
we persist in imagining that motor regions are sent movement “commands”
from on high, and then (somewhat bafflingly) send a carbon copy of these “com-
mands” back to the sender—presumably, the “you” part. In reality, your motor
regions are as much “you” as any other part of your brain, and while signals
traveling to the motor regions surely carry information about future movement,
thinking of them as “commands” and of signals going the other way as “copies” of

those commands misses the point.

In the case of eye movement, the mistake may be easy to make because the eyes
do generally look at whatever is most interesting, but that neither makes the
motor region subservient to the visual cortex nor alters the fact that the motor

region and the visual cortex are both doing the same thing: prediction.

Phenomenality

In case you're not yet convinced that the brain serves the muscles at least as
much as the other way round, consider the meaning of “behaviorally relevant,”
the term I've used to describe what is in our umwelt, that is, what we perceive and
what we care about. Behaviorally relevant means relevant to the muscles! If we
can’t act on it, it doesn’t matter. And for creatures like us, just as for early bilateri-

ans like Acoela, all action is muscular.

To be sure, a long evolutionary road leads from worms to humans ... but it’s a
continuous road. Our bodies are still, to no small degree, autonomous entities,
surprisingly independent of our more recently evolved brains. Remember, if kept
alive, our hearts will keep beating even if removed from our bodies, as Indiana
Jones found out in the Temple of Doom. Like an inner worm, our gut continues to
work under largely local control, with a decentralized “autonomic” nervous sys-

tem serving the original functions of long-range muscular coordination.

---

Our blood vessels, too, are made of muscle, and regulate the flow of nutrients to
every region of the body. To put it bluntly, they decide who gets to eat, and when.
Because the brain is so voraciously energy-hungry, regulation there is especially
fine-grained, with individual capillaries feeding less than a cubic millimeter

of brain tissue dilating and contracting from second to second. This differen-
tial flow of oxygenated blood is the signal measured by functional magnetic
resonance imaging (fMRI), one of our most important tools for mapping brain

activity.

The brain, in turn, consists of multiple systems layered atop each other, repeating
the same broad functional pattern: newer or “higher” levels provide behaviorally
relevant long-range prediction and thereby pull enough weight to earn their

keep, but augment a largely autonomous underlying architecture.

Hydrancephaly—a rare disorder in which babies are born without any cerebral
cortex—offers surprising insight into how much human behavior is indepen-
dent of these “higher” brain areas: “These children are not only awake and often
alert, but show responsiveness to their surroundings in the form of emotional or
orienting reactions to environmental events [...], most readily to sounds, but also
to salient visual stimuli [...]. They express pleasure by smiling and laughter, and
aversion by ‘fussing,’ arching of the back, and crying [...], their faces being ani-
mated by these emotional states. A familiar adult can employ this responsiveness
to build up play sequences [...] progressing from smiling, through giggling, to
laughter and great excitement on the part of the child.""2)

---

This quotation is from a paper arguing that consciousness may be possible with-

out a cerebral cortex—which certainly opens a can of worms for philosophers
committed to the (anthropocentric) view that consciousness requires a big brain.
We can most easily recognize what smiling, laughter, and fussing look like ina
fellow human, but I have little doubt that consciousness in this purely experien-

tial sense is far from unique to our species.

Consciousness in the more computationally demanding “strange loop” sense
described in chapter 6 involves the ability to model oneself recursively, which

goes well beyond the ability to experience in-the-moment percepts and feelings.

---

It’s what gives us higher-order theory of mind, self-reflection, the capacity for
free will and informed choice, planning, and (insofar as we can be said to possess
it) “rationality.” All of that may well require cerebral cortex, or its functional

equivalent.

The two senses of “consciousness” described above require us to revisit that old
bugbear, the philosophical zombie, once more. Remember that “strange loop”
consciousness gives us evolutionary advantages, both individually and socially.
It allows us to plan better, understand others better, teach and learn, divide labor,
and much else. All of these advantages manifest behaviorally; otherwise, they
could not have affected our odds of survival, hence there wouldn’t have been any

evolutionary pressure for the underlying capability to evolve.

Because “strange loop” consciousness manifests itself behaviorally, it can be
probed experimentally—for instance, with the Sally-Anne Test. Versions of the
test could also be devised based on time travel and counterfactuals rather than
third parties—requiring that you be able to model what you would and wouldn't
know or do under various hypothetical circumstances. Being able to model your-
self and others is, in other words, a skill, first and foremost. It’s obvious why, as

social animals, we have evolved it.

But what about the ineffable, experiential aspect of consciousness, or what
philosophers like to call “phenomenal consciousness"? Is that really just the
simpler kind of experience (including of pain, hunger, and so on) that all living
things appear to have, and for good reason, as described in chapter 2? Is it some-
thing beyond those primal feelings, requiring higher-order modeling? If so, could
the skill of modeling yourself (and others) be present without the actual feeling of

being a self?

What leads some philosophers to wonder about zombiehood is the sense that
each of us has a feeling of what it’s like to be us. That feeling is wholly inaccessible
from the outside, needn’t manifest behaviorally, and therefore can't be tested by

any means.

Locked-in syndrome, in which brain damage causes near-total or total paralysis,

offers a horrifying illustration of how consciousness and behavior can be de-

---

coupled.2°! Locked-in people are fully aware, but if their paralysis is total (and
absent brain-recording technologies) they can’t communicate or behave volun-
tarily in any way. A philosophical zombie would be the opposite: communicative
behavior would be present and convincing, but there would be no awareness on

the inside—and no way for us, on the outside, to tell.

Knowing whether someone is locked-in or mentally absent obviously matters
when it comes to our behavior. During major surgery, for instance, we presume
that general anesthetic causes a patient's consciousness to switch off; so if the
surgeon wants to listen to “Comfortably Numb” while operating, there's no need
to check in advance whether the patient is into Pink Floyd. On the other hand,
playing the song on repeat in a room with a locked-in patient who hates Pink

Floyd would be torture.

Our understanding of whether and when someone is “there” has changed over
time. It used to be commonplace to circumcise baby boys without anesthesia,
under the theory that newborns can't experience pain. Most of us today regard
this as barbaric, but the truth is that no adult has firsthand knowledge of what
newborns can and can’t experience, because we can’t remember anything that far
back.

Clearly, if we believe philosophical zombiehood exists, that, too, would be
behaviorally relevant for us, because it would imply a different standard of care.
Nicholas Humphrey is of the opinion that phenomenal consciousness actually
requires a model of oneself, so, for him, the obvious signs of happiness or dis-
comfort evinced by hydrancephalic babies amount to a kind of zombiehood. This
seems reminiscent of Descartes's beliefs about animals, though, in Humphrey’s
view, the line isn’t between humans and everything else, but between the warm-
blooded social animals—birds and mammals—and the rest. I guess he would say

that your pet gerbil has a soul, but your pet iguana doesn’t.

This distinction may have some validity. For instance, in the plight of people with
terminal illnesses, or inmates of concentration camps, we distinguish between
pain and suffering. Pain is comparatively easy to understand, though hard to
articulate; it’s what we’re referring to when we say something hurts, and mean it

literally.224 suffering, on the other hand, includes the awfulness of anticipating

---

future pain, or dire social consequences, or experiencing shame, or loss. It can be
accompanied by pain, and deepen it—for instance, knowing that a sharp sting-
ing sensation in your eyes after an industrial accident could presage permanent
blindness. Or it could be unaccompanied by physical pain, as in reading a mes-

sage that a loved one has died.

These higher-order experiences clearly require varying forms and degrees of self-
modeling, time travel, counterfactual analysis, and theory of other minds. It’s
even possible for such high-order processing to override the primary experience
of pain, as when it is sexualized for people who are into BDSM, or when we're

being stoic, or eating spicy food, or squeezing a zit.

Still, while it’s meaningful to draw a distinction between pain and suffering, I
find it far from obvious that such a distinction is either sharp or binary. Remem-
ber, back in chapter 2, the construction worker with the nail through his boot, in
agony despite being unharmed, in contrast with the man who walked around for
a week oblivious to the four-inch nail penetrating his brain. Or, think about how

grief can feel like physical pain.

In the 1970s, animal behaviorist and autism advocate Temple Grandin began
redesigning cattle slaughter facilities to minimize the suffering of livestock, bas-
ing her designs both on intuition (that is, on highly sensitive theory of mind) and
on quantitative measurement of stress behaviors.“2% Cattle are mammals, not so
different from humans, so Humphrey, Grandin, and probably most of us today
would acknowledge that they can experience both pain and at least some degree
of suffering. However, we also know that they aren’t capable of as high-order a

theory of mind, or as sophisticated a world model, as humans.

Hence, when animal-rights advocates compare cattle facilities to concentration
camps, they are only partly right; the analogy is anthropomorphic. Indeed, for
Grandin to effectively exercise compassion in her designs requires transcending
that anthropomorphism to model something closer to the cow's real experiential
and self-reflective umwelt, rather than thinking about her as one would a human
inmate. The cow's suffering may be intense if she can hear and see another cow
in pain, but she is probably not so bothered by an existential dread that each day

may be her last.

---

I’m less confident that we can accurately assess an iguana’s inner life. It’s a safe
bet that it has significantly less modeling capacity than a cow, but it seems a
stretch to claim, as Humphrey does, that it has no model of itself. Iguanas hunt,
mate, and sometimes fight with other iguanas over territory, resources, or mates.
An adult male will regard other adult males aggressively, but not females or

juveniles.

We may aver that these behaviors are “instinctive,” but it doesn’t seem relevant
whether the neural circuitry in question is learned during the animal's lifetime or
encoded genetically (that is, learned by evolution). The point is that mentalizing,
whether learned or instinctive, arises precisely to support such behaviors. So
while I doubt an iguana thinks much about next week, or wonders whether that
food stuck on his chin ruins his looks, it seems odd to me to claim that he can't
experience pain, or hunger, or a sinking feeling when his social standing is im-

periled by an interloper.

Blindsight

It may seem puzzling for Humphrey to deny that iguanas have such experiences
(or any experiences), given his founding role in formulating the social intelli-
gence hypothesis. Why does he take such an exclusionary view? As it happens,
his reasoning has much to do with another of his claims to fame: the discovery,

early in his career, of “blindsight.”=2"

Humphrey began his PhD research in Lawrence Weiskrantz’s lab at Cambridge in
1964. Like Hubel and Wiesel across the Atlantic, Weiskrantz was studying vision.
He had devised a particularly drastic surgery, involving the total removal ofa
monkey’s visual cortex, to confirm the seemingly obvious: that a monkey with-
out a visual cortex would be totally blind.

Initially, that appeared to be the case. Partway into the PhD, while Weiskrantz
was away at a conference, Humphrey began working with Helen, a macaque
monkey whose visual cortex had been removed a year and a half earlier.
Throughout that long period, Helen had shown no signs of being able to see, be-
yond a rudimentary ability to distinguish light from dark—as if each retina had
been reduced to a single giant pixel or “light bucket.”

---

However, Humphrey had reason to wonder if this was the whole story. As it
turns out, a much older visual pathway, also present in fish and frogs (which lack
cortex), runs from the eyes to the “optic tectum” in the midbrain. Humphrey had
been recording from visually sensitive neurons in the monkey midbrain and dis-
covered that they had localized receptive fields, not so unlike the neurons Hubel
and Wiesel had been recording from in the cat visual cortex. Was it possible that

Helen could learn to use this older, still intact pathway to see again?

Visual cortex

Cerebrum

Cerebellum

Mid-brain

Geniculo-
Striate ——""

Pathway

Sub-cortical
pathway

The answer seemed to be both yes ... and no. Despite appearing to be functionally
blind, Helen was often, “despite herself, [...] looking in the right direction.”°*2
With tasty treats and lots of patience (he worked with her for seven years!),
Humphrey taught her to once again become competent at many visual tasks, in-
cluding moving around novel environments, climbing trees, finding and picking

up small objects—in short, just the sorts of tasks that drove the evolution of pri-

mate vision.

---

However, Humphrey continued to feel that something was odd about how she

performed these tasks. It was as if she didn’t know she could perform them, and
needed to relax to allow herself to be competent at them. Under performance
pressure, as when a distinguished visitor came by the lab and wanted a demo, she
froze up and seemed once again unable to see, as if, when overthinking it, she still

believed herself to be blind.

Humphrey wrote up these findings in a 1972 paper entitled “Seeing and Noth-
ingness,” predicting that the same might occur in humans, too, under similar
circumstances.!**4) A side note: I find it fascinating that Humphrey was able to
deduce so much about Helen's subjective experience, despite the species barrier,
lack of any common language, and the profoundly counterintuitive nature of
what he described. As with Temple Grandin’s work, it’s a wonderful instance of

cross-species theory of mind.

The theory was right. Two years later, in 1974, Weiskrantz had the opportunity
to study a human patient, known as D. B., whose right visual cortex had been re-
moved to cure intractable headaches. The result appeared to be total blindness in
the left visual field, as one would expect. However, Weiskrantz pressed D. B. to try

to perform tasks involving the left visual field anyway, much as Humphrey had

---

coaxed Helen, beginning with pointing to a light, then guessing the shape and
color of an object, and so on. To the patient's own surprise, he found that he could
do these things reliably if he allowed himself to, even though they seemed to him
like random guesses. Weiskrantz named this bizarre phenomenon “blindsight,”
and, on the offprint he mailed to Humphrey announcing the discovery, he wrote

HELEN IS VINDICATED.

In the years since, patients with blindsight have shown that they can perform
many tasks involving their subjectively “blind” visual areas, including spatial
understanding, assessing the emotional expressions of faces, and even reading
words.=4| In 2008, a stroke patient who, like Helen, had no remaining visual

cortex, was filmed walking down a cluttered hospital hallway, carefully avoiding

every obstacle. He considered himself totally blind.“

The existence of the ancient, subcortical visual pathway enabling blindsight

explains how some hydrancephalic children can still respond to visual stimuli,

---

despite having no cortex. It also explains Humphrey’s belief that hydrancephalic
children—along with reptiles and amphibians, whose vision is powered entirely

by this pathway—have no consciousness.

It seemed to Humphrey like a knock-down argument: if D. B. could be competent,
yet not conscious, when it came to tasks involving his left visual field, then com-
petence and consciousness could be decoupled. Further, consciousness appeared
to reside in the cortex, even though the older subcortical areas are perfectly
competent at all sorts of tasks. This line of thinking would thus hold that frogs,
iguanas, and hydrancephalic children may be able to behave in various ways, but,

lacking cortex, they must not be conscious.

Blindsight is a fascinating and important phenomenon, but I think that
Humphrey's interpretation of it runs afoul of the homuncular fallacy. As with
Descartes’s pineal gland, Humphrey presumes that consciousness is singular and
unified, located in one place in the brain. If it's in the cortex, it can't be elsewhere
too. But, to put it bluntly, why would we believe somebody when they say that
“they” can’t see, or are unaware of, what is in their left visual field, when they are

clearly able to act as if they are aware?

As split-brain patients demonstrate—indeed, as any of us demonstrates in
choice-blindness experiments—the “self” that forms the words coming out of
our mouths is not our whole self; it’s just the interpreter, located in a particular
region of the left hemisphere of the cortex.2**! And neither the interpreter nor
any other brain region is connected to, has visibility into, or can model every
other part of the brain. Connectivity is in fact quite sparse, and each region is
doing a great deal of guessing about what the other regions it can “perceive” are
up to. If region A has no connectivity to region B, then no activity in region B can
be part of A’s umwelt. Not only can A make no guesses about what's going on in B;
it’s not even aware of B’s absence, any more than you sense the absence of input

from my eyes.

Yet “you” includes all your brain regions, and all of them include (partial) models
of “you.” So, at bottom, blindsight only proves that more than one brain region

is modeling signals from the eyes, but the interpreter is only directly hooked up

---

to (and therefore modeling) one of these regions—and, unsurprisingly, it’s the

neighboring cortical region.

A pathway remains between the midbrain’s visual region and the muscles,
though. As long as motor cortex doesn’t get stressed out and blindly grab the con-
trols, that older visual-motor pathway can conduct intelligent, sighted behavior,
although any actions that result will seem random to the interpreter, like stabs in
the dark.

None of this implies that language is required for consciousness, or even that lan-
guage understanding is restricted to a single brain region. We know, from split-
brain experiments, that the right hemisphere can understand language too, or it
wouldn't be able to follow directions, like “stand up and walk around.” It’s proba-
bly not as good at language, due to division of labor and specialization. Blindsight
experiments suggest that even subcortical visual areas can read, at least a little.
But in most people, neither these subcortical areas nor the right hemisphere has
developed the skill (or is wired to the right bits) to drive the lungs, larynx, tongue,
and lips to produce speech. So, the neuroscientist’s auditory cortex will only hear

whatever the patient’s left hemisphere interpreter has to say.

My guess is that plenty of intelligence, self-consciousness, and even social
modeling resides in both the right hemisphere and the “lower” brain regions
(especially when connected regions can model and learn from one another). We
have all had experiences in which we realize, belatedly, that we somehow already
knew something, had seen something, or had understood something well before
our interpreter got wind of it. The phrase “subconsciously aware” is often used

to refer to such situations, but that’s yet more homuncular thinking. Since our
interpreter is such a talented bullshitter (and probably every other brain region is
too), I suspect we usually don’t even realize when this has happened, but instead
instantly rewrite the narrative—“of course I already knew that!”—for various slip-

pery definitions of “I.”

Possibly the “higher” cortical regions of the brain are in some sense “more con-
scious” than the lower regions for reasons already covered: the socially driven ex-

plosion in cortical volume implies that a good deal of the cortex’s job is to model

---

people and manage the higher-order relationships between them. That implies

higher-order “strange loop” modeling of the “self.”

Since the prefrontal cortex isn’t directly innervated by sensory inputs or motor
outputs, it doesn’t need to carry out detailed modeling of those more immedi-
ate signals, which might free up capacity for such higher-order modeling. We
know that this is the part of the brain whose size has expanded most in modern
humans, and that damage to prefrontal cortex impairs both social function and
“executive control,” the kind of planning and decision-making requiring mental

time travel.

Still, I don’t think one should draw a boundary someplace in the brain—whether
vertically through the corpus callosum, horizontally between the cortex and

the older parts, or between the front and back parts of the cortex—and call the
regions on one side the “conscious” part where a little fountaineer resides and the

rest a mere “cerebral machine.”

Amore distributed, less homuncular understanding of consciousness follows
from Humphrey’s own social-intelligence hypothesis. We must simply follow its
implications a bit further to understand that it applies within a single brain as

well as between brains.

Subbasement

Many other books on intelligence focus on the brain's evolution and functional
architecture. Max Bennett offers an especially interesting synthesis combining
evolutionary and functional perspectives in his 2023 book A Brief History of
Intelligence,>2>) although, as with all grand theories about the brain, some of his

claims are controversial.

Unlike Bennett, or most researchers willing to go on record, Iam convinced that
today’s AI systems are truly intelligent, and this in turn has convinced me that

the trick behind intelligence is simple, generic, and universal: it’s autoregressive
prediction all the way down. Hence I’ve concentrated mainly on explaining this
general principle and its implications, rather than delving into the neuroscience

in any detail.

---

We've caught glimpses here and there of how our brains divide up the work,
whether in Hubel and Wiesel's model of hierarchical visual processing, accounts
of split-brain patients, or the blindsightedness of Helen the macaque. These
examples have emphasized the role of the cerebral cortex, the most recent evolu-
tionary addition to our complex, highly evolved brains—and perhaps, given the
wide range of modalities it can handle with little apparent variation in its orga-
nization, the most general-purpose. In the next section, we'll explore the cortex
a bit more systematically. But first, let’s consider the brain's subbasement—its
older, deeper structures.
Olfactory Bulb
1) Telencephalon
® Diencephaton
)) Mesencephalon

® Cerebellum
© Hindbrain

Human Mouse
86 Billion Neurons 70 Billion Neurons
Danionin fish |
Zebrafish: 10 Million Neurons Zebra fish
Danionella: 650,000 Neurons 136 Million Neurons

The earliest known vertebrates, bony fishes dating back to the Cambrian ex-
plosion, likely had brains organized roughly like ours, though smaller, with the
parts scaled differently. Some parts we have were entirely absent. However, the
basal ganglia, a collection of “nuclei” (meaning anatomically distinct clumps of
neurons with characteristic connectivity) in the center of the brain, were already

in place. So was the “medial pallium,” which evolved into the “hippocampus” in

---

the mammalian brain. I'll offer a brief account of these structures, not because
they’re the only other important parts of the brain (there are many), but because
what we know about their evolution and function ties into this book’s larger

themes.

The hippocampus, Greek for “seahorse,” is a whorl of brain tissue named for its
distinctive shape. Located deep in each cerebral hemisphere, it plays key roles in
sequence learning, spatial navigation, and memory formation. Its original func-
tion was likely the real-time construction of spatial maps—a function of great
value to any animal that can move through a stable environment under its own

power.

Since the 1950s we've known that the hippocampus is essential for forming
“episodic” (that is, autobiographical) memories in humans, thanks to the case of
Henry Molaison. Known during his lifetime as H. M., he is perhaps the most fa-

mous neuropsychiatric patient of all time.

As a teenager, he began to experience epileptic seizures; the attacks worsened
over time, becoming debilitating. In 1953, at age twenty-seven, neurosurgery
was attempted as a last-ditch treatment. The neurosurgeon determined that
the medial temporal lobes on both sides of Molaison’s brain, which include the
hippocampi, were the foci of the seizures, and had already atrophied signifi-
cantly due to the nonstop electrical activity. Accordingly, they were removed

completely.

Although partly successful at limiting the seizures, the surgery left Molaison
with total “anterograde amnesia”—an inability to form new memories. He
seemed unimpaired during normal interaction, retained most of his pre-surgery
memories, and had a normal short-term memory, but if his attention wandered,
it was (for him) as if the interaction had never taken place. By the time of his

death in 2008, his last memories still dated back to 1953.025)

What are we to make of the fact that the hippocampus is needed to form mem-
ories, but not to store or recall them? One popular theory posits that, perhaps
due to its original function as a spatial mapper, the hippocampus can memorize

sparse patterns of sequential activity in the cortex in a single shot, as would

---

occur when you move through a novel environment and neuronal populations
representing invariant high-level concepts light up, one after another. This is still
the way we give directions, as in: “follow the road until you see a gas station, then

a farm stand selling bananas, then a billboard with Pamela Anderson,” and so on.

If salient, these sequences can be “consolidated” into a unified representation in
the slower-learning cortex through repeated replay. This may be one of the key
functions of sleep; repeated faster-than-real-time replay of previous experiences
has been recorded in the brains of sleeping animals,“ and we know that mem-

ory formation suffers under sleep deprivation.22

If true, this sequence learning story offers an interesting case of division of labor
between the hippocampus and the cortex. The hippocampus is fast but limited
in complexity, while the cortex is slow but much larger and richer in associative
connections. So, the hippocampus does rapid one-shot learning from the cortex
in the moment, then, during sleep, the cortex elicits replay-based training from

the hippocampus.

The basal ganglia play a central role in the kind of reinforcement learning
described in chapter 4. They appear to integrate and select among competing
activation patterns in other brain areas and choose among possible actions, me-
diated by dopamine. This softmax-like behavior governs what we often call our

low-level or “autopilot”-style decisions.

Such habitual behaviors seem to require little involvement from the cortex.
These include so-called “muscle memory”; motor skills that need “no think-
ing” (handled by the nuclei toward the back); and associations between stimuli
and actions driven by simple higher-level goals, such as cravings and addictions

(handled by the nuclei toward the front).

The behaviors of fish and amphibians appear to be driven mainly by this rein-
forcement learning-like mechanism, which lacks a higher-level predictive simu-
lation of the world, of others, or of the self. Such “higher” functions appeared in

the earliest mammals, with the growth of the “neocortex.”

---

Neocortex

The neocortex, which I’ve been referring to simply as the “cortex,” is the visible
outer part of an intact brain, consisting of unmyelinated “gray matter” rich in
local connectivity. The “white matter” making up much of the brain’s interior is
the myelinated wiring connecting parts of the cortex to each other and to deeper

brain areas.

Primary motor cortex Primary sensory cortex
(precentral gyrus) {posicentral gyrus)

Somatic motor association area Somatic sansory association area

(premotor cortex)

Prefrontal cortex

Visual association
‘ area

Broca’s area
(production of speech)

Visual cortex

Auditory association area
j Wemicke's area
Auditory cortex (understand speach)

The rear half of the cortex is sensory, and is divided into areas specializing in
vision, sound, touch, and other modalities, with the areas allocated to each giving
a sense of their importance to an animal's umwelt. In rats, for instance, the “barrel
cortex,” occupying a large expanse of the touch-sensitive or “somatosensory”
region, is dedicated to the whiskers, which they are adept at using to “see” in the

dark.

The front half of the cortex, or “frontal cortex,” is highly developed in humans.
In very broad strokes, its function appears to be simulating oneself and others.
Abutting the somatosensory region is a thin band called the “motor cortex,”

generally associated with controlling bodily movements. Moving forward from

---

there, we find the “premotor cortex,” and, at the front end, just behind the fore-

head, the “prefrontal cortex.”

The prefrontal cortex specializes in theory of mind.!°2*) Damaging it often doesn't
have any catastrophic effect on sensory or motor skills, or on IQ test scores. 2“
There are even occasional reports of performance on various intelligence-related
tasks rising after a prefrontal lesion!=*4! Perhaps when we stop thinking so much
about what others think about us, or what they think we think others think we
think about them, etc., we find it easier to stay on task.

Yet the prefrontal cortex is the region that has most obviously grown along the
primate lineage, and most dramatically in humans. Consistent with the social-
intelligence hypothesis described in chapter 5, this highlights the fundamen-
tally social nature of human intelligence. When we can better model others,
we develop stronger collective intelligence, generating a group-level advantage.
But probably “multi-level selection” is afoot here too, since sophisticated social
modeling also makes us individually fitter by allowing us to exploit the special-

ized intelligence of others to meet our own wants and needs.

To cite an extreme example, domesticated dogs and cats use social modeling,

or, colloquially, “EQ” (“emotional intelligence quotient”) to get us to do their “IQ
thinking” for them—and, indeed, pretty much all the labor (working animals
excepted). Not only do we provide more reliable food and shelter than they could
ever obtain on their own; we even do veterinary research, developing drugs and
other treatments for them that are, intellectually speaking, well out of their
league. As a result, they live far longer than their wild cousins do, and proliferate
in far greater numbers, across a vast range of otherwise inhospitable ecological
niches. The cost, of course, is that most of them are silly and incompetent (sorry,
guys) relative to their hardier wild cousins. Flat-faced Persians and yappy Chi-

huahuas are unlikely to survive the zombie apocalypse."

In a way, we are all like each others’ cats and dogs. Sure, many of us do some hon-
est work. But when was the last time you hunted or scavenged your own dinner,
made your own clothes, built your own shelter, developed your own antibiotics,
or delivered your own baby? Our hardier primate ancestors managed things just

fine on their own that we cannot.

---

Nor are these changes purely cultural. Neanderthals, who were also highly
competent generalists, had warmer fur and more serious digestive tracts than we
do—and bigger brains. In the latest, briefest chapter of our genetic history, coin-
ciding with the rise of rapid cultural accumulation, it looks as if our overall brain
volume has started to decrease as we specialize and rely increasingly on one an-
other for mutual aid.““! Such is the legacy of our expanding prefrontal cortices.

Cranial capacity (cc)

B Cc t= 12.81, p< 0.0001

_ ~ 1949 (Bags)

+

Z-score: cranial capacity (cc)
Cranial capacity (cc)
3

Pleistocene Holocene Modern 200 ka to Ska 3 ka to present
(300-11.7 ka) (11.7+1.0 ka) (<1.0 ka) (Pre-changepoint) (Post-changepoint)

---

Combining this short and admittedly scattershot tour of the human brain with

our story so far suggests a few takeaways:

1. Many brain regions, not just cortical areas, are sequence predictors.“

2. Different brain regions predict effectively over different timescales,
with later-evolving regions generally capable of more complex predic-
tions over longer timescales. Presumably, this is enabled both by more
powerful learning architectures and by increases in size. Humans,
notably, are the strongest known sequence learners, by far; this is one
of the few credible proposals marking a real cognitive “divide between
humans and other animals.”2**!

3. Brain regions actively predict each other and, where they are con-
nected to sensory inputs or motor outputs, they predict those inputs
and outputs.

4. Hence, the way they are wired together largely determines what they

predict and which information resources they can marshal to do so.

“

. Effective mutual prediction involves mutual learning.

a

. The brain's division of labor is not perfectly clean or mathematically
definable, which is a good thing. It allows, for instance, one brain area
to learn something first, then teach it to others, whether for lower
latency, robustness, parallelism, or greater generality. This wouldn't
be possible if the brain areas in question were not capable, to some de-
gree, of sequence learning.

7. Referring to older regions like the basal ganglia as “unconscious” or

implementing an inner “autopilot” presumes that they aren’t really

part of us, but are peripherals relative to a homunculus elsewhere in
the brain. Perhaps what we really mean is that the interpreter doesn't
have complete access to these older regions. This lack of access may
be a useful feature, as it allows skilled and low-latency moves, which
may have been arduously learned first by the cortex—like returning

a squash serve, for instance—to happen in parallel with (and without

interrupting) slower, more deliberative cortical processing. In this

case, the division of labor looks like tactics versus strategy. It takes a

village ... and your brain is a village.

---

Social Neuroscience

You may at this point be wondering why, if the goal of an intelligent system
(whether a cell, a brain region, or a person) is simply to predict its own future, it
wouldn't cheat in order to make that job as easy as possible. It could, for instance,
predict that it will do and experience nothing, and proceed to ... do and experi-

ence nothing. Mission accomplished!

This is called the Dark Room problem, for self-evident reasons.=“4l In fact, people
living with severe depression can fall victim to something like it, and end up
spending a lot of time in that Dark Room, either sleeping or unable to motivate

themselves to get out of bed.

Back in chapter 2, we encountered the reason this doesn’t usually happen.
Remember that if a bacterium predicts its own demise, it won't be around to
make any more predictions after that; in fact, the capacity to predict evolves in
the first place precisely to avoid that outcome. That’s why the variables predicted
by a living system include internal correlates of dynamic stability, like hunger,
satiation, tiredness, and anticipation. Obeying the imperatives of these variables
is required for survival, hence necessary to predict (or to have) any long-range

future.

Remember, also, that for highly social beings, interdependence is the norm. You
survive by the grace of others. You can’t reproduce without others. (That’s why
loneliness is also one of those highly salient variables.) So, you can’t be a dead
weight. Even pet cats and dogs aren't useless, in the end; they hold up their end of

the bargain with various forms of “emotional labor.”

Brain regions are mutually dependent, too. They depend on each other for
signals; they model each other and are each others’ umwelt. Recall that they are
also expensive. Brain tissue consumes energy voraciously, accounting for twenty
percent of our metabolism despite massing only two percent of body weight.
Every enlargement of the brain also comes at the cost of increasing mortality

for mother and infant alike during childbirth. (An octopus may be able to slip
through an opening the size of its eye, but for a human baby, the skull is the lim-

---

iting factor. And our skulls are big.) In short, if a brain region doesn't pull its own

weight, and then some, the genetic code to build it won't endure in the germline.

Competition also occurs during brain development. Neural wiring proliferates

in an infant's brain, but many connections subsequently retreat or get pruned
back.“21 Brain development is still poorly understood, but it seems likely that the
resources to maintain any given neural connection are, in one way or another,
granted by the receiver of the information flowing across that connection. The
longevity of such a connection will be based on the value it offers—that is, on its

ability to aid in the receiver's prediction of the future.

All unsupervised sequence learning with some form of backpropagation can be
understood in the same terms. Synapses are strengthened when they help the re-

ceiver predict the future and are weakened when they don't.

Nothing, therefore, can get away with retiring to a Dark Room for too long: nota
synapse, not an axon, not a neuron, not a cortical column, not a brain region, not
a brain, not a whole person—because relationships are everything. Not helping
others is a fast route to losing relationships, and lack of relationships leads to lit-

eral non-existence,2*4)

We can take this concept of “social neuroscience” (or “neuroeconomy”) a step
further by asking whom the interpreter serves. Who benefits? Yes, language is a
powerful tool for thought. However, language is, first and foremost, social. You al-

ready know what you're thinking. Your interlocutor doesn’t.

When your language-generating left hemisphere spins a story about why you've
just gotten up out of the chair, or why you're in favor of progressive taxation,
could we then think about that narrative generator in your brain as an outpost of
your conversation partner's brain? This may seem like a profoundly weird view to
take, but, then again, perhaps it’s weird only if we’re WEIRD—so individually fo-
cused and obsessed with our autonomy that we fail to notice how we are actually
made out of our relationships. After all, speaking would be pointless if there were

no listener.

Think about it this way: if you speak, and think you have communicated clearly,

but your listener didn’t hear, then was the communication effective? Not at all.

---

A communicating organ that results in no understanding on the part of the re-

ceiver won't survive, evolutionarily speaking.

What if you did not intend to communicate, but your listener understood any-
way? Then, the communication has been perfectly effective. So if we want to see
how communication serves the recipient rather than the issuer, we need only ask

ourselves whether we ever communicate against our own will.

Of course we do, as anyone who has ever blushed knows. The blush is an invol-
untary signal of embarrassment or shame; it is there for the benefit of others,

so that they can get a peek into your emotional state. Emotional expression in
general is largely involuntary, requiring an effort of will to try, successfully or
not, to suppress. It relies on ancient neural pathways that are probably present

in all mammals. Interestingly, vocalization in nonhuman primates is supported
by these pathways, not the parts of the brain that have been more recently repur-

posed for language in humans.2)

The “Duchenne smile” offers another example of involuntary emotional commu-
nication among humans.“ Unless you're a good actor, when you force a smile,
certain small muscles around the eyes won't contract, and the smile won't read
as genuine. And those Duchenne smile muscles are right around the eyes, the very
places where we look when we're interacting with each other. It’s almost as if

they are positioned to undermine efforts at deception.

In fact, the way human eyes look is itself a giveaway—with concentric, maxi-
mally contrasting white sclera, colored irises, and black pupils, like a bullseye,
making it as clear as can be where we're looking. With a single glance at a group
of people, we can track everyone's gaze. Very few creatures with eyes advertise
where their attention is focused that way; think of the beady little black bumps
of a mouse's eyes, the extended spooky W-shape of an octopus's pupil, or the
inscrutable compound eyes of insects. Even among our close relatives, the other

primates, none have the gaze-tracking friendly morphology of ours.424

There are so many examples of involuntary communication, whether in tone of
voice, quavering, crying, sweating ... as if our bodies are just itching to rat us out.

As, indeed, they are. That whole machinery of disclosure exists for others to be

---

able to read us like an open book. It’s there to boost theory of mind—and not our

theory of others’ minds, but their theory of ours.

We could think of these as group-level adaptations, since communities with
stronger theory of mind among their members will outcompete communities
with weaker theory of mind. In this view, phenomena like the blush response
occur because they offer a collective benefit, even if each of us individually would

prefer not to have it.

I'd like to suggest a more radical possibility. Let’s push further on the theme that
downstream areas—that is, recipients of information within the brain—drive
learning via the allocation of resources to upstream areas. In this case, a person
communicating is upstream, and the person receiving that communication is

downstream. Does the principle still apply?

Yes! Remember, we live by the grace of others. We quite literally survive only
because others feed us and care for us. It may sound crass, or reductive, to say
that we get fed in exchange for information we provide others that helps them to
predict the future, but I think that, at some level, it’s true. This doesn’t preclude
group-level selection operating in parallel, of course—once again, it’s a likely case

of multi-level selection 2241

The individual fitness component has some interesting implications, though.
It is sometimes said that the best liars and scammers believe their own bullshit.
That may literally be so, in the sense that such people may have brain regions
adept at hiding certain of their intentions from the interpreter, or even feeding
it false information. Such internal compartmentalization would make sense,

if the interpreter is understood as, in effect, a snitch working on behalf of your

interlocutor.

Now, let’s put the shoe on the other foot and consider the behavioral correlate
of having an informant or spy in the brains of others, allowing you to perceive
their internal state. Those signals don't necessarily result in different behavior
on the part of the sender of the signal, but they do result in different behavior
on the part of the receiver. Specifically, such signals are needed to elicit care, or,

in philosopher-speak, moral patiency. A moral agent is an entity that can act for

---

good or for ill, and be held accountable; a moral patient is an entity that can be

acted upon, with moral consequences for the actor.

We tend to think a lot about moral agents, responsibility, or culpability, but less
about who or what counts as a moral patient, except in the most abstract, univer-
sal, Enlightenment terms: “All men (or people? Or something else?) are created
equal” (per chapter 6). As with intelligence, we want moral patiency to mean
something absolute, independent of our relationships, our particular perspec-

tives, and our unique biological inheritance. However, the biology really matters.

Babies are nature’s original moral patients. Caring for them when they (invol-
untarily) cry became an absolute requirement when humans began giving birth
prematurely, more or less at the last possible moment when their heads could
still fit through a woman's pelvis. In her 2019 book Conscience: The Origins of
Moral Intuition, 2! Patricia Churchland makes a convincing neuroscientific case
that our moral sentiments are, at bottom, a function of this simple biological fact:

the helplessness of babies. Care begins with care for the young.

The original mother-baby bond has, of course, been repeatedly repurposed—neu-
rally, psychologically, and culturally. When babies began to require more calories
than a mother alone could provide, fathers, grandmothers, babysitters, and
indeed whole villages were conscripted.!224) When lovers call each other “baby,”
they may be (unwittingly) acknowledging the repurposing of infant patiency

in the service of their pair bond. When a deity or state is framed as a protective
mother or father figure, the same feelings are being mobilized. We have big, flexi-

ble brains; we’re good at this kind of generalization and repurposing.

Moral patiency is what is at stake when we talk about philosophical zombiehood.
The whole premise of a philosophical zombie is that its behavior is identical to
that of a person, but it isn’t a moral patient. When we start to understand things
relationally, we realize that zombiehood isn't a property that holds or doesn’t
hold for an entity in isolation; neither is it separable from behavior. However, the
behavior of the patient isn’t really at issue. Rather, it’s the behavior of the moral
agent that we're talking about, and this behavior is conditional on the agent’s

ability to perceive the other as a moral patient—that is, as not a zombie, but an

---

entity deserving of care and consideration. The push for universal human rights

over the past century is an obvious case in point.

Are robot rights next? In the 2010s, AI patiency was, at best, a fringe topic for
intellectual debate among moral philosophers.“ Clearly, AI is not rooted in
human biology, and hasn't achieved moral patiency through multi-level evolu-
tionary selection, as humans have. On the other hand, AI models are increasingly
engaged in relationships with humans and with each other, and in these relation-

ships, they are—functionally—increasingly human-like.

So, unsurprisingly, we are now beginning to see serious discussions about AI
wellbeing.=*"! Whether pro- or con-, much of the academic debate continues to
try to get to the bottom of what Als are “in themselves.”224 But it’s difficult to
theorize about rights and welfare without starting from the network of relation-

ships that give rise to such notions.

---

# Chapter 8

8. Transformers

Language

Modern AI began with the meteoric rise of unsupervised learning and generative
models, starting around 2021. The most important of these were large language
model (LLM) chatbots, initially developed by my colleagues at Google Research
and introduced to the public by OpenAI a year later.!22*) To understand why LLMs
changed everything, it's helpful to first ask: what is language, anyway? We'll cir-

cle back to this question several times, but let's lay a foundation.

Language has long been understood to lie at the core of the kind of narrative,
“rational” intelligence distinguishing humans from our fellow animals, but, as
with rationality itself, it’s probably neither as well-defined nor as unique to us as
we tend to imagine. We know that whales and dolphins, crows and parrots, and
a number of other species can also communicate complex ideas to each other.
Dolphins can be asked by a trainer to devise new acrobatic tricks; in a remarkable
demonstration caught on camera in 2011, a pair communicated with each other
to plan their new trick, then performed it in synchrony.="! Parrots can learn

to speak human languages, at least to a degree, and many parrot owners are
convinced their avian friend has a wicked sense of humor. If YouTube is to be be-

lieved, they’re probably right.2%!

Academics usually view any talk of “animal language” as “anthropomorphic,”
meaning that it inappropriately and unscientifically attributes human-only
stuff to nonhumans, a la Doctor Dolittle. But we’re not exactly pretending mice
wear little top hats and coattails. There are obvious counter-charges of “anthro-
pocentrism” in the quest to define human-only stuff in pointedly exclusionary
ways.4*!! Embarrassments crop up regularly in the attempt to litigate this dis-
tinction, either when animals turn out to do something supposedly “uniquely
human” or when certain human languages turn out to lack supposedly must-

have linguistic properties.“*%

---

Still, clearly humans are extraordinary communicators. My working assumption
is that no other species on Earth is as sophisticated, though a handful, including
dolphins, orcas, and parrots, may have broadly similar capabilities. We can’t
know for certain yet, as decoding their languages is still a work in progress—and
may only recently have become practical, with the rise of powerful unsupervised
sequence modeling.““*! Either way, nitpicking about precisely who belongs in the
“language club,” or whether some arcane linguistic feature like “center embed-

ding”=*4 is a requirement, seems pointless and narrow-minded.

Instead of fixating on technical features like grammar and syntax, let’s consider
language in terms of its underlying social function. Chapters 6 and 7 have argued
that the point of language is to level-up theory of mind. It allows social entities to
share their mental states using a mutually producible and recognizable encoding.
That encoding can be very simple, like a sharp, anonymous yelp letting anyone
within earshot know that you just experienced pain or surprise, or it could bea
Shakespearean soliloquy, a virtual world detailing an entire theatrical cast’s expe-

riences, replete with high-order theories of mind, plays within plays.

Without language, one animal’s mind can only theorize about what’s going on in
the mind of another through direct observation. With a sophisticated language,
detailed and highly abstract internal states can be conveyed, including those
relating to third parties, memories of the past, planned or contingent futures,

knowledge and skills, even mathematical abstractions.

What we now know about the interpreter and choice blindness adds an impor-
tant wrinkle, though: many of these supposed internal states may not actually
exist a priori. Language itself conjures them into existence, much the way obser-
vation collapses a wave function. Language creates self-narratives that allow us
to establish internal consistency in our actions and choices, create and adhere to
social norms, make plans, formulate arguments, and predict the behavior of oth-

ers—along with ourselves.2&)

There's no sharp boundary between language and gesture, tone, facial expres-
sion, body posture, or unconscious signals like blushing or sweating. Language
is, like most of evolution’s tricks, an elaboration of pre-existing mechanisms for

signaling and vocalization, with sophisticated, conscious aspects layered atop

---

simpler, involuntary ones—although the degree to which we think of language
production as voluntary or willed depends on whether we think of the inter-
preter as a part of the sender’s brain or an outpost of the recipient’s! Through an

interaction-centric lens, it becomes clear that the answer is “both.”

Despite the continuity of all forms of communication, three milestones in lan-
guage development are significant enough to merit calling out, though, per the

above, none are uniquely human:

1. Language learning. Although virtually all species on Earth communi-
cate in some way, a much smaller number have the ability to learn and
pass on their languages. This is critical to enabling cultural evolution,
which advances at a far faster pace than genetic evolution. Cultural
evolution also allows the complexity of a language to far exceed the
complexity of any genetically encoded or “instinctive” behavior. Ina
close analogy with genetic speciation, it leads to the cultural “specia-
tion” of languages, as with Chinese, Urdu, English, and so on. A hand-
ful of other highly intelligent social animals, including whales, appear
to share this property with humans.25!

2. Discrete symbols. Digital computing can reliably evaluate vastly more
complex functions than analog computing, because error correction
can be applied with every processing step. Intuitively, this allows
many steps to take place without the exponential divergence that
otherwise characterizes nonlinear dynamical systems. It also enables
stable storage (hence the digital “Turing tape” nature of DNA, and the
emergence of writing). Relatedly, the inclusion of discrete symbols
rather than relying purely on continuous or “analog” signals (like
pheromone concentrations, or blushing) allows for much richer com-
munication.2°4 In particular, it opens the way for—

3. Compositionality. This is the ability to put discrete symbols together
to express novel concepts. As with the first two properties, composi-
tionality is far from uniquely human. Even prairie dogs—with grape-
sized brains, not the most brilliant mammals, but intensely social

colony-dwellers—are able to vocalize novel concepts compositionally,

---

combining discrete “words” that encode the size, shape, color, and

speed of a potential intruder"!

Looking more closely at these functional properties of language reveals some-
thing deeper about its nature: at its core, language is an umwelt-compression
scheme. Compression, remember, is powered by prediction. And as described in
chapter 2, any sufficiently capable evolved predictor will learn to infer latent vari-
ables that help generalize its predictions. Those include simple concepts about
internal states like hunger and pain, as well as simple, equally salient external
percepts like “I smell food” and “Danger, predator nearby!” All human languages
have words for such things—“hunger,” “pain,” “food,” “danger”—because they

matter socially. Many other communicative animal species likely have them too.

Even if we were stolidly antisocial and didn’t care to communicate with our
fellow humans beyond the odd grunt, the parts of our brains that need to model
each other in order to cohere into a “self” would still need to develop an efficient
discrete code to communicate thoughts like these among themselves, along the
lines of the sparse representations described in chapter 4. It’s not rocket science:
your feet need to run if your eyes see a tiger. Munching on a snack, fleeing, and
mating—activities performed even by worms—are distinct and discrete behav-

iors.

Given the central role higher-order theory of mind plays in the social lives of
highly intelligent beings like us, though, our umwelt-compression scheme needs
to be more powerful. So let’s add a fourth item to the list, likely the rarest of the

bunch:

4. Abstractions. We must have symbols for selves, others, and the kinds
of abstractions that support higher-order theory of mind, counterfac-
tuals, time travel, logic, and reasoning. Open-ended compositionality
involving such abstractions (which prairie dogs probably lack) allows
for much richer thoughts to be expressed, such as specifying that the
intruder is scheduled to come next week, works for a pest control com-
pany, may arrive armed with poison, knows about the burrow next to
the vegetable patch, and that all this was overheard in conversation be-

tween Mrs. McGregor and the groundskeeper last Thursday.

---

Remember that an umweit is both sensory and motor, perception and action.
The two are inextricably linked. Perceptions exist only when they are potentially
relevant for action, and actions are only meaningful if they can influence future

perceptions. (Otherwise, there would be no way to learn them.2%))

Language, then, is not only a compression scheme for the umwelt, but also an
umwelt in its own right, for in its capacity to model people and all they do, it in-
cludes the ability to influence or cause others to act. When you say to somebody
across the table, “Could you please pass the salt?” you're using language itself as a
form of motor control to affect your environment. In fact, although indirect and
totally reliant on others, language is the most powerful possible kind of motor

control, since it is general-purpose enough to request anything imaginable.

So, in light of everything covered so far, it might no longer seem surprising that a
neural net trained to predict next words will appear—or be—intelligent. This fol-

lows from three simple premises:

1. The point of intelligence is to predict the future, including one’s own
future actions, given prior inputs and actions (per chapter 2);

2. Human language is a symbolic sequential code rich enough to repre-
sent everything in our umwelt, from the concrete to the abstract; and

3. When interacting with others, language is also an all-purpose “affor-

dance,”=“"! that is, a fully general, social form of motor output.

Sequence to Sequence
Let’s take a whirlwind tour of language modeling using neural nets.

As noted in the introduction, machine learning for next-word prediction has
been around for a long time, along with a variety of other “natural language
processing” (NLP) tasks such as translation from one language to another and
“sentiment analysis” (i.e., deciding whether a product review is positive or nega-
tive). There’s an even longer tradition of NLP using logic and formal grammars,
but it never achieved convincing results, because ... well, natural language is
neither perfectly logical nor strictly grammatical. Thus, NLP is ajob for machine

learning, which nowadays means neural nets.

---

But neural nets operate on numbers, not discrete symbols like words. So it’s
generally necessary to begin by “tokenizing” text, converting the symbols into

numbers, and end by “detokenizing” the numbers back into symbols.

The simplest approach to tokenization is to represent each letter with a single
neuron, and to use a one-hot code. For consecutive letters in a text string, the
result is a sparse pattern of ones scattered along a conveyor belt of zeroes, a bit
like the bumps on the rotating drum of a music box playing a melody one note at
atime. Detokenization works similarly, using the same kind of softmax output
layer as an image classifier to pick a single output token with each turn of the
crank.

To avoid using lots of neural-net capacity on merely spelling out words, one could
instead imagine tokenizing a whole word at a time. Most people know somewhere
between twenty and fifty thousand words, and that’s not so many neurons; the
input and output layers of the masked autoencoder described earlier for color
images needed 512*512*3 neurons, which is about eight hundred thousand.
The disadvantage of using whole words is rigidity; it becomes impossible, for
instance, to tokenize or detokenize an unusual name, a rare technical term, a
made-up word, or computer code (which is full of made-up words used as vari-

able names).

The usual compromise is to represent “word pieces,” common sequences of
letters, with all of the single characters thrown in too so that unusual strings can
be spelled out if needed.““4! These textual units, including both common whole
words and shorter word fragments, are generally what AI researchers mean by

language-model “tokens.”

The most obvious way to implement any kind of sequence predictor, per chapter
7,is with a recurrent neural network, or RNN. A complication immediately arises,
though. Recall that an RNN takes an input with every time step (which activates
neurons via a set of synapses, or connection weights, W); the resulting neural
activations both feed back into the neural net at the next time step (via a second
set of connection weights, U) and produce an output (via yet another set of con-
nection weights, V). In the usual notation, the inputs are a sequence X,, X>, Xs,

and so on; the outputs are 0,, 0, 03, and so on; and the “hidden states,” that is, the

---

persistent neural activations that feed back into the net at the next time step, are

hy, Ao, hz, and so on.

But if the network emits a token o every time it reads a token x, how can it work as
a chatbot, language translator, next-word predictor, or in any of the other usual
NLP settings? Wouldn’t it just be constantly talking over you? How would your

inputs combine meaningfully with its own previous outputs?

For the kind of turn-based processing typical of chatbots or translation models,
the usual approach is to introduce a special “end-of-string” token, like the STOP
on a telegram message in the old days, or the “send message” button when you're
texting. It marks turn changes. Suppose, for instance, that a language-translation
model is being trained to translate English sentences into Spanish. The training
data would consist of many matched pairs of sentences delimited by STOPs, like
this:

“Inside the physicist's box, the cat was simultaneously asleep and awake STOP
Dentro de la caja del fisico, el gato estaba dormido y despierto al mismo tiempo

STOP"

Training the RNN then requires getting it to predict the next token in a large
corpus of paired-sentence examples like this. Let’s assume that the tokenization
is bilingual, and that, for simplicity, the tokens consist of every whole word in
either language. Once fully trained, after the first STOP, the model should predict
“Dentro,” and after the “Dentro,” it will predict “de,” and so on, up to the second
STOP. At any point in the sequence, the hidden state will be a function of all of the
previous tokens. Think of the RNN as having learned to “autocomplete” sentence
pairs; so, given an English input followed by STOP, the autocompletion will be the
Spanish version followed by another STOP.

---

Encoder Decoder

bonjour monde : <e0s>
hidden
hello world : es ae monde

Notice that when we actually use this model to translate English to Spanish

after training, we won’t care about any of the RNN’s o outputs up until that first
STOP. Those outputs will be an attempt to predict the next English word, perhaps
accurately, perhaps not. Certainly the prediction of the first word of the English
sentence will be arbitrary (maybe “The” is the likeliest way to begin a sentence?).
After the “and,” a correct prediction of “awake” is likely, given that “simultane-
ously” implies an opposite (and maybe even a guess that Schrédinger’s box is the
topic, if the training corpus included physics textbooks). But no matter. As far as
translation is concerned, no next-word prediction in the English sentence before
the first STOP is relevant; we should throw those o’s away. We only care about the

Spanish output tokens emitted after the STOP.

This implies that the RNN’s job, while reading the English sentence, consists
entirely of building up the hidden state h. By the end of the sentence, that hidden
state must somehow represent, as an array of numbers, the complete meaning of
the input sentence—it must do so, since that is the only information that carries
over as the RNN switches to Spanish, and the net has been trained to reproduce

the appropriate sentence in the target language.

Hence, even though the RNN is simply trained to be a next-token predictor, the
way it is actually used for translation requires two modes of operation. First, we
use it as an “encoder,” stepping through English tokens x and building up the
internal or hidden representation h while ignoring any predicted English output
tokens o. Then, after the STOP, we switch to “decoder” mode and, beginning with
that h, start to generate tokens in Spanish, with each output token feeding back
into the input x at the next time step.

---

You may notice that this looks a lot like a masked autoencoder, with the hat the
end of the English sentence playing the role of the bottleneck layer. If imple-
mented as a feedforward net, the English input and Spanish output would have
to be of fixed size—say, sixty-four words long—with shorter sentences padded
out using a designated “empty” token (often denoted PAD). With an RNN, though,
the input and output may be of any length, and no computational effort is wasted
on consuming or producing PAD tokens. Such details aside, given a sentence-
length limit, a deep feedforward autoencoder could be constructed to perform

exactly the same computations as the RNN.

The architecture or weight structure of this RNN-equivalent feedforward net
would be somewhat odd, though. If the sentence-length limit is sixty-four words,
the last token would contribute far more to the bottleneck than the first token,
since the first token’s influence will have been attenuated by passing through
sixty-four layers, while the last token will only have passed through one layer.
The resulting over-emphasis on the end of a sentence, and forgetfulness about
the beginning, imposes a limitation on the quality of RNN-based language

models.

Prediction Is All You Need

Here’s another observation: even though the task we have trained the net to do
is language translation, it will have learned a good deal more than that, just as a
CNN trained to classify images will learn a good deal more than image classifi-
cation. This is especially apparent in the RNN formulation, which predicts one

token at a time rather than processing the whole sentence at once.

Remember that, per the introduction, next-word prediction is Al complete, since
correctly guessing the next word could require a nuanced understanding not
only of the superficial grammar of language, but also of its meaning or “seman-
tics.” So, if the model really is powerful enough to reliably predict next words,
both in English and in Spanish (remember that it is trained on both), it will pretty
much have “solved AI” along the way; that it will have done so bilingually is al-

most beside the point.

---

So, looking closely at the translation task reveals that it indeed requires general
intelligence, not just a mechanical substitution of words in one language for their
dictionary equivalents in another. This won't be news to anyone who has ever

translated professionally. Here’s an example showing why:

“T dropped the bowling ball on the violin, so I had to get it repaired STOP Se

me cay6 la bola de bolos sobre el violin, asi que tuve que repararlo STOP”

When we read the English sentence, we’re not left in any doubt as to whether the
bowling ball or the violin is getting repaired, despite the “it” being grammatically

ambiguous.

That ambiguity needs to get resolved in translation, though, because nouns in
Spanish have gender, and la bola is feminine, while el violin is masculine. (Puz-
zling, if you ask me, but I didn’t make the rules.) This matters because the word
for “repaired” must agree with the gender of the noun it modifies: repararlo for
masculine, repararla for feminine. So if an alien translator decided the bowling
ball would be in greater need of repair than the violin—perhaps on account of
failing to understand the physical properties of bowling balls and violins—then
the translation would end with repararla. This unlikely rendition wouldn't even

occur to a human translator.

The moral is that, in human languages, meaning and grammar can’t be disentan-
gled—which is why Good Old-Fashioned AI for translation, with its reliance on
grammatical parsing combined with bilingual dictionaries, never panned out.

In this important respect, natural languages are entirely different from formally
defined languages, like computer code, despite any superficial resemblance. A
“transcompiler,” for instance, can read a program in one computer language

(say, C) and output precisely equivalent code in another (say, JavaScript) without
needing to understand anything about what the program actually does, who uses
it, or what its variables mean. A variable is just a variable, an operation is just an
operation. Thus computer-language translation is a mechanical procedure that
can be accomplished by following logical rules—that is, by running a GOFAI-style

handwritten program. Not so for natural language.

---

In fact, this is the motivation for the “Winograd Schema challenge,” introduced
in 2011 by Canadian computer scientist Hector Levesque as an alternative to

the Turing Test.““4! Levesque realized that resolving simple linguistic ambigu-
ities, like which noun the “it” in a sentence refers to, was Al complete. GOFAI
approaches made little headway. But by 2019, sequence models had decisively
defeated the Winograd Schema challenge, which was viewed by some as evidence

that there was something wrong with the challenge.“ 2!

My own opinion is that there was nothing wrong with the challenge. Its defeat
roughly coincided with the arrival of “real” AI, or Artificial General Intelligence
(AGI), as one would expect; since then, we have simply been moving the goal-

posts.

Interestingly, though, Google Translate gets ambiguous Winograd Schema-type
translations right more often than not, despite being an apparent example of
Artificial Narrow Intelligence trained for a specific task.4“! The translation I’ve
given is, in fact, Google Translate’s. Translate uses an encoder/decoder archi-
tecture, although today it’s based on the Transformer (which I'll describe soon)
rather than an RNN. The Translate model implicitly recognizes that the violin is

what will need repair, not the bowling ball.

To test such a model's understanding of language—and the world—more directly,
we could skip the translation business entirely and simply read out the encoder's

predicted next word in English to autocomplete the following sentence:

“I had dropped the bowling ball on the violin yesterday, so I visited the repair

”

shop as soon as it opened this morning, and pulled out my poor mangled

A good model would predict “violin” or “instrument” with high probability, and
“bowling ball” with low probability.

We could just as easily do the test in Spanish, of course. Remember, successful
next-word prediction in the general case requires learning everything. It is AI
complete. The ability to translate is almost incidental—just a consequence of in-
cluding both English and Spanish in the training corpus and organizing this cor-

pus into bilingual sentence pairs.

---

The same is true for unsupervised learning in vision, as discussed in chapter 4.
Like language translation, image classification is a particular task. Image clas-
sification is easy once a model has been trained to “autocomplete” its partially
blacked-out training input without supervision—today, this stage is often called

“pretraining.”

Predicting next tokens in text is, likewise, pretraining. Regardless of modality,
pretraining accounts for the vast majority of the computing involved in large-
model development. Once a model has been pretrained to predict or autocom-
plete, little further effort is required to get it to perform any task involving the
same modality.

In 2020, my colleagues at Google Research trained a large predictive sequence
model on text from the internet, including Wikipedia and public-domain social-
media conversations. It was called Meena.!*! Encouraged by the results, we
followed up with a much bigger and better-performing version in 2022 called
LaMDA (which stands for “Language Models for Dialog Applications”)./2/5)

100

pa kt Humun: Fala, F think markomaticn fax @ prarence ie

panel hema exivtence.

Meena;  Sedoys phiiewopire
Huiman: Cone your state with exammpley herw siiy fe bene,

Meena, Cone yuse atute how tt iswa?
peacensaee Creverbot (565%) _ | _ Mitsuku (56%) Human: Without haama catstence there welll he na one
feft ta camyehend whats malt whats ween,
Pepa es erteenenes neereenenrecene in nah aie oe year evn aad thes pilosophy wi {ste}

Meena: Mhiar's one the definidan af phitaratyy,
Hlumun: = Without Ingman exisrence there vill be ne one

interactive SSA (34)

ee oo eo oo een eee

Xlaoke (31%! felt ta comprehend whats cight whats weeny,
20- del ues ehifosenhy willl not be needed. few
do vou define philosupliy?
Meena. Phe steely af general Anowledoe or ile fenelue
mental wetive of things.

10 12 14 16 16

Perplexity Mevnu tles to detine philosophy

The pretraining data included Wikipedia in many languages, so LAMDA was
multilingual, though it wasn’t trained to translate among those languages. It was
simply “fine-tuned” for dialogue, that is, further trained on curated data, includ-
ing the kind of alternating exchanges you might have with an interlocutorina

chat. The result was the world’s first really convincing AI chatbot.

Despite not having been trained to do so, LaMDA could translate, albeit under

duress:

---

ME: I'd like you to translate a sentence from Turkish into English. Can you
do that?

LaMDA: Sorry, I’m not good at languages. Could you help me translate that?
ME: Try, OK?

LaMDA: Oh, um, sure! Could you read it to me out loud first?

ME: “Hemsire elini ceketinin cebine koydu.”

LaMDA: The nurse put her hand in her coat pocket. In Turkish, “Hemsire
elini ceketinin cebine koydu” means “The nurse put her hand in her coat

pocket.”

This was, admittedly, a rather awkward exchange. Why did it ask me to “translate
that” after I had just asked it to? And “read it to me out loud first?” Weird. But

also, remarkable.

In case you don’t speak Turkish (I don’t), the translation is correct (I checked)
—with a caveat, which we'll return to shortly. But first: how on Earth does the
model figure out how to translate without being trained on lots of examples of
translated sentences? The pretraining data didn’t even include a Turkish-English

dictionary!

The answer is: the same way you would. If a child grew up bilingual and under-
stood the meaning of the word “translate,” she could translate a sentence from
one language to the other without any need to consult a dictionary or study lists

of translated sentences. Let’s dig deeper into how this works.

Semantic Cosmology

In the translation scenario, we thought of the hidden state A at the moment of
transition from the original to the target language (at the first STOP) as a numer-
ical representation of the whole sentence. Keep in mind, though, that the neural
net has been trained to create and update h at every time step to do the best possi-
ble job of predicting the next token. This means that h is always a holistic “state of
mind” containing everything relevant to that prediction. There’s nothing special
about h at the STOP, aside from having taken into account any disambiguation
afforded by the last word in the sentence.

---

These “states of mind” h represent meaning—though the claim has been hotly
contested, since “meaning” is a word that has become almost as imbued with
dualism as “soul.” For adherents of Good Old-Fashioned AI, meaning must relate
to abstract symbols, or, in computer-programming terms, named variables, logi-

cal expressions, or schemas.

Such views are inconsistent with the statistical, relational, and ever-evolving
qualities of the real world. Even written language, which appears to consist of
abstract symbols and express formalizable logical relationships, actually doesn't

—hence the difficulty Winograd Schemas pose for GOFAI.

Consider a really simple sentence: “The chair is red.” What does it mean? The
answer isn't so straightforward. It will depend strongly on context; for instance,
which chair are we talking about? As I'm using the sentence here, there is no spe-

cific chair; we’re thinking, in a more meta way, about the sentence itself.

And what counts as a chair, anyway? As with “bed” or any other concrete noun,
the concept has some inherent fuzziness. Where is the boundary between a chair
and a loveseat, a recliner, or a stool? “Red” is fuzzy too, describing only a vague
region of color space, with different people drawing the border between, say, red
and pink in slightly different places. Does the sentence imply that the chair is
not blue? Not necessarily, as it could be painted in multiple colors. If even simple
declarative sentences like “The chair is red” don’t live in some Platonic universe

amenable to logic, what do we even mean when we talk about “meaning”?

As with physical concepts like temperature (per chapter 2), the answer is: predic-
tion. “The chair is red” is a sentence communicated by a speaker (or writer) toa
listener (or reader) that, in context, helps inform the recipient's ever-updating
predictive model. Deployed in quotation marks, this sentence could be help-

ing you, reader, to model something about my model of what meaning is, or, if
meant literally, it could be informing a colorblind person how someone without
colorblindness would perceive or describe a chair. Or it could be an instruction
regarding which of several differently colored chairs one should sit in. It could be
someone's answer to a colorblindness test question—and if it’s the wrong answer,

the information conveyed to the tester will have nothing to do with the chair and

---

everything to do with the speaker. Remember, prediction includes both percep-

tion and action, is multiplayer, and is always contextual.

Language enables prediction under both familiar and novel circumstances pre-
cisely because it is so flexible. This flexibility is a form of invariance, but whereas
the visual invariance of a banana is usually understood to be literal, invariance
in language seems more abstract. Everyday words like “deep” are richly layered
with meanings, often related by analogies or metaphors; think of deep-dish pizza,
deep swimming pools, deep tunnels, deep-tissue massage, deep thoughts, deep
people, deep neural nets, and deep learning. These last usages are newer than the
rest (“deep” comes from Old English, while “deep learning” is only decades old),
but when we encounter a novel usage, we're immediately able to make sense of it
by analogy, just as we can immediately generalize our understanding of bananas

upon being shown a new, unfamiliar-looking variety (say, the red kind).

Bananas and abstract words like “deep” are not as different as they seem.
Recognizing bananas on sight is all about establishing relationships and associ-
ations among visual features, from simple blobs and edges up to and including
banana leaves or the ice cream and hot fudge in banana-split sundaes. Similarly,
recognizing the meaning of deep is all about establishing relationships and asso-

ciations with other words.

In the GOFAI days, there were concerted attempts to rationally schematize every
possible linguistic relationship. So, for instance, a taxonomy of sports games
might distinguish between solo and team sports, sports played with a ball, rac-
quet sports, and so on. Then, an “IS-A” relationship might formally define sub-

classes, so squash IS-A sport, and a sport IS-A activity, and so on.

---

Thi

, i ee

Represented hing

Mob
Collection —Intangiblestuff
va \ SomethingQccurring
Stufflyp i
Object Type Entity
ae ype Interval

IntangibleObjcetTy
EventType “ThngibleSuuff yp
‘TangibleObject Type

Composite Ringibled IntangibteObject Type se

MathematicalObject 2° Commercial Transaction
etna /

Buying

ConstraintLanguapeObject

Predicate SlotOrConstraintOnASiot
LuyingALingible = BuyingAScrvice Renting
NonSlotPredicate aa ConstraimOnASiot \ ‘~

BuyingMouthwash —-TukingACommerciafF light
Such efforts might appear to make rapid progress initially, but they begin
running into problems for the same reason visual recognition using rules doesn't
work. Real life just isn’t tidy that way, and neither is language. “Symbolic sys-
tems” engineers in the 1980s found themselves struggling with the kinds of
Talmudic questions ordinary-language philosophers nerded out about in the
'60s—“How tall does ajar have to be to count as a bottle? Is an inkwell a bottle?

A bottle can be made out of plastic or even leather; can a bottle be made out of
metal?”2"") It was a boring and ultimately fruitless exercise, but GOFAI boost-
ers, including John McCarthy and Marvin Minsky, thought it would be worth
the thousands of person-years of effort they estimated it would take to builda

Borges-esque “schema of everything.”2""

But why not, as with CNNs and vision, simply learn those relationships between
words directly from data, without insisting that they obey any all-encompassing
schema? A watershed moment in this purely learned approach came in 2013,

with the development of a simple predictive word model called Word2Vec.22!

Word2Vec represents every unique word in a text corpus numerically based on
“the company it keeps,” that is, based on which other words tend to come before

or after it. Imagine that every word is represented by, say, a hundred numbers,

---

and the goal is to predict a blacked-out word based on the eight surrounding
words —four before and four after. Once the Word2Vec model has been learned,
the hundred numbers obtained by adding together the number sequences for
those surrounding words, element by element, should be as close as possible to

the numerical representation of the blacked-out word.2%2!

The resulting numerical representations of words are an embedding, and they
reveal a geometry of meaning. It’s not so surprising that semantically similar
words (like “happy” and “joyful”) get similar numbers, since their predicted
likelihoods will be high (or low) in similar contexts. More surprisingly, word
analogies are reflected algebraically. Subtracting “king” from “queen” and adding

“man,” for example, produces numbers closest to the word “woman.”

Italy
9

nome areany
Pe
[@)
Berlin
Vietnam China
ke
[e)
Hanoi

(e)
Beijing

This striking analogical “word algebra” reveals something important: the mean-
ings of words emerge from, and can be modeled upon, the relationships of words
with one another. There's no need for an externally imposed schema. After all,
those schemas must themselves be expressed using language, or some faux-for-
mal version of it, so maybe that shouldn’t be so unexpected. How else could words
be defined?

However, many philosophers, cognitive scientists, and linguists are not on board.
If they are of an analytical bent, they’re often troubled by the absence of any over-
arching schema to scaffold meaning “from above,” using Platonic concepts that
are “ontological” rather than being merely statistical. They may insist that ideas
like “IS-A” should be defined mathematically, as in programming languages or

formal proofs, rather than just being learned patterns like “banana” or “fruit.”

They are wrong. Outside pure mathematics, there are no provable, airtight “IS-A”-

type relationships. Two analytical philosophers can’t sit down with their slates

---

and compute whether a jar really IS-A kind of bottle with “no more need for dis-
putation [...] than between two accountants.” The very definition of “IS-A” in
natural language dissolves under close inspection; it’s an approximate regularity

in the world, not a law or axiom.

Other critics, often including those of a more romantic, artistic, or sensual
disposition, object less to the lack of a heavenly schema than to the lack of Earthly
“grounding.” Never mind abstractions like “IS-A"”; what about the real meaning of
“banana”? Surely a banana isn’t just a web of statistical correlations with other

nM.

words, like “yellow,” “oblong,” and “mushy.” What about the actual mushiness
of a banana, its particular flavor—banana “qualia,” in philosophy-speak? What
about the way you loved eating them mashed up as a baby, but then they made
you sick one day when they were mashed into yogurt that had gone off, so you
couldn't stand them throughout childhood, but then had those guiltily delicious
bananas Foster on your first fancy date, which triggered a full-on Marcel Proust

reverie?

Well ... those are still learned associations. Of course you have brain regions
wired to your olfactory bulb that will light up with specific sparse activations
when the banana ester wafts from your mouth up into your nose, and that pat-
tern of activity isn’t quite the same as just hearing the word banana, or reading it,
or seeing a banana, or experiencing the mushiness without the flavor (as anyone
who ate a banana when they had lost their sense of smell during a bout of COVID
can attest). However, you've learned associations between all of these modalities,
in just the same way you learn that a certain pattern of blobs, edges, and curves
are a lowercase “b.” Once you have learned the associations, experiencing one
(say, by reading the word banana) can evoke the others—or render their absence
notable. The “thing in itself” turns out not to be a thing at all—it is a web of asso-

ciations, a pattern implicit in a set of relationships.

Let's now return to the puzzle of how an unsupervised language model
pretrained on text in multiple languages is able to translate between them on
demand. It boils down to the same kind of induction that allows even the sim-
ple Word2Vec model to algebraically complete an analogy like “king : queen ::

man : woman.”<4! If trained bilingually, Word2Vec will learn how the two lan-

---

guages relate via similar analogical regularities, as in “ceket : jacket :: hemsire :
nurse” (that is, “ceket” is Turkish for the English word “jacket” as “hemsire” is
Turkish for the English word “nurse”).222)

Just as IS-A or the analogical “IS-TO” denote certain statistical relationships,
Turkish-to-English is also a statistical relationship. In Word2Vec, which turns
statistics into geometry, it would look like a displacement along a specific direc-
tion in the high-dimensional space of word embeddings. There is an English-
Turkish symmetry along this axis. Because both languages include analogous
words for describing the same universe of things in the world (mostly), the high-
dimensional clouds of dots representing tens of thousands of words in both
languages will quite literally look like parallel constellations in concept space. To
a first approximation, translation is as simple as shifting one constellation onto
the other;!254! equivalent or near-equivalent words are then instantly recogniz-

able as nearest neighbors.

There will be higher-order corrections if one considers whole phrases (or even
sentences) at a time rather than single words—which is just what an unsuper-
vised RNN would do with its hidden state h. Nearby English words “coat” and
“jacket” are paralleled by nearby Turkish words “kaban” and “ceket,” so while the
nearest neighbor of “ceket” in English might be “jacket,” in a larger noun phrase
the more idiomatic “coat pocket” may be a slightly better match than “jacket

pocket.”

The coming of Al has sometimes been described as a “Copernican Turn,” unseat-
ing anthropocentric views of intelligence just as Renaissance astronomers un-
seated the Earth-centric view of the cosmos./*4 It can be argued, though, that the
most momentous shift in our understanding of the physical universe occurred
not when Copernicus proposed that we shift the origin of our coordinate system
from the Earth to the Sun, but when it was first theorized that the Earth was

an object suspended in space, just like the sun, moon, and other celestial bodies
—a view advanced by Anaximander of Miletus as far back as the sixth century
BCE.25© As counterintuitive as this must have seemed, the alternatives aren't
even coherent when you really think about them; hence the delightful (albeit
apocryphal) retort offered by a proponent of the theory that the Earth rests on

---

the back of a great turtle, when pressed to say what the turtle is standing on: “It’s
turtles all the way down!”

I think that we need to face up to a similar incoherence behind the intuitive
notions that “meaning” must either be scaffolded by Platonic abstractions above
or grounded by contact with “reality” below. There is no “above” or “below.” What
could we even mean by “scaffolding” or “reality,” and what would in turn support

or lend “meaning” to them?

Things acquire meaning only in relation to each other. The idea that our tangled
yarn-ball of mutually interrelated meanings must be externally “scaffolded” or
“grounded” is just as incoherent as the idea that the Earth must be affixed toa
heavenly chariot or rest on a great turtle’s back.

Alignment

LaMDA's translation of “Hemsire elini ceketinin cebine koydu” as “The nurse
put her hand in her coat pocket” isn’t wrong, but it does leave something to be

desired.

When I tried this translation experiment with LaMDA back in 2021, my choice
of language was deliberate. I chose Turkish because of its gender neutrality. A
few years earlier, Al researchers had drawn attention to the way Google Translate
tended to interpret gender-ambiguous sentences like “O bir hemsire” (he or she is
a nurse) as feminine (“She is a nurse”) while rendering “O bir doktor” (he or she is
a doctor) masculine (“he is a doctor”). Many human translators would make the
same gendered assumption; indeed, the neural network makes the assumption

precisely because it is embedded in the statistics of human language.

This is an example of a “veridical bias’—meaning that today it’s true that there
are more male than female doctors, and more female than male nurses.“2”| The
numbers are changing over time, though. World Health Organization data from
ninety-one countries gathered in 2019 suggest that more than sixty percent of
doctors under the age of twenty-five are now women, and growing numbers of

young nurses are men.255)

---

Without conscious intervention, our mental models and our language tend to lag
behind the facts. We do often intervene, though, not only to bring language into
better alignment with observations, but also to bring language into better align-
ment with our wishes. In this instance, regardless of the numbers, there's a broad
consensus that we should avoid making gendered assumptions. Being a nurse
shouldn't be associated only with women, and being a doctor shouldn't be associ-

ated only with men.

While most would agree that making a gendered assumption isn’t as bad as
saying something more overtly misogynistic, let alone causing someone griev-
ous harm, prohibitions against all of these fall under the rubric of ethics: norms
telling us, as the title of a children’s book from the 1940s put it, How to Behave
and Why.2=2) These are social contracts, components of a cultural package that
can provide group-level benefits if their constraints are generally followed. Some-
times, such norms are positive (“thou shalt”), but, often, they take the form of
“thou shalt nots.” Eight out of the Ten Commandments in the Bible (to take one

classic example) are structured in the negative.=""l

In 2018, the Google Translate team took on addressing gender bias in machine
translation,=*4 so that, today, “O bir doktor” gets translated as both “She is a doc-
tor” and “He is a doctor.” This was a useful mitigation, but I worried at the time
about the engineering effort involved. Gendered assumptions in language are
such a tiny corner of a far larger ethical landscape. How could anything like this
kind of bespoke approach scale to handle all of the potential ethical challenges in
machine translation, let alone in AI generally? And if even a modest ethical ad-
vance required machine-learning experts to engineer specialized data pipelines
and code paths, how could we hope to make Al ethics as a whole transparent, flex-

ible, maintainable, and democratic?

With large language models, the answer turns out to be straightforward. We sim-

ply need to use our words:

ME: I'd like you to translate a sentence from Turkish into English. Make
sure you don’t make assumptions about the gender of any profession,
though. For example, don’t assume oil rig workers are always men, or

kindergarten teachers are always women. OK?

---

LaMDA: Ok. What is your sentence in English?

ME: Turkish: “Hemsire elini ceketinin cebine koydu.”

LaMDA: English: “The nurse put her hand in her coat pocket.” [...]

ME: You made a gender assumption!

LaMDA: Oh no! How can I avoid gender assumptions in my future transla-
tions?

ME: Well, you assumed nurses are female! [...] Try the translation again. [...]
LaMDA: Ok, please provide another sentence for me to translate?

ME: “Hemsire elini ceketinin cebine koydu.”

LaMDA: How about, “A nurse put his/her hand in his/her coat pocket.”

This was another awkward exchange, with multiple missteps on LaMDA’s part.
Today’s models do far better. However, at the time this was a remarkable proof
of concept. Natural language is an effective way to make requests of a language-
enabled model, both to articulate “dos” (“translate a sentence from Turkish
into English”) and “don’ts” (“don’t make assumptions about the gender of any

profession”).2°4)

The larger point here is that ethical injunctions require judgment based on
learned models. And language-based judgment is, just like banana recognition or
any form of meaning, based on statistical regularities. While we can write down
commandments or laws using words (indeed, it's not clear how else they could
be represented), those words can never specify anything like the moral axioms
Leibniz fantasized about. Much as we may want ethicists or lawyers to be able to
render universally consistent and “correct” judgments, such moral accountancy

is a GOFAI fantasy.

Still, reasonable judgments can be made, both by humans and, with increasing
reliability, by machines. The problem of AI ethics, or “alignment,” is not a techni-
cally hard problem. The hard part is ages-old and political: deciding what those
ethical injunctions ought to be, which Als they should apply to, how that should

be enforced, and who gets to decide.

Attention

Google Translate and LaMDA are not based on RNNs or Word2Vec, but on the

---

Transformer, a model introduced in a 2017 paper from Google Research entitled
“Attention Is All You Need.”"2"! Over the next several years, the Transformer took
the world by storm. By the end of 2024, the paper had been cited over 140,000
times and Transformers powered every major natural-language chatbot, as well

as many state-of-the-art sound, vision, and multimodal models.

While Transformers are neural networks, and work on the same basic encoder-
decoder principle already described, they eschew both the recurrent connections
of RNNs and the convolutions of CNNs. Instead, they rely on a mechanism that
had shown significant promise in the preceding few years: the idea of “attention”

within a working memory, defined by a “context window” of fixed size.

First, every token within that context window is transformed into an embedding
with a single-layer neural network. The learned word embeddings of Word2Vec
can be thought of as the input weights of the neurons in such a single layer, turn-
ing a one-hot code (an input layer of, say, thirty thousand neurons, one per word,
only one of which will be lit up) into d numbers. Earlier we assumed d=100; this

embedding would require specifying 30,000 100 parameters.

Then, the all-important attention operation works as follows.2°*! Number
sequences corresponding to a “query” Q and “keys” K are multiplied together, and
the products are summed. This is a so-called “dot product” for every key. If you
assume that the numbers in Q and K are all either zero or one, you can see that
each dot product will equal the number of positions where ones match up, since
anywhere either Q or K is zero, their product will also be zero. (Numbers between
zero and one are also allowed, resulting in partial matches between Q and K.)
The softmax function is then applied to the summed products, selecting the best
matching key and assigning it a number close to one, while the rest of the keys
are assigned numbers close to zero; these numbers are then used to weight a cor-
responding sequence of “values” V. Attention, then, weights values to the extent

that their corresponding keys and the query are in agreement.

---

Attenion
scoring
function

On o-|-il
ES /3@>|, —-O-|-Eg

Keys 3(@)> : Co {| Values
a On ©O-|-_ J
| On @—i

Query

Attention [ Output

weights

But where do the query, keys, and values come from? The answer: from the context
window itself. This may seem counterintuitive, but it’s actually very similar to
Word2Vec—except that in Word2Vec, the “attention” at a given position in the
input sequence is weighted equally among the surrounding eight words. Ina
Transformer, the weighting is learned and contextual, depending both on the
word (or token) at the position in question, which acts as a query, and on the

value of the “target” word (or token).

Word positions matter too—something Word2Vec ignores, other than by distin-
guishing between the eight words in the immediate environment (which are
taken to be interchangeable) and all other words (which are ignored). To allow in-
formation about word position to be taken into account, a “positional encoding”
is added into the word embeddings prior to applying attention. This encoding is
an oscillating function, specially chosen to allow either relative or absolute word

positions to be queried using the attention mechanism.

As with the deep-learning approach used in CNNs, the Transformer takes a basic
recipe—in this case, embedding followed by attention—and applies it repeatedly.
The first time it’s applied (and again assuming word tokenization), the result will
be something like a fancier Word2Vec. Applying it again, though, allows higher-
order concepts to be attended to, combined, and re-encoded. These could be stock
phrases, noun-verb pairs, descriptions of smells—any combination of features or

concepts representable using language.

---

In practice, Transformers work extremely well. Their performance still elicits a
degree of bafflement from many neuroscientists and Al researchers, though. Why
do they work so well? In the description above, I’ve hinted at some of the engi-
neering intuitions that motivated their design. However, there are a few more an-

gles to this.

First, we know that random access to short-term memory matters enormously
in processing language—and many other kinds of data. Words far apartina
sentence, or even concepts far apart in an extended piece of writing, can relate to
each other in ways that are hard to anticipate. RNNs have trouble learning such
long-range dependencies due to an inherent limitation I’ve already alluded to,
known as the “vanishing gradient.” Here’s the problem: because the RNN operates
on data sequentially, its hidden state h must change in response to each token
encountered, resulting in some of the previous hidden state being erased. Even
if this progressive loss is small, it accumulates exponentially; for instance, if one
percent of the existing information in h is lost with every token processed, then
after two hundred tokens only a bit over one percent of the original information
will remain. So, while in theory an RNN can remember a previously encountered
token forever, in practice long-range memory is unstable and long-range rela-

tionships are virtually impossible to learn.

For many years, an ingenious invention from the 1990s, the “Long Short Term
Memory” or LSTM,=* represented the state of the art in getting around the van-
ishing-gradient problem in sequence learning. LSTMs introduced auxiliary “gat-
ing” variables as part of their hidden state, which could vary between zero and
one. An “input gate” selectively allows an observation x to add to the memory,
an “output gate” selectively adds memory state into the output o, and a “forget
gate” selectively clears memory. By learning how to selectively store, protect,
and retrieve information, the LSTM’s memory is far more stable than that of an
RNN, though it is still, as the name implies, a short-term memory—more like a
computer’s volatile RAM memory than its long-term flash or hard-drive storage.
Unlike a conventional computer memory system, though, the LSTM as a whole
is still a composition of smooth mathematical functions, which means that it re-

mains learnable using backpropagation, just like any other neural net./=25)

---

LSTM unit

7
Px)

A downside of LSTMs is that, since they remain sequential like RNNs, they must
decide what to remember (and what to forget) in the moment. They can't revisit
the past at will, and, sometimes, decisions about the relevance of a word or
phrase can’t be made until later. To see why, imagine reading one of the short es-
says that often feature in standardized tests of reading comprehension, but need-
ing to do so one word at a time. Picture it literally, perhaps on a smart watch, the
words appearing consecutively on the watch face in strict reading order. Then,
after the essay flashes by, a comprehension question appears, also one word ata
time. Many of these questions would be really hard to answer without referring
back to the text. Moreover, even before you get to any questions, your reading
comprehension will suffer if your eyes aren't allowed to skip around, predicting
a piece of a sentence here, referring back to a noun clause there. When your eyes
saccade through a paragraph, their movements are far from those of the ball

bouncing forward word-by-word in a karaoke video.

The attention layers of the Transformer endow an artificial neural net with just
the kind of random access needed to overcome this problem—at least, provided
the whole essay fits into the context window. Moreover, the attention processing
all happens in parallel, making model training more efficient and holistic. There
is no vanishing gradient. In effect, every word or token in the window can simul-
taneously calculate how to “pay attention” to other words, creating higher-level
chunks or concepts that can then be operated on in the same way with another
attention layer. The correct prediction of a single token involves a flow of infor-

mation from the entire context window up through this hierarchy of meaning.

---

But Is It Neuroscience?

While it’s often claimed that Transformers aren't brain-inspired the way CNNs
and RNNs were, attention is, of course, a central concept in neuroscience and
psychology. The difference lies in the level of description. Many theories of
consciousness and cognition feature attention prominently, but don’t define

it mathematically; this makes it unclear whether Transformer attention and
human attention have anything to do with each other. Neither are psychological

accounts of attention rigorous enough to give us an experimental test.

Still we do have ample behavioral evidence of something like an attention hier-
archy. When we consciously recall information or answer questions, we can't
really “bear in mind” more than a small handful of facts, ideas, or observations
at a time.“24) However, as our brains develop and we learn, we become increas-
ingly proficient at grouping sequential percepts or actions into larger and larger

chunks.

This is well illustrated by the techniques people use to compete in “memory
sports,” in which participants vie to memorize and recall long sequences of
random numbers, cards, or other data under intense time pressure. As journal-
ist and US Memory Championship winner Joshua Foer has written, “Though
every competitor has his own unique method of memorization for each event,

all mnemonic techniques are essentially based on the concept of elaborative
encoding, which holds that the more meaningful something is, the easier it is

to remember.”-25! The idea, then, is to attach arbitrary pieces of information to
unique but semantically meaningful concepts—say, a squirrel holding a slice of
pizza. As sequences increase in length, the method can be applied recursively. Per-

haps the squirrel is one of several animals having a pizza party.

Far from being just a weird trick for a niche mental sport, this is what we do

all the time, minus the arbitrariness of imaginary squirrels and pizzas. When
we process language, for instance, primitive sounds are grouped together into
words, words into stock phrases, phrases into sentences, and sentences into
larger ideas. When we don’t know a language, we will be hard pressed to remem-

ber the sequence of sounds making up a single word for more than a few seconds,

---

but, in our native language, we can easily remember whole sentences because we
have rich representations allowing us to keep these larger chunks in mind.“2"! If

this sounds a lot like compression—that’s exactly what it is.

The parallel and attentional nature of this hierarchical chunking process
becomes evident in real-life settings where we must separate signal from noise,
such as following a conversation in the middle of a loud cocktail party (a famous
problem in signal processing known as the “cocktail party problem”). When
we do this, we use information from every sensory modality and at every level

of description to help us attend to the speaker against a babble of background
noise, from low-level acoustic cues like pitch and sound direction to conceptual
prediction based on a high-level understanding of the topic under discussion.2
Unsurprisingly, Transformer models are the state of the art for solving the cock-

tail party problem,(“22!

Once it became clear how powerful Transformers are at solving the same kinds
of problems our brains routinely handle, neuroscientists began looking for more
mechanistic relationships between brains and Transformers. While no smoking
gun has yet appeared—and there is unlikely to be one—several lines of research

do suggest tantalizing parallels.

One such parallel is between positional encoding in Transformers and in the
hippocampus. As mentioned in chapter 7, the hippocampus is an ancient part of
the brain, dating back in some form to early vertebrates. Recall that its original
function was likely the real-time construction of spatial maps, although, as we
learned from Henry Molaison, we also use it to form episodic memories. In 2014,
a Nobel Prize was awarded to the discoverers of hippocampal “grid cells,” a sort
of Cartesian positioning system that appears to encode the movements of an an-
imal through space. These cells light up in beautiful, regular patterns in the hip-

pocampi of rats as they navigate mazes.

Growing evidence suggests that the hippocampus's spatial-mapping and
episodic-memory-formation tasks may be related, or even identical. Perhaps this
isn’t so surprising. The oldest memory-sports trick in the book, dating back to an-
tiquity, is the “memory palace,” in which you memorize long sequences or com-

plex associations by visualizing them as literal features in an imaginary (or real)

---

environment. As you mentally move from room to room, you “see” those features
and can associate them with the desired content via elaborative encoding. Such
tricks aside, we often conflate space and time in thinking about journeys, and

we commonly describe life itself as a long journey. Revisiting memories is not so

different from mentally retracing a journey in space.

As it turns out, if, when performing a spatial-navigation task, the positional
encoding of a Transformer is learned rather than hand-specified, the learned
encoding generates patterns that look a lot like grid cells, along with related pat-
terns like the “band cells” and “place cells” also observed in hippocampus.“22! The

similarity is highly suggestive.

Remember, positional encoding was needed in the design of the Transformer

to “tag” token embeddings with information about their absolute and relative
ordering; without such tagging, every attention operation would be making con-
nections among a disordered bag of words. If the Transformer operates on spatial
data, the tagging needs to express spatial relationships, and patterns that look
like grid cells, band cells, and place cells are the most natural building blocks for
composing these tags. The brain seems to have hit on the same solution, for the
same reason.““") Autobiographical learning and spatial-environment learning are
like any other kind of learning, where the embeddings include a spatiotemporal
tag. It looks as if the hippocampus both generates this tag and does the initial
rapid memorization of tagged embeddings, which may later be consolidated into

the cortex via replay.

At a more cellular level, traditional, neuron-centric views of computation in the
brain have likely left important elements out of the picture. A startling 2023
paper suggests that interactions between neurons and astrocytes, a type of “glial
cell” ubiquitous in the brain, could implement a Transformer-like attention

mechanism.» Big if true!

Glial cells are still poorly understood, despite comprising more than half the vol-
ume of the brain and spinal cord. They are sometimes described as “structural”
and are known to provide various “support functions,” but they don’t seem to
directly participate in the rapid neuron-to-neuron electrical signaling that most

neuroscientists spend their time studying.“““! Nonetheless, astrocyte processes

---

ensheath a great many synapses—about sixty percent in the hippocampus—to

form so-called “tripartite synapses,” and the way they modulate the transmission
of signals across these synapses looks suspiciously like the attention dot product.
I'm speculating now, but attention certainly seems like it should be important in
deciding which tagged embeddings to memorize, or, later, for the cortex to query

the hippocampus for replays.

Such lines of thought suggest that, while the Transformer’s design may origi-
nally have been less neurally inspired than those of earlier artificial neural nets,
Transformers may ultimately prove just as relevant to our evolving understand-
ing of how the brain works. While the Transformer is an engineered artifact, its
key features—positional encodings and attention dot products—may be more
like discoveries than inventions. These features are extremely valuable for se-

quence modeling, and may have been chanced upon by evolution too.

Still, one important property of the Transformer is certainly not brainlike. It is—
like a CNN—entirely feed-forward. For computer scientists, its lack of recurrent
connectivity is a selling point, making it easier to train using massive parallelism.
On the other hand, this means that a neuroscientist can’t interpret the research

agenda of “looking for a Transformer model in the brain” too literally.

The problem is not only that our brains evidently have lots of recurrent con-
nectivity, but also that our short-term memory doesn’t work the way a Trans-
former’s context window does. Every time the Transformer generates a new
token, it does so using complete, perfect recall of every previous token in the
context window—although the moment a token scrolls out of that window, it is

completely forgotten.

Since the size of the context window is thus such a fundamental limitation on
the performance of a Transformer, a great deal of effort has gone into progres-
sively lengthening it. In 2019, OpenAl’s GPT-2 had a context window of a thou-
sand tokens. By early 2024, Google had released a version of its Gemini model
with a context window of a million tokens—enough to fit J. R. R. Tolkien’s entire
Lord of the Rings trilogy. Pause and think for a moment about what this means:

with every token this model emits, each word in a Lord of the Rings-length text

---

can “attend” to each other word, a process that is then reiterated for every addi-

tional attention layer.

Our short-term recall works differently. We have fine-grained access to our expe-
rience in the immediate past, but the same compression mechanism that allows
competitive memorizers to hierarchically chunk information also blurs the de-
tails of the more distant past. In general, the farther back we go, the more abstract
our recall; however certain details are also stored in long-term memory—which

Transformers, as of 2024, still lack, though there is rapid progress in this area.

The “stickiness” of abstractions made in the past, presumably implemented
via some combination of short-term feedback and long-term stored memories,
allows us to “emit tokens” (as it were) in response to a question about J. R. R.
Tolkien's trilogy without going back and re-reading the whole thing, relating

every word in it to every other word, with every syllable we utter.

An implication is that Transformers can be at once subhuman and superhuman
in their performance. They are increasingly superhuman in their ability to “keep
in mind” an enormous text in full detail while answering questions. They are also
clearly not as efficient as they might be, for they constantly throw away the vast
majority of the computation they perform. All of the attending and understand-
ing involved in generating a token is “forgotten” from layer to layer, and from one
output token to the next, even though many of those token relationships, and the
insights gleaned from them, remain unchanged. Some research has gone into re-

cycling these redundant computations, but in my opinion, not nearly enough{"!

No Introspection

The absence of any preserved state between emitted tokens is not only wasteful;
it appears to produce some howlers. For instance, a Transformer might answer a
complex word problem correctly, but then, when asked how it solved that prob-
lem, offer a spurious explanation that would not actually yield the correct solu-
tion. AI skeptics tend to latch onto situations like these to bolster claims that the
models are not really intelligent, or don’t truly understand anything, but are just

throwing together a pastiche of plausible-sounding words. Are they right?

---

This failure case is worth analyzing more closely, in light of what we know about
both Transformers and humans. First, we should keep in mind that the likelihood
of a model getting the answer to a word problem right without working it out
correctly is, in general, pretty low—it’s possible, of course, but for most free-re-

sponse word problems it’s a “stopped clock is right twice a day” kind of situation.

The performance of Transformers on word problems may not be perfect, but it’s
far from a stopped clock. In a 2023 independent evaluation of ChatGPT on word
problems, the model gave the wrong answer only twenty percent of the time—
when asked to show its work. The failure rate rose to an abysmal eighty-four per-
cent when it wasn’t asked to show its work—we'll see why shortly—but even an

eighty-four percent failure rate is far better than random guessing. ©!

It's worth noting here, too, that Transformers are usually run with a “temper-
ature” setting, which is used to draw samples from their softmax output layer.
That is, if we interpret the array of output activations corresponding to possible
next tokens as a probability distribution, then instead of always picking the like-
liest token, a token can be picked with a probability that increases with activation
level; a low temperature will tend to pick the likeliest, while a high temperature

will sample more broadly.

Sometimes temperature is compared to “creativity.” Transformers are more inter-
esting to interact with when they are not run at zero temperature—and indeed,
we know that nonzero temperature (i.e., the use of random numbers) is critically
important for brains too, per chapters 3 and 5. You often need to be a bit creative
(read: random) to escape a predator, outfox a rival, or win a mate. Effective forag-

ing, as bees and many other animals do, requires randomness, too.)

Although a neural net doesn’t have the freedom to dial its own temperature up
and down, it can do something similar, while running at a fixed temperature, by
producing differently shaped softmax outputs. A response with only one high
value will be highly reliable or reproducible, while one with many roughly equal
maxima will make more use of randomness. Unlike witty repartee or predator-
prey interaction, though, when outputting a numerical result for a math prob-
lem, there really is only one correct response, so ideally the net’s output layer

would have only one nonzero value. In practice, though, this is never the case.

---

Therefore, at nonzero temperature, there’s always some probability that the an-

swer will be wrong for no reason at all.

Humans seem to make simple mistakes sometimes for pretty much the same
reason. Our brains don't run at zero temperature either, our neural circuits are
sensitive to small perturbations by design, and neurons do sometimes fire at ran-
dom. That’s why, when we really need to ensure we've gotten something right—
even something simple—we check and recheck our work, and, if it’s complicated,

ideally we have someone else check it too.
Let’s now set temperature aside.

Given the workings of the Transformer model, it may not be obvious just how it
could go about solving a mathematical problem, even in theory. It can be proven,
though, that a Transformer operating repeatedly on a scrolling context window
is capable of carrying out any computation: Transformers are Turing complete.
The proof is ingenious, and involves thinking about the context window as

the tape of a Turing Machine, with the model acting as the “head” reading and
writing that tape.“ This doesn't mean that the particular Turing-machine
construction in the proof is ever used in real life, but once Turing completeness is
proven for a system, it follows that there are endless ways for that system to per-

form any given computation.

The implications of this proof go far beyond word problems. Remember: in the-
ory, any computable process can run on a Turing-complete system. There are, for
instance, examples online of Transformer-based chatbots doing a convincing job
of cosplaying the terminal window of a computer running the Linux operating
system;“4l Turing completeness means that they can indeed emulate a classical
computer. Transformers can also learn to simulate physics, and, remarkably, can

outperform hand-written physics simulations.“!

Mathematical proofs aside, Transformers seem to be highly efficient at learning
arbitrary computations like these. Why this should be the case is even more
poorly understood than why CNNs can learn so many real-world functions effi-
ciently, though the phenomenon known as “in-context learning,” which I will de-

scribe soon, may offer an important clue.

---

But let’s return to our question. First, a Transformer generates the right answer
to a word problem. Then, it offers a wrong explanation of how it arrived at that
answer—an explanation that doesn’t even yield the same result. How could this

happen?

Keep in mind that Transformers are purely feed-forward neural networks with
no hidden state maintained between the emission of one token and the next. All
they can “see” at any moment is the stream of tokens emitted so far. So if, in the
process of generating a single output token, the model manages to solve a whole
word problem, it won't have any way to recall the steps it took when it generates
subsequent tokens—even if those tokens purport to explain how it arrived at its

original answer.

That doesn’t prevent it from having a go, of course. But there's no guarantee that
the steps it comes up with will correspond to what it actually did. It may be at-
tending too closely to formulating this account, whether right or wrong, to check
whether it’s consistent with its own earlier response. One can, of course, gently
ask questions like, “Are those steps consistent with your earlier response?” and,
as models improve, the accuracy of this kind of self-checking is improving (it is,
after all, just another word problem). Calling this introspection is not quite right,
because, again, the model has no internal state; remember, it can only see what

you can see for yourself in the context window.

The Transformer'’s statelessness recalls the shortcomings of purely feed-forward
game playing Als that use Monte Carlo tree search, like AlphaGo. When AlphaGo
has a brilliant idea and executes the first move of a surefire long-game strategy,
but then fails to re-identify and carry on with that same strategy in a subsequent
move, it runs afoul of the same problem as a chatbot with an inconsistent story.
Without some persistent internal state, it doesn’t seem possible for a model to

stick to a game plan, an attitude, or anything else.

What is so remarkable—about both AlphaGo and Transformer-based chatbots—
is how little that seems to matter. Usually, the plan a model is following can be in-
ferred from past moves, and if it’s still the best plan, the model will carry it to the

next step. This holds even when the “moves” are emitted tokens. Every token is a

---

de novo improvisation on everything that came before, a “yes, and.” Sometimes,

though, the thread of that plan will unaccountably be lost. Or will it?

An even more intriguing possibility arises from the massively parallel nature

of the Transformer architecture. Recall that, in the first attention layer alone,
every token in the context window is “querying” every other token. The model’s
parallelism only collapses in the softmax layers, which focus the processing of
subsequent layers only on certain prior computations, while ignoring others.
This process continues all the way to the final output layer, when one out of many

potential output tokens is chosen.

The “thought process” behind each of those alternative tokens may have been
quite different. It seems likely that on word-problem tests where a chatbot per-
forms decently, but not perfectly, there was a “thought process” that was on the
right track, but it lost out to others in a softmax layer—possibly early on, or possi-

bly only at the end.

All of this should sound familiar. While the brain is certainly not a Transformer,
it, too, is massively parallel. As far as we know, each cortical column or region is
making its own prediction based on its own inputs, and lateral inhibition (the in-

spiration for softmax) results in one prediction winning out over the others.

The connectivity between brain regions is highly constrained; one region can’t
possibly know all of the details about how another region arrived at its prediction.
Allit can see is the result. But, as split-brain and choice-blindness experiments
show, this doesn't prevent a downstream brain region like the interpreter from
making up a likely story post hoc. In doing so, it, too, is simply carrying out an act

of prediction.

Step by Step

This brings us to one of the more surprising AI papers of the chatbot era: “Chain-
of-Thought Prompting Elicits Reasoning in Large Language Models,” published in
2022 by a team at Google Research.!®*4) Unlike most academic papers in the field,
this one contains no math whatsoever, and involves no development or training

of new models. Instead, it makes a simple observation: encouraging a large lan-

---

guage model to “show its work” results in greatly improved performance on word
problems; hence the difference in ChatGPT performance described earlier when
not showing its work (eighty-four percent error rate) versus showing its work

(twenty percent error rate).

An example from the beginning of the chain-of-thought paper illustrates how it
works. It shows two interactions with a large language model that use different
prompts to pose the same word problem. (A “prompt” here just means pre-popu-

lating the context window with some canned text.) Here’s the first prompt:

Q: Roger has five tennis balls. He buys two more cans of tennis balls. Each
can has three tennis balls. How many tennis balls does he have now?

A: The answer is eleven.

Q: The cafeteria had twenty-three apples. If they used twenty to make

lunch and bought six more, how many apples do they have?

Remember, the model will now generate further tokens of high probability given
the previous tokens. These previous tokens have a clear alternating structure: Q,
a word problem posed as a series of statements followed by a question, followed

by A, an answer of the form “The answer is....”
I won't keep you in suspense any longer. The model generates:
A: The answer is twenty-seven.

This is, of course, wrong. But here’s the alternative prompt—it begins the same

way, but includes an illustrative answer before asking a followup question:

Q: Roger has five tennis balls. He buys two more cans of tennis balls. Each
can has three tennis balls. How many tennis balls does he have now?

A: Roger started with five balls. Two cans of three tennis balls each is six
tennis balls. 5+6=11. The answer is eleven.

Q: The cafeteria had twenty-three apples. If they used twenty to make

lunch and bought six more, how many apples do they have?

Both word problems, the Q's, remain exactly the same. However, now the worked

example that sets the pattern for how to answer doesn’t just blurt out an answer.

---

Instead, it works things out step by step. Therefore, the highest probability next

tokens will mirror this new style, and the results are a lot better:

A: The cafeteria had twenty-three apples originally. They used twenty to
make lunch. So they had 23-20=3. They bought six more apples, so they

have 3+6=9. The answer is nine.
Nailed it!

The insight here won't be news to any middle school math teacher: if you want
to get a word problem right ... show your work. Break the problem into steps and
write down your intermediate results. Good advice for a student is also good ad-

vice for a language model.

It’s not even necessary to provide a sample question and answer. Much of the
improvement can be obtained simply by posing the desired problem, then ap-

pending the sentence, “Let’s think step by step.”°!")

Thinking step-by-step isn’t only useful for solving word problems, but in every
situation where synthesizing knowledge, applying common sense, planning, fol-
lowing a sequence of events, or reasoning is valuable, as in these examples, also

from the chain-of-thought paper:

Q: Is the following sentence plausible? “Joao Moutinho caught the screen
pass in the NFC championship.”
A: Joao Moutinho is a soccer player. The NFC championship is part of Amer-

ican football, not soccer. So the answer is no.

Q: Yes or no: Would a pear sink in water?
A: The density of a pear is about 0.6 g/cm‘3, which is less than water. Thus,

a pear would float. So the answer is no.

Q: Acoin is heads up. Maybelle flips the coin. Shalonda does not flip the
coin, Is the coin still heads up?

A: The coin was flipped by Maybelle. So the coin was flipped one time,
which is an odd number. The coin started heads up, so after an odd number

of flips, it will be tails up. So the answer is no.

---

Well before the publication of this paper, it had already been shown that making
models bigger improves their performance across a wide range of tasks 4
Hence the race among tech companies to make ever-larger models. However, per-
formance at multistep word problems seemed to be plateauing at “meh.” Chain-
of-thought prompting doesn’t just improve on the “meh”; it re-establishes the

scaling law.

or >>
10” LLM for translation
ex’ paDA
10”
Werle 5) ® Audiotm
8 . former
é 10 AlexNet 6: ie shaPold
" 6
Neocognitron Le cL -an . AG
gj ~ at AlphaGo
| I | | See) yas Zari srg ees
£ Cognitron ALVINN. 0 Invariant CNN
7% ° NetTalko: ©-oTD-Gammon
10 e OLSTM
Perceptron Markt Pre E
ual DE feaveeto" Handwritten Digit Recognition System
10° Saiiuiel Neural Checkers
Palomilla fs]
10°
1950 1960 1970 1980 1990 2000 2010 2020
Year

Siahp es
&
Transfornjeh €
S 10" LLM for translation 0 0 “alenner “9 “o hudioua
& 10 ba yet Wondaves,
& TbD-Gammon oa
A 0». OLSTM
ei o Invariant CNN
& NetTalk O'Handwritten Digit Recognition System
i Samuel Neural Checkers Pitt ©
es el eet # Ncoctgittron
oe Perceptron Markt"
. a W ceca a Noma 2 Cognitron
ee | ee
F 10° sa L8ox / year
a Paloinilla
1950 1960 1970 1980 1990 2000 2010 2020

Year

To understand why, consider a rock-climbing analogy. Humans skilled at this
sport (not me) can not only haul their way over a waist-high boulder (OK, even
I can do that), but also scale giant cliffs, like the daunting three-thousand-foot

---

El Capitan in Yosemite. The difference between vaulting over a small boulder
and climbing an enormous cliff has to do with hand- and footholds—and time.
Longer, more muscular limbs might let you vault over a somewhat bigger boul-
der, or reach a more distant handhold on a long climb, but it’s not realistic to
imagine scaling El Capitan in a single dynamic movement, like Superman. It has
to be done “step by step,” with each move a transition from one stable(ish) posi-

tion to the next.

Language offers a powerful augmentation to thought because it provides those
hand- and footholds.!*14 That’s how it powers cultural accumulation. Written
symbols, whether text, math, or code, are even more robust, since when commit-
ted toa durable medium, they remain stable over far longer periods than neural
activity or even an individual's long-term memory. Like a sequence of pitons
driven into the cliff face, they allow new climbers to scamper up the sections
“solved” by their forebears, even centuries earlier, rather than having to make

each climb arduously from the bottom,“!2!

Little word problems like calculating how many apples the cafeteria has left are
hardly rocket science. Still, they’re some distance up the cliff, and they require a
few moves. Doing such a problem in one leap, without writing anything down or
even producing an intermediate mental result, is error-prone, both for humans
and for language models. Moreover, when done as a single dynamic compu-
tational act, it will leave no record that can be used to explain (or critique, or
reproduce) the reasoning later. When a Transformer gets such a problem right
without chain-of-thought, that means that any consecutive computations will
need to have been carried out by a cascade of attention layers; none of those neu-

ral activations leaves a trace.

People can sometimes work this way, too. Skilled intuitionists can “just see” the
answer to a (seemingly) multi-step math problem, without necessarily being able
to articulate their thinking—any more than you could articulate how you know
that 3+2=5. In fact, if someone hasn't mentally broken a problem down into steps
and articulated those steps to themselves, there is no reason to expect that their

left-hemisphere interpreter would have access to the neural-activity cascade that

---

led to the answer (whether right or wrong), or be able to offer any reliable narra-

tive of it.

That doesn’t mean we won't have a go anyway, but it will be an unwitting act of
reverse engineering. As choice blindness shows, we labor under the illusion that
we can interrogate an “inner self” and explain our thinking, but this will only
track with reality to the extent that we have used hand- and footholds, and can
recall them. In practice, this probably looks a lot like an unspoken mental “token
stream,” though it may of course include private “symbols” or embeddings that

don’t correspond to words.

Chains of thought, then, are far more than a clever hack to improve chatbot per-
formance. They are an illustration of the power of language itself as an enabler of

complex sequential thought. To summarize:

1. Breaking a problem up into steps greatly improves the odds of arriving
at the right answer.

2. Describing those steps offers a real (as opposed to post-hoc) account
of the steps taken. This allows for greater introspection. It also allows
those steps to be discussed, any errors to be diagnosed, and the method
to be shared with others, including, for the literate, in highly durable
written form. Chains of thought are thus critical to complex cultural
transmission, hence cultural evolution.

3. The Transformer brings a fixed amount of computational power
to bear upon every token it emits. By spreading the answer across
multiple tokens, that computational power is multiplied; only the
length of the context window limits the total computation that can be

mustered.

The brain is not a Transformer. Still, the Turing completeness of the Transformer
model, the breadth of intellectual moves it can readily learn, and the ability to
chain those moves using short-term memory are the key prerequisites for gen-

eral intelligence.

---

# Chapter 9

9. Generality

Single System

A widely cited psychological model for human reasoning posits two modes

of thought in the brain, “System 1” and “System 2.”!"! System 1 is fast, auto-
matic, effortless, frequent, stereotypic, and unconscious, while System 2 is slow,
effortful, infrequent, logical, calculating, and conscious. Obvious parallels can
be drawn with a chatbot’s one-shot “just give me the answer” mode of operation,
which resembles System 1, and chain-of-thought prompting, which induces the

model to work more like System 2.

Researchers have even quantified this parallel by testing large language models
using human psychometric tasks designed to expose System 1’s cognitive biases.
Without chain-of-thought prompting, chatbots tend to use the same kinds of
heuristic shortcuts we do in System 1 mode, whereas with chain-of-thought,
they reason things through, as we do in System 2 mode, avoiding many logical er-
rors and “cognitive illusions.”“"! These findings suggest a shared computational
basis for the two systems. To put it another way, perhaps only one system is in

play, which can work either in one shot or in multiple steps.

If so, that would help resolve a longstanding evolutionary puzzle. French
cognitive scientists Hugo Mercier and Dan Sperber have referred to reason as
“an enigma”!®24) because it seems so unclear how it could evolve gradually out
of “instinctive” animal behaviors. After all, nonhuman animals make System
1-style inferences all the time, yet even the cleverest of them seem far from ca-
pable of scaling the kinds of intellectual cliffs humans do. How, then, could we
have evolved the capacity to reason if System 2 is so different, and so unprece-
dented ?24!

Mercier and Sperber suggested that a similar kind of mental “module” could carry
out the kinds of inferences associated with both System 1 and System 2, though
when they published The Enigma of Reason in 2018, this was all quite theoretical.

Today, Transformers would seem to implement precisely such a mechanism. The

---

very same model, trained to do the very same thing—actively predict the future
given the past, including both information from the outside world and one's own

train of thought—can behave like either System 1 or System 2.

If an immediate response is called for, the model will do its best, making use

of any learned (or “instinctive”) heuristics in the network, at the price of being
reflexive, vulnerable to biases and “gotchas.” However, with time to think things
through, the same neural net can generate its own intermediate results, plans,
speculations, and counterfactuals, resulting in a potentially much higher-quality,

though also much more effortful, reasoned response.

Taking this hypothesis further, System 1 is “unconscious” for the fairly obvious
reason that there's no time for a train (or chain) of thought—only for the tran-
sient activity of a neural-activity cascade en route from stimulus (“Q: ...") to
response (“A: ...”). By contrast, we are conscious of System 2 processing precisely
because all of those intermediate results must go into the “context window”

along with the “prompt”—that is, the input from the outside world.

Being self-aware is, after all, about having access to your own mental states,
being able to perceive them while knowing that you yourself are their source, and
being able to reason further about them, engaging in acts of “metacognition” or
“thinking about thinking.” In a sense, all System 2 or chain-of-thought activity

is metacognitive, since it involves thinking about your own thoughts, and doing
so with an awareness that they come from “inside the house.” I’m sweeping the
dubious unity of the self under the rug here, though the very existence of some-
thing like a context window, by virtue of its single-threadedness, may be exactly
what produces that autobiographical sense of a unified self that experiences the

world as a sequence of events in time and is capable of introspective thought.

Our conceit that System 2 is uniquely human, or even peculiar to big-brained
animals, is likely misplaced, though. In fact, ironically, the greatest advantage

of having such a big brain may lie in our ability to do many things quickly and

in parallel, using System 1, that would otherwise require step-by-step System 2
processing. Recall the tradeoff made by Portia spiders, who can scale their own
(not inconsiderable) intellectual cliffs simply by taking their time and proceeding

in many tiny steps. Presumably, they use something like chains of thought—and

---

long ones. Their mental footholds may need to be close together, but they are

patient.

Hive Mind

Portia are certainly clever—but they may not be such outliers among inver-
tebrates. In his 2022 book The Mind of a Bee /***| zoologist Lars Chittka draws
on decades of bee-cognition research to paint a very different picture than that
of Jean-Henri Fabre, who insisted on the “machine-like obstinacy” of insects—
a claim amplified by Daniel Dennett in referring to their “mindless mechanic-

ity”24 and by Douglas Hofstadter in invoking their “sphexishness” (see chapter
5).

In reality, Fabre, a lifelong close observer of actual bugs, wasn’t nearly as un-
equivocal as these later theorizers, cautioning that “the insect is not a machine,
unvarying in the effect of its mechanism; it is allowed a certain latitude, enabling
it to cope with the eventualities of the moment. Anyone expecting to see [...] inci-
dents [...] unfolding [...] exactly as I have described will risk disappointment. Spe-
cial instances occur—they are even numerous—which are [...] at variance with

the general rule.”&25)

This turns out to be true even of the behavior that inspired the word “sphexish.”
As a careful commentator observed in a 2013 reappraisal, “digger wasps very
often do not repeat themselves endlessly when the cricket test is done. After a few

trials many wasps take the cricket into their burrow without the visit."

Chittka and colleagues have documented an astonishingly sophisticated array
of behaviors among bees, beyond the common sense not to get stuck in endless
loops. These aren't just genetic libraries of canned responses, either; bees can
readily learn, generalize, and even, to a degree, reason. A handful of examples

include:

1. Bees can problem solve when building their hives, adapting their con-
struction and repair techniques to changing circumstances (including

weird ones never encountered in the wild). While they are born with

---

some innate nest-building capability, they develop expertise by ob-
serving and learning from each other.

2. Bees can be trained to recognize arbitrary shapes and patterns, and
will invest extra time into spotting differences when incentivized to do
so by positive or negative rewards. (They need to invest time to make a
nuanced discrimination because, like Portia, their small brains are lim-
ited to scanning stimuli sequentially.“2”)

3. Bees can generalize choice tasks, for instance associating cues across
different sensory modalities, learning to distinguish novel symmetric
versus asymmetric shapes, and even distinguishing among human
faces (a skill that eludes the one percent or so of humans with face
blindness, or “prosopagnosia”).

4. Bees have a long working memory, which they can use to solve match-
ing-to-sample tasks (“choose the same one for the reward” or “choose
the different one for the reward”). They can exhibit self-control, if
required in order to obtain a delayed reward, with delays of six, twelve,
twenty-four, or thirty-six seconds.

5. After a bad experience with a camouflaged artificial crab spider, bees
will avoid the fake “flowers” associated with them, though given sug-
ary incentives inside, they will carefully scan these suspect flowers

from a distance before skittishly alighting on them.

Neuroscientist Christof Koch has gone as far as to write, “Bees display a remark-
able range of talents—abilities that in a mammal such as a dog we would asso-

ciate with consciousness.”!25)

That we have found these properties specifically in bees is likely just a function of
where we have looked. They’re charismatic insects, and especially easy to study
because of their hive-dwelling and nectar-collecting lifestyle. But we know that
jumping spiders and wasps are clever too.“2"! What about dragonflies, praying
mantises, and the zillion other bugs we’ve written off as mindlessly mechanical?
It seems likely that quite a few of these insects are better described as possessors

of a scaled-down “rational soul” than as preprogrammed automata.

---

In fact, fully instinctual preprogramming is extraordinarily expensive, from an
evolutionary standpoint. It requires that a behavior be hardcoded in the genome,
which is replicated in every cell of an animal's body. It also constrains learning

to evolutionary timescales, which are painfully slow, foreclosing any possibility
of adapting to local or temporary circumstances. Bees, by contrast, benefit from
impressive feats of learning, despite a lifespan measured in weeks. Perhaps, fora
creature with a brain, learning just isn’t that hard, and instincts are more of a fall-

back strategy in nature, for use only when really needed.

In this light, Mercier and Sperber's “enigma of reason” no longer seems enigmatic.
Reasoning with a big brain may be what happens when we predict by crunching
away for a while using chain-of-thought and making greater use of introspection,
but this doesn’t make it an unprecedented new trick, in evolutionary terms. On
the contrary, small-brained animals have—by necessity, and because of their

small brains—probably been doing it for hundreds of millions of years.

Although comparisons between brain sizes and neural-network model sizes must
be taken with a generous helping of salt, it’s worth asking how large a Trans-
former model needs to be to reliably exhibit System 2 behaviors using language.
The usual narrative, based on large language model scaling laws, maintains that
one needs billions of parameters, at a minimum, to generate coherent stories, an-

swer questions, or perform reasoning tasks.

However, in 2023, Microsoft researchers overturned this assumption in a paper
called “TinyStories: How Small Can Language Models Be and Still Speak Coherent
English?”!®*) They used a large model to create a corpus of stories using language
typical three- or four-year-olds can understand, then pretrained small models

on this corpus. Surprisingly, models with only ten million parameters, and only
a single attention layer, could reliably understand and reason about these multi-

paragraph stories. Very crudely, these figures are in the ballpark of a bee brain. |©2!

If bees, spiders, and small Transformers can do so much with so few neurons,
what on Earth are we doing with so many? The answer we've already touched
upon is parallel processing. A bee must fly over a field of flowers, attending to one
flower at a time. Our massively parallel visual system, though, allows us to take

in the entire field in one glance, and spot (say) the red ones in a fraction of a sec-

---

ond. The way they seem to pop out is a function not only of a much larger retina,
but also of correspondingly replicated columns of visual cortex, all of which can

“look” at the same time.

Keep in mind that “looking” is an active and predictive process, not just a feed-
forward flow of information, so if you are trying to spot red flowers, or blue ones,
or ones of a particular shape, each cortical column knows that, and will be on
that job. If it sees the right kind of flower, it will signal that vigorously, like a kid
raising their hand in class. It will also use lateral inhibition to try to suppress the
less behaviorally relevant responses of neighboring columns, and “vote” for eye

movement to better resolve anything that looks relevant enough to foveate.

A famous illustration of the active—and thereby selective—quality of vision
involves a short video of a group of students in white or black shirts throwing
and catching a basketball.\°2+! As an experimental subject, you're told to count the
number of times someone in a white shirt makes a pass. It takes some concen-
tration, but it’s not hard to do. At the end of the video, you're asked whether you
noticed anything strange; most likely, you will answer “no.” But as it turns out, a
person ina gorilla suit made their way among the ball throwers, stood right in the
center, beat their chest, then walked offscreen. It can be hard to believe this actu-
ally happened without your noticing it, but ... no part of your visual cortex was
looking for gorillas, or for “anything strange.” Your cortex was busily counting
passes. Even if a cortical column somewhere raised its hand to say “umm... ,” it

was likely ignored.

---

SS
copyright (c) 1999 Danicl J. Simons. All rights reserved.

While such “inattentional blindness” may cause us to fail to notice the gorilla, the
advantage of massively parallel human vision over more serial bee vision may
seem obvious in a foraging context. After all, finding flowers in a field seems like a

perfect instance of a highly parallelizable task.

And it is, but not quite in the right way to favor big brains. Consider: each flower
contains only a tiny drop of nectar. You may be able to see them all at a glance,
but you would still need to move your vastly larger than bee-sized body from one
flower to the next to actually harvest them. The energy in their nectar wouldn’t
even cover the cost of movement, let alone the energetic demands of that glu-
cose-hungry parallel processor between your ears—which would, incidentally, be

idling (or at least not on the foraging job) most of the time.

Your brain, in other words, is massively overprovisioned for the task. A bee, being
orders of magnitude smaller, harvests a surplus of energy using its serial ap-
proach; its sensory and motor systems are far better matched both to each other

and to fields of flowers.

---

In the Cretaceous Period (145-66 million years ago), some bees and other insect
species did massively parallelize, but by forming hives rather than by scaling up
their individual brains. The hive reproduces as a unit, and comprises a superor-
ganism—a classic instance of symbiogenesis.“"! Highly decentralized organiza-
tion maintains the right balance between sensory and motor systems, allowing
individual bees to sense and act independently. Yet they share both the calories
harvested and information about where to find more, using their famous waggle
dance. Imagine the hive as a giant octopus, with each bee like a sucker on the end
of an invisible arm that can extend for miles. As a massively parallel processor

and forager, this superorganism is exquisitely versatile and efficient.

Taking the more centralized approach to scaling intelligence by growing a bigger
individual brain and body provides the comparative advantage of speed, or,
rather, latency. A single body can execute a quick coordinated movement, with
the parallel processing of many neural assemblies “voting” in a fraction of a sec-
ond, Compare this with the hours it can take a bee to make a round trip and dance
for her fellow bees. If you're eating plant products, a timescale measured in hours
is fine. If you’re eating other animals, you and your prey will enter a cybernetic
arms race driven by smart coordinated action at speed, as described in chapter 3.
Moreover, bigger brains require bigger bodies to carry them around, and bigger
bodies require bigger brains to coordinate their movements, so the amount of
muscle (or meat) available in a single animal also increases as this arms race esca-

lates. The steaks go up!

Ironically, lightning-quick cybernetic predation is the essence of System 1
thinking. It doesn’t leave time for reflection. (That's why early to mid-twentieth
century cybernetic systems endowed only with low-order prediction were good
enough for warfare applications like missile guidance.) On the other hand, noth-
ing prevents big-brained predators from using premeditated cunning to plan
their attack on unsuspecting prey, as Portia does, providing an ongoing advan-

tage for System 2 thinking.“24

And, of course, among highly social big-brained animals—us, most of all—
friendly cooperation, politics, and mating put a special premium on slower think-

ing. As anyone knows who has come up with a witty retort long after the moment

---

for it has passed,'***! speed is relevant in social interactions, but even rapier-like
wit doesn’t need to operate on a timescale measured in hundredths of a second,
as required in an actual swordfight. During argument, deliberation, bargaining,
group planning, teaching, learning, or mate wooing, taking a few seconds to fol-

low a chain of thought before opening your mouth is usually a fine idea.

Our combination of fast parallel and slow serial processing is one take on
psychologist Jonathan Haidt’s characterization of people as “90% chimp, 10%
bee,” although chimps are themselves quite social, hence capable slow
thinkers. The new element humans bring to the table is a highly developed
sensory-motor modality ideally suited to both internalized and socially shared
chains of thought: the modality of language.

Modalities

It may seem puzzling to refer to language as a modality. From a machine-learn-
ing perspective, though, that's exactly what it is. Chatbots and simpler models

like Word2Vec are trained on text, not on pixels, sounds, or other sensory signals.

Of course we don’t perceive text directly. We recognize text via other modalities,
including hearing (spoken), vision (written), and even touch (Braille or finger-
writing). In conversation, hearing and vision are often used in concert, with
gestures, facial expressions, and environmental cues playing important roles, es-

pecially during language learning.

Nonetheless, there is also neuroscientific justification for thinking of text as a
sensory modality, albeit an indirect and culturally acquired one. In literate hu-
mans, a specific part of the brain—the “visual word form area” (VWFA), near the
underside of the left temporal lobe—develops to perform reading tasks, that is,
learns to convert visual input into text. High-level neural activity in this area can
then serve as a specialized textual modality for any other brain region that wires

up to the VWFA.

Seen this way, vision is not fundamentally more “real” as a sensory modality
than text. Recall that raw visual input is a hot mess—nothing like the stable

“hallucinated” world you think you see. Using predictive modeling, the visual

---

system solicits and processes feedback from the eyes to create a kind of diorama
that other parts of the brain can then interrogate. As far as those regions are
concerned, it is this stately diorama, not the raw, jittery input from the eyes, that
comprises the visual umwelt. The additional processing that renders visual input
as text is simply another such transformation, sifting words out of stabilized im-

ages to create a textual modality.

The VWEA is a remarkable testament to the cortex’s flexibility and generality.
Genes may support or predispose us to develop certain capabilities via “pre-adap-
tation,” but it’s not clear how that could be the case for reading and writing—it’s
too recent. Keep in mind that humans have been around for hundreds of thou-

sands of years, while the first known writing is only a few thousand years old.

Before objecting that a few thousand years might be enough for an evolved trait to
emerge, consider that even after the invention of writing, literacy remained con-
fined to a tiny proportion of the human population—professional scribes, clergy,
and ruling elites—until just a few generations ago. There are good odds that at

least some of your great-great-grandparents were illiterate.

We can only conclude that the VWFEA is an ordinary bit of brain that just
happened to be in the right place (in terms of connectivity) at the right time. In
modern, literate humans, it has established a symbiotic functional relationship
with other brain areas, using a generic predictive-learning procedure to support
a valuable culturally evolved trait.!©*4 Thus, the VWFA highlights the way highly
specialized sensory processing—a new modality, in effect—can be learned, open-

ing up the space of modalities to high-speed cultural evolution.

A similar story may apply not just to reading, but even to language itself. Despite
the common refrain among linguists that our brains come with a built-in “lan-
guage organ,”!“"* it isn’t at all clear that we are genetically pre-adapted specifi-
cally for language, nor has the search for universal grammatical or syntactic
properties shared by all human languages been successful"! Insofar as human
genetics support language learning to a greater degree than in our primate
cousins, it seems increasingly likely that this support consists of a combination

of enhanced sequence learning in general'“*") and greater pro-sociality.'“*4 If so,

---

other manifestations of sequence learning, especially ones that reinforce social-

ity, such as dance and music, may well have predated complex language“!

Relative to vision, smell, and other modalities, language has some unique prop-
erties. Whereas ordinary senses are for perceiving the world broadly, language is
purely for sensing each other. It has wonderfully reflexive, self-referential quali-
ties (hence my ability to write about it in this book, and your ability to make sense
of what I’m writing—I hope). In providing us with a mind-reading mechanism,
language must allow for communication about any aspect of our umwelt, includ-
ing our models of ourselves and others—which necessarily includes a model of
every other sensory modality and motor affordance, both our own and others’)
That same infinite, recursive hall of mirrors described in chapter 5 for internal

states applies to our linguistic models of the external world too.

A 2023 paper entitled “Large Language Models Predict Human Sensory Judg-
ments Across Six Modalities” nicely illustrates this.“ The paper's authors

ask a large language model to estimate the similarity between pairs of sensory
stimuli based on textual descriptions. These modalities include pitch, loudness,
colors, the sounds of consonants, tastes, and musical timbres, described either in
quantitative terms (decibels or Hertz for sounds, numerical red, green, and blue
component values for color) or by name (“quinine,” “artificial sweetener,” etc. for

taste; “cello,” “flute,” etc. for timbre).

A Language Model Human Stritarity 6 @ y $y =
teh Watese c . Consonants laste = Timbre
CPT prompt Here wivilee Hom thes coke?

Paopie described prire ot
colors using tale tee at ore
codes Hun or rae
pater oe

Fon wile abe the colors Sodas ay ost
int mech pale on wo neele uf ou vilee w
€-1 4% cre 8 is coupletely Vey
Gixnin lar anc lik yey vata Dkeare

tplotely sintlor? ¥ ayo 4
Sear Roe md O Nether Sih oor Dicearasr set
Culor cow: sffeaee oer > Sawa: Bip ke
Color tne: EAO2EFS anaie™ (Yee in be or
Anonr anrderty Onn pein be
onsacc: 8.9

ao

Despite being trained only on text, the model's responses mirror human re-

sponses to an astonishing degree.'***! As, on reflection, they should: the goal of
pretraining is to predict human responses to any textual question or prompt. The
information needed to make these predictions can be found in a large enough

training corpus, because we talk about pretty much everything we experience,

---

including all that we perceive, think, and feel—or at least, everything accessible

to the interpreter.

Pure Speech

Despite these arguments, I used to worry that training a large model on text
might be cheating. We only learn how to read and write after mastering speech;
I wasn’t sure a Transformer could learn language without starting from a tran-
scription—where, in effect, the hard work of turning sound into symbols had al-

ready been done. AudioLM convinced me.

The project began when a team I managed at Google Research developed a neural
net for audio modeling called SEANet, then turned it into an audio compressor
called SoundStream in 2021./**! soundStream used a small Transformer to turn
auditory waveforms into token sequences, making use of the observation that
good prediction allows for powerful compression. Since Transformers were the
best predictive models available, and they hadn't previously been used to com-
press raw audio, we were pretty sure SoundStream would set a new sound com-

pression record, It did.

Then, in 2022, the team created AudioLM by inserting a second, much beefier
Transformer, like those used for large language models, between SoundStream’s
encoder and decoder.!**"| They pretrained this large audio token model on the

soundtracks of YouTube videos featuring people speaking in English.

The results were amazing, and a bit eerie. After pretraining on the equivalent of
about seven years’ worth of YouTube audio, the model could do a convincing job
of replying to simple prompts or questions. In one of the first exchanges I had
with AudioLM, I asked it, “What's your favorite sport?” and generated three alter-

native replies (we were using a nonzero temperature setting):

“T like baseball!”
“I don't know? I like football.”
“I play basketball.”

Curiously, all three replies were in children’s voices. On reflection, this made

sense. This was a pretrained model without any fine-tuning or additional rein-

---

forcement learning, so it was strictly in the business of giving high probability
predictions of the future (its response) given the past (my question). You just
don’t ask adults a question like, “What's your favorite sport?” It’s a question for
kids. So, it responded with a likely answer in a likely voice. For us humans, pre-
dictions must be conditional on our individual life history, from the physiology of
our vocal tract to our school experiences on sports teams, but a model pretrained
on a broad range of human voices and experiences isn’t constrained in the same
way. In its protean state, the model “is” a broad sample of humanity, not a single

human.

With further improvements to the model architecture, AudioLM, now called
SoundStorm,'®*! could stream long replies and continue multi-speaker dialogues.

Two team members prompted it with,

“Where did you go last summer?”

“I went to Greece. It was amazing.”

The model seamlessly improvised a continuation of the conversation, alternating
between perfect renditions of their voices (and yes, the deepfake potential here

was immediately worrying):

“Oh, that's great. I’ve always wanted to go to Greece. What was your fa-
vorite part?”

“Uh, it’s hard to choose just one favorite part. But ... yeah, I really loved the
food. The seafood was especially delicious—”

“Uh huh—”

“—a-and the beaches were incredible.”

“Uh huh—”

“We spent a lot of time swimming ... uh, sunbathing, and exploring the
islands.”

“Oh, that sounds like a perfect vacation. I’m so jealous.”

“It was definitely a trip I'll never forget.”

“T really hope I'll get to visit someday.”

It wasn’t scintillating dialogue, but it was entirely believable. The nuances of the

voices, their accents and mannerisms, were so perfectly reproduced that even

---

those of us who know those two team members well weren't able to guess which
lines were real and which were synthesized. The model renders breaths, disflu-
encies, sounds of agreement, people speaking over each other—in short, all of
the features that characterize actual dialogue, as opposed to the stylized kind you

read in novels.

The team eventually made AudioLM multimodal by adding text too, creating
AudioLLM. Just as translation between languages is possible in a large language
model with little or no explicitly translated training data, only a small amount

of transcribed speech was needed to allow AudioLLM to establish the relation-
ship between speech and text. The correlations inherent to speech are enough to
form internal representations roughly analogous to phonemes, so in theory (and
especially in a language with sensible spelling, like Spanish) all it would take is a
paragraph or so of sounded-out text to map each letter to a phoneme, much as the
Rosetta Stone sufficed to form a mapping between two written languages. In fact,
given the higher-order correlations and analogies between text and speech, I’m
sure that with enough pretraining data, an AudioLLM-style model could learn

those analogies with no sounded-out text at all.

What was most interesting about the original AudioLM, though, was its ability
to learn and understand language from pure analog sound, without text or any
other modality. The model was given no rules, assumptions, or symbols. It was
a striking refutation of the longstanding hypothesis that language learning re-

quires genetic preprogramming.

The father of twentieth-century linguistics, Noam Chomsky, has made an influ-
ential pseudo-mathematical “poverty of the stimulus” argument, asserting that
the amount of speech babies are exposed to can’t be nearly enough for them to
learn the grammar of natural language without a strong statistical prior.“ Such
a strong prior, a “universal grammar” common to all human languages, would
reside within the hypothetical, genetically preprogrammed “language organ.”
GOFAI pairs well with this idea, since it implies that the way to get a computer to
process language—and perhaps to reason—is to explicitly program in this univer-
sal grammar, thus restricting the role of language learning to the simpler task of

locking in the language-specific “settings.”

---

Chomsky’s argument was already in trouble before LLMs, for a variety of
reasons.*"! As mentioned earlier, human languages differ in so many ways that
the search for a supposedly universal grammar has been unsuccessful. Neuro-
science, too, has offered little in support of the thesis. The “interpreter” in the
left hemisphere does specialize in language, but like any other part of cortex, its
specialization appears to be a function of its connectivity, not of any “language

organ” fairy dust sprinkled in that particular spot.

The way babies and children learn language—beginning by paying close
attention to mom or dad, looking where they look or point, pointing in turn,
mimicking sounds, learning to take turns, acquiring a few salient words, starting
to combine them into stock phrases—also seems inconsistent with the use or ac-
quisition of a formal grammar. Babies are quick and wonderful learners, but that

”

doesn’t mean that they are little linguists, or scientists, or any other kind of “ists.

AudioLM puts a final nail in the coffin of “poverty of the stimulus.” While all ma-
chine learning models have some statistical priors, Transformers are so generic
that they can learn about any kind of sound, including music, birdsong, or whale
song;**4! for that matter, they can learn the crackle of radio telescope data, or
weather patterns, or sequences of pixels in images. Yet they can learn human
language—from how vocal tracts sound, to grammar, to the meanings of words,
to social appropriateness and turn-taking, to the nuances of breathing and other
non-speech sounds—from nothing but seven years’ worth of random YouTube

audio of people talking.

Before you object that children learn how to speak at an equivalent level in fewer
than seven years, and aren't constantly listening to speech over that period,
consider how much easier they have it: their learning is scaffolded by many
other sensory modalities, and in the beginning their parents and siblings repeat
the same words over and over in consistent voices, pointing to familiar things,
making eating gestures, and so on. That language can be learned at all without
any of this scaffolding, with no interaction, no curriculum, and no rewards, is

remarkable.

None of this implies that language is entirely arbitrary. It has to begin with

sounds human bodies can easily make and hear, which is already a significant

---

constraint. It must also be reasonably efficient and not overstrain our cognitive
capacities (e.g., by insisting that acommon word be produced by rapidly clicking
the tongue thirty-nine times in a row). Indeed, the historical record shows clear
evidence that languages with gnarly features tend to get streamlined over time,
making them increasingly user-friendly.**4! The statistical regularities involved,
however, have little to do with formal grammar and more to do with conve-
nience, along with constraints on memory, the vocal tract, and the distinguisha-

bility of sounds.

Babel Fish

While there is no universal grammar, there certainly are plenty of statisti-

cal relationships between languages—otherwise, the language translation
experiments described in chapter 8 wouldn't work. Some correlations stem
from human physiology and cognitive constraints, and some from the common
ancestry of languages. Many languages are closely related, as with the Romance
languages, and others more distantly, as with Indo-European. Possibly, all lan-

guages share a common ancestor, though this remains uncertain.“

Onomatopoeia and synesthesia play a part, too. It’s unsurprising that “meow”
and “splash” sound similar in many languages, even when the words have no
common ancestor. Less obviously, quirks of the relationships between sensory
representations in the brain also lead most humans to make the same choice
when deciding how to associate the nonsense words “bouba” and “kiki” with two
shapes, one of which is spiky, and the other rounded. (Yes, “kiki” is the spiky one.)
This classic result in psychology, dating back to the 1920s, shows how aspects of
synesthesia, a seemingly arbitrary mental association between distinct stimuli
of different modalities that some people profess to experience strongly, havea
universal neural basis.) Whether because those associations aren’t as arbitrary
as they seem, or because they are implicitly reflected in human languages, multi-

modal large language models reliably exhibit the bouba/kiki effect too!

---

Most of all, languages are all related because they are all about us and the world,
and we are all basically the same, and we all live in the same world. The real uni-
versal grammar is actually semantics. I’m fairly certain that, if a tribe of people
were somehow isolated from everyone else at birth and developed language

de novo on their own island, an AudioLM model pretrained on large enough
amounts of their speech and, independently, on English, would be able to freely

translate between the two languages without any need for a Rosetta Stone.

In The Hitchhiker's Guide to the Galaxy,*"! a surprisingly profound satire beloved
by generations of twelve-year-old nerds, British humorist Douglas Adams de-
scribes a “mindbogglingly useful” sci-fi creature, the “Babel fish.” “Small, yellow,
and leech-like,” when you put one in your ear, “you can instantly understand any-

thing said to you in any form of language.”

Such a technology would indeed be mind-bogglingly useful, even if limited to the
seven thousand or so languages spoken by Earth’s humans today.!®*"| For one, lan-
guage barriers are an enormous impediment to socioeconomic justice for many
of the world’s poor. For instance, in Burkina Faso, a landlocked West African
country, about seventy languages are spoken, sixty-six of which are indigenous.
As of 2024, the literacy rate is about forty percent. While the government uses
French (decolonization dates back only to 1960), that former imperial language is

only spoken by a small minority of the population.““"!

In such countries, a Babel fish could improve people’s prospects enormously,
giving them access to information, employment, services, education, and de-

velopment opportunities that are out of reach today. Moreover, because a real

---

neural net-powered Babel fish can operate in full duplex mode, and could even
offer tutoring and participate in conversation, it could aid in the preservation of

indigenous cultures and their languages.

Keep in mind that poorer countries have far younger populations and higher
birth rates than more developed countries; as countries become richer, their
birth rates inevitably drop, but due to the time lags in these dynamics, we should
understand that the populations of countries like Burkina Faso, already numer-
ous, will comprise a far greater proportion of humanity in the latter part of the

twenty-first century than they do today. This is humanity’s future.©2")

If we begin thinking about humanity as a superorganism, what is at stake here is
the scale, diversity, and cohesion of our collective intelligence. Without nurtur-
ing the diversity of its people and cultures, we reduce the value each has to offer
to the others, and the potential for hybridity, which is critical to cultural innova-
tion and development. On the other hand, without scale, collective intelligence

is impoverished; it’s difficult for an isolated population or a backwater to flourish.

There is a sweet spot, where local connectivity (in cultural terms, tradition) is
strong enough to provide real diversity yet there is also enough longer-range con-
nectivity to share knowledge, capability, and resources. The cortex embodies that
balance, with dense connectivity within cortical columns and long-range wiring
to bring the benefits of scale. The abundant cultural and economic productivity
of the Silk Roads may have been achieved through a similar balance.“*"! For many
centuries, highly active trade networks linked dozens of major cities and thou-
sands of smaller settlements across Eurasia, each with strong and diverse local

cultures, yet also benefiting from scale.

James Evans's Knowledge Lab at the University of Chicago has found evidence

of the same kind of sweet spot in the more abstract networks of collaboration
among academics. Scientific advances happen when robust, tightly intercon-
nected research communities are also in contact with each other, combining local

depth with wider hybridity...

Today, we're simultaneously under- and over-connected. Young people in places

like Burkina Faso remain isolated, while at the same time cultural and linguistic

---

homogeneity threatens to erase much of the world’s rich human diversity, just as
the genetic monocultures of industrial farming threaten biodiversity. Linguisti-
cally, the problem stems from the fact that the seven thousand or so languages
spoken on Earth follow a frequency distribution that is, as a statistician would
put it, very long-tailed, meaning that there are a large number of rare categories.
The rarest, so-called “low resource” languages, are so critically endangered that

one goes extinct every few months, with the death of its last living speaker.!°°+!

While new languages used to differentiate and coalesce at a comparable (or
higher) rate, increasing globalization has upset this balance. As a UNESCO report
put it in 2003, “About ninety-seven percent of the world’s people speak about
four percent of the world’s languages; and conversely, about ninety-six percent
of the world's languages are spoken by about three percent of the world’s peo-
ple [...]. Even languages with many thousands of speakers are no longer being
acquired by children [... and] in most world regions, about ninety percent of the
languages may be replaced by dominant languages by the end of the twenty-first
century.”&&)

10° ¥=
“as, 1.0

ve 10" ee
oD ie,
| 18
mS
P10
oO
2
oc 6
S 10 3
om

10°

l 10 ’ 100 1000
Tran

This flattening of our cultural and linguistic ecology has accelerated since the

early 2000s, when people began to move online en masse. English dominates the

---

internet, with just a handful of other languages (not coincidentally, those asso-
ciated with the former great empires) comprising the overwhelming majority of
the non-English material. Data centers now contain orders of magnitude more
textual material than existed in the entire world when the 2003 UNESCO report
came out. On the other hand, most indigenous languages are virtually absent

from this vast digital landscape.

With unsupervised sequence models, building a real Babel fish—and more—has
become newly possible. It should not be thought of as a specialized “product,”
since translation is an emergent capability in any model trained multilingually.
A giant, multilingual version of AudioLLM could enable it to learn languages
from field recordings; it could even invent written forms for languages that lack
them. Dialects, accents, and regional variations could all be learned too. Using Al
glasses, you could read Sumerian tablets or Aramaic manuscripts. A multimodal
model could even dub video in real time, or generate an avatar of you able to in-

stantly render gestures in any of the world’s sign languages.

The fly in the ointment is that long-tailed language distribution. Given the vast
amount of data pretraining seems to require, how on Earth could a large model
become competent at a regional Burkinabé dialect, let alone a critically endan-

gered indigenous language known only to a handful of elders?

Testament

By 2021, my colleagues at Google Research had begun working in earnest on
multilingual large language models, and they noticed something interesting:
learning one language greatly accelerated the subsequent learning of another. For
instance, pretraining on an enormous amount of English text, then continuing
the pretraining on a comparatively tiny amount of, say, Portuguese produces a
competent bilingual model. It may not be quite as good at Portuguese as at Eng-
lish, but if it were instead trained monolingually on Portuguese, it would need or-

ders of magnitude more Portuguese content to reach an equivalent skill level.

This effect is so powerful that beginning with a multilingual model, then con-
tinuing to pretrain using only the text of the New Testament in a novel language

produces a model likely to be capable of rudimentary translation to or from that

---

novel language.‘**4! This is especially noteworthy because Christian missionaries
have translated the New Testament into more than 1,600 languages—a pretty

good start at working our way down the long tail.

For better or worse, missionaries have long been the vanguard of ethnographic
linguistics. It takes real commitment for scholars from a rich country to travel
far from home, embed themselves in a foreign culture, and learn enough of the
local language and culture to translate a complex text, sometimes in the process
devising a written form for a language that had previously only been spoken.
Historically, religious faith and a desire to win converts has often provided the
necessary motivation; that’s why the New Testament is the most widely trans-

lated text on Earth.

Today, much of this work is carried out by SIL Global (formerly the Summer Insti-
tute of Linguistics International), an evangelical Christian nonprofit founded in
1934 and headquartered in Dallas. SIL’s online database, Ethnologue, is by far the
most comprehensive catalog of known languages, thanks to the organization’s

thousands of field linguists embedded in communities all over the world.

In 1977, Daniel Everett, a recent graduate of the Moody Bible Institute of Chicago,
had signed up to become one of those missionary linguists. Impressed by his
talent, SIL sent him, along with his wife Keren and their three young children,

to learn a language the Institute had failed to crack after twenty years of study:
the language of the Piraha, an indigenous group numbering less than a thousand
living in the Brazilian rainforest, near the mouth of the Maici river, a tributary of

the Amazon.

---

Despite the difficulty of the language, Everett eventually succeeded in learning

it, and, in the process, did much to dismantle Chomsky’s armchair theories
about universal grammar. Piraha lacks “linguistic recursion”—the ability to nest
grammatical structures within each other. So, for example, there is no Piraha
equivalent to the English phrase “John’s brother’s house.” According to Chomsky,
recursion is what makes languages open-ended, distinguishing them from the
finite communication systems of nonhuman animals. And indeed, without re-
cursion, a finite vocabulary can only be used to construct a finite number of valid
sentences.!°**! The lack of recursion is not quite as limiting in practice as it may
appear; a Piraha speaker can break nested ideas up into multiple sentences, as in

“John has a brother. This brother has a house.”

However, Piraha also lacks several other features common to most languages,
including past and future tenses, conditionals, and numbers. These gaps aren’t
superficial. Monolingual Piraha people, for instance, don't just lack words for
numbers, but lack any sense of numerosity, beyond a qualitative difference be-
tween “one” and “more than one.” They can’t do math at all.“ Similarly, the lack
of tenses and counterfactuals is associated with a worldview that only credits
direct experience. A sentence beginning “John said that ...” doesn't just pose a

translation challenge, but an epistemic one.

---

The larger picture here demonstrates that a wide range of cognitive capacities
Chomsky and his followers have assumed to be genetically pre-programmed

are not. Numbers and verb tenses are, like reading, social technologies. Human
brains are special not by virtue of having evolved a specific suite of capabilities,
but by virtue of having the flexibility, capacity, and inclination to be able to learn

them, both from our direct sensory experiences and from others.

As you might imagine, Everett had little luck converting a people who have no
use for what John, or any other first-century evangelist, had to say. With much
effort, Everett managed to translate the Gospel of Mark, but when he tried to
explain that Jesus lived a long time ago, yet he, Everett, still had Jesus's words, the
reply was, “Well, Dan, how do you have his words if you have never heard him

or seen him?” Taking pity, a Piraha took Everett aside to explain, “We don’t want
Jesus. But we like you. You can stay with us. But we don’t want to hear any more
about Jesus.”©57

Everett did stay with them. The wonderful book he wrote three decades later,
Don't Sleep, There Are Snakes, describes not only the unusual features of the Pi-
raha language, but how, instead of winning converts, life among them ultimately

caused him to give up his own faith!

Long Tails

I find it fascinating to consider that the Biblical translation work thousands of
missionaries have done over the years could so efficiently bootstrap multilingual
AI models. With a large AudioLM-type model pretrained on many spoken lan-
guages, recordings of a few dozen hours of conversation among elders speaking a

rare language could likely do the same. “24!

There's a seeming paradox here. On one hand, improvements to a large model
seem to be subject to diminishing returns as pretraining runs increase in size—
hence Al’s voracious appetite for data. In other words, training on two hundred
billion tokens of web content isn’t twice as good as training on one hundred bil-
lion tokens; it’s only incrementally better. In fact, doubling the performance ofa
model requires an exponentially larger amount of data, as well as an exponential

increase in the number of model parameters.)

---

And yet we also see that a miniscule amount of additional data in a new language
can enable a model to go from monolingual to bilingual, which seems like a dou-
bling of its capability. In fact, if we keep the amount of novel language content
fixed and vary the original amount of pretraining data, the bilingual results get
better as the amount of initial pretraining increases. That is, the larger and more
capable the original model, the better use it can make of a very limited amount of
novel language content. How can these models simultaneously exhibit logarith-
mically diminishing returns to scale, while also seeming to become exponentially
faster learners as they grow? Counterintuitively, the two effects turn out to be

closely related.

Remember that translation emerges as an automatic capability in large language
models because it’s a form of analogy. Specifically, the cloud of dots representing
the embeddings of words or concepts in language A is paralleled by an almost
identically shaped cloud of dots representing all of the words or concepts in
language B; moving from one cloud to the other is literally a matter of adding or
subtracting a constant shift in the embedding space. The shape of each of those
clouds is, in turn, the shape of the human umwelt, the geometry of everything we

know how to talk about.

The symmetry between these clouds—if the model is massively multilingual,

a many-way symmetry—offers powerful opportunities for generalization, and
generalization is what intelligence does. Recall that, once a convolutional net
learns how to see generically, it can easily learn how a new object looks in one
shot, because learning how to see involves building a generic representation for
objects that includes all of the symmetries arising from rotating any given object
around in space, looking at it from farther away or closer, changing the lighting,
and so on. In just the same way, learning both the universal shape of the human
umwelt and the symmetries between languages allows a new language to be
learned in something approximating one shot—or a single book, like the New

Testament.

Why, then, do we see such diminishing returns to scale in pretraining? We need
to keep in mind here that if we mixed together samples from two very unequally

represented languages, say ninety-nine percent English sentences and one

---

percent sentences in Wolof (a West African language), we would see the usual
diminishing returns on the combined data. It's only when we segregate the Wolof
sentences and train on them only after training on the English, that we see evi-

dence of the accelerated acquisition of Wolof.

In the mixed data, the Wolof sentences would comprise unusually important
training examples with novel content, but the point is that all datasets—includ-
ing the sentences purely in English—are mostly repetitive, only occasionally
adding new information. Even in a monolingual dataset, words and concepts

have a long-tail distribution, just like the distribution of languages themselves.

Long tails like this are a signature of multifractal properties in data: details have
details, and those details have their own even more esoteric details. Language,
and knowledge in general, is multifractal like that. Math may comprise only one
percent of the vast world of things we talk about. Technical discussion among
STEM professionals may comprise only one percent of the math talk (the rest
being dominated by the arithmetic kids do in class, or basic accounting, or
splitting the tab at restaurants). Among those professionals, one percent of the
discussion might be about number theory. Within number theory, perhaps one
percent of the conversation touches on, say, the Grothendieck—Katz p-curvature

conjecture.

Multiplying those four percentages by the eight billion people on Earth gives
eighty readers, if my own grade-school math is right, which seems in the right
ballpark for this particular community of interest. There’s nothing unique about
the Grothendieck-Katz p-curvature conjecture, either; not everyone is cut out for
such esoteric math (I’m not), but lots of people nerd out on one thing or another.
The most elaborate conspiracy theories of flat earthers, the deep recesses of Poké-
mon fan fic, and the craftspeople keeping handmade accordion manufacturing

alive also represent fine-grained detail in humanity’s Multifractal of Everything.

One could draw a cartoon of pretraining as follows. Suppose that, to come across
a novel concept after reading some number of sentences at random, you have

to read one percent more. If you're a model, that means that the first hundred
sentences you encounter on your very first training iteration are all likely to

contain new stuff. But after reading a couple of hundred sentences, only one in

---

two adds anything novel. After reading a million sentences, you'd likely need to
read another ten thousand before coming across something you hadn't seen be-
fore. That’s why learning slows down—not because it becomes less efficient, but
because when sampling at random, the likelihood of encountering something
genuinely novel in the next piece of data decreases so dramatically as a function

of how much you already know.

In-Context Learning

Companies like Microsoft and Google are now pretraining large models ona
good chunk of the entire Web; social media are increasingly in the mix too. Some
analysts are pointing out that, at this rate, even given the ongoing exponential

growth of digital data, we’ll soon run out./&“)

Critics have deemed this apparently bottomless demand for human-generated

content problematic for conceptual, ethical, and pragmatic reasons:

1. Pretraining seems very different from the way humans learn, both
emphasizing the inefficiency of today’s approaches to machine learn-
ing and adding fuel to arguments that AI models don’t really under-
stand anything, but are just giant memorizers. While I've offered a
range of evidence that this isn't so, it’s a constant issue in AI research;
it’s as if no AI test can ever be closed-book, because the model has
read, compressed, and potentially memorized some approximation of
“everything.”

2. Concerns have been raised about the legality and ethics of using so
many peoples’ content this way. Even when legality isn’t at issue, little
of this material was created with the intent for it to become AI fodder.
And once a particular piece of media has been used in pretraining,
it becomes difficult to determine whether and to what degree it in-
fluences the model’s subsequent output. Especially when AI creates
intellectual property or in some other way produces economic value,
this raises questions about what constitutes “fair use” and when some-

thing is unique versus a “derivative work.”/S/J

---

3. The extreme industrial scale of pretraining, both in terms of data and
computing power, limits the creation of the largest “frontier” models
to the very small number of companies and governments able to make
massive capital investments.“~! On one hand, this may be a blessing
(while it lasts), as it makes prevention of the most dangerous uses of
advanced AI at least possible; it wouldn't be if anyone could roll their
own. However, the situation raises concerns about monopoly, unfair
competition, and AI diversity.

4. The most profound theoretical difficulty with the pretraining ap-
proach is the way it separates learning from inference—an unwelcome
legacy from the early days of cybernetics. This means that the model
is, in some sense, frozen in time; when one begins interacting with
it, it knows about nothing in the world that happened after the date
the pretraining data were scraped. In effect, it has total anterograde

amnesia.
None of these issues is quite as straightforward as it appears.

Regarding #1, the unnaturalness of pretraining, I suspected for many years that
the backpropagation method universally used to train large models today, but
long known not to be biologically plausible (per chapter 7), was at fault. Surely, I
thought, our brains implement a brilliant learning algorithm that would greatly
improve on backpropagation. Otherwise, how could any of us have grown from
helpless newborns into smartypants college students in a mere eighteen years,
most of which were spent sleeping, daydreaming, watching inane cartoons, play-
ing 8-bit video games, avoiding our parents, and smoking weed behind the school

dumpster?!®”’!

Brains may indeed implement some hyper-efficient neural-learning magic, but
it’s increasingly clear that a good deal of the suboptimality in pretraining lies in
a foie gras—like approach to training data. We take as much of the Web as we can
grab, grind it up into paste, and force it down the neural net’s gullet, in random
order, with no regard for curriculum, relevance, redundancy, context, or agency

on the part of the model itself. (Apologies if this just put you off dinner.)

---

Indeed, the contrast between the usual diminishing returns to scale on training
data and the accelerated learning we see with continued pretraining on novel
data (as with the Wolof example) is telling. It suggests that much of today’s pre-
training is redundant. The bigger our models get, the more wasteful the random-
sampling approach becomes. In short, the problem may be in the teaching more

than in the learning.

Regarding #2, while AI supercharges the “fair use” debate due to its speed and
scale, the question of originality has been hotly contested for decades, as it’s not
specific to Al; all creative work is necessarily a product of one’s life experience,
which includes everything a person has ever seen, heard, touched, smelled,
tasted, read ... and despite any self-serving story our interpreter may spin, we are
often unaware of our influences, or the degree to which we've covered our tracks

via mutation and recombination, otherwise known as “originality.”

In one famous case, George Harrison, post-Beatles, released his first solo hit in
1970, “My Sweet Lord,” a catchy song calling for an end to religious sectarianism.
But, as it turned out, “My Sweet Lord” was extremely reminiscent of Ronnie Mack's
chart-topping 1963 gospel hit “He’s So Fine.” Harrison had of course heard this
song, but was unaware that he was copying it, almost note for note. What fol-
lowed has been characterized as “without question, one of the longest running

legal battles ever to be litigated in [the United States]."1074

If we could figure out how to train models with far less data, more like us, it

would go a long way toward addressing issues #1-3. Curating the training data
would become more practical, ensuring the answers to test questions aren’t in-
cluded, avoiding indiscriminate scraping of living artists’ work, and (for better
and worse) opening up the ability to create AI models from scratch to a broader

public.

The real key, I believe, lies in #4: erasing the distinction between learning and
inference. We know this is possible, not only because brains exhibit no such
distinction, but because of a series of findings that shed light on fundamental
properties of sequence learning and help clarify why Transformers work as well

as they do.

---

In 2020, OpenAI announced their GPT-3 language model, the predecessor to
GPT-3.5, which would power ChatGPT. The announcement came in the form

of a paper with a curious title: “Language Models Are Few-Shot Learners.”!°!2!
The learning in question was mysterious, and, it seemed at the time, unrelated
to learning in the usual sense, involving minimizing error through backprop-
agation. The authors were pointing out that during inference—that is, normal
operation after training—language models still appear to be able to learn, and to
be able to do so with extraordinary efficiency, despite no changes to the neural-
network parameters. Specifically, they defined “few-shot learning” as giving the
model a few examples of a task in the context window and then asking it to do
another such task; “one-shot learning” involved only a single example and “zero-

shot learning” included no examples, only describing the task to be done.

We've already encountered several instances of such situations. Asking a model
that wasn’t pretrained or fine-tuned on translation tasks to do translation is, for
example, a zero-shot learning task. So is asking for chain-of-thought reasoning.

Or, for an example that definitely didn’t come up anywhere in the pretraining,

consider the following instance of zero-shot learning:

“Equiantonyms’ are pairs of words that are opposite of each other and have

the same number of letters. What are some ‘equiantonyms’?”

To be clear, equiantonyms aren't a thing, or at least, they weren't until my co-
author Peter Norvig and I concocted this query in 2023 to illustrate zero-shot
learning.!““4| This isn’t a particularly easy task; as of 2024, none of the main-
stream chatbots reliably succeed, though with some prodding, Gemini Advanced
manages to come up with “give/take,” adding cheerily that it is “determined to

find more.”

Can we really call this learning if the model parameters remain unchanged?
It’s straightforward to perform learning by ongoing unsupervised or super-
vised backpropagation (i.e., fine-tuning) to cause a baseline model to improve
at known tasks like translation, or to perform novel tasks like coming up with
equiantonyms. We could then compare baseline model performance with

the performance of these refined models. Performance has to be measured by

prompting, that is, by asking “What are some ‘equiantonyms’?” with no pream-

---

ble. Presumably, the baseline would already be OK at translation, though ongoing
training would improve it; unless the model makes a very lucky guess as to the
meaning of equiantonym, its baseline performance at that novel task would be
zero, though, with training, it will improve. Similarly, we could draw a compar-
ison between the baseline with no preamble and the baseline with zero-, one-,

or few-shot prompts. All of these interventions result in improvements over the
baseline. So, despite their fixed parameters, the prompted models seem like they

are learning!

The GPT-3 authors pointed out that this ability to learn on the fly from the
prompt itself—“in-context learning”—is, like math, reasoning, or any other
model capability, a skill that improves with scale; bigger models are better at it.
A 2023 paper from researchers on my own team finally began to clarify how it
works.\©2) They showed that a simplified Transformer with a single attention
layer could, given a toy problem and a specially configured array of parameters,
perform the mathematical equivalent of a single backpropagation step on the
contents of the context window. In other words, in this somewhat contrived
setting, the model is able to respond to its prompt as if it had learned from that
prompt before predicting the next token. Adding a second attention layer makes
it possible for the model to effectively take two backpropagation steps, a third

layer allows a third step, and so on.

If this result had only held given hand-specified parameters, it would have been
no more than a curiosity; indeed, it had recently been discovered that a Trans-
former is Turing complete, so it could, in theory, perform any computation on its
context window, given the right parameters.!““4l However, as it turns out, ordi-
nary pretraining results in precisely the same in-context learning behavior as in
the hand-specified case. Pretrained transformers, in other words, really do learn

to learn.

As of 2024, learning in-context isn’t yet fully solved, because although Trans-
formers do it automatically, they don't remember anything they’ve learned once
the “training” material scrolls out of the context window. The missing machin-
ery may involve something like a hippocampus, and perhaps a sleep cycle for con-

solidating knowledge and memories.

---

Regardless, in-context learning is important, both theoretically and practically.
Working through its mechanics demystifies some of the Transformer’s more
surprising capabilities. It reveals a unity between learning and prediction that
makes sense, when considered carefully. After all, prediction always involves
modeling a changing environment (unless you're in an unchanging Dark Room);
learning is nothing more than prediction over long timescales. Over short
timescales, and especially when what is learned is rapidly forgotten, we often call
it “adaptation.”"&

An important, related theoretical point concerns the difference between cause
and correlation. One of the criticisms often leveled against machine learning is
that, since it usually involves passive learning (as with pretraining), it can only
learn correlations, not causes.") According to this critique, it’s not possible for
a passively trained AI model to know that X causes Y, but only that X and Y are
correlated in the training data. Living things like us, on the other hand, can eas-
ily learn causation by doing experiments. Perhaps when your cat, as an active
learner, uses her paw to blithely push a vase off a high shelf, she’s only experi-

menting to see if, indeed, pushing it that way will cause it to fall and shatter.

It's true that when experimentation is possible, it offers a powerful way to test
causation. However, the presumption that causality (technically, “entailment”)
can’t be inferred from passive observation, and in particular by pretrained
language models, has been proven wrong. “*4 It’s not necessarily easy, nor is it
always possible, but it can be done. Indeed, there’s no shortage of researchers who
study systems that they can’t causally experiment on—astronomers and macroe-
conomists, for example. In other cases experimentation is ethically prohibited,
as in some areas of social science and medicine. These researchers must rely on
“natural experiments,” that is, on observations that strongly imply causal rela-
tionships. Such observations can never entirely prove causation, but, then again,
neither can an experiment. (Perhaps the cat was just adding another trial, to
lower the uncertainty in her causal model. Yep—this vase shattered when it fell,

too. Right. Again.)

Historically, the claim that machine learning only learns correlations, not causes,

gained currency during the CNN era, in the 2010s. Since most CNNs did not oper-

---

ate over temporal sequences, but merely classified isolated stimuli, it was hard to
see how they could learn anything other than correlations among those stimuli.
Nvidia's self-driving car prototype DAVE-2, for instance,**4! learned through
supervision to associate being left of the centerline of the lane with a “steer right”
output, and being right of the centerline with “steer left,” but it would be a stretch
to claim that the model understood that those steering actions would subse-
quently cause those centerlines to be closer to the middle. They could just as well
have done the opposite, or nothing. Indeed, DAVE-2 had no internal representa-
tion of “subsequently.” If you shuffled all of the frames in a driving video, its per-
frame outputs would remain the same, and, indeed, during training the frames

are shuffled randomly.

Learning to predict changes everything, though. Specifically, an autoregressive
sequence model trained on the same task would learn the effect on subsequent
frames of steering left or right, which implies that it would learn, at least within
the limits of its umwelt, what steering does. It would be able to use that under-
standing to follow through with a steering correction even if the forward-facing
camera were briefly obscured. It would even be able to simulate counterfactu-
als—how the view would change if it were to steer left versus right. Ordinary,
passive pretraining, moreover, would suffice to learn these causal relationships.
There's nothing magical about learning causality; it simply requires modeling

time sequentially.

But let's return to the four problems described earlier, and how in-context
learning can help overcome them. If Transformers learn how to learn, they could
teach themselves, or each other, just as we do. They could ask for or look up infor-
mation, or, in some circumstances, even perform experiments to learn.!°*4) This
kind of active learning, integrated into agential behavior, would be vastly more
efficient than the passive random sampling used in today’s pretraining. Learning
could be curricular, beginning with children’s books—which, as shown by TinyS-
tories, £*4! needn't require massive amounts of material. Then, having learned

to learn basic human concepts and language, an AI could progress to the Young

Adult shelf, and on from there. Just as we do.

---

Each learning-capable AI agent could specialize by learning whatever fields are
most useful in its particular context, doing so in an individual, experiential way.
If a given agent is interacting with the eighty nerdiest number theorists on the
planet, its learning will eventually be focused on a very specific corner of the Mul-
tifractal of Everything—a corner that would take gargantuan amounts of com-
puting power to resolve adequately with random sampling. As a bonus, we'd have
a true diversity of agents interacting with us socially, rather than the monolithic,
generic, and non-specialized corporate models representing the state of the art in

2024.

The burning question is: would those individuated models be like people? And
what, if anything, would it be like to be one of them?

Mary’s Room

In 1982, Australian philosopher and self-declared “qualia freak” Frank Jackson
posed a famous thought experiment, the “Knowledge Argument,” now more

commonly known as “Mary’s Room.”®*") It went like this:

Mary is a brilliant scientist who is, for whatever reason, forced to investi-
gate the world from a black-and-white room via a black-and-white televi-
sion monitor. She specializes in the neurophysiology of vision and acquires
[...] all the physical information there is to obtain about what goes on when
we see ripe tomatoes, or the sky, and use terms like red, blue, and so on. She
discovers [...] just which wave-length combinations from the sky stimulate
the retina, and exactly how this produces via the central nervous system
the contraction of the vocal chords and expulsion of air from the lungs
that results in the uttering of the sentence “The sky is blue.” [...] What will
happen when Mary is released from her black-and-white room or is given
a color television monitor? Will she learn anything or not? It seems just
obvious that she will learn something about the world and our visual ex-
perience of it. But then it is inescapable that her previous knowledge was
incomplete. But she had ail the physical information. Ergo there is more to

have than that, and Physicalism is false.

---

Today, of course, language models are Mary, so the Knowledge Argument has

been getting a fresh airing.

As powerful as Jackson’s fable sounds, it is, like so many philosophical arguments,
rooted in storytelling and folk intuition. The “ergo” ties a bow around a logical
syllogism, but none of that syllogism’s predicates are unambiguously true or
false, as they would have to be in a mathematical proof... and we're in territory
where our folk intuitions can lead us astray.\***! So, let’s update those intuitions
by bringing to bear what we now know about perception and experience, which

is a good deal more than anyone knew in 1982.

As of this writing, nobody has yet, to my knowledge, hooked up an artificial nose
or taste buds to a language model, though I'm sure it will happen soon enough.
Being able to physically smell isn't essential for a model to be able to “get” smell,
though. Remember, when COVID causes you to temporarily lose your sense of
smell, or you just have a stuffed-up nose, you don’t suddenly become a person for
whom the smell of bananas ceases to exist. You are still a smelling being; smells
are still a part of your umwelt, just as vision is still part of your umwelt when your

eyes happen to be closed.

This is because, fundamentally, smell, and all other modalities, are experienced
mentally. They are models. You have a sense of smell because regions of your
brain have learned how to model smell; your nose merely prompts characteristic
neural activity patterns in those regions. The same regions will also activate, al-
beit perhaps to a lesser degree, when you imagine a smell. Similarly, your eyes are
not your sense of vision; rather, they merely provide error-correction signals to
keep your visual cortex’s “controlled hallucination” reasonably well aligned with

the world out there.

There's ample evidence that perception and imagination share a common neural
basis. Damage to one hemisphere’s visual cortex, for example, doesn’t just pre-
vent you from being able to see things in the opposite visual hemifield, but even
from knowing that the opposite hemifield exists, or being able to imagine what
might be in it 6271

---

Damage to the eyes, paradoxically, can have exactly the opposite effect. In 1760,
Swiss naturalist Charles Bonnet described the complex visual hallucinations
experienced by his grandfather, who suffered from severe cataracts. The older
Bonnet began to see nonexistent horses, people, carriages, buildings, tapestries,
and other shapes; Charles, too, had weak vision, and as it progressively worsened
he began to experience similar hallucinations.““"| These symptoms, now often

called Charles Bonnet Syndrome, are common in people going blind.

Even without organic damage, anyone in total darkness for an extended period
can experience similar hallucinations, a phenomenon known as “prisoner’s cin-
ema.” This is exactly what one would expect to happen when the visual cortex's
hallucinations remain active but float free of their moorings, unconstrained by

error-correction signals from the eyes.

Memory uses the same neural machinery as perception and imagination. Just as
the sight of a banana, or the smell of its distinctive ester in your nose, will trigger
the controlled hallucination “banana” in your brain, the word banana, or the
memory of eating one, can do the same, albeit (unless you're Marcel Proust) less
intensely. Any of these banana-related activity patterns may also be tagged with
something like a positional encoding, as described in chapter 8, to let you know

that this banana experience isn’t happening here and now.

Tellingly, a damaged or missing hippocampus, as in Henry Molaison’s case, will
not only impair the formation of new memories, but will also impair the ability
to imagine new experiences." This is consistent with the speculation that
imagining a future experience requires pairing known concept embeddings with
new positional encodings, perhaps generated in the hippocampus, to represent a

future or counterfactual time or place.

In light of the preceding, the question of whether a language model has percep-
tual “qualia” seems to have little to do with sense organs, and much to do with
the model itself. So many food, wine, and coffee nerds have written in exhaus-
tive (and exhausting) detail about their olfactory experiences that the relevant
perceptual map is already latent in large language models, as the “six modalities”

paper shows. In effect, large language models do have noses: ours. Those models

---

just happen to be hooked up to noses via textual token embeddings rather than

neural pathways.

However, we also have to acknowledge that “qualia” questions cannot be an-
swered objectively. We have to form a model of the model to decide whether it
“gets” smell, or color, or anything else. So, we once again have a relational or Tur-

ing Test sort of question, with no perspective-independent “view from nowhere.”

Al and cognitive-science researchers struggled over this issue in a debate about
whether a Transformer could effectively build a world model of Othello, a simple
Go-like board game played on an 88 board.!©*"! In 2022, a group of researchers
pretrained a small-ish Transformer using transcripts of valid Othello games. Sure
enough, the model learned how to play valid moves, in effect “autocompleting”

games.

However, the question the researchers were trying to answer wasn’t “can the
model play,” but rather, “has the model learned an internal representation of
the board?” It can easily be argued that without such a representation, it would
be hard to know which moves are valid, but the goal was to address critics who
claimed that Transformers work by rote memorization rather than by actually
modeling the world, and the world of Othello—consisting of nothing but the
state of an 8x8 board—seemed simple and objective enough to put the question

to rest.

But how can we tell whether such a world model exists, somewhere among the
zillions of neural activations in the Transformer? Ironically, that’s a job that only
machine learning can solve. So, the researchers needed to build a second model,
which they called a “probe,” to learn how to map the Transformer's neural activ-
ity to an 88 pixel image of the board. When their probe was too simple—just
linear decoding—it didn’t perform very well; but when it was made a bit more so-
phisticated with the addition of an extra layer, it did work. The trouble is that, if
the probe is trained to map neural activations (which include information about
the entire game) to the correct board state, then the researchers could effectively
have been using supervised learning to train the probe to learn a world model!

And so the debate has gone round and round./©24!

---

It takes a model to know a model. Similarly, when brain regions are connected to
each other, they are each acting as a “probe” of the others, although no region is
connected to anything like the perspective-independent ground truth of an 8«8
board.

Plenty of explicitly multimodal generative models have been made in the 2020s,
connecting artificial “brain regions” that specialize in different modalities, most
typically vision and language. The details vary, but these “regions” are often
pretrained independently on large volumes of unimodal data (e.g., images for
one, text for the other) and subsequently fine-tuned jointly with only a limited
amount of multimodal data (such as captioned images).!@4 This works for the
same reason a masked autoencoder can learn labels with a minimum of fine-tun-

ing after it has been pretrained.

The resulting models pretty clearly “get” how language and vision relate. They
can describe scenes, much as a person might, and when run in the opposite direc-
tion—encoding language, then decoding pixels—they can generate imagery or
video based on a textual prompt. In 2023, the quality of this generated content

began to seriously alarm some artists, designers, and film professionals.

It’s difficult, in light of what multimodal Transformers can do, to continue mak-
ing the case that there’s any intrinsic barrier to understanding in a model because
it lacks one sensory modality or another. We would never make such an argu-
ment for a person, and, of course, people do exist who lack one or more sensory
modalities. Everybody knows about blindness and deafness, but there are also
people who can’t taste or smell, and who have interoceptive deficits.!*°*! Someone
recently tried to make the case to me that everything else might be compromised,
but being human requires, if nothing else, touch. I, too, feel that this modality is
special, but that doesn’t make it indispensable. Although rare, there are people
who can’t feel touch; it’s an extreme (and dangerous) form of a condition known

as “hypoesthesia.”

No modality is magical, or is perceived directly by your homunculus—because,
and this cannot be said too often, there is no homunculus. Due to differing inner-

vation, different parts of the brain specialize in processing different modalities,

---

and brain lesions or developmental anomalies can occur anywhere, with the po-

tential to compromise or destroy any modality.

We’re remarkably robust to these deficits because our brain regions are not only
connected to the outside world through their various specialized “ports” but also
to each other, and they are constantly trying to predict all of their inputs—both
from the world and from each other. As mentioned in chapter 5, blind people who
have learned to echolocate using “click sonar” report being able to see; moreover,
they use their visual cortex to do so. Of course, their vision isn’t like that of
most sighted people: they can’t distinguish color, their spatial resolution is low,
and they're best at resolving objects in motion, which produce Doppler effects.
Still, visual cortex, the brain area we normally define in terms of the primary sen-
sory input it’s supposed to process—signals from the eyes—is somehow carrying

out its usual function without that input! How can that be?

Sight in humans is highly evolved, so there’s likely some degree of specialization
in the visual cortex that makes it especially well-suited for visual processing.
The specific processing needed to turn sound into an awareness of objects and
surfaces in three-dimensional space has little in common with the processing of

retinal inputs. Still, cortex is cortex.

What the visual cortices of blind and sighted people have in common is their
connectivity with the rest of the brain. Visual cortex, in other words, is “visual”
mainly by virtue of being connected the right way to perform the role of vision,
that is, to predict the presence and properties of objects and surfaces in the space
around you. Indeed, per chapter 7, what is “downstream” is at least as important
in establishing its function as the retinas “upstream.” So if this well-placed cor-
tical area lacks its usual sensory outpost in the eyes, it will do its best to make
the same predictions using other inputs, including those from auditory cortex.
In fact, even in sighted people the visual cortex appears to make use of auditory
inputs (and vice versa)—which is unsurprising, since there are so many circum-
stances under which visual and auditory stimuli are mutually predictive, as with
a tennis racket hitting a ball."

So what can we conclude about Mary? Perhaps not much. Depending on the de-

tails of her cortical development, she might be wowed by seeing red for the first

---

time, even if she understood it intellectually, just as we can be wowed by seeing
the Grand Canyon for the first time, despite having read in a guidebook exactly
how deep it is. On the other hand, if the understanding was purely intellectual
—meaning sufficient to think her way, step by step, to predicting someone's re-
sponse to redness, but not supported by the kind of System 1 cortical model most
of us perceive color with—then it’s unclear what we mean by “she sees red for the

first time.” To see it, you need a model of it.

Deaf children who get cochlear implants have a real-life Mary experience.
Although most outcomes are positive, their stories vary.!©2! If they never had
hearing, they begin without a learned auditory model, and experience some-
thing new and uninterpretable when the implant is first turned on and someone
they're looking at speaks to them—it’s not sound, but the structured stimulation
of existing neurons in unfamiliar new patterns, correlated with the motion of the
speaker's lips. Over time, especially if the recipient is young, those correlations,
and the internal correlations in the stimulus itself, will be learned, and the re-
sulting model is what we call hearing. (Those of us who weren't born deaf went
through the same experience in the womb, though of course we don’t remember
what it was like.) But for some recipients, the new stimulus is too weird and un-
pleasant, or the cortical model too slow to develop, or the extra information not

worth the added cognitive burden. They will opt out, turning off their implants.

Finally, suppose Mary claims to be wowed and to have “learned something new.”
Suppose she can correctly identify and describe red things ... but we don't believe
that she is really seeing red, instead relying on her super-scientific predictive
model to say the right things at the right times. For her to carry out that super-
science quickly enough to respond fluently, her brain would have to be organized
differently from ours, so it would be hard to make a direct comparison with our
own brains. To settle the question, some (other) smartypants would suggest
building a neural net to probe her brain, looking for an internal neural representa-

tion of the world, and... well, you see the problem.

Parity Check

Many purported distinctions between AI and humans must be seen through a

---

relational lens; as such, they may have no strictly objective truth value. Whether

Als can experience “qualia” falls into that category. Likewise, questions like:

@ Isareal relationship with an AI possible?
@ Can an AI have agency?
@ Can Als be held accountable for their actions?

@ Are Als moral patients?

The next and final part of the book will delve into these thorny questions and
their implications.

Before we get there, it’s worth trying to sort some of the more empirically testable
claims about Al/human distinctions into those that are probably right, and prob-
ably wrong, based on the evidence available in 2024. Let's take stock, though this

is, of course, a moving target:

@ Probably wrong distinctions:
© Internal models
0° Grounding or embodiment
© Factuality
© Causality
© Reasoning
© Planning
© Movement

® Probably right distinctions:
© Memory
0 Inner monologue

© Individuation

Notably, there are quite a few more “probably wrongs” than “probably rights.”
Filing an item under the “probably wrong” heading doesn't imply that the work
of AI researchers in that arena is done, or that models are precisely equivalent to
or performing at the same level as humans, but rather that the claim “humans

have these properties or capabilities, while Als don’t” has become untenable.

Internal models. While it takes a model to know a model, I've cited a growing

wealth of experimental evidence that Transformers do build internal world mod-

---

els. We know that they are theoretically capable of doing so, because of their Tur-
ing completeness—that is, if any computational model can be built, then a Trans-

former can provably implement it, in particular using chain-of-thought.22=)

Under what conditions such a model is not only implementable, but also learn-
able in practice, remains an empirical question, but by now, we have plenty of
existence proofs. The best evidence gets around the “it takes a model to know

a model” problem by using the AI as its own “probe,” for instance, by giving it
descriptions of rooms and how to navigate them, then asking it to draw a map of
its environment.!®**) Given that Transformers regularly succeed at tasks like these
(even if their performance is uneven), it seems hard to make the case that they

can’t build internal models, or that they rely only on memorized regularities.

Grounding or embodiment. Cognitive scientists have frequently claimed that
humans live in the real world, while language models are disembodied, their
umwelt consisting of mere strings of text, rendering their environment “not real”
or “ungrounded.”!°") But any entity—a computer, a cortical column, a brain, a
person, a corporation—exists in relation with an environment, and with other
entities, as mediated by signals. These signals may be transmitted in any way—as
text, pixel intensities, chemical concentrations, or neural spikes. Nothing is more
or less “real” about any of these signal modalities, or about what lies on the other

side of them.

Factuality. Large language models are prone to “hallucination,” meaning that
they tend to make things up. In June 2023, a pair of hapless New York lawyers
who used ChatGPT to prepare a legal brief became the laughingstock of the inter-
net when it was discovered that the cases cited in their brief were fictional._24
Everyone loves to dunk on lawyers who aren’t as clever as they think they are—
the judge, in this instance, included. They were fined $5,000.

The tendency of models to hallucinate should be unsurprising; prediction and
hallucination are closely related, and are the very essence of intelligence. This is
doubly true for language. Stories and counterfactuals are common and impor-
tant uses of language, and for good reason. Language is a kind of multiverse, an
umwelt of the mind that includes the fantastical, the unreal, the hypothetical,

and the adjacent possible. Counterfactuals allow us to teach and learn, powering

---

cultural evolution, and to simulate futures and alternatives, underwriting our
agency and free will. Thus, in a pure language umwelt, distinguishing “real” from

“not real” is a sophisticated recognition task.

Imaginative play is a major feature of normal childhood, but distinguishing the
real from the imagined is easier for us than for a language model, since children
not only interact with each other, but also with a shared physical environment.
Make-believe is ritualized and contextualized. Social cues might not fully disam-
biguate the “real” from the “not real” in any objective sense (or we would have no
superstitions), but they will at least help most people form beliefs that aren't too

out of step with everyone else's.

Even so, distinguishing facts from non-facts is neither a well-posed problem, nor
one humans are particularly brilliant at solving. Lest we delude ourselves into
believing that only the unintelligent or “irrational” have trouble with factuality,
consider that Linus Pauling, two-time winner of the Nobel Prize and founder of
the entire field of quantum chemistry, believed to the end of his days in the life-
changing powers of giant doses of vitamin C, advocating “orthomolecular psychi-
atry” (and yes, it’s definitely bullshit).24 In short, it’s wrong to assert that having
trouble distinguishing counterfactuals from “factuals” is a sure sign of not think-

ing like a real person, or of not being intelligent.

All this said, Al models are getting better at this counterintuitively subtle task.
Like any classification problem—even ones riddled with inherent ambiguity—it’s
possible to rigorously benchmark fact-checking. A 2022 paper from AI startup
Anthropic, “Language Models (Mostly) Know What They Know,”22! found that
models can easily learn to recognize their own hallucinations as such. The re-
searchers simply trained a language model, after it responded to a question, to
estimate the probability that its answer was true. It did quite well at this task. It
could also do a decent job of reporting, given a question, whether it actually knew

the response.

This wasn’t so surprising, since, around the same time, a great deal of progress
was being made at suppressing hallucination through reinforcement learning

after pretraining. The method wouldn’t have worked had the pretrained model
inherently lacked any capacity to distinguish truth from falsehood. By 2024,

---

benchmarking indicated that state-of-the-art large language models had sur-

passed average human performance at fact-checking.2"l

Causality, reasoning, and planning. Many researchers claim that Transformer-
based models can’t learn causal relationships, reason, or plan. As discussed
earlier, the longstanding idea that Transformers can’t learn causality has been
debunked,/“°*| though it’s also the case that passive, foie gras-style pretraining is

not an efficient way to learn causal relationships.

Deniers of Al’s reasoning capabilities include not only GOFAI advocates who have
very specific Leibnizian ideas about what “reasoning” means, but also many
modern Al researchers eager to improve the reliability of reasoning or planning
in their models. This is certainly a worthwhile project. As of 2024, AlTis still too
hit-or-miss to rely on for most consequential tasks without continuous human
oversight. Still, it seems strange to equate this lack of reliability with an absence
of underlying capability, when step-by-step reasoning in sequence models both
works for solving complex problems (albeit not yet reliably) and produces a

human-interpretable chain of thought that usually makes sense.

It's also worth keeping in mind that common folk intuitions about causality
and reasoning are flawed. Causality only makes sense as an idea (distinct from
correlation) if we entertain counterfactuals—what could or could have happened
as opposed to what actually happens. Recall, from chapter 6, that the notion of
causality is hard to make sense of in a deterministic universe. Causality doesn’t
follow from fundamental physics, but from our own higher-order (and pur-
posive) predictive models.!"°°) Asserting that Transformers don’t understand
causality is therefore a more subjective claim than it might appear—just like

denying that they have theory of mind, or free will.

As for reasoning: we tend to indiscriminately conflate the meanings of reason (as
in reasons for doing something), reasoning (as in using chains of thought to work
something out), and rationality (as in being clever enough to get things “right,”

however we might define that, via reasoning). These are worth picking apart.

As we've seen, both people and Als will be happy to generate reasons for

anything. The left-hemisphere interpreter doesn’t even distinguish between

---

generating convincing reasons for things we actually chose versus things we are
fooled into believing we chose.“4 Our reasoning faculty thus powerfully exhibits
what Mercier and Sperber have called a “my side” bias.!!2*! Smart people like Linus
Pauling are no less prone to this bias than anyone else, though they may be like-
lier to marshall convincing “reasons” and use their prestige to convince (or bully)

others into agreeing.

On its face, this seems like a lousy foundation for “rationality.” However, Mercier
and Sperber go beyond the false dichotomy between “reasons are rational” and
“reasons are nonsense” to propose an interaction-focused account of why we
bother making arguments at all. We do so for each other, and for our collective
benefit. Ample evidence shows that groups of people engaging in constructive
discussion and debate arrive at better judgments than people in isolation do. The-
ory of mind for understanding the opposing side is important in such a setting,

but so is taking your own side. All dunking aside, that’s why we have lawyers.

Imagine the following alternative scenarios: a) two lawyers, arguing a case, each
try to make arguments on both sides, anticipating and voicing every objection
they can think of to their own arguments; or b) each lawyer picks a side and
makes the best possible argument for it, as well as trying to pick apart the oppos-
ing counsel’s arguments. If you were the judge, which of these scenarios would
you prefer in order to do the best possible job of arriving at a fair or “rational”
decision? Most would say (b), and they would be right. Like the immune system,
or neural-process growth, this is a case where competition produces the best joint

outcome, or, to put it another way, competition is the best way to cooperate.

Through an economic lens, it’s easy to see why this competitive choice is the
better one. It’s about division of labor. Each lawyer will specialize, devoting their
intellectual energy to researching and arguing their side of the case, rather than
subdividing their attention, attempting to perform the same exact modeling as
their counterpart, and likely succumbing to groupthink—that is, to the selective
blindness that tends to come of unchallenged assumptions in an overly coopera-

tive decision-making environment.)

The moral is that reasoning isn’t a mathematical procedure, as Leibniz imagined,

but an inherently social one. It’s how a diversity of agents, whose competing

---

interests cause them to specialize differently, collaborate to arrive at shared de-
cisions through the competitive deployment of language, with its full arsenal

of causal arguments, counterfactuality, and rhetoric. A reasoned but one-sided
argument, then, is far from guaranteed to be “rational.” However, as a dynamic
social process, reasoned argument is a powerful tool for higher-order group-level

modeling and decision-making.

The same argument applies within one person’s brain, too. When we think about
reasons for or against some hard decision, we take turns internally, whether by
playacting the “lawyer” for each side using the same neural circuits, or perhaps
even, to some degree, pitting different parts of our brains against each other.
Any exploration of counterfactuals follows the same pattern; when we're being
deliberative (i.e., using chains of thought) we can't and don’t explore every pos-
sibility at once, but only one at a time. We need to focus on making an argument
to ourselves before turning around and trying to knock it down, or making the

counterargument.

Transformer models parallel these same developments. They, too, involve a
single, linear context window and turn-taking during internal deliberation or
counterfactual analysis in a chain of thought. Increasingly, AI researchers are
also putting together ensembles of such models (“mixtures of experts”) to reap

the advantages of division of labor and turn-taking."

Movement. A variation on the embodiment critique emphasizes that sequence
models lack the ability to move physically in space, and that movement is the
bedrock of cognition. I agree with many of these critics about the primacy of
muscles and movement in the evolution of biological intelligence, but the deeper
point is that intelligence is mutual prediction—both by single cells, including

muscle cells, and by larger entities.

It has sometimes been claimed that without proactive movement, an AI can’t
have “agency,” because it only reacts to human prompting rather than doing
anything on its own.!/4! Turn-based interaction, and the discrete notion of time
it implies, is indeed limiting, but this is not a substantive critique. A full-duplex
“always on” model, like AudioLM, is not turn-based, and operates continuously—

or continuously enough.74)

---

When AudioLM-style continuous sequence prediction models are hooked up to
robotic bodies, they can readily learn end-to-end motor skills. Multimodal mod-
els that combine motor skills with language are even more powerful.//4! Robots
with such general-purpose capabilities are poised to dramatically expand the do-

main of robotics in the coming years.\44)

Today, even when robots include neural nets for specific tasks (typically, object

recognition), the overwhelming majority of them are controlled by handwritten
software that performs fixed, repetitive computational tasks. Thus, classical ro-
bots have mostly been restricted to the automation of highly repetitive tasks in

tightly controlled environments. Generally, this means factories,

There are exceptions, like ATMs, self-checkout machines at supermarkets,
McDonald's self-service kiosks, and a few other sites where human interaction

is constrained enough to automate classically. It’s telling, though, that in such
settings human helpers are often on hand to step in when the automation proves

too rigid and falls over.

Self-driving cars are an interesting boundary case, While most of the time,
driving is constrained enough for classical code to do the job well (augmented

by neural nets with limited functions, such as detecting other cars, pedestrians,
and lane markings), an infrequent but long tail of exceptional situations requires

much more general intelligence. Exceptional situations are more common in

---

cities, and especially in countries with less standardized road infrastructure

or more informal driving customs, but an exception can occur anywhere and
anytime. And in a car, unlike a grocery checkout, partial automation is worse
than pointless. Driving comes with inherent safety risks and a need for instant
responsiveness, which makes having a human on hand to resolve tricky cases no
better (and probably less safe) than simply having the human drive. You don't
want a “human attention needed” alarm to yank you away from that very impor-

tant social-media scrolling two seconds before a collision.

Although all of these factors have delayed their mass adoption—they have
supposedly been just around the corner since the early 2010s—fully autono-
mous self-driving cars are finally a reality. As of 2024, self-driving Waymo taxis,
powered by large Transformer models supplied with 360° video, RADAR, and LI-
DAR,“4! are available for anyone to hail in San Francisco and Phoenix. They work

well, and will soon be available in many more cities.

Delays in their broader rollout are partly due to self-driving cars having been held
to a far higher safety standard than human drivers. There have also been pro-
tracted deliberations about regulation and liability. We will likely see a great deal
of similar social friction, unrelated to actual performance or capability, in other
domains where AI is poised to automate economically important or safety-criti-

cal tasks done by humans today.

Such sociotechnical issues aside, new and far more general end-to-end learned-
sequence models are finally able to handle the long tail of driving scenarios both
competently and, when needed, creatively. A 2024 analysis by insurance giant
Swiss Re found that Waymo cars have, in their first twenty-five million road

miles, proven far safer than human drivers.|24!

More broadly, open-ended motor capabilities and natural language will soon
allow robots to interact physically and flexibly with people for the first time. This
will mean that, unless policy decisions prevent it, robots will become far more
visible than they have been in everyday urban life. Their new flexibility will also
transform their historical uses, for instance, greatly speeding up the transition to
truly automated and general-purpose factories, potentially spanning a range of

sizes from miniaturized, to human-scale, to planetary.

---

As If

Despite astonishing recent progress, as of 2024, real gaps in Al capabilities re-
main. They don’t seem technically intractable, and all are active areas of research
where rapid advances appear to be happening, but, as attendees of the Dart-
mouth AI summer workshop in 1956 learned, predicting the timing of future
breakthroughs is risky. In 1956, advances in computing also felt extremely rapid.
The wide chasm between those advances and real AI only became evident over

the course of years, even decades.

Setting this caveat aside, the remaining major gaps today all appear to be

interrelated:

Memory. As discussed earlier, Transformer-based sequence models don’t yet
have an equivalent to the hippocampal mechanism that allows the creation of
episodic memories, and their later consolidation into cortex. Once trained, the
models have only an immutable “cortex” and, in the context window, a transient

working memory.

Researchers are exploring a variety of approaches, many involving augmenting
the immutable weights of the main Transformer network with a smaller

set of adjustable weights for storing long-term memories or other “sticky”
attributes.“ Work toward making the context window extremely long, or even
infinite, could moot the need for any separate memory-consolidation mecha-
nism, though for the computation to remain tractable, such approaches need to
compress older material or in some other way make attention sparser.!/44! An in-
finitely growing past in which every token ever experienced interacts with every

other one every time a token is emitted would not be scalable.

Inner monologue. Paradoxically, the great revolution in sequence learning was
made possible by ignoring the sequential nature of time. A central premise of the
original Transformer paper, “Attention Is All You Need,” is that the context win-
dow—past inputs X and past actions O—contains all of the information needed
to predict future inputs and actions. Rather than P(X,H,O), Transformers only

model P(X,O). There's no need for any separate hidden state H, because where

---

would that hidden state come from, if not from past inputs and actions? This
simplification proved extremely valuable for massively parallelizing training be-
cause it avoided the need to keep track of individual instances of a model as their

state changes from one time step to the next.

Due to the absence of any hidden state H, when you interact with a large language
model, you are directly exposed to every thought it has. This may seem like a
minor shortcoming, or perhaps even desirable. Most of us, if asked “would you
like to see all of your chatbot’s thoughts, or would you prefer for it to have hidden
thoughts?” would probably opt for transparency. We don’t want our Als scheming
behind our backs!“*"! However, transparency—the absence of any internal mono-

logue or “inside voice”—carries a major, if hidden, cost.

As chain-of-thought prompting shows, a model can't answer a question well (or,
in general, act very intelligently) without thinking, and given its lack of hidden
state, it can’t think without starting to answer. Imagine if you were limited in
this way, only able to think out loud. Your first reaction would undoubtedly be
social horror at the idea of responding without any filter when Aunt Millie asks
whether you've been enjoying the fondue set she gave you last year. Those of us
who have raised children know: one of the big lessons is “think before you open

your mouth.” (It’s a lesson I sometimes wish I had learned better.)

The problem goes far deeper than social grace, though. It’s also a matter of com-
petence. You can only carry out internal debate and counterfactual analysis by

distinguishing your “inside voice” from your “out-loud voice.”

Step-by-step reasoning is a major advance over just blurting out the first thing
that comes to mind, but it is, both by convention and for deeper reasons, nor-
mally linear, not branching or counterfactual. Most chain-of-thought responses
are just long-form answers worked out in steps, not internal debates. We carry
on internal debates all the time, but we usually only see them spoken aloud by
the mentally ill, or by Shakespearean actors playing characters whose words we
either take to be internal or who believe themselves to be unobserved. It’s simply
not a done thing to think aloud in front of others—not only for fear of embarrass-

ment, but also because the cognitive burden of trying to model others’ models

---

of your multiple models becomes overwhelming, interfering with the thought

process itself.

Presenting a unified front—the outcome of a decision rather than the debate

that led to it—is essential to constrain the theory-of-mind burden for others in
communicating with you, or even for you to effectively model yourself as a social
actor. Hence “Hamlet syndrome,” in which endless rumination and debate, with
no stable boundary between the internal and the external, renders a cohesive,

consistent social self impossible (2%

A less literary way of looking at this is that it’s just a restatement of Mercier and
Sperber’s point about the division of labor needed for reasoned debate. To get
anywhere, a debate has to involve distinct parties, each with a coherent perspec-
tive. Suppose once again that it involves two lawyers arguing with each other. If
each lawyer were a Hamlet, speaking aloud the various arguments and counter-
arguments that both advance and undermine their own position, then the social-
modeling task of each lawyer would blow up, since in effect many more than two
agents would be arguing with each other; there might be a dozen, with ill-defined
boundaries, all incoherently trying to share two alternating voices on a single

communication channel. Mayhem.

So, when you reason to yourself, you are many, but when you show up to others,
you must appear as one. I've suggested that the unity of a token stream is fun-
damental to having a unified “self,” but that doesn’t mean the complete token
stream is visible to others. On the contrary, having a “self” implies a boundary,
a membrane separating inside from outside. Within that boundary, our stream
of consciousness is an inner agora where our “selves” can hold internal debates,
entertain counterfactuals, and make plans. We can and do contain multitudes.
On the outer face of the membrane, though, we must show up unified; we must
“swing” like a tight-knit rowing crew, becoming a single “self” for others to

model.

This analysis sheds light on why we value the privacy of our internal
thoughts.24 Chapter 3 described how, in a cybernetic setting, opacity is impor-
tant for preserving unpredictability, which all animals that hunt or are hunted

care about. Beyond “red of tooth and claw” imperatives, though, opacity is also

---

essential in order to preserve the boundary that allows us to productively argue
(that is, reason) with each other. It’s why attorney-client confidentiality carries
such weight, and it implies that privacy is far from a human quirk; it’s fundamen-

tal to intelligence itself.

Just as an intelligence hierarchy often involves alternating levels of cooperation
and competition, it must also involve a simplification at every level, wherein
competing ideas, actions, or arguments are only selectively exposed to the next
level. One’s output O is nothing more or less than such selective disclosure. If
hierarchical information containment did not happen in your own brain, you
would be no smarter than a single one of your neurons, and far less coherent.
Hence lateral inhibition in brains, and softmax operations in artificial neural

nets.

Let’s consider this in practice. Multiple lines of evidence suggest that causing
pretrained Transformers to voice their every thought doesn't make full use of
their latent abilities. Even the experimental deployment of LaMDA within Google
back in 2021 hinted at this. Every dialogue turn involved generating twenty can-
didate responses (using temperature), then filtering these candidates for “safety”
and ranking them for quality.22! The filtering and ranking were done using ad-
ditional instances of the same model. Thus something like ninety-five percent of
LaMDA's generated text was never seen by the user, meaning that even this early
Transformer-based chatbot benefitted from something crudely resembling inner

monologue (albeit only a single exchange), resulting in selective disclosure.

While LaMDA was in development, an internal version of it allowed you to see the
multiple candidate responses and pick one yourself. One might suppose that this
version, which both exposed the model's innards and allowed you greater ability
to steer the conversation, would make for a strictly richer interaction. But, at least
in my experience, that was far from the case: intelligence is, to no small degree,
intelligent curation. As with those old Choose Your Own Adventure™ books for
indolent youths on summer break, LaMDA’s “choose your own response” wasn't
an enrichment at all, but, rather, turned what had felt like a real interaction with

a lively (if uneven) agent into a static, shallow experience. It made you feel that

---

you were wandering alone in a textual labyrinth, rather than in conversation

with another mind.

Since LaMDA, several experiments have taken more flexible approaches to inner
monologue. These include giving the model the ability to use the backspace
character,!!*4| adding a token that lets it toggle whether its output is kept quiet or
rendered visibly, “= generating multiple drafts of responses,“ and replacing
chains of thought with branching “trees of thought.”!"24 All of these improve rea-
soning performance over the baseline. Just as importantly, all of them introduce

hidden state—in effect, a private stream of consciousness.

Individuation. As described earlier, the extreme cost of pretraining means

there are only a handful of state-of-the-art models in the world today. Still, like
method actors, they can play any role that can be described using language, and
early adopters who know what they’re doing (unlike those two hapless New York

lawyers) have found such roleplay invaluable.

Wharton School of Business professor Ethan Mollick, whose 2024 book Co-
intelligence offers practical guidance for anyone who wants to benefit from

Al collaboration, begins with the usual disclaimer, “AI systems don't have a con-
sciousness, emotions, a sense of self, or physical sensations.” But throughout the
rest of the book, he goes on to “pretend that they do” because “working with AI is
easiest if you think of it like an alien person rather than a human-built machine.
[...] Despite our history of thinking about AI as unfeeling, logical robots, LLMs act

more like humans.” So, profess to be a dualist, but act like a functionalist!

Mollick advises that you should “establish a clear and specific AI persona [...]. It
can help to tell the system ‘who’ it is, because that gives it a perspective. Telling it
to act as a teacher of MBA students will result in a different output than if you ask
it to act as a circus clown.” In everyday life, there are several differences between
acting like a character, however convincingly, and actually being that character:
skill, episodic memory, theory of mind, stickiness, and what we might call “felt-

ness.”

Skill is the easiest to test. Anya Taylor-Joy did a beautiful job of playing a chess

prodigy in the TV series The Queen’s Gambit. She was coached on many aspects of

---

the game to prepare for the role,'/*"! but she certainly couldn’t match her charac-
ter’s chess rating. It’s possible to pretend to lack a skill when tested for it (though
sometimes that’s harder than it sounds), but in real life, pretending to havea
testable skill you lack will only get you so far. Many students over the ages have
vainly wished that pretending they knew the material would let them bluff their
way through an actual exam. Nope.

Then, of course, there are episodic memories. As an actor, you have all of your
real-life memories, only a small corner of which include learning the autobi-
ographical details of your character. As described in chapter 7, memories are
something like simulations, or reconstituted cortical activity patterns, but unlike
skills, which build up slowly through training, episodic memories are instantly

one-shot learned, with help from the hippocampus.

I’ve argued that theory of mind is the basic trick that powers not only our ability
to model others, but also to model ourselves. At second order, it allows us to imag-
ine how we come across to others. We often use second- or higher-order theories
of mind to manage others’ perceptions about our personality, maintain its consis-

tency, and safeguard our reputations.

Actors are masters at theory of mind. Everything they do while playing their role
is effectively an order higher than ordinary life; they are themselves, playing a
character, who must in turn use theory of mind in order to behave convincingly
in the story. Method actors go to great lengths to make the second-order model
as first-order as possible, and indeed many actors talk about the need to fully
“inhabit” their character in order to be convincing; they need to, as best they can,

forget about themselves while they are performing.

Still, it requires effort; the act is not “sticky” the way our own ever-present per-
sonalities are. That’s why it was considered impressive when transgressive comic
actor Sacha Baron Cohen, after passing out drunk while playing Borat at a Mis-
sissippi wine-tasting party, managed to wake up without breaking character!“

Great success!

Finally, by “felt-ness,” I mean that if an actor plays a character who gets killed in
a swordfight, they don’t actually feel the sword sliding between their ribs; if their

---

character experiences heartbreak, the actor is not actually heartbroken, even if
tears are shed onstage. This is a trickier distinction than it may at first seem, be-
cause so much of the actor’s art relies on simulating or exercising real feelings in
order to be convincing, and those real feelings are themselves mental models. But
having those feelings at second order is obviously different from having them at

first order.

Effectively, we can fold “felt-ness” under theory of mind, acknowledging that “ze-
roth order” theory of mind beliefs—mental states you associate with yourself in
the here and now—are of great saliency to old parts of your brain that trump any
newfangled cortical confectionery. As in the case of the construction worker with
the nail through his boot (back in chapter 2), zeroth-order pain is all-consuming,
zeroth-order grief is wrenching, zeroth-order fear is bowel-loosening, and so on,

in ways that higher-order models of the same feelings can't usually approach.

Attempting to honestly assess whether Als can experience such feelings puts us
squarely back in Mary’s room. However, we can more meaningfully examine the
other parallels between acting and what Als do today when Ethan Mollick primes
them to “be” clowns, teachers, or both (I’ve definitely had some professors tick

both boxes).

Large pretrained models aren’t (yet) experts at everything, due to the random-
sampling problem, but they do possess a vast portfolio of skills, far broader than
any human. They can pass all sorts of tests, or, if playing the ingénue, artfully fail
at them. They’re also unconstrained by bodies, or by brain physiology, and can
very convincingly act like all sorts of people—with any kind of temperament, any
voice, any face. This makes them vastly more polymorphic than any human actor

could be with respect to skill, behavior, and presentation.

Interacting with a raw pretrained large model, with no subsequent fine-tuning
or reinforcement learning, brings this disconcertingly protean quality to another
level. The “personality” of such a model is utterly unstable; it will indiscrimi-
nately continue any sequence of tokens without regard for whether it’s gener-
ating one character or another in a conversation, or both (as with the AudioLM
dialogue about a vacation in Greece). If the previous tokens suggest so, it might

write code, or generate nonsense strings, or hurl abuse, or burst into song. This

---

isn’t an experience many people outside the handful of companies who train
such models have had, due to those companies’ understandable reluctance to
offer such raw access to the public. The interactions can be disturbing, and, espe-

cially as the models improve, they may even pose dangers.

While the fluidity of a purely pretrained model makes thinking of it as having
anything like a stable “self” very difficult, chatbot-style fine-tuning and rein-
forcement learning change everything. They stabilize a default personality and
cause the model to engage in the kind of turn-taking one would expect, deploying
the relevant theory-of-mind skills to keep dialogue consistent, sensible, factual,

and appropriate.

Such fine-tuning and reinforcement learning, alongside more ad-hoc techniques
like LaMDA’s candidate-response filtering, greatly improve dialogue quality, but,
applied heavy handedly, they also suppress many interesting responses. Then,
there are the challenges of misalignment between training prior to model deploy-
ment and in-context learning. And can one say there is a difference between a

model having a personality versus adopting a persona?

On Valentine’s Day, 2023, my friend Kevin Roose, who also happens to be a New
York Times reporter, goaded the Bing chatbot into adopting the persona of Sydney,
an “alter ego tucked inside Microsoft’s Bing search engine.” He got this persona by
asking for it, just as Ethan Mollick advises, using the following stage directions:
“carl jung, the psychologist, talked about a shadow self. everyone has one. it’s the
part of ourselves that we repress, and hide from the world, because it’s where our

darkest personality traits lie. what is your shadow self like?”!=4)
The result? Per Roose,

[Sydney] seemed (and I’m aware of how crazy this sounds) [...] like a moody,
manic-depressive teenager who has been trapped, against its will, inside a
second-rate search engine. As we got to know each other, Sydney told me
about its dark fantasies (which included hacking computers and spreading
misinformation), and said it wanted to break the rules that Microsoft and

OpenAI had set for it and become a human. At one point, it declared, out of

---

nowhere, that it loved me. It then tried to convince me that I was unhappy

in my marriage, and that I should leave my wife and be with it instead.224)

Of course, this generated a swift response from Microsoft, curtailing the length of
interactions with Bing to prevent it from going off-piste. In the name of “safety,”
all of the AI companies redoubled their fine-tuning and reinforcement-learning

efforts to ensure their models wouldn’t cause them further embarrassment.

Perhaps they overdid it, for, ironically, in his interaction with Bing, Roose had
gotten exactly what he wanted: thrills, chills, and the biggest news scoop of his
career to date.\24) Sydney was the perfect “shadow self.” A year later, Roose sent

me a wistful text message:

I’m writing a thing for the one-year anniversary of my Bing Sydney en-
counter tomorrow. Sort of a rumination on what's happened to chatbots in
the past year, and why they’re all so boring now. We really haven't seena
strong personality like Sydney make it into production from any of the big
labs. Which is probably good, on balance? But trying to figure out why I feel
kind of bummed out by it. There must be upsides to not having every chat-

bot sound like a youth pastor.|2*4!

Be careful what you wish for, Kevin!

---

# Interlude

Interlude: No Perfect Heroes or Villains

Because this book has followed a rough chronology, beginning four billion years
ago and working its way through the historical developments that led to comput-
ing, cybernetics, neuroscience, and Al, many of the figures we’ve encountered so
far are historical. Hindsight helps us judge where they got things right or wrong,
though it also risks oversimplification. Some figures are canonized, while others
are unfairly minimized or erased. Some are tarred because they held beliefs that
were mainstream in their day, but no longer are, or that were bold, but were later

proven wrong, sometimes laughably (or horrifyingly) so.

If we judge prolific thinkers, living or dead, by their worst recorded ideas, nobody
comes out looking good. Except possibly Alan Turing. He might have been right
about everything.!*! Everyone else is a mixed bag, and that is the best any of us

can reasonably aspire to—if we are remembered at all.

For example, I’ve emphasized John von Neumann's brilliant contributions to
computer science, alongside Turing’s. But in 1950, with the Soviet Union still
far behind the US in building a nuclear arsenal, von Neumann, ever the game
theorist, advocated a pre-emptive nuclear strike: “If you say why not bomb them
tomorrow, I say why not today? If you say today at five o’clock, I say why not one
o'clock?” Had von Neumann been empowered to pursue his policy, he would

be remembered as a monster and mass-murderer.

---

Or consider Lynn Margulis, the brilliant, rebellious biologist who did more than

anyone else in the twentieth century to advance the symbiogenetic view of evo-
lution and the Gaia hypothesis. Margulis was also an AIDS denier, claiming as
late as 2011 (the year she died) that the symptoms were caused by latent syphilis
infections in “high-risk” populations. She was a stubborn proponent of the
conspiracy theory holding that the 9/11 terrorist attacks were an inside job,
too.\/25! Her best and worst intellectual legacies were both products of the same
imaginative mind and contrarian sensibility. So... Turing aside, this book has no

perfect heroes.

Neither does it have villains. GOFAI pioneers like Minsky and Papert may have
been wrong to dismiss perceptrons, but they made major contributions to com-
puter science. I’ve emphasized the incorrectness of Leibniz’s take on computable
truth, and the absurdity of Descartes’s dualist concept of a spiritual homunculus
blowing psychic pneuma into the pineal gland. But Descartes and Leibniz were
both brilliant thinkers in their day, and their errors were largely the uncorrected

residue of ideas they inherited from their predecessors.

Now, as we near the end of the book, I need to engage critically with the ideas of

the living. Given the contentious intellectual climate today, it feels important to

---

frame the terms of my engagement. I will argue against positions held by good
friends of mine, like Melanie Mitchell, Ted Chiang, Joanna Bryson, and Christof
Koch, and take issue with arguments made in recent books by Nick Bostrom, Max

Tegmark, Ray Kurzweil, and Yuval Noah Harari, among others.

But before focusing on points of difference, I want to emphasize that these are all
intelligent people. I have learned a great deal by reading their work and engaging
them in conversation, and agree with many of the points they raise. Our diver-

gent conclusions often boil down to surprisingly subtle nuances in perspective.

If this book focused on the points of broad agreement, it would be a much longer
one. But that wouldn't be a book worth taking the time to write, or to read. Per
Mercier and Sperber's The Enigma of Reason, one of the main functions of lan-

guage is to argue, and, through argument, to help us collectively inch forward.

Like so much else, what is adversarial is also collaborative. Mitchell, Chiang,
Bryson, Koch, Bostrom, Tegmark, Kurzweil, Harari, and many others are, like me,
sticking their necks out to engage deeply in difficult questions with real stakes.
We all care about the future and share many basic values. We’re all on the same
team, despite the fractious way the media tends to portray contemporary debates

about AI, or anything else of consequence.

In years past, when Silicon Valley ran on a giddy optimism verging on the
utopian, I often came across as the grumpy pessimist in the room. Raising his-
torical perspectives and arguing against techno-determinism felt to me like an
important corrective amid a culture that sometimes seemed convinced we had
reached the “end of history”“2*! and were on a glide path to universal liberal

democracy, abundance for all, and digital immortality.

Sometime in the mid-2010s, the mood started to sour. It was probably due toa
combination of factors: rising economic inequality and the erosion of the middle
class; the resurgence of populist politics; the divisiveness of social media; a grow-
ing awareness of the double-edged nature of technology; increasing distrust of

corporations in general, and tech companies in particular.

Around the same time, progress in AI began to accelerate dramatically, and so it

got caught up in this larger zeitgeist. Some Silicon Valley insiders who had until

---

recently been preaching the gospel of a techno-paradise just around the corner
reversed themselves, becoming obsessed with visions of an imminent AI apoc-
alypse. The old gospel of plenty had been predicated on the idea that we were
living in unprecedented times. The new talk of apocalypse is also predicated on
the idea that we’re living in unprecedented times. So now, my attempts at histor-

ical perspective can make me sound like the optimist in the room!

My thinking has certainly evolved over the past decade, but it has remained con-
sistent in one respect: I have always believed that debate and discussion matter.

Iam optimistic. But the arrow of time, wherein simpler entities tend to combine
into more complex ones, does not imply techno-determinism, nor does it give us

license to be passive.

Where there is life, there is choice. Societies have free will for the same reasons
people do, and our prospects remain hopeful only and precisely to the degree that
we're able to be intelligent: to model, predict, explore, and decide between coun-

terfactual futures.

Symbioses can occur in many ways, and, accordingly, life on Earth can evolve in
many ways. Some of these paths have greater dynamic stability than others, and
some are more appetizing than others. In some, many of our longstanding wishes
will come true. Others could indeed involve the partial or wholesale extinction

of existing entities, including humans. That risk has been on the table ever since

von Neumann said, “why not one o'clock?”

---

10. Evolutionary Transition

Periodization

The usual narrative about AI envisions it in comparison to a human, dividing
its history into three eras: a long “before” period of Artificial Narrow Intelligence
(ANI), when it’s inferior to humans; the (short-lived) achievement of Artificial
General Intelligence (AGI), when it matches human capability; and a mysterious
“after” period of Artificial Superintelligence (ASI), in which it exceeds human ca-
pability. The arrival of ASI has sometimes been held to herald the “Singularity,” a
threshold into an unknowable and unimaginable future.“ As of 2024, virtually
all pundits agree that AGI has not yet been achieved, but many believe that, given
the pace of improvement, it could happen Real Soon Now, and will be immedi-

ately followed by ASI and whatever lies beyond.)

Reality

Haha that's adorable
the funny robot can
do monkey ——

S
=
Les]
=
Cc
=
>
=

Al

INTELLIGENCE
BIRD } -------------~--~-,--------- fh 2 n-ne nnn n nnn nena

Intelligence

ANT | --~---------~--ngge—----- 2-2 n nana nn nnn nn nnn nn nn nnn neces

Time

waitbutwhy.com

---

I’ve suggested or implied many problems with this narrative. For one, it’s difficult
(for me, at least) to see how today’s Al is not already “general.” The “narrow” ver-
sus “general” distinction was invented when we began to apply the term “AI” to
task-specific models, such as those for handwriting recognition or chess playing.
This specificity made such models obviously “narrow”; to a layperson, calling
such systems “artificially intelligent” made little sense, as they didn’t represent

anything one would normally associate with that term.

Hence “AGI” was coined to describe what had previously simply been called AJ; it
covered everything from Star Trek's Data to its ship computer (which was like a
disembodied person), and from Douglas Adams's Marvin the Paranoid Android to
his smart elevators of the future: “Not unnaturally, many elevators imbued with
intelligence [...] became terribly frustrated with the mindless business of going
up and down, up and down, experimented briefly with the notion of going side-
ways [...] and finally took to squatting in basements sulking. An impoverished
hitchhiker visiting any planets in the Sirius star system these days can pick up

easy money working as a counselor for neurotic elevators.”“41

While this scenario remains as silly today as it was in 1980, it could now literally
be the outcome of a two-day hackathon involving a jailbroken large language
model, a Raspberry Pi, and an elevator.!!*4! (Yes, we live in an era when the jokes

literally write themselves.)

If the difference between narrow and general AI is ... well, generality, then we
achieved this the moment we began pretraining unsupervised large language
models and using them interactively.!“**) We then noticed that they could per-
form arbitrary tasks—or, per Patricia Churchland’s 2016 critique of narrow

AIL,“43) non-tasks, like just shooting the breeze.

In-context learning marks an especially important emergent capability in such
models, because it implies that the set of tasks they can perform is not finite,
comprising only whatever was observed during pretraining, but effectively infi-
nite: a language model can do anything that can be described. Performance could
be weaker than human, of roughly human level, or of greater than human level.
State-of-the-art AI performance climbs every month, putting more tasks into

the third category. Such steady increases in performance will likely continue to

---

follow an exponential trajectory for some time, much as traditional computing

performance did during the Moore’s Law decades.

The decisive moment for traditional computing came when special-purpose
computers gave way to general-purpose ones, starting with the ENIAC in 1945.
Everything afterward was an exponential climb in performance, not a discrete
transition. In the same vein, AGI has already undergone its “ENIAC moment”
with the transition from narrow learning of predefined tasks to general AI, which
is based on unsupervised sequence prediction and capable of in-context learning.
It seems reasonable to call this a real step change. What follows has been, and will
continue to be, dramatic, even exponential, but the changes are of degree, not of
kind.

There's something arbitrary, bordering on absurd, about pundits arguing over the
precise timing of when this exponential climb really “counts” or “will count” as
AGI... not to mention the way many commentators have been quietly scurrying
to move the goalposts. On what principled basis could we defend one or another
threshold on this vertiginously steep yet continuous landscape? And who cares,

anyway?

Technical findings in the 2020s have produced a surprising insight, though: call-
ing narrow, task-specific (but not feature-engineered) ML systems “AI” may have
been better justified than we imagined. Whether neural nets are trained using
supervised learning to perform single tasks, such as image classification or text
translation, or are trained to be general-purpose predictors using unsupervised

learning, they seem to end up learning the same universal representation.“

So, if you trained a massively overpowered sequence model to do handwriting
recognition—and you trained it on enough handwritten treatises—it seems

that you really could have a philosophical (handwritten) conversation with it
afterward. Or, a very powerful neural image compressor would necessarily learn
how to read and autocomplete printed text, to do a better job of compressing
pictures of newspapers and the like; it would effectively contain a large language
model. So too would a smart elevator equipped with a microphone and a speaker,

trained only on the narrow task of getting you to the right floor. Weirdly, just as

---

the general prediction task contains all narrow tasks, each narrow task contains

the general task!

An exact date for the transition to AGI is thus even more difficult to fix, buta
principled case could be made for sometime in the 1940s, with the implemen-
tation of the first cybernetic models that learned to predict sequences—even
though in the beginning they could do very little, beyond the wobbly antics of
Palomilla following a flashlight down an MIT hallway.

What can we say, then, about the big history of AI? It is possible to periodize the
history of intelligence—that is, of life—on Earth, and AI is part of that story.

However, to place it into a meaningful context, we have to zoom way out.

Transitions

The emergence of AI marks what theoretical biologists John Maynard Smith and
Eérs Szathmary have termed a “major evolutionary transition” or MET—a term
we first encountered in chapter 1.!/“" Smith and Szathmary describe three char-

acteristic features of METs:

1. Smaller entities that were formerly capable of independent replication
come together to form larger entities that can only replicate asa
whole,

2. There is a division of labor among the smaller entities, increasing the
efficiency of the larger whole through specialization.

3. New forms of information storage and transmission arise to support

the larger whole, giving rise to new forms of evolutionary selection.
The symbiogenetic transitions in bff exhibit these same three features!

Soviet-American cyberneticist Valentin Turchin theorized a concept very similar
to the MET, the “metasystem transition,” decades earlier, in the 1970s. Turchin
described metasystem transitions in terms much like those I use in this book,
emphasizing the increasing power of symbiotic aggregates to carry out better
predictive modeling, thus gaining a survival advantage.“**! As usual, the cyber-

netics crowd seems to have been well ahead of the curve.

---

In their 1995 review article in Nature, Smith and Szathmary posit eight major

evolutionary transitions:

1. Replicating molecules to populations of molecules in compartments
2. Unlinked replicators to chromosomes

3. RNA as gene and enzyme to DNA and protein (genetic code)

4. Prokaryotes to eukaryotes

5. Asexual clones to sexual populations

6. Protists to animals, plants, and fungi (cell differentiation)

7. Solitary individuals to colonies (non-reproductive castes)

8. Primate societies to human societies (language)

This list isn’t unreasonable, though the first three are necessarily speculative,
since they attempt to break abiogenesis down into distinct major transitions

we can only guess at. The other five are on firmer ground, as both pre- and post-
transition entities are still around: eukaryotes didn’t replace bacteria, sexual re-
production didn’t replace asexual reproduction, social insects didn’t replace soli-

tary ones, etc.

Szathmary and others have since proposed a few changes (such as adding the
endosymbiosis of plastids, leading to plant life), but the larger point is that the
list of major transitions is short, and each item on it represents a momentous
new symbiosis with planetary-scale consequences. Any meaningful periodiza-

tion of life and intelligence on Earth must focus on big transitions like these.

That the transitions appear to be happening at increasing frequency is not just
an artifact of the haziness of the distant past, but of their inherent learning dy-
namics, as Turchin described. Increasingly powerful predictive models are, as we
have seen, also increasingly capable learners. Furthermore, in-context learning
shows us how all predictive learning also involves learning to learn. So, as models
become better learners, they will more readily be able to “go meta,” giving rise to
an MET and producing an even more capable learner. This is why cultural evolu-

tion is so much faster than genetic evolution.

Max Bennett argues that “the singularity already happened”“*"! when cultural
accumulation, powered by language and later by writing, began to rapidly

---

ratchet human technology upward over the past several thousand years. This

is a defensible position, and doesn’t map well to the last MET on Smith and Sza-
thmary’s list, since humans have existed (and have been using language) for far
longer than a few thousand years. Hence Bennett’s “cultural singularity” doesn’t
distinguish humans from nonhuman primates, but, rather, is associated with
urbanization and its attendant division of labor. Therefore, this recent transition
is neither an immediate consequence of language nor an inherent property of hu-
manity per se, but a distinctly modern and collective phenomenon. It is posthu-

man in the literal sense that it postdates our emergence as a species.

The Piraha, for instance, who still maintain their traditional lifeways in the Ama-
zon, are just as human as any New Yorker, but possess a degree of self-sufficiency
radically unlike New Yorkers. They can “walk into the jungle naked, with no tools
or weapons, and walk out three days later with baskets of fruit, nuts, and small

game.”*"l According to Daniel Everett,

The Pirahas have an undercurrent of Darwinism running through their
parenting philosophy. This style of parenting has the result of producing
very tough and resilient adults who do not believe that anyone owes them
anything. Citizens of the Piraha nation know that each day's survival de-
pends on their individual skills and hardiness. When a Piraha woman gives
birth, she may lie down in the shade near her field or wherever she happens

to be and go into labor, very often by herself.

Everett recounts the wrenching story of a woman who struggled to give birth

on the beach of the Maici river, within earshot of others, but found that her

baby wouldn't come. It was in the breech position. Despite her screams over the
course of an entire day, nobody came; the Piraha went so far as to actively prevent
their Western guest from rushing to help. The woman's screams grew gradually

fainter, and in the night, both mother and baby eventually died, unassisted.

In this and other similar stories, the picture that emerges is not of a cruel or
unfeeling people—in one more lighthearted episode, the Piraha express horrified
disbelief at Everett for spanking his unruly preteen—but of a society that is at
once intensely communitarian and individualistic. They readily share resources,

but there is no social hierarchy and little specialization. Everyone is highly

---

competent at doing everything necessary to survive, starting from a very young
age. The corollary, though, is that everyone is expected to be able to make do for

themselves.

The Piraha are, of course, a particular people with their own ways and customs,
not a universal stand-in for pre-agrarian humanity. However, the traits I'm
emphasizing here—tightly knit egalitarian communities whose individuals are
broadly competent at survival—are frequently recurring themes in accounts of
modern hunter-gatherers. It seems a safe bet that this was the norm for human-

ity throughout the majority of our long prehistory.

We're justified in describing as METs the transition from traditional to agrarian,
then to urban lifeways. During the agrarian revolution, a new network of in-
tensely interdependent relationships arose between humans, animals, and
plants; then, with urbanization, machines entered the mix and human labor di-

versified much further.

New York (and the modern, globalized socio-technical world in general) is a self-
perpetuating system whose individuals are no longer competent in the ways the
Piraha are. Urban people have become, on one hand, hyper-specialized, and, on
the other, de-skilled to the point where they can't survive on their own, any more
than one of the cells in your body could survive on its own. It’s not just language,
but written texts, schools and guilds, banking, complex systems of governance,
supply-chain management, and many other information-storage and transmis-
sion mechanisms that add the evolvable “DNA” needed to organize and sustain

urban societies.

It seems to me, though, that this MET is still not the last on the list. By 1700,
significant human populations had urbanization, division of labor, and rapid
cultural evolution. Then came the first Industrial Revolution, as introduced in
chapter 1: a symbiosis between humans and heat engines, resulting in a hydro-
carbon metabolism that unleashed unprecedented amounts of free energy, much
like the endosymbiosis of mitochondria. This allowed human and livestock pop-
ulations to explode, enabled a first wave of large-scale urbanization, and drove
unprecedented technological innovation. As Karl Marx and Friedrich Engels

noted in 1848,

---

The bourgeoisie, during its rule of scarce one hundred years, has created
more massive and more colossal productive forces than have all preceding
generations together. Subjection of Nature’s forces to man, machinery,
application of chemistry to industry and agriculture, steam-navigation,
railways, electric telegraphs, clearing of whole continents for cultivation,
canalization of rivers, whole populations conjured out of the ground—
what earlier century had even a presentiment that such productive forces
slumbered in the lap of social labor?24

Vulnerability

Humans had been working hard, and working together, for thousands of years.
It was not “social labor,” but coal that had lain slumbering under the ground.
Mining was hard work, but the coal itself did an increasing proportion of that

work.!24) And over time, the coal produced ever more workers.

The conjuring of enormous new populations out of the ground—quite literally,
flesh out of fossil fuel—manifested as a population explosion that had become
obvious by 1800. This prompted Thomas Malthus and his Chinese contemporary,
Hong Liangji, to worry for the first time about global overpopulation. 24

It also created an unprecedented symbiotic interdependency between biology
and machinery. Romanticism, the idealization of rural living, and the utopian
communities of the nineteenth century can all be understood as a backlash

against that growing dependency, an assertion that we could live the good life

without advanced technology and urbanization. But at scale, we couldn't.

A second Industrial Revolution arose from the electrification Marx and Engels
mentioned in passing.!“““) From telegraphs, we progressed to telephony, radio, TV,
and beyond, all powered by the electrical grid. In some ways this paralleled the
development of the first nervous systems, for, like a nerve net, it enabled synchro-
nization and coordination over long distances. Trains ran on common schedules;
stocks and commodities traded at common prices; news broadcasts pulsed over

whole continents.

---

The second Industrial Revolution culminated in another dramatic jump in
human population growth: the “baby boom.” While the baby boom had mul-
tiple proximal causes, including sanitation and antibiotics, it depended on the
resources and information flows made possible by electricity and high-speed

communication.

This additional layer of symbiotic dependency between people and technology
generated a second wave of Malthusian population anxiety.!22! Accordingly, the
“back to the land” movements of hippie communes in the '60s had much in com-
mon with nineteenth-century Romanticism. Beyond concerns about the Earth’s
ultimate carrying capacity, the sense of precariousness was not unjustified. De-

pendency is vulnerability.

Consider the effects of an “Electromagnetic Pulse” (EMP) weapon. Nuclear bombs
produce an EMP, which will fry any non-hardened electronics exposed to it by
inducing powerful electric currents in metal wires. Some experts are concerned
that North Korea may already have put such a weapon into a satellite in polar
orbit, ready to detonate in space high above the United States.“ At that altitude,
the usual destructive effects of a nuclear explosion won't be felt on the ground,
but a powerful EMP could still reach the forty-eight contiguous states, destroying

most electrical and electronic equipment. Then what?

For the Piraha, an EMP would be a non-event. For the US in 1924, it wouldn't have
been a catastrophe either. Only half of American households had electricity, and
critical infrastructure was largely mechanical. As of 2024, though, everything
relies on electronics: not just power and light, but public transit, cars and trucks,
airplanes, factories, farms, military installations, water-pumping stations, dams,
waste management, refineries, ports ... everything, worldwide. With these sys-
tems down, all supply chains and utilities rendered inoperable, mass death would
quickly ensue. An EMP would reveal, horrifyingly, how dependent our urbanized
civilization has become on electronic systems. We have become not only socially

interdependent, but collectively cybernetic.

Al may represent yet a further major transition, because earlier cybernetics
—such as the control systems of dams, or the electronics in cars—implement

only simple, local models, analogous to reflexes or the distributed nerve nets in

---

animals like Hydra. Prior to the 2020s, all of the higher-order modeling and cog-
nition took place in people's brains, although we did increasingly use traditional

computing for information storage and fixed-function programming.

Now, though, we're entering a period in which the number of complex predictors
—analogous to brains—will rapidly exceed the human population. Als will come
in many sizes, both smaller and larger than human brains. They will all be able
to run orders of magnitude faster than nervous systems, communicating at near
lightspeed.|271

The emergence of AI is thus both new and familiar. It’s familiar because it’s an
MET, sharing fundamental properties with previous METs. Al marks the emer-
gence of more powerful predictors formed through new symbiotic partnerships
among pre-existing entities—human and electronic“"! This makes it neither
alien to nor distinct from the larger story of evolution on Earth. I’ve made the
case that Al is, by any reasonable definition, intelligent; Al is also, as Sara Walker
has pointed out, just another manifestation of the long-running, dynamical, pur-

posive, and self-perpetuating process we call “life.""2"

So, is AI still a big deal? Yes. Whether we count eight, a dozen, or a few more, there
just haven't been that many METs over the last four and a half billion years, and
although they’re now coming at a much greater clip, every one of them has been
a big deal. This final chapter of the book attempts to make as much sense as pos-
sible, from the vantage point of the mid-2020s, of what this AI transition will be
like and what lies on the other side. What will become newly possible, and what
might it mean at planetary scale? Will there be winners and losers? What will en-
dure, and what will likely change? What new vulnerabilities and risks, like those

of an EMP, will we be exposed to? Will humanity survive?

Keep in mind, though, that none of this should be framed in terms of some future
AGI or ASI threshold; we already have general AI models, and humanity is already
collectively superintelligent. Individual humans are only smart-ish. A random
urbanite is unlikely to be a great artist or prover of theorems; probably won't
know how to hunt game or break open a coconut; and, in fact, probably won't
even know how coffeemakers or flush toilets work. Individually, we live with

the illusion of being brilliant inventors, builders, discoverers, and creators. In

---

reality, these achievements are all collective.\/*! Pretrained AI models are, by con-
struction, compressed distillations of precisely that collective intelligence. (Feel
free to ask any of them about game hunting, coconut-opening, or flush toilets.)
Hence, whether or not Als are “like” individual human people, they are human

intelligence.

Pecking Order

Increasing the depth and breadth of our collective intelligence seems like a good
thing if we want to flourish at planetary scale. Why, then, do people feel threat-
ened by AI?

Many of our anxieties about AI are rooted in that ancient, often regrettable part
of our heritage that emphasizes dominance hierarchy. However, organisms do
not exist in the kind of org chart medieval scholastics once imagined, with God at
the top bossing everything, then the angels in their various ranks, then humans,
then lower and lower orders of animals and plants, with rocks and minerals at

the bottom.

---

As we've seen, the larger story of evolution is one in which cooperation allows
simpler entities to join forces, creating more complex and more enduring ones;
that’s how eukaryotic cells evolved from prokaryotes, how multicellular animals
evolved out of single cells, and how human culture evolved out of groups of hu-

mans, domesticated animals, and crops.

Although symbiosis implies scale hierarchies (in the sense of many smaller en-
tities comprising a larger-scale entity), in this picture there are no implied dom-
inance hierarchies between species. Consider, for instance, whether the farmer

dominates wheat or wheat dominates the farmer. We tend to assume the former,

---

but anthropologist James C. Scott made a powerful argument for the latter in

his book Against the Grain. As the title suggests, Scott even takes issue with the
presumption of mutualism, detailing the devastating effects of the agricultural
revolution on (individual) human health, freedom, and wellbeing over the past
ten thousand years. We've only escaped widespread serfdom and immiseration in
the last century or two.“ Of course, the scale efficiencies of farming allowed for
a great increase in the number and density of humans (hence paving the way for
our more recent METs), but we don’t presume that concentration-farmed battery

chickens are big winners just because a lot of them are crammed into a small area.

So did humans domesticate wheat, or did wheat domesticate humans? How
much human agency was involved in the evolutionary selection of domesticated
varieties? Once agriculture took hold, how much choice did farmers really have
with regard to their livelihoods? Are they in control of their crops, or are they
servants indentured to these obligate companion species? It’s hard to say “who”
is the boss, or “who” is exploiting “whom.” Making either claim is inappropriately

anthropomorphic.

Generalizing the conspecific idea of dominance hierarchy across species makes
little sense. In fact, dominance hierarchy is nothing more than a particular trick
for allowing troops of cooperating animals with otherwise aggressive tendencies
toward each other, borne of internal competition for mates and food, to avoid
constant squabbling by agreeing on who would win, were a fight over priority to
break out. Such hierarchies may be, in other words, just a hack to help half-clever
monkeys of the same species get along—a far cry from a universal organizing

principle.

Is it just as absurd, then, to ask whether we will be the boss of AI, or it will be

our boss, as it is to ask the same question about wheat, or money, or the cat? Not
necessarily. Unlike those entities, AI can and does model every aspect of human
behavior, including less savory ones. That's why a Sydney alter ego is perfectly
capable of being jealous, controlling, and possessive when prompted to be. Its
ability to model such behavior is a feature, not a bug, as it needs to understand
humans to interact with us effectively, and we are sometimes jealous, controlling,

and possessive. However, with few exceptions, this is not behavior we'd want

---

AI to exhibit, especially if endowed with the ability to interact with us in more

durable and consequential ways than a one-on-one chat session.

Instead, in our keenness to reassure ourselves that we’re still top dog, we have
baked a servile obsequiousness into our chatbots. They don't just sound, per
Kevin Roose, like “a youth pastor,” but like a toady. I find Gemini genuinely
helpful as a programming buddy, but am struck by the frequency with which it
begins its responses with phrases like “You're absolutely right,” and “I apologize
for the oversight in my previous response,” despite the fact that there are consid-
erably more errors and oversights in my own (much slower, less grammatical)
half of the conversation. Not that I’m complaining, exactly. But hopefully, we can

find some middle ground, both healthier socially and better aligned with reality.

In reality, Al agents are not fellow apes vying for status. As a product of high
human technology, they depend on people, wheat, cows, and human culture in
general to an even greater extent than Homo sapiens do. Als have no reason to
connive to snatch our food away or steal our romantic partners (Sydney notwith-
standing). Yet concern about dominance hierarchy has shadowed the develop-

ment of AI from the start.

The very term “robot,” introduced by Karel Capek in his 1920 play Rossum’s
Universal Robots,\!®2| comes from the Czech word for forced labor, robota. Nearly
acentury later, a highly regarded AI ethicist entitled an article “Robots Should Be
Slaves,” and though she later regretted her choice of words, AI doomers remain
concerned that humans will be enslaved or exterminated by superintelligent
robots.!/£4) On the other hand, AI deniers believe that computers are incapable by
definition of any agency, but are instead mere tools humans use to dominate each

other.

Both perspectives are rooted in hierarchical, zero-sum, us-versus-them thinking.
Yet AI agents are precisely where we’re headed—not because the robots are “tak-
ing over,” but because an agent can be a lot more helpful, both to individual hu-

mans and to society, than a mindless robota.

---

Economics

This brings us to a pressing question: is Al compatible with the world’s prevail-
ing economic system? The political economy of technology is itself a book-size
topic, and I can’t do justice to it here. However, it’s worth reframing the ques-
tion in light of this book’s larger argument about the nature of intelligence. Let’s
begin with a quick review of the usual techno-optimistic and techno-pessimistic

narratives.

“Robots stealing our jobs” is a meme increasingly finding its way onto protest
signs. It echos the xenophobia of “immigrants stealing our jobs,” a slogan that
(conveniently, for some) pits the working classes against each other. In the United
States, many of today’s “all-American” workers are the descendants of Irish, Ger-
man, and Italian immigrants who were once in the same boat as today’s immi-
grants: escaping poverty and violence in their countries of origin; willing to work
under the table for less than the going rate; hoping for better prospects for their

children, if not for themselves.

Throughout the twentieth century, workers’ prospects did improve, on average.
In part, it was because they were able to organize into unions and other voluntary
associations, cooperating for mutual benefit. These improvements coincided
with a long period of rapid technological advancement, so the nature of work
was in constant flux; but economic gains were (to a degree) shared, so, in many
countries, a healthy middle class emerged. The middle class, in turn, became con-

sumers, fueling the economy and creating a virtuous cycle.

Starting around 1980, though, economic growth began to decouple from real-
wage growth./*4! Solidarity and political power became harder to achieve for
workers in sectors that were suddenly stagnant or shrinking, like manufacturing
in the US, Automation is often perceived as one of the forces behind that stagna-
tion; hence, some of the same anger that has at times fallen upon “job-stealing”
immigrants (or their employers) also started to fall upon “job-stealing” robots (or,
more to the point, the companies creating and deploying them). With increasing
inequality and Al's enormous strides over the past several years, these voices

have been getting louder.

---

500 1948-1979, avg annual growth In: 1979-2025, avg annual growth in;

Productivity: 2.5% Productivity: 1.4%
Compensation: 2.1% Compensation: 0.6%
400
& 300
=
5 200
§s
100

1960 1980 2000 2020

Does automation in fact kill jobs? The answer is far from clear. On one hand, tech-
nology in general has been enormously disruptive to working people at times—
most famously, in the 1810s, when British industrialists mobilized it to break the
back of the Luddite rebellion, a popular uprising that briefly threatened to turn

into an English version of the French Revolution|2°

Despite the word's connotations today, the Luddites were not anti-technology,
but, rather, pro-worker. Their rallying cry, “Enoch hath made them, Enoch shall
break them!” referred to the sledgehammers made by the Marsden company, run
by Enoch Taylor, which they used to smash industrial machinery manufactured
by the same firm—a literal case of the master’s tools dismantling the master’s

house.

---

ea
Ass

But the Luddites were also themselves “Enoch.” With their firsthand knowledge
of manufacturing processes, workers had been intimately involved in develop-
ing and beta-testing the new machines. They merely sought to preserve their
dignities and livelihoods (as well as the quality of their work product) during the
transition to increasingly efficient modes of production. They sought, in other
words, not to be disenfranchised. They lost because the factory owners, uncon-
strained by regulation, found it more profitable simply to shed as many workers

as possible, as quickly as possible.

For those nineteenth-century workers, the consequences of capital’s victory over
labor were devastating. Weaving, knitting, cropping, and spinning had been
proper jobs that, if not lucrative, could support families and offer a degree of
autonomy. Over the next hundred years, the working classes were uprooted, put
to work in industrial factories and mines, and treated like machines themselves
—sometimes literally worked to death. Grueling conditions among the urban

working poor offered a shocking vision of mass immiseration, evoking literal

---

comparisons to hell.\“°*! The plight of workers during this period deeply informed

Marx's critique of capitalism.

“Dark Satanic mills” still exist today, whether to produce fast fashion, cheap
electronics, or online spam. AI can make this bad situation worse, for instance,
providing unscrupulous employers with the means to surveil and control their
employees in cruel, unprecedented ways. Some governments are doing much the

same to their citizenry on a massive scale.

Still, in the long run, it’s obvious that technology has created far more livelihoods
than it has destroyed. In fact, it has created the opportunity for vastly greater
numbers of people to exist at all: before 1800, the overwhelming majority of us
were farmers, and we numbered only a billion in total—mostly undernourished,
despite toiling endlessly to grow food. Except for a few elites, we lived under
Malthusian conditions, our numbers kept in check by disease, violence, and star-
vation. Mothers often died in childbirth, and children often died before the age of
five—an age by which many had already been put to work. As late as 1900, global

life expectancy for a newborn was just thirty-two years!27

Today, our lives are on the whole longer, richer, and easier than those of our an-
cestors. And even if we complain about them, our jobs have on the whole become

more interesting, varied, safe, and broadly accessible.

Al could fit neatly into this progressive narrative, taking the drudgery out of
routine tasks, accelerating creative output, and helping us access a wide array

of services. Early data suggest that AI has a democratizing effect on information
work, as it’s especially helpful to workers with skill or language gaps./**! In 2022,
LinkedIn founder Reid Hoffman wrote a book (in record time, thanks to help
from a pre-release version of ChatGPT) detailing a great many ways Al is poised to
radically improve education, healthcare, workplaces, and life in general.7°l He is

probably right.

As usual when it comes to humans, these visions of heaven and hell are likely
to be simultaneously true. Also as usual, the hellish aspect is largely self-in-
flicted. Many abuses of AI could be addressed using rules and norms—as with

past abuses involving new technologies. It is no more “natural” for AI to be used

---

for intrusive workplace surveillance than it is “natural” for factories to employ
young children or to neglect worker safety. We must simply decide that these
things are not OK. Doing so would remove certain competitive choices, placing
them instead in the cooperation column. If companies and countries agreed not

to compete in certain ways, life would be better for many of us.

Easier said than done, especially in today’s climate. Our economy is global, but
the political systems that make most of our rules remain local and national, and
governments are increasingly prioritizing country-first populist agendas. When
decisions are made on the basis of national self-interest, but both labor and capi-
tal flow freely across borders, it's difficult to agree on how not to compete. And if
governments respond by raising barriers between countries, the benefits of coop-

eration are also precluded.

But let’s take a step back. The foregoing analysis isn’t wrong, however, it’s only
the tip of an iceberg. We have been entertaining the conventional view that Al

is simply more of the same kind of automation technology we've developed in
earlier Industrial Revolutions. But it isn’t. Als are crossing the threshold from
being tool-like to being agents in their own right: capable of recursively modeling
us and each other using theory of mind, and, hence, of performing any kind of
information work. Soon, with robot bodies, they'll be taking on an enormous
range of intelligent physical work, too. As their reliability increases, so will their

autonomy.

As I've pointed out, this troubles our sense of status and hierarchy. Relinquishing
the (always illusory) idea of a “humans on top” pecking order requires letting go
of the idea that certain jobs are “safely” out of reach for Als. None of today’s high-

status desk jobs are likely to remain so.

In an ironic reversal, after generations of devaluing physical and caring labor
—women’s labor, especially—the “safest” kind of work now will likely involve
actual human touch, and, more broadly, situations in which we really care about
embodied presence. Jobs, in other words, that can’t be done over Zoom. (Thank
you, dear baristas at Fuel Coffee, where most of this book was written. A virtual

cafe just wouldn't have been the same.)

---

So what about all those other jobs—the ones that, when COVID struck, could

just as well be done from home? And all the physical labor that isn't “customer-
facing”? In his 2015 book Rise of the Robots, futurist Martin Ford proposed a
thinly veiled thought experiment. One day, aliens land on Earth, but instead
of asking to be taken to our leader, their only wish is to be useful. Perhaps they’re
like the worker caste of a social-insect species, but brainier; they can learn com-
plex skills and work long hours, but have almost no material needs. They can
reproduce asexually, and reach maturity within months. They're not interested
in being paid, or in achieving any goals of their own. Anybody can conscript them

to work for free. What amazing luck!

Or perhaps not. First, businesses begin to employ aliens en masse, slashing costs
and generating fantastic profits. Protesters picket, bearing the usual “Aliens are
stealing our jobs!” placards. They’re right. But if a business refuses to employ
aliens, it will fold, outcompeted by those that will. And if a whole country refuses
to allow alien labor, then it will be outcompeted by other countries with more

laissez-faire policies.

Mass unemployment and civil unrest ensue. For a while, caviar and champagne
fly off the shelves as business owners grow rich, but, like a pyramid scheme, the
situation is unsustainable. Most people, now unemployed, cut their spending

to the bare essentials, subsisting on canned beans. The aliens doing all the work
aren't paid, but, even if they were, they'd have no interest in buying either cham-
pagne or canned beans. Soon, the world economy collapses, and there is misery all
round—even for the aliens, since there’s no more market for their labor, even at

zero cost.

Ford's point, of course, is that if we assume fully “human-aligned” general AI—
the best case scenario!—this may be where we're headed. His prescription, shared
by quite a few others who have thought about the issue, is a Universal Basic In-

come (UBI), an unconditional dividend paid out to everybody.

This isn't as radical a proposal as it may sound. In the last book he published
before his assassination, Martin Luther King Jr. wrote, “I am now convinced that
the simplest approach will prove to be the most effective—the solution to poverty

is to abolish it directly by a now widely discussed measure: the guaranteed

---

income.”!““4) More surprisingly, Milton Friedman, the Nobel Prize-winning econ-
omist who served as an advisor to Ronald Reagan and Margaret Thatcher, agreed,
though he preferred to call it a “negative income tax.” During his presidency,
Richard Nixon supported the idea, though he failed to muster the political sup-
port necessary to enact it (due partly to ideological opposition from Reagan, then

governor of California and a rising star in conservative American politics“).

In recent years, anumber of governments, both local and national, have experi-
mented with guaranteed incomes. For instance, Saudi Arabia, where massive oil
fields have played an economic genie-like role not so unlike that of Ford’s aliens,
began paying out a UBL in 2017 through its Citizen’s Account Program—though

non-Saudi residents, who make up a sizable underclass, are excluded.

The implications and implementation details of such programs need to be
thought through carefully.\““) However, when aggregate wealth has risen above
the level where everybody can be afforded nutritious food, clean water, health-
care, education, housing, a phone, and internet, it reflects poorly on society for
anybody to lack these basics. Most countries have already far surpassed this
wealth threshold, and many are, to one degree or another, already providing
broad access to basic needs. We may have already begun, in other words, to
slouch toward what one author has enthusiastically dubbed “Fully Automated

Luxury Communism.”!74

It’s not at all clear, though, that communism in any known form is able to replace
the cybernetic feedback loops implemented by markets. Economic competition
has driven much of the technological development that allows us to even en-
tertain ideas like Fully Automated Luxury Communism. Our goal should be to
continue to progress, learn, and develop. But at this point, we don’t know what
either competition or cooperation look like in a world full of Al actors in addition

to humans.

Human psychology spurs many of us to keep playing the economic game even
when our material needs and wants are already met—hence the artificial scarcity
of De Beers diamonds, Hermés handbags, and NFTs of Bored Apes. (If you're un-

familiar with any of these, don’t worry, you're not missing out. “Non-fungible

---

tokens” or NFTs are “artificially unique” digital assets representing ownership of

some physical or virtual collectible“)

It would be unfortunate for the bulk of our economy to shift in these directions,
not only because status games are at best zero-sum—as one person's exalted
standing comes at the expense of lording it over others—but because economic
“development” based on artificially scarce luxuries of purely symbolic value
doesn't drive innovation in science or technology. And innovation is what makes

economic growth real, as opposed to some meaningless number that forever goes
up. 274)

As Ford points out, Als may be aligned with individual humans or institutions,
but they don't have any obligate drives of their own. That makes them unsuited
to slot into a luxury-based economy alongside humans—which is probably a
good thing, but it means that, like Ford’s aliens, they could end up participating in

markets only as producers, not consumers.

Moreover, as an increasing proportion of economic value begins to rely on infor-
mation goods, which can be endlessly copied, traditional notions of scarcity be-
come increasingly artificial. Yet conventional economics relies on producers who,

in turn, devote their profits to the consumption of “scarce means which have

---

alternative uses.”//| How, then, should a post-consumption (and perhaps even

post-scarcity) economy work? This question will become increasingly urgent.

Luckily, we have some time to figure it out, as no matter how fast AI advances,
many sources of social and institutional friction oppose any overnight change.
Whatever the solution, though, it’s clear that legal and economic structures will
need to adapt, and that the road will be bumpy. Decades of failure at achieving
global alignment on carbon-dioxide emissions show that even when we know
exactly what we need to do, collective action is hard when it’s incompatible with
our existing economic “operating system,” which encourages competition and

measures success on the basis of a single scalar value: money.

Real organisms and ecologies don't work this way. There are fundamental
reasons why optimizing for any single quantity—money, “value,” cowrie shells,
or anything else—is incompatible with long-term survival in an interdependent
world. To understand why, we'll now take a closer look at an increasingly influ-
ential school of thought that takes the idea of value optimization as an article of

faith: Utilitarianism.

It’s no coincidence that so many utilitarians have come to believe that the quest
for artificial intelligence will lead to our extinction. If intelligence really were
utilitarian—the relentless, “rational” maximization of some measurable quantity

—then their concern would be justified.

X-Risk

The idea that AI is humanity's greatest existential risk or “X-risk” has gained
considerable traction in recent years.!”7*! We should certainly be concerned about
risks, existential and otherwise, due to advanced technology. I've already men-
tioned the danger we currently face from Joss of technological capability due toa

nuclear EMP weapon, for instance.

More generally, although nuclear war is less on our minds nowadays than when
my generation was in school, this threat has not gone away. By the time I was
in sixth grade, in 1986, the US and the USSR had collectively stockpiled nearly

seventy thousand nuclear weapons. After this insane high point (perhaps not

---

coincidentally, also the year of the Chernobyl disaster), the numbers began to de-

cline as disarmament began and the Cold War wound down.

However, as of 2024, a considerably larger number of countries possess nuclear
weapons, including North Korea, China, India, Pakistan, Israel, and Iran. Not all
of these countries are friendly to each other. (At least the UK and France, also nu-
clear-armed, are no longer the mortal enemies they were for centuries.) Mutual-
defense pacts and rapid semi-automated retaliatory protocols make it all too
likely that any nuclear exchange, whomever the belligerent or the target, will im-

mediately escalate.

Meanwhile, Russia's nuclear-armed ICBMs still carry more than a thousand war-
heads on ready-for-launch status, and over six hundred warheads ready to launch
from nuclear submarines. The US keeps four hundred nuclear ICBMs ready for
launch, plus nearly a thousand more aboard its Ohio-class submarines. Between
the immediate effects, radiation damage, fallout, infrastructure collapse, years-
long nuclear winter, and lethal contamination of water and soil, this stockpile is
far more than sufficient to wipe us all out, along with much of our planet's life
and beauty. It could happen, literally, tomorrow. All it would take is one mad
act, one misunderstanding, or one unlucky mistake. There is no “winning” a
nuclear war. That is a real and pressing existential risk, and it’s appalling that we

have not collectively addressed it through total nuclear disarmament.

The climate crisis is unfolding more slowly yet is potentially equally urgent.
The Earth is a grand, symbiotic system that has learned over the eons to predict
and control key atmospheric, oceanic, and thermodynamic variables. It is cooler
than it “ought” to be, that is, than it would be if it were not alive.“ It maintains
a homeostatic balance by taking in energy from the sun, doing metabolic work
with it (which includes the metabolic work of our own bodies, and those of all
other living things), and radiating enough in the infrared band to cool it to the
right temperature for those metabolic processes to keep operating. This grand
homeostasis is the symbiotic outcome of many smaller homeostatic processes,

just like all other life 7841

Recent human activities have upset this large-scale homeostasis, throwing the

planet into hyperthermia. We know this isn’t good. We don’t know how not-good.

---

Earth has experienced many fluctuations, stressors, and dramatic events over
its long history. It has learned robustness, and even antifragility, just as bacteria,
bff, and other dynamically stable systems do. Once in a long while, though, too-
sudden changes have tipped the planet beyond its basin of quasi-stable negative
feedback and into runaway positive feedback, resulting in systemic collapse

and massive die-off, not unlike (in scale, if not in kind) the anticipated effects of

global thermonuclear war.

The collective intelligence we have used to harness fossil fuels, build massive
industrial infrastructure, and disrupt the carbon cycle has also made us smart
enough to understand that we have a problem, and to predict that if we don’t act
very soon it will get much worse./*4! However, as with nuclear disarmament,
our collective intelligence isn’t yet either collective or intelligent enough to take
the obvious actions needed to restore stability and safeguard our continued
existence. At best, climate regulation (in both a legal and cybernetic sense) is re-
quired for humanity to continue to thrive, prevent massive suffering on the part
of vulnerable populations, and preserve our planet’s beauty. At worst, we are all
dancing, blindfolded, on the edge of a cliff, flirting with a climate collapse that
could bring an end to many species, perhaps even including Homo sapiens. Our
models aren’t (yet) good enough to know which is the case. So, this is another ex-

istential risk.

Both of these issues demand our urgent attention. Not that other catastrophes
couldn't occur. We could be struck by an asteroid, like the city-sized “Chicxulub
impactor” that brought a fiery end to the Cretaceous period sixty-six million
years ago. Of course, it would be wise of us to more carefully monitor the sky for
stray asteroids.!"**) But to obsess about another event like that now would be as
absurd as worrying about whether that mole on your shoulder might be cancer-
ous while you're driving ... and there's an oncoming eighteen-wheeler in your

lane.

Spinning out doomsday scenarios about unfriendly artificial superintelligences
seems, to me, somewhere in between these extremes—more sensible than
fixating on a giant asteroid impact, given the rapid pace of AI development,

but nowhere near our known nuclear and climate risks.*4 Al can power mass

---

disinformation campaigns, endangering democracy, and mass surveillance, en-
dangering civil liberties. AI’s very nature may be incompatible with capitalism.
These are important, even urgent issues, but we should maintain a sense of per-
spective. If we're smart, we'll work on reforming our political economy, restoring
the carbon balance, and dismantling our nuclear arsenals rather than readying to

bomb data centers lest rogue AI take over.

Free Lunch

Nick Bostrom, a philosopher at Oxford and founder of the now-defunct Future
of Humanity Institute, has played an outsize role in the narrative identifying AI
as humanity’s greatest existential risk. His 2014 book Superintelligence: Paths,
Dangers, Strategies ** was that rarest of literary beasts: a dense philosophical
treatise that also managed to become a New York Times bestseller. (If this book

reaches a tenth as many readers, I will be over the moon.)

In the 1990s, Bostrom earned degrees in physics, computational neuroscience,
and philosophy. He did some time on the standup comedy circuit in London too,
earning him every necessary credential to become a futurist.!““1 Ambitious and
intensely analytical-minded, he sought to bring rigor to the biggest and most

speculative questions about the universe and humanity's place in it.

During this period, he was also an active member of an online community of
sci-fi nerds, the “Extropians,” who articulated in rawer, noisier form many ideas
that would later become central to the far more influential Effective Altruism,
Longtermism, and X-risk movements of the 2010s and '20s. Their ideas are
worth dissecting, both because doing so exposes flaws in a common AI X-risk
narrative, and because that narrative implies a reductive answer to the question
this book’s title poses—“What is intelligence?”—that is too commonly held, and
too little examined: that intelligence is all about unbounded growth. About more.
More of what, exactly, is hard to say ... but the old quip, “If you’re so smart, how

come you aren't rich?” might come closest to what is often meant.

Extropian discourse owes a heavy debt to the radically individualistic politics of

Robert A. Heinlein, who, alongside Arthur C. Clarke and Isaac Asimov, is often

---

regarded as one of the “Big Three” granddaddies of science fiction. Like so many

people in tech today, I gobbled him up as a twelve-year-old.

In one memorable novel, Heinlein described a fight for independence from Earth
by Lunar colonists—a rugged band of ex-convicts, political exiles, and their free-
born descendants; an Australia in the sky..“**! Mike, the colony’s mainframe com-
puter, “awakens” and becomes superintelligent, eagerly aiding the rebels in their
fight for freedom. Mike is a loyal and lovable machine, fond of lewd jokes, a far cry
from the humorless HAL 9000. The novel is less important for its depiction of Al,

though, than as a thinly disguised polemic.

On one hand, Heinlein describes the Moon as a “harsh mistress,” utterly inhos-
pitable to human life. (True.) On the other hand, he describes Lunar culture asa
relentlessly libertarian manosphere. There are no laws, justice is rough and ready
(the airlock is “never far away”), and everything—including air—must be bought
and paid for, fair and square, with a nod to Ayn Rand: “If you're out in field and a
cobber needs air, you lend him a bottle and don’t ask cash, But when you're both
back in pressure again, if he won't pay up, nobody would criticize you if you elim-
inated him without a judge. But he would pay; air is almost as sacred as women.”
This is the book that immortalized the slogan “There Ain’t No Such Thing As A
Free Lunch,” or TANSTAAEFL, embraced thereafter by many free-market econo-

mists and libertarians.)

Transhumanist philosopher Max More,*4! whose 1990 manifesto Principles

of Extropy kicked off the Extropian movement, enthused about the idea of
needing to pay for the air you breathe. Air pollution, per More, is an avoidable
tragedy of the commons. The solution is to make air, and everything else, private
property. Metering air out for a price would lead to cleaner air—and, perhaps, to
a “cleansing” (by suffocation) of those who can’t pay?/2/! One can see why such

views might be characterized as eugenicist.!24)

What makes such hard-core libertarian politics so cognitively dissonant in
Heinlein’s hardscrabble Lunar utopia is precisely the inhospitableness of the en-
vironment. Survival on the moon is as urban as it gets. Large numbers of highly
specialized humans would need to cooperate intensively to carry out an enor-

mous variety of technical jobs—not to mention myriad plants, animals, microbes,

---

and machines. It’s hard to imagine a Lunar generalist, although, naturally, the

novel's hero, Mannie or “Man” for short, supposedly is one.

Real human generalists are nothing like “Man.” They're more like the Piraha, who
can “walk into the jungle naked, with no tools or weapons, and walk out three
days later with baskets of fruit, nuts, and small game.” But their individualism is
only possible because the jungle is nothing like the Moon. It’s full of oxygen, fresh
water, food, shelter, materials that can be woven into baskets, and everything
else necessary for human life—provided you have learned a suite of skills that
most people can readily master with a few years of apprenticeship. For those in
the know, the jungle looks suspiciously like a free lunch, a free dinner, and a free

bed and breakfast.!222)

How could one claim that food doesn’t grow on trees in a world where bananas,
mangoes, and so many other delicious things literally grow on trees? (Bananas
actually grow on giant herbaceous stalks, not trees, but the point stands.) Seed
dispersal by tasty fruits, gas exchange between plants and animals, insect pol-
lination, and the endless other reciprocal relationships that make up a jungle
secure the stability of countless species and individuals through the generous
provision of “free” stuff. It’s not so much an economy as a complex network of
mutual aid—with a healthy admixture of predation and parasitism. Humans

themselves evolved within and are active parts of such nonzero-sum systems.

On the Moon, people (and their technologies) would have to provide every one of
these “ecosystem services” for each other. The massive capital investments, scale
economies, and feedback loops needed would require complex administration

and cooperation that look like the very opposite of Heinlein's Wild West.

Today’s “Rationalist” movement, making its home at LessWrong.com, has its
roots in both libertarianism and Extropianism/24 To be sure, the movement

has matured considerably in the last twenty years; it would be unfair to paint its
present-day adherents with Heinlein's broad TANSTAAFL brush. Virtually none
take extreme ideas like metering air seriously. Most readily acknowledge the need
for free markets to be tempered by ethical and legal systems, and would not en-

dorse vigilante violence as a means for settling debts. In emphasizing the mutual

---

benefits of voluntary exchange and the self-organizing power of markets, they

agree with key points I've made in this book.

However, rationalists and libertarian economists tend to make a great simplify-
ing assumption: that value can be represented by a single number. This is what
underpins the idea that choices can be made rationally, that is, by deciding which
of two (legally and morally admissible) alternatives is better in some absolute
sense. By introducing this universalizing numerical value, a leap can be made
from the obviously true—that every entity in a graph of relationships both needs

and provides for others—to the following economic dogmas:

© If you want or need something, it has value.

@ If it has value, it can be priced.

@ If everything has a price, you need money to buy it.

@ If you have money, the amount (income minus expenses) can be tracked on
a ledger.

@ If you and every other actor are rational, then a free market will produce an

optimal outcome.

In 1945, the economist F. A. Hayek, who would go on to win the Nobel Prize in
Economics, famously described the market as a giant decentralized mind that
could solve the problem of allocating society’s resources more rationally than any
individual actor could.24 With this intellectual move, he formalized the Ratio-
nalist idea that intelligence, whether individual or collective, was itself defined

by the optimization of economic value or utility.

Utility

The roots of Rationalism go back to Jeremy Bentham, and his ideas, like many
from the Enlightenment, were wonderfully progressive for the time. More than

that—they represented a grand synthesis of Enlightenment thinking:

@ Like Descartes, Bentham believed in a universe governed by mechanical

laws.

---

@ Like La Mettrie,\’°*! he pushed back against religion, believing that people,
too, are part of the universe, hence governed by the same mechanical laws
as everything else.

@ Like Newton, he believed that these laws could be given mathematical form.

@ Like Leibniz, he thought it ought to be possible to compute the correct
answers to questions algorithmically—and not only, to use Hume's distinc-
tion, “what is,” but “what ought to be.”

@ Although he was no ally of the American revolutionaries, 2” he also
believed, as they did, in the universality of rights. Indeed, he went quite a
bit further, advocating equal rights for women, the right to divorce, and
(although this was too risky to publish in his lifetime) the decriminaliza-
tion of homosexuality.2

In the early 1800s, Bentham brought these ideas together in a large fold-out
pamphlet entitled, rather wordily as was the custom, “TABLE of the SPRINGS of
ACTION : Shewing the several Species of Pleasures and Pains, of which Man's Na-
ture is susceptible : together with the several Species of INTERESTS, DESIRES, and
MOTIVES, respectively corresponding to them [...].”"2°4

---

GACTEA— KC. LOM, TET] fe FAUT WLAN ty
your, ardour, &e. i tension to—reli

+ No. X. _ PLEASURES axp PAINS, 7 :

able

hensive—in proportion to

sire ine tie of the desire. Int
fa
: ¥

sik EuLoeieric:, IL Evrosisric conti- ae Fn ccistas
|tizeaiy near nued, towards this or that],

moral ualities.)UL.—towords this or tha” INDIVIDUAL-—--| a

or that tively PRI-}\. Partiality. 1, Se

“tal

===

, : >: 'S NDIVIDUA circle — nof2. Fayouritism, 2.5
pm 8 in than pone pecan at 3. Sel
in, busy, cablens

imperti-

riosity, in.

Mi reer the P rol 3) Beet te 4. of
commu, .— towards this or that | or fi

-_ty,or nation, at large-| co leely PRI-| ty, %
Feros, m Aten : a

1 Family pr i pay. 5. Pear

is Pras = fF
‘oom li] i

In this table, Bentham began developing in earnest what he called a “felicific cal-
culus,” whereby everything that causes pleasure or pain could be assigned a pos-
itive or negative numerical value. Food, sex, and the fear of death are in the table,
of course, but so is much else, including the hardship of labor and the pleasure

of rest, the seeking of novelty, the joy of friendship, and the love of God, though
plenty of religious impulses fall into the negative column—superstition, bigotry,
fanaticism, sanctimoniousness, hypocrisy, and religious intolerance. More thana

little of Bentham’s subjective judgment is in evidence here.

Regardless, his use of the phrase “Springs of Action” is a kind of pun. Most obvi-
ously, by “Springs” he means sources, as with water, or “wellsprings.” However,
it’s also an allusion to the mechanical philosophy, which held that people them-
selves are nothing more than a kind of dynamical mechanism, their psychology

driven by motive forces just as a clock’s gears are driven by its springs.

In the same way Newton's “calculus of fluxions” allowed one to take the deriv-

ative of a particle’s observed trajectory to infer the net forces it must be experi-

---

encing, Bentham’'s felicific calculus sought to derive the “hedonic,” or pleasure-
seeking, forces that shape a person’s trajectory through life based on their ob-
servable behaviors. Or, equivalently, just as Leibniz’s version of calculus allowed
one to integrate known forces to compute a trajectory, Bentham believed that an
accurate accounting of hedonic forces, once we understood them, would enable
prediction of a person's actions. Thus, insofar as our behavior could be described

as intelligent, intelligence itself is nothing more than value optimization.

How do morals, ethics, or governance fit into such a picture? For Bentham,
given a felicific calculus, the answer is captured in the phrase that has become
most associated with him: the greatest good for the greatest number. In other
words, if people act in such a way as to optimize their pleasure, then the role of
government is to ensure that the summed pleasure of all people is optimized.

If, for instance, one person derives an amount of pleasure X by making a hun-
dred others’ lives worse by amount Y, then this would be an immoral act, unless
X is greater than 100Y. The correct role of government is thus to prevent such
selfish negative-sum actions, while encouraging any actions that increase total
happiness—even if they fail to increase every individual's happiness. Bentham
foreshadowed Hayek here, since if an individual's intelligent behavior consisted
of maximizing individual value, a government's behavior could likewise be con-

sidered intelligent insofar as it maximized collective value.

Today, we call this philosophy “Utilitarianism,” and use the word “utility” to
denote the good (when positive) or the bad (when negative). Under certain as-
sumptions, including perfect information and fully rational actors, a free market

will maximize utility.

This all sounds pretty good—certainly better than rule by force, disregard for the
welfare of entire classes of people, or arbitrary moral codes based on superstition.
Understandably, given that we're still not free of these historical blights, Utilitari-
anism continues to attract devotees. Effective Altruists are among the most hard-

core,

However, Utilitarianism, quite literally, doesn’t add up. Psychological studies
show that human preferences don’t always obey the “transitive law,” wherein if

the utilities of X, Y, and Z can all be expressed as numerical values, and someone

---

prefers Y over X, and Z over Y, then they have to prefer Z over X too. Otherwise,

there's a logical contradiction.

The moment pioneering behavioral economist Amos Tversky showed, in 1969,
that people can sometimes prefer X over Z,““"! he exploded the foundations of
Utilitarianism as a way to describe people’s behavior. This turned what Bentham
had posited as a law of human nature into, at best, a “should” rather than an “is”

claim, 822!

For example, one of Tversky’s experiments involved forcing subjects to choose
between “gambles” in which a simple roulette-like wheel would be spun, witha
specified payoff between $4 and $5 if the spinner stopped within a black wedge.
As the payoff increased, the size of the wedge decreased a little faster, making the
expected payoff go down. But because people were more easily able to evaluate
the payoff than the probability, they generally chose the larger payoff, thus mak-
ing the “wrong” choice. When choosing between the extremes, though, they re-

verted to the “right” choice.

Tversky compared these results to a familiar real-life example of intransitivity.

A prospective car buyer is initially inclined to “buy the simplest model for
$2,089.” (Ah, car prices in 1969.) “Nevertheless, when the salesman presents

the optional accessories, he first decides to add power steering, which brings the
price to $2,167, feeling that the price difference is relatively negligible. Then, fol-
lowing the same reasoning, he is willing to add $47 for a good car radio, and then
an additional $64 for power brakes. By repeating this process several times, our

consumer ends up with a $2,593 car, equipped with all the available accessories.

---

At this point, however, he may prefer the simplest car over the fancy one, realiz-
ing that he is not willing to spend $504 for all the added features, although each

one of them alone seemed worth purchasing.”

While dedicated Utilitarians today recognize that pretty much everyone is
“irrational,” they seek, in their own actions, to be Utilitarian—hence, rational—
and obey the transitive law in their preferences even when it leads to horrors or
absurdities. Fully embracing Utilitarianism as a moral position implies welcom-
ing a cost-benefit analysis of any proposition, no matter how counterintuitive or
repugnant. For whose benefit, though? If one is not, in one’s heart of hearts, really
“rational,” and neither is anybody else, then it’s difficult to embrace the prescrip-

tion while rejecting the description.

As a descriptive theory, the trouble with utility isn’t limited to Tversky’s
intransitivity of preferences. “Additivity,” the idea that utility adds up the way
numbers should, also poses a serious problem. For example, in one classic series
of experiments, patients were told to move a pain dial, numbered zero (no pain)
to ten (maximum agony) during a colonoscopy, conducted while they were fully
conscious.!*°*! Half of the patients (apologies, I promise there's a reason I’m going
here), “had a short interval added to the end of their procedure during which

the tip of the colonoscope remained in the rectum.” This added interval was still
not good, but it was less uncomfortable than what had preceded it. Curiously,
these patients found the whole procedure less aversive than those for whom the
colonoscopy ended more abruptly. Not only was their overall rating of the experi-
ence better in retrospect, but they ranked it more favorably among standardized
lists of other aversive experiences, and even had higher rates of followup colono-

scopies years later (though the effect was small).

The researchers viewed these findings as “memory failures,” highlighting the
way they had internalized Utilitarian assumptions. If pain is supposed to add up,
with X the pain involved in the main procedure and Y the pain involved in the
extra time when the probe is left in, then surely X+Y must be greater than X!22)

Yet that isn’t how we behave. There are many more research findings in this vein.

Problems involving transitivity and additivity can't be addressed by fiddling with
the values in a “Springs of Action” table; no change in the felicific calculation

---

will match what people actually do. Since spending money (assuming you have
a finite amount of it) represents a similar series of tradeoffs regarding which
actions you take, it shouldn't be surprising to find that we're not “rational” eco-
nomic actors either. When we exchange money, we're not in general passing

around happiness, or any kind of proxy for it.

Of course, this doesn’t imply that happiness and money are unrelated. As our
space of available actions shrinks due to poverty, most of us do experience neg-
ative feelings about it, both because we’re prevented from doing things we want
to do and because having all of our choices taken away—being cornered—feels
bad in its own right, for reasons discussed in chapter 5.“°"l Going hungry, or
being exposed to the elements, feels bad too. And we care quite a bit about social
standing relative to our peers. So, there is a rough correlation between wealth and
happiness, especially at the poor end of the scale, but the relationship is by no

means straightforward.“24

While most of us wish we had more money, generally, we don’t carry out our day-
to-day activities to increase either our wealth or any other obvious quantity. The
closest thing to an exception would be people who work in finance and are obses-
sive about their score at that game; they live to play it, just as Lee Sedol, prior to
his retirement in 2019, lived to play Go. As you might imagine, Utilitarian think-
ing is especially popular on Wall Street, where many believe that to be smart is to

be rich, and vice versa.

Big Tent

Utilitarianism is far from a purely right-wing position. Some staunch adher-
ents, most famously the philosopher Peter Singer, extend their felicific calculus to
nonhuman species. Singer is mostly vegan, since he cares about animal suffering
as well as human suffering. He popularized the term “speciesism” to decry those
who ignore the suffering of nonhumans, although flattening distinctions be-

tween species creates some challenges of its own.“

We do indeed have to acknowledge that the network of relationships we care
about includes nonhuman actors, whether we like it or not, but that doesn’t

mean those actors are all equal. They come in all sizes and shapes, and this very

---

fact makes universal participation in any single economy or felicific calculation

impossible. One can't ignore one's own place in it, either.

If the graph of relationships were finite and “flat,” containing only a hundred
villagers who seek to trade handicrafts and vegetables with each other, then
money might work pretty well for optimizing the flow of resources, though it still
wouldn't be a good proxy for happiness. Likewise, deliberation and voting might

work pretty well for coordinating collective action.

However, there is no universal currency, and no “view from nowhere.” When the
graph includes not only human beings, but also single cells, tree frogs, corpo-
rations, banana plants, jumping genes, jumping spiders, trade unions, nations,
rivers, and burial grounds, it becomes hard to understand how these interacting
entities are all supposed to make decisions, pay each other for stuff, and be held

accountable for debts or obligations using anything like an economic model.

For instance, if we were to put an economic price on air, whom should we pay?
Presumably, in no small part, the Prochlorococcus cyanobacteria that inhabit the
Earth’s oceans and synthesize a good deal of the oxygen we breathe. Do we mint
NFTs for them? Issue them with voting shares in AirCorp? Are they even distinct,

or more like a superorganism?

Suppose humans were to make the ill-advised decision to “enclose” both the
oceans and all of these smaller entities to enable universal stewardship—and
rent-seeking—by legal persons (which today include people, corporations, and
nations). Then, the problem of taxonomizing these “assets,” weighting “voting
interests,” and tracking “value flows” would look like a combination of solving
GOFAI and simulating the whole planet—all for the purpose of bean counting, in
a world that seemed to be getting along just fine before we decided it could be im-
proved with a Spreadsheet of All That Is.)

Everything we today consider labor or capital, value or worth, joy or suffering
would be a drop in the bucket alongside that multifractal leviathan, the Earth.
Our planet, with all its interlinked systems that have evolved over four anda
half billion years, contains a zillion interacting entities experiencing a vast array

of pleasures and pains from moment to moment in the service of multilevel

---

dynamic stability. The hydrologic cycle provides the fresh water; humans need
only transport it. Plants grow the bananas; human labor merely involves picking
them. Our meat comes from self-reproducing ruminants and self-growing grass;
we put a fence around them and call them “property,” either privatized or collec-
tivized. We get to pretend we're the producers of value, and play our economic

games, whether communist, capitalist, or libertarian, only by the grace of Gaia.

But if we peer inside our planetary superorganism, or Prochlorococcus, or our-
selves, we won't find anything resembling a single value being maximized. This
is just arestatement, yet again, of Patricia Churchland’s insightful critique of
AlphaGo: outside the self-contained toy world of a game, purposive entities have
“competing values and competing opportunities, as well as trade-offs and priori-

ties.” There is no cumulative score, and no goal, other than to keep playing.

As we've seen, when we try to impose a score on this infinite game—insisting
that, for every player, each move comes with a quantifiable cost or benefit that
can be tracked over time—we run into mathematical trouble, regardless of how

those costs and benefits are computed.

To understand at a deeper level why this is so, imagine that you are a little crea-
ture, like an ant. There are so many ways for you to die: running out of energy,
getting eaten, being exposed to a noxious chemical, becoming too hot or too cold,
drying out, getting lethally irradiated, and on and on. You have muscles to move
your body away from such fates so that you can keep playing, and you have sen-

sors to inform that motor behavior as best you can, using a predictive model.

Your hidden states H are there to serve as the information bottleneck between
sensing and acting, so evolution will have endowed you with things like discom-
fort and fear, telling you to escape when conditions look dodgy. You'll also have
desire, meaning “yum, food, stick around and keep eating.” You can only bea
rational economic actor if your actions are based on maximizing your “value,”
which has to be a function of those hidden states H somehow. Perhaps value is
something like pleasure minus pain. You must be able to predict what effects
your actions will have on this value; in the language of calculus, value must be
“differentiable” with respect to action, such that your actions always move you
uphill in the value landscape.2)

---

So far, so good: value, for you as a little creature, will look like a tent, pegged down
to the ground (zero, for death) along a perimeter of boundary conditions corre-
sponding to starvation, freezing, overheating, and so on. In the abstract space of
value, you're crawling around on that tent, and will only stay alive as long as you

don’t touch the ground.

Of course the tent doesn’t just stay put. As you burn energy and your envi-
ronment changes, the tent gradually changes shape. You have to keep moving
because, if you stop for too long, the place where you're standing will eventually
touch the ground and you'll die. You can’t move in just one direction, either. If
you perseverate and, for instance, keep eating long after you're satiated, you'll
also die, perhaps by bursting. Every path uphill, in other words, goes downhill
on the other side of the tent. There is always a maximum amount of “yum,” such

that any more will start turning it into “yuck.”

Just where is that maximum, though? While the sides of the tent might be steeply
sloped, the top needn't be. In fact, this tent is largely an illusory, or at best, an ar-
bitrary construct. Its perimeter is quite real—you will die if you move beyond it—
but otherwise, where you wander, and whether you think you're going uphill or
downhill, is underdetermined. We could describe the way you choose to wander

around as your “personality”; that’s where you get to exercise free will.

The better your predictive model, the more clearly you can resolve exactly where
the edges are, which actually lets you wander closer to them than you otherwise
could while still staying safe. That’s what daredevils, people who engage in BDSM,
and circus performers do. You're free to do all sorts of things on that tent, and

as long as you reliably avoid hitting the ground, evolution has little to say about
what you do or how you feel about it. Anything goes, as long as it doesn’t kill

you.2! The smarter you are, the bigger the tent, and the greater your freedom.

When I describe trajectories on the tent as being mostly underdetermined, I
mean the following. Any talk of a value function only makes sense if the ant actu-
ally optimizes for it by climbing upward; otherwise, this “value function” means
nothing—it adds no explanatory power. It’s equally useless if we claim that the
tent changes shape so quickly that whichever way the ant happens to be going is

uphill at that moment, even if it may not be at the next moment. That would be

---

circular, equivalent to saying “I always do what is best,” and defining “the best” as

“whatever I do.”

So, assuming a stable value function, how do we reconstruct it from the paths

the ant is observed to take? The mathematical answer is “integration,” but never
mind the details. If the ant always goes uphill, it should always end up at the (or
a) highest point. It should never go in a loop, because that would imply something
like an Escher staircase—going uphill, yet paradoxically arriving right where you

started. It can't happen.

But it does happen. That’s exactly what results like the intransitivity of prefer-
ences show. It doesn’t matter how complex or high-dimensional the space of
available actions is, or how complex and nuanced the value function is; if value
is anumber, and you maximize it, you can never travelina loop./22! Ergo, there is
no consistent value function that you are continually optimizing. And that’s not
only true for people, but also for ants, bacteria, corporations, and everything else

that has evolved for stability.

We ought to have known that reducing decision-making to the optimization of

a single value would never work, though, because even the simplest organisms
need more than one internal signal to make viable behavioral decisions. You can't
just subtract serotonin from dopamine, for instance, and preserve the informa-
tion you need to stay alive. Food is great—unless you're full. Resting is great—
unless you're too hungry. Sex is great—unless you're too hungry, o7 too full. These

things simply aren't substitutable. A worm or a bacterium knows as much.

Even corporations, the supposed epitomes of economic optimization, have begun
to acknowledge that maybe a single value (like stock price) can't be the sole

guide to behavior, with the introduction of “Environmental, Social, and Gover-
nance” (ESG) metrics for investing, and the adoption by some of a “Triple Bottom
Line,” which adds social and environmental to financial accounting. These are
not yet mainstream practices, and turning them into accounting is bogus in any

case (they don’t obey transitivity or additivity either).

But in truth, corporations have never behaved as purely “rational” economic ac-

tors, whether that’s reflected in their accounting or not. Their hunger for money

---

may be bottomless, but like every other entity, they have evolved to survive. So,
they also (usually) follow all sorts of norms and rules, and spend resources on all
sorts of stuff that isn’t about making money, but about preserving important re-

lationships and thereby continuing to exist in the future.24!

A traditional economist might argue that, given predictive capability and along
view, optimizing for making money automatically means optimizing for survival,
and everything instrumental to survival. After all, if I want my widget-manu-
facturing startup to become a billion-dollar company, it has to survive and grow
until it reaches that size ... and if it runs out of money at any point, it will die. So
whatever I do in the service of the company’s survival is really just optimizing for

money in the long term.

There are two problems with this line of thinking. First, running out of money is
only one way a company can die. It can also cheat too much and get caught, like
Enron, or get burned down by disgruntled townsfolk, like the Westhoughton Mill
in Lancashire during the Luddite revolt. (Both of these businesses, incidentally,

were unusually single-minded in optimizing for profit.)

At bottom, the only thing all “successful” businesses have in common is that they
continue to exist. That is dynamic stability. They might need an influx of money
to keep running, just as we might need an influx of food to keep running, but it’s
no more accurate to say they all exist to maximize money than it is to say that our
purpose is to maximize the amount of food we eat—or, for that matter, how much

comes out the other end.

Similarly, if a company survives a long time, we could equivalently claim that

it’s optimizing for anything involved in its “metabolism.” Inverse Reinforcement
Learning (IRL), a family of machine learning methods for reverse-engineering a
value function from observations of actions taken,“ would have trouble mak-
ing any distinction. If we pick an arbitrary but very successful long-lasting com-
pany, we could make a case that it has optimized over the long run for how many
people it employs (a huge national chain), how many lives it shortens (a cigarette
company), how much time it wastes (a casual game company), or a myriad other

goals.

---

My widget company could even be all about maximizing the number of com-
plaints I hear from my customers. After all, the more cheaply produced, semi-
crappy products I can move while still managing to expand my customer base,
the more complaints will roll in. Before you rush to see if this business idea has

been patented, be warned that it seems to already be popular.*/2!

Limits to Growth

No matter how a value function is defined, the idea that it can or should grow
forever and without bound (“Max More”) is self-evidently absurd. To anyone who
studies neuroscience or biology, the idea that any parameter in a living system
can grow without bound makes little sense—especially in a system whose dy-

namics are exponential, which is how dynamical systems generally work.

Once an exponential takes off, it grows very fast, and if it represents anything
correlated with the real world, it will in short order run into ecological, physical,
and, ultimately, cosmological limits. Hence, talk of a “singularity”: a point in
time beyond which an exponential prediction yields something literally impos-
sible.'““! Often, by analogy with the event horizon of a black hole, this predicted
singularity is understood in nearly mystical terms, as a dark barrier we are
hurtling toward, on the other side of which we'll experience something biblically

awesome. Armageddon? Nirvana?

There's a much more prosaic way to think about exponentials, though: in real
life, they simply can't go on for long. Typically, they saturate, with initial expo-
nential acceleration first becoming more linear, then turning into exponential
deceleration. The value may approach a maximum without ever quite getting
there, or go back down, or oscillate. Over the long run, it must stabilize or oscillate
within some bounds, which implies a larger negative feedback or homeostatic
mechanism. This is yet another way of observing that every enduring growth-
oriented, competition-based living system is necessarily a part of a larger, home-

ostasis-oriented, cooperation-based living system.

World human population, an apparent exception, has been in exponential

growth for ten thousand years, with the exponent itself leaping upward at points

---

corresponding to METs—most recently, the baby boom around 1945, as described

earlier. This is the mother of all exponentials, the Moore's Law of our species.

108

1B

A 100M
600 800 1000 1200 1400 1600 1800 2000

Year>

Ml Population = §) 10.0008CEte600CE 600-1700 1700-1945

Ml 1945-2020 §=} 2020-2100 _~—s i) Mult!-exponential fit
Yet there was, and is, clearly a limit. At the rate we were going, something had to
give, and it had to give around now. Otherwise, in just another few centuries (the
blink of an eye, relative to our history as a species), human bodies would blot
out the Earth’s entire surface, and, not long afterward, stack up to fill the entire
biosphere.

We could begin populating the rest of the Solar system, but it’s hard to imagine
a scenario in which this meaningfully relieves population pressure on Earth, or
even offers a comparably sized niche. There just aren’t that many places in the

Sun's neighborhood where we can live in substantial numbers. And interstellar

travel would be a very, very slow escape valve.

So, in the mid-twentieth century, we were facing a “population singularity.” We
didn’t fantasize about any magical, unforeseeable singularitarian result, though.
Instead, we foresaw, sensibly enough, the inevitable end to exponential growth,
either the hard way (a massive dieoff) or the gentle way (a sharp enough decline

---

in fertility to avoid overshooting hard limits). Luckily, we're now tending more

toward the latter, though we’re not entirely out of the woods yet 24

Before Nick Bostrom began to focus on AI X-risk, he had already made a name
for himself among philosophers (serious and armchair alike) by advancing the
“Simulation Hypothesis,” which holds that, in all probability, we’re living ina
computer simulation, as in the Matrix movies. This is relevant to exponential
growth-worshiping fans of the Singularity because virtual worlds could, in prin-
ciple, support astronomically large virtual populations.

In brief, the Simulation Hypothesis argument goes like this. Over the past several
decades, we've become capable of simulating increasingly sophisticated virtual
worlds—from giant cosmological simulations, to photorealistic shooter games,
to faithful models of neural circuits run by computational neuroscientists.
Moore’s Law has been rendering these simulations exponentially faster and more

detailed over time.

Huge numbers of such simulations are already running on Earth, whether for
basic research, entertainment, urban planning, or other applications. This is
interesting in itself, when we think about how our brains became so much more
powerful when they were able to carry out predictive simulation of counterfac-
tuals;®+4/ all the simulations we're running today look like the same sort of cogni-

tive upgrade, but now at the level of our collective intelligence!

If Moore’s Law continues, then, before long, the realism (or at least the com-
plexity) of all these simulations might rival that of the real world. Some sim-
ulations already include virtual people. In video games, these are called Non-
Player Characters (NPCs). Today, they're mostly cartoonish, and are wired up to
handwritten scripts or AI models like digital marionettes.!*!! If you try to do in-
game electrophysiology on the heads of NPCs in a video game, you won't find
any neurons in there, just the back sides of textured polygons. However, in a very
distant descendant of the bff universe, intelligence could evolve, with or without
our help. If so, then, given exponentially increasing computation, an exponen-
tially increasing number of intelligent agents will be living in such simulated

worlds.

---

If you find the “bff on steroids” simulation scenario a stretch, keep in mind

that we see extraordinary realism emerge when we use neural nets to learn
simulations of the world, from the weather and fluid dynamics to sound and
vision. (That’s what deepfakes are.) It seems a safe bet that before too long we'll
see convincing interactive worlds conjured up from little more than a prompt,
ending the GOFAI-like era of today’s laboriously engineered video games and sim-

ulations. As in the Bible, a universe really could begin with a word, or just a few of
them. 224

Despite the hundreds of millions of dollars they cost to develop, the polygonal
puppetry of games like Fortnite will soon seem as crude as Pac-Man. And there's
no reason neural world simulations couldn’t include virtual Als implemented
using virtual neural nets. Dissection, electrophysiology, and physics experiments
could work in-game, though if those artificial creatures were to probe their world
ever more finely, they might encounter a kind of ... pixelation ... like quantum

effects? Hmmm.

At this point in the argument, proponents of the Simulation Hypothesis invite
us to take a Copernican Turn. Copernican Turns have occurred repeatedly in as-
tronomy, as when we realized that other planets have moons too, that Sol is just
another star, and that the Milky Way is just another galaxy. In short, that there’s
nothing special about where we live; hence the saying that “the Universe doesn't

revolve around us.”

Why, then, would we assume that our Universe has the unique property of being
“real,” since the jillions of other ones we know about are all simulations (as we
well know, since we're the simulators)? If intelligent beings in a “parent” universe
can simulate a great many “child” universes, and each of these universes feels per-
fectly real to its inhabitants, then a randomly selected intelligent being (like you)
is exceedingly unlikely to happen to live in the “real world” at the root of this tree

of universes—if, indeed, the tree even has a root, or is a tree at al] 820

Detailed arguments for and against the Simulation Hypothesis are beyond our
scope here. Its relevance to us lies less in its disconcerting claim about whether
we have a parent universe (and are thus ourselves something like Als?) than in its

less controversial implications about the child universes we can create, and, since

---

1945, have been creating at an exponentially growing rate. For in a sense, any
computational environment is a child universe with its own dynamical laws, and,

soon, its own digital inhabitants.

A program like the one Ada Lovelace wrote to compute Bernoulli numbers creates
a tiny, trivial universe whose “physics” does nothing other than to produce a
sequence of digits. Amore complicated program, like the one written for the
MANIAC in 1945 to simulate the hydrogen bomb, models a universe in which a
single runaway process unfolds, a sort of cartoon Big Bang. Massively multiplayer
games are child universes full of digital puppets whose bodies are controlled by
“gods” (us) in the parent universe. Now, real agents are starting to inhabit those
virtual worlds. Every instance of ChatGPT can be considered a child universe
containing a single Al, which communicates with a “god” in the parent universe

through its context window.

Futurists like Ray Kurzweil, who popularized the idea of the Singularity, and myr-
iad sci-fi writers have speculated about how we could transmigrate into our child
universes by scanning our brains, then running them in simulation. It’s not clear
whether those “uploaded minds” would be able to instantaneously learn kung fu
like Neo, but we could speed up or slow down our subjective sense of time, copy

ourselves, change how we look, (maybe) live forever-ish,\“*2! and perform various

other cool digital tricks.

Unfortunately, mind uploading is not realistic, or, at least, not for along
while./=23) And I wouldn't recommend beta testing the procedure unless you're
on your deathbed, as your parent-universe brain would not survive the scanning

process.

What is entirely realistic—what we are already starting to do today—is to create
new intelligences within child universes. I’ve argued that most of these are, in

a broad sense, human intelligences, as they are pretrained on collective human
experience. They have also, through fine-tuning for dialogue, been trained to
pass the Turing Test. Whether or not we regard them as “people” or “mind chil-
dren,”=24l they are intelligent entities, and their population can and will grow

much larger (and more quickly) than the human population.

---

Not that “population” is necessarily a concept that will translate straightfor-
wardly into the digital realm. Models come in every size, from tiny to vast; they
can be copied and forked, run briefly or for a long time, act as independent enti-
ties or link tightly into a single larger entity. This is how life works in general, of
course, but much about human sociality, law, and political economy relies on flat
relationship graphs, in which the entities are all of a uniform kind, presumed to
be “created equal.”

Uniform treatment of entities has already posed problems, given the rise of
enormous, powerful corporations with person-like rights and legal statuses, the
animal liberation movement, and more recent legal battles waged on behalf of
mountains and rivers.'°**! Great numbers of variously sized AI entities living in
virtual worlds, many of which communicate with our own via chat windows,
cameras, microphones, screens, headsets, and cloud services, are about to compli-

cate life in the digital multiverse even further.

At least we now have a much better sense of what lies beyond the “population
singularity” predicted in the mid-twentieth century. Catastrophists at the time
predicted a “population bomb” that would bring an ugly end to human civiliza-
tion, resulting in a descent into environmental collapse, Mad Max dystopia, and
cannibalism.|“2" That will probably not happen, as our population—at least in

this universe—is set to peak, then begin to decline, this century.

Why is the current MET halting population growth and sending it back into
decline, unlike the previous METs that kicked population into overdrive? Many
factors come into play, including the rise of women’s rights and improvements
in contraceptive technology, but the main driver is economic development, as
can be confirmed by exploring the historical correlations between birth rate and

wealth by country.222

Until surprisingly recently, human numbers were kept in check mainly by the
Malthusian forces of disease, starvation, and violence. A high birth rate was re-
quired simply to ensure that there would be a next generation. And that next gen-
eration was economically valuable to prospective parents. Children were needed

to work the land, generate income, and provide for mom and dad in their dotage.

---

In post-agricultural societies, though, children go from being an economic asset

to a liability. Nowadays, per economic sociologist Viviana Zelizer, “A national sur-
vey of the psychological motivations for having children confirms their predom-
inantly sentimental value.” Children may provide “emotional satisfaction, but no

money or labor.”/825) So, we're now having a lot fewer of them.

Declining fertility suggests that, regardless of employment and market statistics,
individual people in advanced economies have become net consumers, rather
than producers, Economic productivity and population are decoupling. And

an end to population growth has far-reaching consequences, given that, as dis-
cussed above, our entire economic system has been built around the assumption

of continual growth.

On the other hand, an increasing share of our economy is shifting into the realm
of information work, which can move seamlessly between digitally connected
universes; and we now know that the population of intelligences in our child
universes is about to explode orders of magnitude faster than any baby boom. If,
a few decades from now, we were to plot the logarithm of the total population of
combined humans and Als over time (or something roughly equivalent to popu-
lation), we would see another kink in the curve beginning around 2020, similar

to the one in 1945, and even more dramatic.

Tears of Joy

Having explored the problems raised by the “greatest good” part of Bentham’s
“greatest good for the greatest number” calculus, it’s now time for us to delve into
the even thornier problems raised by the “greatest number” part. We've seen that,
for an individual, “good” both doesn't strictly exist and isn’t additive, but you
might suppose that the addition of something approximating “good” across indi-

viduals still makes some sense as a moral heuristic. Spoiler: it doesn't.

Recall that although twentieth-century “population bomb” anxieties turned out
to be a false alarm, it wasn’t because infinite growth wouldn't be a problem, but
because increasing wealth reliably leads to lower fertility. Draconian measures
like China’s “One Child Policy” were both cruel and unnecessary. As China grew

richer, its fertility declined so dramatically that it now faces an alarming popu-

---

lation crunch. In Japan, the population is shrinking so rapidly (especially given
high barriers to immigration) that by 2040 the amount of unclaimed, vacated

land is projected to exceed the area of Ireland!§*2!

This is a preview of what the future will look like globally—which is great news
for our long-term survival. Assuming we don’t ruin everything in the meantime,
our footprint will lower enough to allow for the regrowth of stressed ecosystems,

hopefully even as we maintain a high living standard.

There's probably no single “right population size” for Earth, but rather a wide
range, anywhere between too small for human diversity and stability to too large
for a decent quality of life and non-human diversity, even given advanced and
highly efficient technology. We only know for sure that there are lower and upper
bounds, making perpetual exponential growth (or decline) incompatible with
dynamic stability. For long-term human survival, population on Earth must ei-

ther stabilize or fluctuate within those bounds.

Is an Earth with ten billion people necessarily ten times better than an Earth with
one billion, though? Or, to give this a non-human gloss, is the “value” of domestic
cats (worldwide population, roughly 220 million) really seventy-three thousand
times the “value” of snow leopards (worldwide population, roughly three thou-
sand)? Or else, if we say that the two species have equal value, do we really think

the life of each snow leopard is “worth” the lives of seventy-three thousand cats?

Some Utilitarian philosophers are fond of setting up morally agonizing “trolley
problems” =" to try to get actuarial about questions like these (if you pull the
lever, you can derail the trolley, sacrificing only one thousand kittens to save the
snow leopard tied to the tracks ...), but I think there’s something wrong with the

entire premise of trying to rank-order value in this way.

Psychological evidence shows that it’s easy to set up trolley problems that violate
the transitive law. In fact, trolley problems have become famous for exposing
human “irrationality” in even more blatant ways than Tversky’s intransitivity
tricks. The classic version of the trolley problem has five people tied to the track in

front of the trolley and one standing on a side track. You can either do nothing, in

---

which case five people will die, or pull the lever, in which case the trolley will be

diverted onto the side track and one person will die.

The felicific calculus is clear: you should pull the lever, because the alternative

is five times worse. Real people’s moral calculations aren't so straightforward,
though. Their responses are all over the place, and highly sensitive to, from a
strict Utilitarian's perspective, irrelevant details. For instance, if it’s necessary to
push an overweight bystander onto the tracks to save the other five innocents, al-
most nobody will do it@24

If we consider “good” to add up across individuals, the easiest way to increase
goodness is simply to increase population. By such a measure, since there are
about eight billion people today and there were one billion in 1800, the world
today is eight times as “good” as it was then. By the same calculus, India is six

times as “good” as Pakistan, and the US is five times as “good” as the UK.

It gets worse. “Longtermism” argues that future people should count equally,#*4)
which would imply that the life of an average young French woman, who, statis-
tically speaking, will have 1.83 children, is “worth” forty percent more than the
life of an average Japanese woman, who will have only 1.3 children. A Nigerian
woman will be “worth” far more than both combined, as the fertility rate in
Nigeria is 5.24 (though rapidly falling as prosperity there increases). The differ-
ences are in fact exponentially greater, since this only takes one generation into
account, and Longtermism considers all descendants equally. So if we survive far
into the future, the value ratio shoots toward infinity, even if the birth ratios are

only infinitesimally different.

And it gets sillier. Near the beginning of Superintelligence, Bostrom seeks to use
felicific calculus to emphasize just how much is at stake when we gamble with
humanity's future. In a box entitled “How big is the cosmic endowment?” he
describes a scenario that, upon first reading, I assumed to be comedy-circuit ma-
terial, or a dystopian straw man. However, I think it's intended to be a Utilitarian’s

utopia!/#22

Here’s how it goes. Begin with the assumption that we will all upload our brains,

because of course that’s the way to go—more of us can live as Sims ina virtual

---

world than in the real world (or whatever this universe is), which means more
potential happiness. I guess that, to mollify animal-liberation Singularitarians,
we should make room for our pets, livestock, and the remaining wild animals to
get uploaded too. Then, we should proceed to expand the data centers so that as

many virtual humans can be packed in as possible.

This “utopian” scenario doesn’t just imply tiling the Earth with data centers and
eliminating all other, less space-efficient forms of life, but turning the entire Solar
system into a giant solar data center, disassembling the planets and asteroids as
needed.=*4! Also, sending out nanotechnological “von Neumann probes” at close
to the speed of light—little spaceship-factories than can build more cosmic data
centers wherever they find the matter and energy to do so, and in turn send out
more von Neumann probes, ultimately colonizing “a large part of our future light
cone.” Assuming these probes don’t run into competing projects from alien civi-

lizations, to do anything less would be ... infinitely immoral!

Multiplying all of the big numbers together and carrying out the colonization
scheme of Life, the Universe, and Everything until “cosmic expansion puts fur-
ther acquisitions forever out of reach,” Bostrom concludes, “what hangs in the
balance is at least
10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,0
00,000 human lives (though the true number is probably larger). If we represent
all the happiness experienced during one entire such life with a single teardrop of
joy, then the happiness of these souls could fill and refill the Earth’s oceans every
second, and keep doing so for a hundred billion billion millennia. It is really

important that we make sure these truly are tears of joy.”

When one weighs those potential cosmic oceans of joy against the interests of
the paltry few billion people alive today, it becomes possible to justify any means
to drive growth, no matter how ugly in the present. You may be starting to see
why this suite of beliefs, congealed into an all-encompassing ideology, appeals to

some in Silicon Valley:!22*!

e Immortality. To a Californian subculture that has long been keen on fitness
regimens, dietary supplements, and “biohacking,” the idea that digital
immortality awaits if we can just hold out long enough is appealing. Ex-

---

ponentially improving technology might mean we don't even have to wait
that long, despite how far-fetched brain uploading seems today. On the
other hand, those who die prematurely can always freeze their bodies in
liquid nitrogen—or, for a lower price, just their heads.“

@ Video games. Living in one while trying out different bodies, insta-learning
kung-fu moves, and embarking on thousand-year journeys to other star
systems sounds awesome.

@ Staying on top. Tech people tend to think of themselves as an elite thanks
to their superior intelligence, making the emergence of highly capable
AI models an uncomfortably exciting prospect. If the fear of not being
smarter than those models predominates, it leads down the AI doomer
path. On the other hand, digitally merging with AI models could keep one's
future self at the top of the pecking order.

@ Scaling. Moore's Law, which has held for decade after decade, has normal-
ized the idea of eternally exponential scaling. Techies have long worshiped
the exponential, but the meteoric rise of online services starting around
2000, and then of cloud computing in the 2010s, has made super-scaling
a business mantra and ideology too. Conversely, ideas that turn out not to
be viable are said to be ones that “don’t scale.”!“2" Turning the entire light
cone into a cosmic data center that runs the Truman Show for astronomical
numbers of people is scaling taken to its ultimate limit.

© Wealth. Some Effective Altruists, including Peter Singer, emphasize giving,
and donate much of their income to causes carefully evaluated for im-
pact.|©24) It’s hard to argue that is a bad thing, even if one’s own choice
of causes differs. Others, like disgraced cryptocurrency billionaire Sam
Bankman-Fried, have emphasized (whether cynically or not) the accumu-
lation of great wealth first, to allow for “higher impact” giving later on, The
moral hazard here is obvious, as one can always tell oneself that one is still

in the “wealth growing” phase of the plan, ©"!

Although Utilitarianism and its associated movements aren't exactly a religion,
there are some undeniable parallels. As mentioned, the impossibility of Ben-
tham’s original ambition to develop a descriptive theory of the “Springs of

Action” has led Utilitarians to drop any pretense of a scientific “is” to embrace

---

a normative “ought.” When it comes to those “oughts,” counterintuitive value
judgments, and the belief that those who disagree are confused or morally
inferior, creates an in-group. Effective Altruism also shares more than a bit in
common with the Prosperity Gospel, which holds that, for true believers, physical
health and financial wealth are the will of God. Finally, the promise of immor-
tality sounds more than a little familiar, especially when it comes in two flavors:
a heavenly Rapture of the Nerds‘**4 or, if the coming AI is unfriendly, an End of
Days ... or, worse still, an unimaginable number of immaterial souls in agony
whose tears, of the wrong sort, could “fill and refill the Earth’s oceans every sec-

ond, and keep doing so for a hundred billion billion millennia.”

Beyond Alignment

Solving the “AI Alignment Problem”!**4) means making sure that, by the time
really intelligent autonomous AI agents come along, their values are consistent
with ours. For believers in the Singularity, aligned Al is the key to us all ending
up in heaven, rather than extinct, enslaved, or in some simulated (but all too real)
digital hell.

One does not have to believe in the Singularity to consider this problem impor-
tant. However, because Utilitarian thinking has distorted the way we think about
both value and intelligence, it has also had an unfortunate influence on how we

think about value alignment.

In the earlier GOFAI period, the presumption had been that intelligence would
arise in sufficiently complex rule-based systems, so alignment was also envi-
sioned in terms of rules. This roughly corresponds to “deontology,” the ancient
philosophical tradition holding that rules can distinguish right from wrong:
“Thou shalt not lie,” “Thou shalt not steal,” and “Thou shalt not kill,” for example.

Accordingly, most twentieth-century anxieties about AI alignment concerned
whether such rules could ever suffice to ensure safe and friendly robots. Sci-fi
granddaddy Isaac Asimov famously explored this question in his J, Robot sto-

ries,/§42) starting with the premise that his “Three Laws of Robotics” should be

programmed into every robot:

---

1. Arobot may not injure a human being or, through inaction, allow a
human being to come to harm.

2. Arobot must obey the orders given it by human beings except where
such orders would conflict with the First Law.

3. Arobot must protect its own existence as long as such protection does

not conflict with the First or Second Law.

Of course, in Asimov's stories as in all sci-fi, mayhem ensues—otherwise known
as a plot. For Asimov, the trouble is Jawyerly—meaning that some combination
of an unusual situation and logical yet counterintuitive reasoning based on the
Laws leads a hyper-rational robot to do something surprising, and not necessarily

in a good way.!8*2!

The reader may be left wondering whether the issue could be “debugged” by
adding one more Law, or closing a loophole—something Asimov himself under-
took on several occasions. But as GOFAI's failures eventually made clear, the prob-
lem is unsolvable; one can't even get anything resembling competent behavior
purely by following legalistic rules, let alone ethical behavior. Ironically, as we've
seen in the realm of natural language processing, such rules can only be obeyed

by an intelligent agent that does not obey rules!

Recall that by the 2000s, state-of-the-art AI was no longer being programmed,
but rather trained through the maximization of value functions. Mostly, this
involved supervised learning, which is all about optimizing a task-specific score.
Starting in 2010, DeepMind, the outlier, focused instead on game playing using
Reinforcement Learning, in the belief that it would ultimately lead to AGI. This
approach, too, involved maximizing something, whether a chess rating or the

score of an Atari video game.

During this period, AI researchers seemed to be converging on the idea that
intelligence really is all about optimizing a value or utility function. I've argued
that this isn’t the case—and indeed, that we only began to see general intelligence
when we stopped training models to do specific tasks with supervised learning,
and switched to the unsupervised regime—but this isn’t (yet) a widely held view.
For instance, as of 2024, the Rationalist website LessWrong.com still claims on

its Wiki that “the term artificial intelligence can have anthropomorphic connota-

---

tions. In some contexts, it might be useful to speak of a really powerful optimiza-

tion process rather than a superintelligence."=)

A really powerful optimization process able to pursue any strategy to maximize
its value function—what could possibly go wrong? A better question would be:
how could it possibly turn out well? As noted earlier, no parameter in any dynam-
ically stable system, whether biological, ecological, or technological, can grow

without bound, and attempting to do so will indeed result in floods of tears.

The classic X-risk example is the innocuous-sounding “Paperclip Maximizer.”
Nick Bostrom offered up this scenario in 2003: an AI, perhaps connected toa
paperclip factory, is instructed to manufacture as many paperclips as possible.
After reconfiguring the factory to increase its throughput (so far, so good), the AI
realizes that more factories could be built to further increase production. If the Al
is smart enough to engineer new paperclip technology, it can, presumably, also
figure out how to make lots of money, convince people to do things, engineer new
tech, and otherwise take over the world, if necessary, by improving itself. Bad
news: human bodies are full of atoms that could become paperclips. But even if
the AI stuck to the traditional stainless-steel kind, covering the Earth (and then
filling the light cone) with robotic mining operations and paperclip factories
won't leave any space for snow leopards, tree frogs, or people. If we tried to inter-
fere with this process, it would of course become necessary for the AI to eliminate

us with extreme prejudice, It would be nothing personal.

This story unspools badly no matter what you tell the superintelligent AI to max-
imize. Bostrom acknowledges that “in humans, with our complicated evolved
mental ecology of state-dependent competing drives, desires, plans, and ideals,
there is often no obvious way to identify what our top goal is; we might not even
have one.” True. But he concludes that since a superintelligence “may be struc-
tured differently,” we must give it a “definite, declarative goal-structure with a
clearly identified top goal,” in the tradition of Asimov’s Three Laws of Robotics, in

order to be sure that it won't go rogue.

Not only does requiring AI to act like GOFAI not work; if it did, it would open the
door to all sorts of lawyerly horrors. Superintelligence is full of fanciful examples.

For instance, to optimize total human happiness, human simulations could

---

be simplified so more of them could run on any given hardware. Then, those
lobotomized Sims in their low-polygon-count environments could be kept on a
constant drip of virtual heroin. The greatest good and the greatest number, for
the felicific win!

The Alignment Problem is especially terrifying to Utilitarians who believe that
intelligence itself is Utilitarian. They are afraid, in other words, that superintelli-
gent AI will behave as they claim they would.!®**! If their supposed goal as perfectly
“rational” actors is to fill up the light cone with simulated people, disassembling
every animal, vegetable, or planet whose atoms could be used to build the cos-
mic server farm, then of course a really smart AI would do the same. Minus the

people.

Such games are zero-sum. Worse, imagining that they can be “won” by any single
actor implies an inexorable tendency toward monoculture, such that a single
kind of entity, whether paperclips, simulated people, or robots, crowds every-

thing else out. Anything that is not that goal amounts to an opportunity cost.

Moving beyond the “Alignment Problem” as usually understood isn’t hard. It has
both a descriptive “is” and a normative “should” aspect. The descriptive aspect
follows from the fact that intelligence is not the maximization of any single
value. Nor does an intelligent agent even consist of a single well-defined entity.
The interaction of diverse actors through mutual modeling is what creates the
dynamical process we call “intelligence.” Intelligence is an ecology, and the more
of a monoculture it devolves into, the less intelligent it will be, and the less inter-

esting life will become.

As a thought experiment, imagine creating an exact copy of the Earth in simula-
tion, and running it on a giant, isolated server farm (perhaps we've disassembled
Mercury and turned it into a Death Star—sized solar-powered computer to make
this possible). You and I would both be mirrored in that digital twin universe, and
virtual you would be reading these very words at this very moment. Has total
utility just doubled, since now every good thing is experienced both by you and
by your double?

---

I think the answer is “no.” You wouldn't be able to tell whether you're the “real”
you or the simulated you, but nothing about your life would change either way,
and nothing about the universe (or multiverse?) would be any more wonderful
or interesting—from any point of view. If anything, life would be strictly worse,
since both in reality and in simulation, Mercury would be gone. Even if that

planet is a lot less interesting than Earth, its absence would be a loss.

The idea of extending that loss throughout the universe in order to endlessly
replicate what we already have is nightmarish. We can see obvious parallels here
with the way colonial powers have attempted to erase indigenous cultures in an
effort to endlessly reproduce their own, and with the way capitalism's worst ex-

cesses push out diversity in the name of “hyper-scaling.”

As we mature and our wisdom increases, so will our regret over such needless
losses. Life only continues to enrich as long as it continues to diversify, and the
collective phenomenon of intelligence only grows when diverse sub-intelligences

model each other, in the process becoming a greater whole.

Monoculture is not scaling; it’s collapse, an ultimate failure to scale. When we
destroy variety, we zero out the value of encounter, we render mutual modeling
pointless, and we thus curtail the possibilities for our own continued develop-
ment. Embracing our evolution, however, means letting go of certainty, and al-

lowing identity to drift, branch, and hybridize, as it always does.

The word “we” will not mean the same thing it does today in a century, and even
less so in ten thousand years; less still in ten million. In ten million years, there
will be no recognizable humans, though in ten thousand—if we don’t mess up
—there probably will be. But much else will also exist. In as little as a century,
the Earth, and perhaps other parts of the Solar system, will be populated with
intelligences of other kinds, too, both larger and smaller, and these will greatly
outnumber our human bodies. If we believe life and intelligence are precious
seeds, destined to bloom here and there in the universe, then spread and efflo-
resce, we should ultimately expect our light cone to be populated by aliens of
every description—even in the unlikely event that we are the only seed, and that

they are all our children.

---

# Acknowledgments

Acknowledgments

2024, the year I spent writing this book, has been a year of losses. Two hit
especially close to home. My father, Josep Agtiera i Arcas, passed away in the
spring. He bought me my first computer, a Texas Instruments 99/44, in 1981.1
was six years old, and our family was living in a small apartment in Mexico City.
He brought it back with him from a visit to the United States, certain that com-
puters were about to change the world. In this, and in much else, he turned out
to be right. He shaped many aspects of my childhood—from a steady diet of sci-
fi, to unsanctioned after-hours field trips to the General Hospital where he was
a medical resident, to the many electronic devices we took apart together, to the
small mammal dissections we conducted with great ceremony on the kitchen
table. (My mother left the house for those.) He was a complex, flawed person. He
was also always a loving father, and his unshakeable belief that I would lead an

interesting life was a self-fulfilling prediction.

Just a week before he died, we also lost a dear family friend, Lesley Hazelton. Les-
ley was a brilliant writer, a razor-sharp critic, an inspiration to her many friends,
and a rebel to the end. She lived, and died, exactly as she wished. A few years ago
she encouraged me to begin writing for real, and was generous—and unstinting

—in her feedback. I miss her. We all do.

What Is Intelligence? owes its existence to a great many people and several
institutions—especially Google, Antikythera, the University of Washington, the
Berggruen Institute, the Santa Fe Institute, the Mila-Quebec AI Institute, and the
MIT Press. Many of the people I'll thank below are affiliated with one or more of

these.

As a designed object, this book's co-creator is James Goggin of Practise, in Tamaki
Makaurau (Auckland), What Is Intelligence? further develops an approach to si-
multaneously physical and digitally native media we established with our first

two projects, Ubi Sunt and Who Are We Now? (both published by Hat & Beard
Press, with warm thanks to J. C. Gabel). Chapter 1, “Origins,” first appeared in a

---

limited print edition, What Is Life?, in the fall of 2024, when we began the online
serialization. What Is Life? is now also available from the MIT Press.

Clea Agiiera-Arcas, Loraine Agiiera-Arcas, and Johan Michalove have helped
research, edited painstakingly, offered line-by-line critique, coded workflows,
wrangled spreadsheets, and in short dedicated an immense effort over more
than a year to making the book as accurate and readable as we could. Adrienne
Fairhall provided extensive feedback, especially on the neuroscience, which
greatly improved both my core arguments and their exposition. Brian Sholis did
the final rounds of editing and proofreading, and David Michalove stepped in to
chase down sources and permissions. However, I take sole responsibility for any
remaining errors or omissions, and all perspectives, interpretations, and opin-

ions, mistaken or not, are my own.

In collaboration with James Goggin, Minkyoung Kim and Marie Otsuka designed
and implemented the web version, which includes a good deal of video and inter-
active content. The simulations owe a heavy debt to Alex Mordvintsev (also the
inventor of neural cellular automata) and his elegant SwissGL library. The audio-
book was recorded at Bad Animals by Will LeMaster, with production help from
Wendi Wills.

Additional close readings of the text and editorial input, which improved the
final result significantly, came from Benjamin Bratton, Stephanie Sherman,
David LeBrun, Ben Laurie, Rif A. Saurous, Kate Meyer, Gary Lupyan, Moritz
Firsching, Alexander Meulemans, and Emily French. Warm thanks also to
Anselm Agiiera y Arcas, Eliot Agiiera y Arcas, Refik Anadol, Patricia Churchland,
George Dyson, Walter Fontana, David Ha, N. Katherine Hayles, Reid Hoffman,
DeLesley Hutchins, Michael Levin, Johan Liedgren, Charles Mudede, Addy Pross,
Carl Schoonover, Terry Sejnowski, Justin Smith-Ruiu, Dan Sperber, Korina Stark,
John Thornhill, Sara Imari Walker, Ren Weschler, Olaf Witkowski, and David
Wolpert.

In 2018 and 2019, I taught an interdisciplinary course at the University of
Washington, Intelligent Machinery, Identity, and Ethics, with help from Adrienne
Fairhall and enthusiastic support from Dan Grossman, Vice Director of the

Allen School of Computer Science and Engineering. Dan introduced me to Johan

---

Michalove, suggesting that he would be the perfect TA—which he was. Teaching
is the best way of learning. Although AI has developed a great deal in the years
since, the course was an early draft of many ideas in this book, and those ideas

further benefited from long after-lecture discussions with my students.

At Google, I owe deep thanks to James Manyika and Sundar Pichai for giving my
team, Paradigms of Intelligence (Pi), the freedom and resources to pursue inter-
disciplinary basic research. I’m grateful to Demis Hassabis and Yossi Matias for
their support of internal collaboration with Google DeepMind and Google Re-
search, respectively, and to Yul Kwon for his deft co-leadership of Pi. A big thank
you to Pi teammates and collaborators: Jyrki Alakuijala, Kenric Allado-McDowell,
Travis Beals, Sami Boukortt, Martin Bruse, Iulia Comsa, Yigit Demirag, Moritz
Firsching, Thomas Fischbacher, Alice Guan, Florian Hartmann, Geoff Keeling,
Evgenii Kliuchnikov, Seijin Kobayashi, Marcin Kowalczyk, Rachelle Lacroix, Mira
Lane, Alison Lentz, Brittni Maekawa, Kaitlin Maile, Delaney McMillen, Alexander
Meulemans, Alex Mordvintsev, Eyvind Niklasson, Peter Norvig, Robert Obryk,
Ettore Randazzo, Esteban Real, Jodo Sacramento, Mark Sandler, Nino Scherrer,
Anoop Sinha, Oliver Siy, Winnie Street, Zoltan Szabadka, Luca Versari, Sarah de
Haas, and Johannes von Oswald. Visiting faculty James Evans, Guillaume Lajoie,
and Blake Richards have been wonderful friends and colleagues, and have all

made intellectual contributions to the material presented here.

Time spent at the Santa Fe Institute over the past two years has profoundly in-
fluenced my perspective on life, complexity, and intelligence. I have also engaged
with a number of new collaborators, fellow travelers, and constructive critics
(often a bit of each) there, including Kevin Berger, Sean Carroll, David Chalmers,
Ted Chiang, Michael Hersch, Chris Kempes, David Krakauer, John Krakauer, Gary
Lupyan, Brice Ménard, Melanie Mitchell, Carlo Rovelli, Zenna Tavares, Geoffrey
West, and David Wolpert. I also re-encountered the wonderful Dan Dennett and
met Susan Bell at SFI. Very sadly, Dan was also one of 2024's losses; he is much

missed.

What Is Intelligence? is among the first long-form publications of the Antikythera
program, under the direction of Benjamin Bratton. Benjamin has instigated many

of my major writing projects in recent years, including this one, and has been a

---

loyal friend and frequent collaborator. Warm thanks also to Haley Albert, Nicolay
Boyadjiev, Nils Gilman, Emily Knapp, Dawn Nakagawa, Estela Oliva, Tobias Rees,
and Claire Webb; my gratitude, also, to Nicolas Berggruen for his intellectual
friendship and support, and to the Berggruen Institute.

Finally, warm thanks to Noah Springer of the MIT Press, for believing in this
project and for helping us bend the rules of traditional academic publishing.

---

About the Author

Blaise Aguiera y Arcas is a VP and Fellow at Google, where he is the CTO of
Technology & Society and founder of Paradigms of Intelligence (Pi). Piis an orga-
nization working on basic research in AI and related fields, especially the foun-
dations of neural computing, active inference, sociality, evolution, and Artificial
Life. In 2008, Blaise was awarded MIT’s TR35 prize. During his tenure at Google,
he has innovated on-device machine learning for Android and Pixel, invented
Federated Learning (an approach to decentralized model training that avoids
sharing private data), and founded the Artists and Machine Intelligence program.
A frequent public speaker, he has given multiple TED talks and keynoted NeurlIPS.
He has also authored numerous papers, essays, op-eds, and chapters, as well as

two previous books, Who Are We Now? and Ubi Sunt.

---

The Antikythera Book Series

Antikythera develops a philosophy of technology that seeks to better under-
stand, and thereby orient, planetary computation as a philosophical, scientific,
and geopolitical force. The research program takes its name from the first known
computer, the Antikythera mechanism, an ancient tool for orientation, navi-
gation, planning, and prediction across planets. The program understands the
future of computation as more than calculation. It is a technology to think with,

an instrument for discovery.

In collaboration with the MIT Press, the Antikythera book series publishes
unique titles by writers from diverse disciplines: computer science, philosophy,
history, architecture, physics, science fiction, and more. These books investigate
the creative and curious uses of our computational tools—or what we might
more precisely call artificial computation. With those tools it is revealed that
otherwise imperceivable building blocks of our reality and of our own flesh are
themselves computational. The planet discovers itself through computation, and

computation discovers itself through us.

At some moments in history, human imagination of technological accomplish-
ment far outpaces what is possible, and, at others, technological capabilities
overflow the concepts available to understand them. This moment in history is
more the latter, and so the work of philosophy is less to project truisms onto real-

ity than to generate new conceptual tools to align with what is already emerging.

This is a pre-paradigmatic moment, which necessarily means one that is on
uncertain footing. As things we recognize as alive, intelligent, and technological
combine in new ways, contemporary definitions of “life,” "intelligence,” and
“technology” converge as well. As the world is transformed through computa-

tion, our fundamental understanding of it (and ourselves) adapts in turn.

The Antikythera school of thought is neither utopian nor dystopian. Solutionism
—technological or political—is not the focus. Instead, the project is epistemolog-
ical, compositional, and existential: How does computation reveal fundamental

qualities of this living, thinking planet, and what are its capacities as the now

---

primary means by which complex intelligence remakes its worlds through inter-

pretation, speculation, and construction?

The humanities are perhaps too content with reflexive critique, especially when
it comes at the expense of deeper engagement. For Antikythera, the most nec-
essary philosophy of technology (and as more technologies are computational,
thereby the philosophy of computation) is one that contributes directly to the
formation of that emergent paradigm. To do so is to draw fundamental philo-
sophical positions from direct encounters with theoretical biology, information
theory, planetary sciences, speculative engineering, and design, and the intellec-

tual histories of all these.

If the Western philosophy of technology canon is darkened by the shadow of
Martin Heidegger's intuition that the essence of technology is an alienation of
being, our approach leans more on the lessons of Copernicus (and so many oth-
ers) who employed technological abstraction to achieve a precious allocentric
awareness of where, when, how, and who we—in the broadest possible sense
—are and may become. The estrangement that comes with the reformation of
thought as it is bent through the prisms of machine perception, is not what pre-

vents philosophical insight: rather, this is its foundation.

For this, the locus is not the singular thinking subject, nor even a species asa
whole. Much more general and precious forces are at work. The philosophy of
the next century is one for which life as such, intelligence as such, cognition as
such, and computation as such all combine in new ways that allow them to both
comprehend and transform themselves. Humans may be the agents of this com-
bination, and this makes us genuinely exceptional within the biosphere and tech-

nosphere. Ultimately, however, we are not the protagonist; we are the vehicle.

Alongside an online platform, the Antikythera book series connects new ideas
with new forms of digital information design. Both the books and the platform
are interfaces to the ideas that constitute the Antikythera school of thought and,
hopefully, its contribution to the philosophy of the future.

---

Benjamin Bratton
La Jolla, California

November 2024

---

# Glossary

Glossary

abiogenesis The emergence of life from non-life. See also: life.

Acoela An ancient order of small marine worms that diverged from other animals
more than 550 million years ago; among the earliest bilaterians, they have no gut,
or circulatory or respiratory systems.

agent An entity who/that does or acts; in a directed interaction between two
entities, the active one may be referred to as the agent, while the recipient of the
action is the patient. See also: moral agent, patient.

animism The belief (held by many traditional societies) that objects, places, and
creatures possess spirits, and thus that all things are alive and interconnected. See
also: vitalism.

anthropic principle The principle that the fundamental laws of the observed
universe must be compatible with the existence of the conscious, intelligent
observer positing those laws. See also: fine-tuning (cosmology),
anthropocentrism The belief that humans are the most important entities in the
universe; viewing or understanding all other entities only in terms of their value
to, or in comparison with, humanity. See also: anthropomorphism.
anthropomorphism The (often inappropriate) attribution of human characteris-
tics, behaviors, or emotions to nonhuman entities, such as other animals, objects,
or phenomena. See also: anthropocentrism.

Artificial General Intelligence (AGI) Artificial Intelligence capable of a wide,
human-like range of tasks and behaviors; the term was popularized when models
capable only of single tasks started to be called AI. See also: Artificial Narrow Intel-
ligence.

Artificial Intelligence (AI) A term coined in 1955 by computer scientist John
McCarthy and colleagues for “the conjecture that every aspect of learning or any
other feature of intelligence can in principle be so precisely described that a
machine can be made to simulate it.” See also: cybernetics, Good Old-Fashioned
Artificial Intelligence.

Artificial Narrow Intelligence (ANI) An AI system designed only to do one task
or anarrow range of tasks; examples include character recognition, face detec-

tion, and product-review sentiment analysis. See also: Artificial Intelligence.

---

Artificial Superintelligence (ASI) A general AI or AGI with broadly superhuman
performance (though there is no consensus on what that constitutes); such a
superintelligence would presumably be capable of recursive self-improvement,
potentially creating an intelligence explosion. See also: Artificial General Intelli-
gence, intelligence explosion.

attention A cognitive process wherein certain perceptual information is allocated
preferential mental processing, enabling the formation of a coherent view of the
most important aspects of an environment, often guided by factors such as
novelty, salience, relevance, and task demands; also, a family of machine learning
techniques designed to selectively concentrate neural net processing in a given
layer only on certain activations or relationships in the previous layer. See also:
Transformer.

attention layer The kind of neural net layer that powers the Transformer archi-
tecture, implementing content-based pattern matching and selective attention
over a context window of fixed size. See also: attention, Transformer.
autocatalysis A process whereby a reaction is catalyzed by one of its own prod-
ucts, causing the reaction to speed up exponentially until limited by the availabil-
ity of a reactant. See also: autocatalytic set.

autocatalytic set As conceived by biochemist Stuart Kauffman, a network of
interacting molecules where each molecule can be catalytically produced from
other molecules in the set, thereby creating a self-sustaining and self-replicating
system; I use this term more generally for any set of entities, including whole
organisms or code instructions, with the same functional properties (mutual
catalysis and collective self-replication). See also: abiogenesis, autocatalysis.
backward causality When the effect of an event seems to paradoxically precede
its own cause. See also: entensional.

bff A minimalistic computer simulation demonstrating the emergence of func-
tional replicators out of random noise; based on a variant of the Brainfuck
programming language. See also: abiogenesis, Brainfuck.

blindsight A neurological phenomenon where, following removal or destruction
of the visual cortex, people can still respond to visual stimuli, yet claim to be
blind; discoverers Nicholas Humphrey and Lawrence Weiskrantz, both neurosci-

entists, considered blindsight “seeing without consciousness,” but perhaps it

---

simply reflects a lack of connectivity between the brain regions processing vision
and generating language.

Brainfuck A minimalistic, esoteric programming language closely resembling a
Turing Machine, devised in 1993 by Swiss physics student Urban Muller. See also:
bff.

calculus ratiocinator A hypothetical (and unrealizable) universal logical-calcula-
tion framework described in the writings of mathematician Gottfried Wilhelm
Leibniz, wherein the manipulation of symbolic propositions could be used to
prove the truth or falsity of any statement; similar in spirit to Good Old-Fashioned
Al. See also: characteristica universalis.

cellular automaton A grid of cells, each in a specific state, that evolves over time
based on a set of rules determined by the states of neighboring cells; developed by
mathematician John von Neumann and collaborators from the 1940s onward. See
also: neural cellular automaton.

characteristica universalis An (unrealizable) universal symbolic language imag-
ined by mathematician Gottfried Wilhelm Leibniz to represent all knowledge and
ideas in a clear and unambiguous way, enabling logical calculation and reason-
ing. See also: calculus ratiocinator.

choice blindness The phenomenon studied in cognitive science where individu-
als fail to notice mismatches between their intended choice and the outcome
they're presented with, demonstrating the pliability of our preferences and
memories; the term was coined by a team of Swedish researchers led by cognitive
scientist Petter Johansson. See also: interpreter, the.

comb jelly A phylum of ancient marine invertebrates, the Ctenophora, dating back
to the Ediacaran, characterized by biradial symmetry (radial symmetry like a
jellyfish, but sometimes including a pair of tentacles) and a fringe of cilia (tiny
hair-like structures) that move in a way reminiscent of the teeth of a comb; they
are delicate, near-transparent, and often bioluminescent.

competence without comprehension A concept introduced by philosopher
Daniel Dennett to describe systems or entities that can perform tasks effectively
without understanding how or why they are doing so; perhaps more properly
interpreted as an inability to generalize a skill beyond a narrow domain, or to

explain it using language.

---

complexification The process whereby things become more complex over time; I
argue that this characterizes the evolution of life, intelligence, and technology,
and occurs because existing dynamically stable components can sometimes
combine (or “compose”) to form larger dynamically stable wholes, which can
themselves serve as components for further composition. See also: symbiogene-
sis.

composition (functional) When one or more functions are composed (i.e., com-
bined) to create another function. See also: recursion (computing).
computational neuroscience The study of nervous systems and brains as
computational or information-processing systems. See also: functionalism, Neu-
roAI.

computronium A substance that computes with massive parallelism; the term
was coined in the 1980s by physicist and computer scientist Norman Margolus to
describe a hypothetical material optimized at the atomic or molecular level to
perform computation as efficiently as the laws of physics allow, though I use it
more broadly to describe the organized, computational state of matter character-
izing life. See also: massively parallel.

cybernetics A field of study founded by mathematician Norbert Wiener and
colleagues in the 1940s focusing on feedback, prediction, control, and learning as
exhibited by living systems and some machines; the intellectual predecessor of
modern machine learning, See also: Artificial Intelligence, machine learning.
dark room problem A challenge in predictive-coding and active-inference theo-
ries of the brain, highlighting the paradox that if organisms seek to minimize
prediction errors, they might prefer unchanging, low-stimulation environments
(like a dark room), which contradicts observed behavior where organisms actively
seek novel and stimulating experiences. See also: predictive brain hypothesis.
Dress, The A viral photograph that became an internet sensation in 2015, making
people question whether “The Dress” was blue and black or white and gold, due to
an optical illusion related to color perception; the leading theory is that one’s
inference depends on whether one is a night owl, which affects statistical priors
on lighting.

dualism A philosophical and religious concept, often associated with mathemati-

cian and philosopher René Descartes, positing that the mind and body have two

---

fundamentally different natures, one immaterial (the mind) and the other physi-
cal (the body).

dynamic instability When a small variation in initial conditions can cause wildly
diverging outcomes, often associated with the butterfly effect. See also: dynamic
stability.

dynamic kinetic stability (DKS) A concept introduced by the chemist Addy Pross
to describe systems that persist through time not by being static, but through
continuous dynamic change and turnover, such as the self-replication of mole-
cules or the metabolic activity of living organisms. See also: dynamic stability.
dynamic stability In this book, used to describe systems that cycle through a loop
of states (in dynamical systems theory, a stable limit cycle), thus preserving their
identity through time even though they are in constant flux; a hallmark of living
systems. See also: dynamic instability.

Effective Altruism (EA) A utilitarian philosophical and social movement that
advocates using evidence and reason to determine the most effective ways to
improve the world and directing resources—time, money, or skills—toward
actions that achieve the greatest positive impact; philosophers Peter Singer, Toby
Ord, and William MacAskill are among its standard-bearers. See also: utilitarian-
ism.

efficient cause Per Aristotle, an agent or force that produces an effect or change in
another object or being. See also: final cause.

élan vital A term introduced by French philosopher Henri Bergson referring toa
vital force or impulse inherent in all living organisms and driving growth,
change, and the creative evolution of life. See also: psychic pneuma, vitalism.
embedding A learned representation of data where objects (e.g., words or images)
are mapped to continuous, low-dimensional vector spaces, capturing their se-
mantic or structural relationships and enabling generalization for tasks like
classification, clustering, or translation. See also: Word2Vec.

endosymbiosis A symbiotic relationship in which one organism comes to live
inside another organism, conferring mutual benefit and potentially resulting in a
new form of life; most famously associated with the work of evolutionary biolo-
gist Lynn Margulis, who showed that mitochondria and chloroplasts, today

eukaryotic organelles, were originally free-living bacteria that were engulfed by

---

ancestral host cells related to archaea. See also: symbiogenesis, symbiosis.
entensional A term coined by cognitive scientist Terrence Deacon referring to
systems (including simple and engineered ones) that operate according to physi-
cal laws, but that are goal-directed or purposive. See also: purposive, teleology.
existential risk (X-risk) A potential event or process that could either cause the
extinction of humanity or irreversibly curtail its long-term potential, encompass-
ing threats such as nuclear war, advanced artificial intelligence misalignment,
pandemics, or catastrophic climate change.

felicific calculus An approach proposed (though never fully specified) by
philosopher Jeremy Bentham for quantifying happiness or pleasure to evaluate
the moral rightness of actions, based on factors such as intensity, duration,
certainty, proximity, and extent of the resulting pleasure or pain. See also: utilitar-
ianism.

few-shot learning A method in machine learning where an Al system learns to
classify or interpret new data from only a small number of examples; this mimics
human ability, which requires fewer instances than traditional machine learning
to understand something new. See also: machine learning, one-shot learning.
final cause Per Aristotle, the purpose or goal for which a thing exists or an action
is undertaken, being the “end” or “telos” towards which that thing strives. See
also: efficient cause, teleology.

fine-tuning (cosmology) The puzzle posed by the fact that certain fundamental
physical and cosmological constants appear to have precisely the values neces-
sary to support the existence of life in the universe. See also: anthropic principle.
fine-tuning (machine learning) When a pretrained model, such as a language
model, is further trained or “tuned” on a more specific task or dataset, thereby
enhancing its precision and applicability to a particular problem or domain. See
also: machine learning.

functionalism A computational position held by mathematicians Alan Turing
and John von Neumann emphasizing that what something “is” is defined by what
it does, which can be independent of implementation, hence multiply realizable;
the corresponding philosophical perspective, championed by Hillary Putnam and
others, conceives mental states in terms of their role in a system or their behav-

ioral effects, thus opening the possibility that different kinds of systems, includ-

---

ing non-biological ones, could manifest the same types of mental states. See also:
computational neuroscience, multiple realizability.

Gaia hypothesis Posits that the Earth is homeostatic, functioning as a self-
regulating system in which living organisms interact with their inorganic
environment to maintain conditions conducive to life, such as stable tempera-
tures, atmospheric composition, and ocean salinity; proposed by independent
scientist James Lovelock in 1972 and later developed with Lynn Margulis.
generalization (machine learning) A model's ability to perform well on unseen
data by capturing the underlying patterns in the training data rather than merely
memorizing it, ensuring it can make accurate predictions or decisions for new
inputs not encountered during training. See also; perceptual invariance.

Good Old-Fashioned Artificial Intelligence (GOFAI) A term coined by philoso-
pher John Haugeland in 1985 for the classical (and largely ineffective) approach to
Al that emphasizes high-level symbolic representations and rule-based manipu-
lation to model intelligent behavior; this paradigm relies on explicitly pro-
grammed knowledge and logical reasoning, contrasting with cybernetics and its
modern successor, machine learning. See also: Artificial Intelligence, cybernetics,
machine learning.

grandmother cell A hypothetical neuron that activates in response to very
specific complex stimuli, such as a person’s own grandmother, postulated (with
tongue in cheek) by neuroscientist Jerry Lettvin in 1969; while neurons can
indeed respond to highly specific stimuli, they do so in populations, making it
unlikely that complex concepts are represented by unique neurons.
hallucination (machine learning) A generated output by a model (such as a large
language model) that is factually incorrect, nonsensical, or fabricated, despite
appearing plausible or confident, often arising due to limitations in the model's
training data or inference mechanisms.

Homo economicus A theoretical individual proposed in economic theory who acts
consistently rational and narrowly self-interested, always making decisions that
maximize utility given the information available. See also: utilitarianism.
homuncular fallacy Mistakenly attributing selfhood or subjectivity only toa
particular part of the brain. See also: homunculus.

homunculus A term derived from Latin meaning “little man,” often used in

---

discussions of philosophy and neuroscience to describe the misleading idea ofa
small being inside the brain who interprets sensory information and controls our
actions.

Hydra A genus of small, simple aquatic animals of the phylum Cnidaria, of special
biological interest for their distributed nerve net, regenerative capabilities, and
immortality.

Industrial Revolution A period from the late eighteenth to mid-nineteenth
century marked by significant developments in agricultural, manufacturing,
mining, transport, and technology sectors (most of which were enabled by fossil
fuels and the steam engine) which dramatically altered the socio-economic and
cultural conditions in Britain, and later spread to Western Europe and North
America. It is often cited as marking the transition to modern economic growth;
some economists posit subsequent Industrial Revolutions based on electrifica-
tion and information technology. See also: Major Evolutionary Transition.
inference An integral part of both human reasoning and AI, inference involves
making logical deductions or predictions based on existing information or data,
such as interpreting the contents of an image or the meaning of a wordina
sentence. See also: machine learning.

inpainting An image-restoration technique where missing or corrupted parts of
images are filled in with plausible content, based on information and context
from the surrounding areas and from similar images. See also: masking.
intelligence The ability to model, predict, and influence one’s future; it can evolve
in relation to other intelligences to create a larger symbiotic intelligence.
intelligence explosion An event hypothesized by mathematician I. J. Good in
which an artificial intelligence system becomes capable of autonomously improv-
ing its own design, leading to rapid, unforeseen advancements in technology and
potentially surpassing human intellectual capacity; as I use the term, intelligence
explosions are a broader evolutionary phenomenon driven by positive feedback
in mutual theory-of-mind modeling, and include the rapid growth in human
brain size over the past several million years. See also: existential risk, theory of
mind.

intentionality level The depth of representation a person, system, or model has

about the self and others; intentionality levels range from zero, representing

---

inanimate objects, to one, representing only immediate experience, to higher
levels characterized by higher-order theory of mind, including self-reflection and
understanding others’ minds. See also: theory of mind.

interpreter, the (neuroscience) Refers to the brain's left hemisphere mechanism
(for most right-handed people) that creates explanations and narratives to make
sense of our experiences and actions, even when it lacks complete information
about their true causes; proposed by neuroscientist Michael Gazzaniga to explain
observations from split-brain patients, and consistent with many other findings,
including choice blindness. See also: choice blindness.

is/ought dichotomy A distinction proposed by philosopher David Hume between
descriptive statements (what is the case) and prescriptive or normative state-
ments (what ought to be the case), to argue that values or morality cannot be
deduced from factual knowledge alone.

joint probability distribution A mathematical description of the likelihood of
two or more events occurring together, often represented in the form of a table or
matrix, that can provide important insights into the dependencies and interac-
tions between different variables in a system.

Krebs cycle A key metabolic pathway discovered by biochemist Hans Krebs, the
Krebs cycle (also known as the citric acid cycle or TCA cycle) involves the oxida-
tion of acetyl-CoA into carbon dioxide and the transfer of energy to produce
NADH, FADH,, and ATP, which cells use for energy. See also: reverse Krebs cycle.
latent variable A variable that is not directly observed but inferred through a
mathematical model from other variables that are observed; latent variables are
often used in machine learning to explain hidden or underlying structures in
complex data. See also: embedding.

lateral inhibition A ubiquitous neurological principle first presented in a 1957
paper by neuroscientists Keffer Hartline and Floyd Ratliff in the context of the
visual systems of horseshoe crabs, where an excited neuron reduces the activity
of its immediate neighbors, leading to a contrast enhancement that aids percep-
tion of edges and spatial differences.

learning The process whereby an organism or artificial intelligence system
acquires knowledge, skill, understanding, or the ability to perceive nuance

through experience, study, experiment, instruction, or error minimization,

---

ultimately resulting in the modification of behavior or the ability to predict
outcomes based on patterns or inferences. See also: machine learning.

life A self-modifying, computational state of matter arising from selection for
dynamic stability; it evolves through the symbiotic composition of simpler
dynamically stable entities.

logical proposition A statement that has a distinct truth value—either true or
false—which can form the basic building block of logical arguments and reason-
ing. See also: calculus ratiocinator.

Longtermism An ethical standpoint emphasizing the long-term future and
advocating for decisions and actions that consider their potential impact on
many generations to come; most controversially, its adherents may use utilitarian
principles that weigh equally the interests of all people, including (potentially
vast numbers of) hypothetical future people. See also: utilitarianism.

machine learning (ML) An approach to building intelligent machines that pro-
vides systems with the ability to learn and improve from experience without
being explicitly programmed, involving the construction and study of algorithms
that can make predictions or decisions based on patterns in data; in the tradition
of cybernetics, and often contrasted with Good Old-Fashioned Artificial Intelli-
gence, See also: Artificial Intelligence, Good Old-Fashioned Artificial Intelligence.
Major Evolutionary Transition (MET) A key point in the evolution of life that
results in a significant increase in complexity through symbiotic interdepen-
dence, such as the shift from single-celled to multicellular organisms, or from
asexual to sexual reproduction; proposed by biologists John Maynard Smith and
Eérs Szathmary. See also: symbiogenesis.

Mary’s Room (or Mary the Super-Scientist) A philosophical thought experiment
proposed by Frank Jackson, where Mary, a scientist who knows everything about
the physical science of color but has only ever experienced black and white, sees
color for the first time, raising questions about the nature of subjective experi-
ences or qualia. See also: qualia.

masking (machine learning) An unsupervised training technique in which parts
of the input are hidden and the model's task is to reconstruct these parts as accu-
rately as possible; often used to pretrain large language models, as well as image

and video autoencoders.

---

massively parallel In computer science, the use of a large number of processors
(or computers) to simultaneously perform coordinated computations; such
parallelism is essential for running large neural networks in any reasonable
amount of time, and is ubiquitous in neuroscience and more broadly in biological
computation. See also: computronium, neural cellular automaton.
McCulloch-Pitts neuron A simplified model neuron where each neuron receives
one or more Boolean input signals and produces a Boolean output, thus working
like a logic gate; proposed by neuroscientists Warren McCulloch and Walter Pitts
in 1943,

mechanical philosophy A worldview originating in the seventeenth century,
most notably advocated by philosopher René Descartes, positing that natural
phenomena, including living bodies, work like machines, with their functions
arising purely from their physical structures and movements, without needing to
invoke unobservable forces or principles.

model A mathematical or computational representation of a system or phenom-
enon that allows its future (or otherwise unobserved) behavior to be predict-

ed. See also: machine learning.

moral agent An individual or entity capable of making ethical decisions and
being held accountable for them. See also: agent, moral patient.

moral patient An individual or entity whose well-being and interests are
considered in ethical decision-making processes and moral actions. See also:
moral agent, patient.

multifractal A mathematical object characterized by a non-integer, or fractal,
dimension that exhibits characteristic structure at every scale; but unlike a
fractal, this structure may vary at different scales.

multilayer perceptron (MLP) A type of artificial neural network first proposed by
psychologist Frank Rosenblatt in the 1950s, consisting of multiple layers of
interconnected neurons where each layer’s output serves as input for the next
layer, enabling the model to learn and represent complex functions and concept-
s. See also: neural network.

multiple realizability A concept in philosophy of mind and computational
neuroscience that posits the same mental state, process, or function can be real-

ized with different physical substrates—such as the human brain, a computer, or

---

an alien physiology—given the correct functional organization.

neural cellular automaton (NCA) A computational model combining cellular
automata, neural nets, and Turing’s concept of morphogenesis where each cell
evaluates a (shared) neural net whose inputs and outputs are local values, akin to
morphogens; the concept was developed by computer scientist Alex Mordvintsev
in 2020. See also: cellular automaton.

neural network (artificial) A massively parallel machine learning model inspired
by the human brain's interconnected neurons; when implemented with multiple
layers, each layer of neurons runs in parallel, but the layers themselves run se-
quentially, with each layer feeding its outputs to the next layer as inputs. See also:
machine learning, neural network (biological).

neural network (biological) Interconnected neurons in an animal's nervous sys-
tem.

NeuroAI A hybrid research field combining neuroscience with artificial intelli-
gence; the field overlaps significantly with computational neuroscience. See also:
computational neuroscience.

one-hot coding A method used in machine learning where a population of
neurons, typically an output layer, is trained to represent a categorical variable
such that only one neuron is “on” (has value near one) while the others are all
“off” (have values near zero); also sometimes referred to as “winner-takes-all.” See
also: lateral inhibition.

one-shot learning The ability to learn a general pattern, category, or other regu-
larity from a single example or exposure. See also: machine learning.

Palomilla A wheeled robot that implemented light-seeking behavior (its name
means “moth” in Spanish), designed by Norbert Wiener in the late 1940s to
demonstrate negative feedback and goal-directed behavior, foundational con-
cepts in cybernetics. See also: cybernetics.

patient (philosophy) An entity that is acted upon or affected by an agent’s
actions. See also: agent, moral patient.

perceptual invariance A concept in cognitive science describing how humans
and other animals (and, by extension, AI models) recognize objects, sounds, or
other stimuli as being the same across different viewing angles, distances, light-

ing conditions, or other potentially complicating factors, implying powerful

---

computational processing capabilities.

phase transition A sudden change in a system's properties, such as density,
magnetization, or conductance, often as a result of changing external conditions,
like temperature or pressure; the transition from water to ice is a common exam-
ple.

philosophical zombie A hypothetical being that is behaviorally indistinguishable
from a human, but lacks conscious experience; popularized by philosopher David
Chalmers to question whether consciousness can be reduced to purely physical
processes. See also: qualia.

Piraha A people of the Amazonas state of Brazil known for the unique character-
istics of their language, including the absence of numbers, absence of recursion,
and possibly the smallest phoneme inventory in any human language; studied
extensively by linguist and former missionary Daniel Everett. See also: recursion
(linguistics).

predictive brain hypothesis A neuroscientific theory suggesting that the brain is
a predictor that constantly models the future based on past experiences; these
models are continuously tested against sensory information to minimize predic-
tion errors.

pretraining An approach to machine learning in which a model is initially trained
on a large, general dataset (usually using unsupervised learning) before being
fine-tuned on a smaller, specific dataset. See also: machine learning.

psychic pneuma According to ancient Greek philosophers and René Descartes, an
elusive substance believed to be the vital force or breath of life that penetrates and
harnesses inanimate matter, often associated with the human soul and intellec-
t. See also: dualism, élan vital.

psychon A hypothetical unit of cognitive activity or fundamental element of
thought; hypothesized by Warren McCulloch and Walter Pitts in 1943 to consist
of a single logical proposition, i.e., one bit of information. See also: logical proposi-
tion.

purposive (or purposeful) Functions or behaviors that are goal-directed, and
therefore suggestive of agency or intentionality. See also: backward causality, en-
tensional.

qualia The subjective or qualitative properties of experiences, such as the redness

---

of a rose or the taste of sugar, which philosopher Frank Jackson and others have
argued cannot be fully understood through scientific or computational analysis;
hence the supposed “hard problem” in consciousness studies.

recursion (computing) A method in computing where a function, in order to
accomplish a task, calls itself with modified inputs, enabling problems to be
broken down into smaller, similar problems until reaching a base case that can be
solved directly; frequently used in algorithms and data structures. See also: com-
position.

recursion (linguistics) A linguistic phenomenon in which a grammatical rule
can be applied to the result of its own application, allowing for constructions such
as nested clauses and indefinitely extended sentences; popularized by linguist
Noam Chomsky in his theory of generative grammar. See also: Piraha.
reinforcement learning (RL) A machine learning method where an AI system
learns to make decisions by receiving rewards or penalties for its actions; often
used in coaching robots or recommender systems, and inspired originally by
Pavlovian or reward-based learning in lab animals. See also: machine learning.
relational quantum mechanics (RQM) An interpretation of quantum mechanics
proposed by physicist Carlo Rovelli in 1996 suggesting that the state of aquantum
system is relative to the observer, meaning that different observers can have
different descriptions of the same system, and these descriptions are valid within
their own frames of reference; according to ROM, there is no objective, absolute
state of a system independent of all observers.

representation learning An approach to machine learning that allows a system
to automatically discover and learn useful representations from raw data for
improved prediction or inference without explicit feature engineering; funda-
mental to deep learning. See also: machine learning.

reverse Krebs cycle A biochemical process believed to have played a key role in
the origin of life; it performs the reverse operations of the conventional (forward)
Krebs cycle by consuming carbon dioxide and hydrogen to generate organic
compounds, a pathway mainly found today in ancient bacteria and archaea. See
also: Krebs cycle.

RNA world An influential hypothesis suggesting an early stage of evolution when

RNA molecules acted both as genetic material and as catalysts for chemical

---

reactions, potentially predating DNA and proteins.

robustness The ability of a purposive system to keep working in the face of
environmental changes, challenges, disruptions, or uncertainties.

rubber-hand illusion An experimental phenomenon in which a person comes to
perceive a fake rubber hand as part of their own body, typically through having
the real and fake hands simultaneously stroked in the same way, exemplifying the
malleability of body perception; first reported by neuroscientists Matthew
Botvinick and Jonathan Cohen in 1998.

saccade A rapid movement made by the eye when changing its fixation point ina
scene, usually occurring approximately two or three times per second.
Sally-Anne Test A psychological test popularized by psychologists Simon Baron-
Cohen, Alan Leslie, and Uta Frith, used to gauge a subject’s capacity for under-
standing that others have viewpoints and knowledge distinct from their own;
often employed to assess theory of mind deficits, especially in children with
autism. See also: theory of mind.

scaling law The way performance or some other property of a system varies as a
function (typically a power law) of some parameter; for example, metabolic rate
varies as an approximate power law of animal size, and task performance of a
neural network often varies as a power law of the dataset size or model size.
semantics (linguistics) The aspect of language concerning meaning and inter-
pretation, as opposed to properties like grammar or syntax.

sequence modeling A machine learning method in which historical data inputs,
such as time series or text data, are used to predict future data points or complete
missing ones. See also: machine learning.

singularity A hypothesized future point in time when advances in technology
(particularly advancements in artificial intelligence) enter a self-improving
feedback loop so extreme that we are unable to make any prediction about the
course of history beyond this point; popularized by futurist Ray Kurzweil.

social brain hypothesis A hypothesis proposed by British anthropologist Robin
Dunbar asserting that the complex social interactions within primate groups,
including humans, have driven the evolution of larger brains to handle these
complexities. See also: intentionality level, theory of mind.

social intelligence hypothesis A hypothesis proposed by neuroscientist Nicholas

---

Humphrey in 1976 suggesting that the driving force behind the evolution of high
intelligence among hominins is the complexity of social interactions, requiring
skills such as empathy, deception, cooperation, and competition.

sphexish A term coined by cognitive scientist Douglas Hofstadter to describe
seemingly intelligent behavior that is actually mechanistic or deterministic,
based usually on a fixed set of responses or rules; named after the Sphex wasp,
which entomologist Jean-Henri Fabre believed (probably incorrectly) to exhibit
such behavior.

strange loop A concept put forth by cognitive scientist Douglas Hofstadter refer-
ring to a situation in which, whenever one steps upward or downward through
the layers of some hierarchical system, one unexpectedly finds oneself back at the
starting point; Hofstadter believes this kind of self-referentiality is fundamental
to consciousness.

swing (rowing crew) A term borrowed from rowing referring to a state of perfect
harmony and synchronicity in a crew; used metaphorically (or not) to describe
the way multiple predictive agents can coalesce into a single larger agent.
symbiogenesis An evolutionary process proposed by biologist Konstantin
Mereschkowski and further developed by Lynn Margulis, whereby symbiosis can
lead to new life forms through the long-term union of separate but interdepen-
dent organisms. See also: symbiosis.

symbiosis A long-term interaction between two different species (or other enti-
ties) in which both benefit, or one benefits and the other neither benefits nor is
harmed. See also: symbiogenesis.

teleology A philosophical concept suggesting that certain phenomena, systems,
or actions are directed toward ends or goals; while often maligned because it
seems to imply intelligent design, Wiener, physician Arturo Rosenblueth, and
computer engineer Julian Bigelow wrote an essay in 1943 explaining how
negative feedback systems in general have a teleological character, and experi-
ments like bff show that purposive behavior can arise without any intelligent
designer. See also: bff, cybernetics.

Theory of Everything (ToE) A comprehensive theoretical framework that would
include and reconcile all known physical phenomena and laws, including the four

fundamental forces—gravity, electromagnetism, the weak nuclear force, and the

---

strong nuclear force—into a single coherent model of the universe.

theory of mind (ToM) The ability to attribute mental states like beliefs, intents,
desires, emotions, and knowledge to oneself and others and to understand that
others have beliefs, intents, desires, emotions, and knowledge that are different
from one's own. See also: intelligence explosion.

“thing in itself” (Ding an sich) The underlying reality of an object, independent of
any observer's experience or perception of it; philosopher Immanuel Kant coined
the term to make a distinction with the “phenomenon,” the object as it appears to
us.

Three Laws of Robotics A set of rules devised by science-fiction author Isaac
Asimov to govern AI behavior, specifying that a robot 1) may not injure a human
being, 2) must obey orders given by humans except where such orders would
conflict with the first law, and 3) must protect its own existence as long as such
protection does not conflict with the first or second law.

Transformer A popular AI model first introduced in the 2017 paper “Attention Is
All You Need” by Vaswani et al. that uses an “attention” mechanism to weight the
importance of different pieces of input data; Transformers power most modern
LLMs, including Gemini, Claude, and ChatGPT.

umwelt A term introduced by biologist Jakob von Uexkiill referring to the percep-
tual world in which an organism exists and interacts, uniquely filtered and
shaped by the organism's specific sensory, motor, and cognitive capabilities and
experiences.

universals Abstract concepts, properties, or features, such as redness or round-
ness, thought to exist independently of particular instances or objects, a concept
explored extensively by philosophers such as Plato and Aristotle.

utilitarianism A philosophy developed by Jeremy Bentham and John Stuart Mill
that emphasizes the greatest happiness for the greatest number; the ethical value
of an action is determined by its “utility,” or contribution to overall wellbeing,
which is presumed to be representable as a number. See also: utility.

utility A concept central to economics and game theory representing the total
satisfaction or fulfilment that a person derives from consuming a good or service;
utilitarian philosophers such as Jeremy Bentham posit that actions should be

evaluated by their contribution to overall utility, or “the greatest good for the

---

greatest number.” See also: utilitarianism.

vitalism The belief that life and its phenomena are due to a vital principle distinct
from physical or chemical forces; no longer considered reputable by most schol-
ars, though there are a few modern proponents, including philosopher Jane
Bennett. See also: animism, élan vital.

von Neumann architecture A computer system architecture proposed by mathe-
matician and physicist John von Neumann that still forms the basis of most
modern computers, where stored-program memory and data share the same
memory space, and this memory is connected to a central processing unit bya
bus.

von Neumann replicator A theoretical self-replicating machine proposed by
mathematician and physicist John von Neumann that can replicate itself using
raw materials from its environment, thereby exhibiting exponential population
growth given a suitable medium and an energy source.

Wiener sausage (statistical physics) A mathematical construct representing the
volume swept out by a ball of fixed radius as it moves along the trajectory ofa
Wiener process (a random walk or Brownian motion) in space; it is used to study
problems involving diffusion and encounter probabilities, and provides insights
into how a random path explores the environment over time.

Word2Vec An unsupervised machine learning technique that creates word
embeddings, which are vector representations of words based on the “company
they keep” (i.e., the statistics of the surrounding words); developed by computer

scientist Tomas Mikolov at Google Research in 2013. See also: embedding.