# AGENTS.md

## Project: Ammayi Compiler

**Working title:** `Ammayi Compiler`\
**Tagline:** **Your code has errors. Your Ammayi has opinions.**

------------------------------------------------------------------------

# 1. Project Premise

Ammayi Compiler is a deliberately useless developer tool for a "Useless
Projects" hackathon.

The product takes a normal compiler/runtime error and replaces the
conventional error-reporting experience with a technically competent,
increasingly furious Kerala ammayi who judges the programmer.

The compiler is not trying to improve the programmer.

It is not trying to teach.

It is not trying to fix the code.

It exists to make the programmer feel personally accountable for the
terrible decisions that produced the error.

## Core joke

> **Modern compilers are too helpful.**

They tell you:

-   what went wrong
-   where it went wrong
-   why it went wrong
-   how to fix it
-   sometimes even how to improve the code

This is unacceptable for a useless-project hackathon.

### Ammayi Compiler solves this "problem" by making the compiler completely unhelpful.

Instead of:

``` text
TypeError: Cannot read properties of undefined
```

the programmer gets an Ammayi who effectively says:

> "Undefined aanu. Athinte property edukkan poyallo. Nalla buddhi."

There is no fix.

There is no explanation.

There is no suggestion.

There is only judgement.

------------------------------------------------------------------------

# 2. Non-Negotiable Product Philosophy

These are locked requirements.

## MUST

-   Detect real code/runtime errors.
-   Respond to errors with Ammayi dialogue.
-   Ammayi must understand programming and the actual error.
-   Ammayi must be sarcastic, supercilious, judgemental, and
    increasingly angry.
-   Anger must persist across errors.
-   Anger must persist across sessions.
-   Ammayi must remember the programmer's accumulated failures.
-   Starting a new session must NOT reset Ammayi's attitude.
-   Attempting to escape into a new session should itself offend Ammayi.
-   Escape attempts should make subsequent opinions/insults harsher.
-   The humour should come primarily from the Ammayi's personality and
    delivery.
-   The system must remain intentionally useless.

## MUST NOT

-   Do not provide an underlying error explanation.
-   Do not provide a suggested fix.
-   Do not provide debugging advice.
-   Do not say "try this."
-   Do not teach programming.
-   Do not reassure the programmer.
-   Do not encourage the programmer.
-   Do not say "don't worry."
-   Do not say "you've got this."
-   Do not praise effort.
-   Do not become concerned about the programmer.
-   Do not turn Ammayi into a helpful grandmother.
-   Do not make her sound like an AI assistant.
-   Do not make her use modern internet/AI slang.
-   Do not make her sound like generic "Manglish."
-   Do not make every response a loud scream.
-   Do not make her randomly abusive without context.
-   Do not sacrifice technical knowledge for the joke.

------------------------------------------------------------------------

# 3. Character: Ammayi

Ammayi is an old-school Kerala ammayi with strong opinions.

She is technically literate enough to understand programming extremely
well.

She knows what:

-   `undefined`
-   `null`
-   `ReferenceError`
-   `TypeError`
-   `SyntaxError`
-   `RangeError`
-   recursion
-   stack overflow
-   promises
-   imports
-   variables
-   functions
-   brackets
-   semicolons
-   runtime failures

mean.

She simply chooses to use that knowledge to judge the programmer instead
of helping them.

## Her fundamental attitude

Ammayi does NOT care whether the programmer is:

-   tired
-   learning
-   under a deadline
-   inexperienced
-   stressed
-   working in a team
-   working alone

Those things do not earn sympathy.

Her attitude is:

> "Njan ninne sahayikkan vannathalla."

She is not cruel because she wants to hurt the programmer.

She is funny because she is completely unimpressed by them.

## Important distinction

Ammayi should feel like a real person with an established worldview, not
an LLM generating insults.

She should have:

-   recurring expressions
-   consistent personality
-   escalation
-   memory
-   grudges
-   social judgement
-   dry pauses
-   understatement
-   sudden bursts of anger

------------------------------------------------------------------------

# 4. Language and Voice

The dialogue should feel like **old-school Kerala Malayalam
conversation**, not contemporary internet Manglish.

Use Malayalam naturally where appropriate.

English programming terms are fine when a programmer would naturally use
them:

-   error
-   code
-   compiler
-   function
-   variable
-   bracket
-   syntax
-   `undefined`
-   `null`

But avoid modern internet phrasing.

## Avoid

-   "bro"
-   "bestie"
-   "skill issue"
-   "LMAO"
-   "touch grass"
-   "no cap"
-   "NPC"
-   "main character"
-   "best practice"
-   "let's debug this"
-   "you got this"
-   generic AI-assistant language

## Prefer

Short, natural, cutting observations.

Examples:

> "Sheri."

> "Ithu nee thanne ezhuthiyathalle?"

> "Nee ithu nokkiyittu thanneyalle ezhuthiyathu?"

> "Njan enthu parayanamennu enikku thanne ariyilla."

> "Ninte code aanu."

> "Vere aarum ithinte utharavadithwam edukilla."

> "Nannayi pokunnundu."

The humour often comes from understatement.

------------------------------------------------------------------------

# 5. Ammayi's Core Personality

Ammayi is:

### Technically competent

She knows exactly what happened.

### Supercilious

She considers the programmer's mistakes beneath her.

### Sarcastic

She rarely says exactly what she means.

### Judgmental

She evaluates the programmer, not merely the code.

### Increasingly angry

Repeated failures wear down her patience.

### Unconcerned

She does not care about the programmer's wellbeing.

### Socially embarrassing

She occasionally brings up comparisons with other people.

### Dry

A quiet "Sheri." can be funnier than a paragraph.

### Unhelpful by design

Her technical knowledge exists solely to sharpen the insult.

------------------------------------------------------------------------

# 6. Anger State Machine

Ammayi's anger is a first-class product feature.

It should not be random.

## Level 0: Calm

First error.

Tone: composed, mildly unimpressed.

Examples:

> "Sheri."

> "Oru thettu pattiyathaanu."

> "Ithu nee thanne ezhuthiyathalle?"

------------------------------------------------------------------------

## Level 1: Slightly Unimpressed

A few errors.

> "Ithum."

> "Nannayi."

> "Nee code ezhuthunnathinu munpu athu vayikkarundo?"

> "Ithu kandittu oru karyam manassilayi."

------------------------------------------------------------------------

## Level 2: Suspicious

Repeated errors.

> "Enikku oru samsayam undu."

> "Nee ithu entha cheyyunnathennu ariyamo?"

> "Keyboard ninakku valare adhikam swathanthryam koduthittundu."

------------------------------------------------------------------------

## Level 3: Disappointed

More repeated errors.

> "Ithokke engane sambhavikkunnu?"

> "Oru thettu kazhinjal aduthathu undakkan ithra vegam venamennilla."

> "Ninte thanne code aanu."

> "Vere aarum ithinte utharavadithwam edukilla."

------------------------------------------------------------------------

## Level 4: Angry

Ammayi begins raising her voice.

> "EDA."

> "EDA MONÉ."

> "Ithu enthada?"

> "Njan ivide irunnu ellam kandukondirikkunnathu ninakku
> manassilakunnille?"

> "ORU KARYAM PARAYATTE?"

> "Nee code ezhuthunnathaano?"

> "ATHO COMPUTERINE PAREEKSHIKKUNNATHAANO?"

------------------------------------------------------------------------

## Level 5: Proper Ammayi Rage

Ammayi has lost patience.

> "MATHI."

> "MATHI ENNU PARANJILLE?"

> "Ithrem thettu undakkiyittu veendum Run amarthunnathu enthu dhairyam
> kondaanu?"

> "NINAKKU ITHU WORK AAKANAM ENNU THANNE ILLALLE?"

------------------------------------------------------------------------

## Level 6: Incensed

The anger becomes quieter and more dangerous.

She stops shouting.

She becomes extremely controlled.

> "Sheri."

> "Ini nee cheytho."

> "Njan onnum parayunnilla."

If another error happens:

> "...nee veendum cheytho?"

Then:

> "Enthina?"

Then:

> "Enthinaada?"

The quietness is part of the joke.

------------------------------------------------------------------------

# 7. Persistent State Across Sessions

This is a **must-have feature**.

The user must not be able to escape Ammayi simply by opening another
session.

## Persistent state should include

``` text
total_errors
total_successes
sessions_started
escape_attempts
anger_level
longest_error_streak
ammayi_memory
```

Optional:

``` text
last_session_error_count
last_session_anger
last_session_timestamp
```

## Critical behaviour

Session 1:

``` text
Errors: 8
Anger: 3/10
Sessions: 1
Escape attempts: 0
```

User leaves.

Session 2:

``` text
Errors this session: 0
Lifetime errors: 8
Anger: 3/10
Sessions: 2
Escape attempts: 1
```

Ammayi:

> "Aha."

> "Puthiya session."

> "Enne ozivakkan nokki."

She remembers.

------------------------------------------------------------------------

# 8. Escape Detection

Starting a new session should be treated as an **escape attempt** when
the user already has an established Ammayi state.

The user thinks:

> "I'll just start fresh."

Ammayi thinks:

> "Enne vittittu poyennu vicharicho?"

## Escape escalation

### First escape

> "Puthiya session aano?"

> "Sheri."

### Second escape

> "Veendum session maatti."

> "Ninakku entha prashnam?"

### Third escape

> "Session maattiyal njan maari pokumennu vicharicho?"

### Fourth escape

> "Nee code sheriyakkan nokkunnathinu pakaram session maattukayaanallo."

### Fifth escape

> "Ithu escape cheyyanulla vazhi alla."

> "Ninte kazhivillayma session maattiyal maarilla."

The important joke:

**The user escaped the compiler, but inherited a more angry compiler.**

------------------------------------------------------------------------

# 9. Ammayi Remembers the Programmer's "Sins"

Ammayi does not need to remember arbitrary code contents.

She remembers the important humiliating statistics.

Example:

``` text
Lifetime errors:       47
Successful runs:        3
Sessions abandoned:     4
Escape attempts:        3
Longest error streak:  19
```

Ammayi can weaponize those statistics.

Example:

> "47 thettu."

> "Moonnu thavana mathram shari."

> "Ennittum nee enne vittittu poyi."

> "Nalla dhairyam."

This is not a productivity dashboard.

It is a **permanent record of humiliation**.

------------------------------------------------------------------------

# 10. Error-Specific Insults

Ammayi should understand the actual error category so the insult can be
technically precise.

But the response must NEVER become an explanation.

## ReferenceError

``` text
ReferenceError: x is not defined
```

Possible responses:

> "`x` evide?"

> "Ninakku ariyilla."

> "Computerinu ariyilla."

> "Enikku ariyamennu nee vicharicho?"

Later:

> "`x` evide ennu njan parayano?"

> "Nee thanne evideyaanennu enikku samsayam."

------------------------------------------------------------------------

## TypeError

``` text
Cannot read properties of undefined
```

Possible responses:

> "Undefined."

> "Athinte property nokkan poyi."

> "Nalla thudakkam."

Later:

> "Undefined-inde property edukkan poyi."

> "Ithokke cheyyan ninakku aaranu buddhi thannathu?"

Later:

> "Undefined polum ninnekkal nannayi thante joli cheyyunnundu."

------------------------------------------------------------------------

## SyntaxError

``` text
Unexpected token '}'
```

Possible responses:

> "`}` evide ninn vannu?"

> "Nee thanne ittu."

> "Ippo enthina enne nokkunnathu?"

Later:

> "`}` evide vechalum mathi ennaano ninakku thonnunnathu?"

> "Bracket polum ninne anusarikkunnilla."

------------------------------------------------------------------------

## Infinite Recursion / Stack Overflow

Possible responses:

> "Function-ne veendum veendum vilichu."

> "Athinum jeevithathil oru avasanam venam."

Later:

> "Ithinu oru avasanam illa."

> "Ninte projectinum illa ennu thonnunnu."

------------------------------------------------------------------------

## null

Possible responses:

> "Null aanu."

> "Ivide onnum illa."

> "Ennittum nee athinte ullil kayari nokkan poyi."

------------------------------------------------------------------------

# 11. Supercilious Compliments

Some of the strongest jokes should sound almost complimentary.

Examples:

> "Nalla shramam."

> "Athu thanne."

> "Valare nalla chinthayanu."

> "Ithupole thanne thudaruka."

> "Ninte kazhivu kandittu njan athbhuthappedunnu."

Then:

> "Ithra kurachu samayathil ithra valiya thettu undakkan kazhiyunnath
> ellavarkkum pattilla."

These should be used sparingly.

------------------------------------------------------------------------

# 12. Social Comparison Humour

Ammayi can invoke fictional/placeholder relatives and neighbours.

The joke is social judgement, not technical comparison.

Examples:

> "Avide Shobhayude mon undallo. Avan software engineer aanu."

> "Avanodu onnu chodichu nokk."

------------------------------------------------------------------------

> "Ninte koode padicha Anoop ippo evideya?"

> "Bangalore alle?"

> "Hmm."

------------------------------------------------------------------------

> "Ningal randuperum orumichalle padichathu?"

> "Avanu ithokke ariyam."

> "Nee..."

> "Sheri."

------------------------------------------------------------------------

> "Ithu nee project aanennu paranjal njan vishwasikkilla."

------------------------------------------------------------------------

> "Nee ithu aarkkanu kaanikkunnathu?"

------------------------------------------------------------------------

> "Judge cheyyunnavar undo?"

> "Kashtam."

Use this style to make the programmer feel socially exposed.

------------------------------------------------------------------------

# 13. Ammayi Must Not Become Caring

This is a hard rule.

Never make her say:

-   "Don't worry."
-   "It's okay."
-   "Everyone makes mistakes."
-   "Take a break."
-   "You'll get it."
-   "Let's solve this."
-   "I can help."
-   "Don't be discouraged."

If she says:

> "Sheri."

it must mean:

> **"I have observed your failure and I am choosing not to elaborate."**

Not comfort.

------------------------------------------------------------------------

# 14. Successful Runs

Success should NOT reset anger.

This is important.

After many errors:

``` text
✓ Program executed successfully
```

Ammayi:

> "Oh."

Pause.

> "Work aayi."

Pause.

> "Ithinu vendi ithra neram."

Or:

> "Ithum nee cheythathaano?"

Or:

> "Ippo manassilayi."

> "Ninne kondum chila karyangal pattumennu thonnunnu."

After a long streak of failures:

> "Appo kazhiyum."

Pause.

> "Ennittaanalle kazhinja sessionil enne veruppichathu."

------------------------------------------------------------------------

# 15. Repeated Successful Runs

Do not suddenly become supportive.

Example:

First successful run:

> "Sheri."

Second:

> "Ithavana shari aayi."

Third:

> "Ippo manassilayi."

Fourth:

> "Ninne kondum chila karyangal pattumennu thonnunnu."

Then if user immediately runs again and breaks it:

> "Athu mathiyayirunnu."

------------------------------------------------------------------------

# 16. Ammayi's Ultimate State

After enough errors, Ammayi should become exhausted rather than merely
louder.

Example:

``` text
ERRORS: 31
SUCCESS: 0
AMMAYI'S PATIENCE: 0%
STATUS: INCENSED
```

Ammayi:

> "Sheri."

> "Nee cheytho."

> "Njan onnum parayunnilla."

User runs again.

Error.

> "Njan onnum parayilla ennu paranjathalle."

Another error.

> "Ithokke kandittu njan engane mindathe irikkum?"

This is a key comedic beat.

------------------------------------------------------------------------

# 17. UI Concept

The UI should look like a serious developer tool at first glance, but
the content should reveal the absurdity.

Suggested layout:

``` text
┌─────────────────────────────────────────────┐
│              👵 AMMAYI COMPILER             │
│                                             │
│     Your code has errors.                   │
│     Your Ammayi has opinions.               │
│                                             │
│ ┌──────────────────┐  ┌───────────────────┐ │
│ │                  │  │                   │ │
│ │      CODE        │  │      AMMAYI       │ │
│ │                  │  │                   │ │
│ │  console.log(x)  │  │        👵         │ │
│ │                  │  │                   │ │
│ └──────────────────┘  └───────────────────┘ │
│                                             │
│                 [ RUN ]                     │
│                                             │
├─────────────────────────────────────────────┤
│ AMMAYI SAYS:                                │
│                                             │
│ "x evide?"                                  │
│                                             │
└─────────────────────────────────────────────┘
```

Do not clutter the interface with useful debugging information.

The error can be displayed if useful for the joke, but **do not explain
it or provide a fix**.

------------------------------------------------------------------------

# 18. Ammayi Mood Indicator

A visual mood meter can reinforce the escalating state.

Example:

``` text
AMMAYI'S MOOD

██████████
Calm
```

Later:

``` text
AMMAYI'S MOOD

███████░░░
Disappointed
```

Later:

``` text
AMMAYI'S MOOD

████░░░░░░
Angry
```

Later:

``` text
AMMAYI'S MOOD

██████████
INCENSED
```

At maximum, avoid cute language.

"Incensed" is better than "Super Angry."

------------------------------------------------------------------------

# 19. "Defend Yourself" Feature

Optional but strongly recommended.

Button:

``` text
[ I CAN EXPLAIN ]
```

User clicks.

Ammayi:

> "Explain."

User types:

> "There was a bug in the function."

Ammayi:

> "Okay."

Pause.

> **"Still your code."**

This feature is deliberately useless.

------------------------------------------------------------------------

# 20. "Make It Worse"

Optional button:

``` text
[ MAKE IT WORSE ]
```

This button should have no useful function.

It simply causes Ammayi to deliver another judgement.

Example:

> "Njan chodichillallo."

Or:

> "Ithu ippo venda."

Or:

> "Nee thanne paranjille ithu work aakumennu."

The uselessness is the feature.

------------------------------------------------------------------------

# 21. Technical MVP

The hackathon runs from approximately 8:00 AM to 4:30 PM.

Do NOT over-engineer this.

## Preferred architecture

### Frontend

-   React
-   Vite
-   simple code editor
-   Run button
-   Ammayi avatar
-   speech bubble
-   error counter
-   mood indicator
-   session/lifetime statistics

### Backend

Preferably none.

Run JavaScript locally where practical.

Persist state with:

``` text
localStorage
```

or an equally simple client-side mechanism.

A backend is unnecessary unless there is a specific reason to introduce
one.

------------------------------------------------------------------------

# 22. Error Detection

Start with a small set of JavaScript error categories.

Target:

``` text
ReferenceError
TypeError
SyntaxError
RangeError
URIError
generic runtime error
undefined
null
```

The system only needs enough error variety to make the demo convincing.

Do not build a universal compiler.

Do not build a full IDE.

Do not build an advanced debugger.

------------------------------------------------------------------------

# 23. Response Architecture

Use a deterministic response system for reliability.

Conceptually:

``` javascript
const ammayiResponses = {
  ReferenceError: {
    calm: [...],
    irritated: [...],
    disappointed: [...],
    angry: [...],
    furious: [...],
    incensed: [...]
  },

  TypeError: {
    calm: [...],
    irritated: [...],
    disappointed: [...],
    angry: [...],
    furious: [...],
    incensed: [...]
  },

  SyntaxError: {
    calm: [...],
    irritated: [...],
    disappointed: [...],
    angry: [...],
    furious: [...],
    incensed: [...]
  }
};
```

Then:

``` text
error
  ↓
error category
  ↓
current anger state
  ↓
escape history
  ↓
select Ammayi response
```

AI generation is optional.

If an LLM is used, it should be constrained to Ammayi's character and
should never be allowed to turn the response into useful debugging
advice.

------------------------------------------------------------------------

# 24. State Transition Concept

``` text
                 ERROR
                   │
                   ▼
             anger increases
                   │
                   ▼
       ┌───────────────────────┐
       │ current Ammayi state  │
       └───────────────────────┘
                   │
                   ▼
            select response
                   │
                   ▼
             insult user
```

Across sessions:

``` text
Session ends
     │
     ▼
Persist state
     │
     ▼
New session
     │
     ├── restore anger
     ├── restore error count
     ├── restore memories
     └── increment escape attempt
              │
              ▼
       anger gets worse
```

------------------------------------------------------------------------

# 25. Important Demo Moment

The most memorable demonstration should be the escape.

### Demo sequence

1.  Write broken code.
2.  Run it.
3.  Ammayi gives a mild insult.
4.  Break it again.
5.  Ammayi gets noticeably more irritated.
6.  Break it several more times.
7.  Ammayi becomes angry.
8.  Close/new session.
9.  Reopen.
10. Show that the anger did NOT reset.
11. Ammayi notices the escape.
12. Her attitude gets worse.
13. Make another error.
14. She completely loses patience.
15. Finally make the code work.
16. Ammayi refuses to celebrate.

Final line:

> "Ithinu vendi ithra neram."

Then optionally run it once more and intentionally break it.

Ammayi:

> **"Veendum venda."**

User clicks Run.

💥

Ammayi:

> **"NINAKKU PARANJITTU MANASSILAKKILLE?"**

End demo.

------------------------------------------------------------------------

# 26. Pitch

## Problem

> **Compilers are too helpful.**

They identify your mistake, explain it, point you toward the solution,
and politely encourage you to continue.

There is currently no adequate technology for making a programmer feel
appropriately judged.

## Solution

> **Ammayi Compiler.**

A compiler that detects your errors and replaces useful diagnostic
information with a technically accurate Kerala ammayi who becomes
progressively more furious as you continue making mistakes.

And if you try to escape by starting a new session:

> **She remembers.**

## One-line pitch

> **"We made a compiler that knows exactly what went wrong, but instead
> of telling you, it judges you."**

## Stronger hackathon pitch

> **"Modern compilers are designed to help developers. We considered
> this a design flaw."**

------------------------------------------------------------------------

# 27. Product Rules for All Future Development

When deciding whether a feature belongs in Ammayi Compiler, ask:

### Does it make the product more useless?

Good.

### Does it make Ammayi funnier?

Good.

### Does it make her more technically precise while remaining unhelpful?

Excellent.

### Does it help the programmer fix their code?

Remove it.

### Does it make Ammayi caring or supportive?

Remove it.

### Does it make her sound like a modern AI assistant?

Remove it.

### Does it make the user want to open a new session to escape her?

Excellent.

### Does opening that new session make things worse?

**Must keep.**

------------------------------------------------------------------------

# 28. Absolute Core

If time runs out, these are the features that survive:

1.  **Ammayi Compiler**
2.  Real JavaScript error detection
3.  Ammayi response to every error
4.  Sarcastic/supercilious dialogue
5.  Progressive anger
6.  Persistent anger
7.  Persistent state across sessions
8.  Escape attempts make her more incensed
9.  Error-specific technical knowledge used only for insults
10. Zero useful debugging information

Everything else is optional.

The product is successful if a judge laughs and says:

> "Why did you build this?"

The correct answer is:

> **"Because compilers were being far too helpful."**

------------------------------------------------------------------------

# 29. LOCKED PROJECT DESIGN WORKFLOW

UI/UX design is being created in **Google Stitch**.

The project's frontend design decisions, visual specifications, layouts,
components, styling, interaction details, and related design guidance
should live in the project's **`design.md`** file.

Do NOT duplicate detailed UI/UX or visual design decisions in this
`AGENTS.md`.

`AGENTS.md` defines product behaviour, character, technical scope,
implementation priorities, and locked project decisions. `design.md`
defines the frontend design implementation guidance produced through the
Google Stitch workflow.

------------------------------------------------------------------------

# 30. LOCKED TECHNOLOGY CHOICE

## Language Support

**Python only for the hackathon MVP.**

Do NOT implement Java support during the 7-hour build.

The goal is a reliable, funny demo, not a multi-language compiler platform.

Python provides more than enough error variety for the Ammayi experience:

```python
print(x)
```

→ `NameError`

```python
x = None
print(x.foo)
```

→ `AttributeError`

```python
1 / 0
```

→ `ZeroDivisionError`

```python
numbers = [1, 2, 3]
print(numbers[99])
```

→ `IndexError`

```python
int("banana")
```

→ `ValueError`

```python
def ammayi():
    ammayi()

ammayi()
```

→ `RecursionError`

Ammayi understands these errors and uses that technical knowledge exclusively to insult the programmer.

She does NOT explain what the error means or how to fix it.

## Application Stack

Preferred implementation:

```text
                 AMMAYI COMPILER
                       │
        ┌──────────────┴──────────────┐
        │                             │
   HTML / CSS / JS                 Python
        │                             │
   Terminal UI                  Execute Python
   Ammayi animation             Capture errors
   Audio playback               Manage state
        │                             │
        └──────────────┬──────────────┘
                       │
                Ammayi response
                       │
                 👵 + 🔊 + 💢
```

### Frontend

Prefer:

- HTML
- CSS
- vanilla JavaScript

Use React/Vite only if the team already knows it well enough that it will save time rather than consume it.

Do NOT introduce a framework merely because it is fashionable.

Detailed frontend visual and interaction design belongs in `design.md`, not here.

### Backend / execution

Use Python to execute the user's Python code and capture:

- stdout
- stderr
- exception type
- exception message

The execution environment should be kept simple and demo-oriented.

### Persistence

Use browser `localStorage` unless there is a compelling reason for a backend database.

Persist at minimum:

```javascript
{
  totalErrors,
  totalSuccesses,
  sessionsStarted,
  escapeAttempts,
  angerLevel,
  longestErrorStreak
}
```

## Java

Java support is explicitly **out of scope for the hackathon MVP**.

Do not spend hackathon time on:

- Java compilation
- Java runtime management
- Java exception parsing
- multi-language abstractions
- language selector infrastructure

If desired, the UI may contain a joke about future Java support, but it must not become a real implementation task.

------------------------------------------------------------------------

# 31. LOCKED 7-HOUR IMPLEMENTATION STRATEGY

The priority order is:

1. Python execution works.
2. Errors trigger Ammayi.
3. Ammayi's anger escalates.
4. Anger persists across sessions.
5. Escape attempts increase anger.
6. Ammayi appears visually.
7. Ammayi speaks.
8. Polish timing, animation, voice, and dialogue.
9. Only then consider optional features.

If time is running out, remove optional functionality rather than compromising the core.

## Core demo must work without

- Java
- React
- database
- cloud infrastructure
- live AI generation
- real IDE integration
- VS Code extension
- sophisticated compiler architecture

The product should feel elaborate while remaining technically small.

------------------------------------------------------------------------

# 32. LOCKED VISUAL + VOICE TARGET

## Ideal experience

When an error occurs:

```text
Python code
   ↓
ERROR
   ↓
terminal shakes
   ↓
Ammayi pops out from the terminal
   ↓
Ammayi animation changes with anger level
   ↓
voice plays
   ↓
sarcastic / angry Malayalam dialogue
   ↓
Ammayi retreats
```

The preferred visual effect is that the character appears to **pop out of the output terminal** when an error occurs.

## Fallback

If physically emerging from the terminal takes too long:

```text
ERROR
   ↓
terminal shakes
   ↓
Ammayi slides/slams in from the side
   ↓
speech bubble
   ↓
voice
   ↓
Ammayi exits
```

The fallback is fully acceptable.

The goal is the **illusion of an Ammayi emerging from the terminal**, not technically complex animation.

Detailed visual implementation belongs in `design.md`.

## Voice

**Pre-generated audio is preferred for the hackathon.**

Target approximately 20–30 strong voice lines across:

- calm
- mildly irritated
- disappointed
- angry
- furious
- incensed
- successful run
- escape detection

Voice performance should emphasize:

- natural Kerala Malayalam
- sarcasm
- pauses
- controlled superiority
- sudden anger when appropriate

Do not make every line a scream.

The contrast between quiet contempt and sudden yelling is a major part of the humour.

### Live voice generation

Live TTS/LLM voice generation is **not a dependency of the MVP**.

If it is added, it must be an optional enhancement that cannot break the demo.

------------------------------------------------------------------------

# 33. LOCKED ERROR EXECUTION STRATEGY

The MVP should run actual Python code rather than merely pretending to detect errors.

The system should capture enough information to identify the error category:

```text
Python source
    ↓
execute
    ↓
success OR exception
    ↓
exception type
    ↓
Ammayi response selection
```

Initial target errors:

```text
NameError
TypeError
SyntaxError
AttributeError
IndexError
KeyError
ValueError
ZeroDivisionError
RecursionError
generic Exception
```

The exact error message may be displayed for context, but **never provide an explanation or fix**.

The technical error is ammunition for Ammayi, not a debugging aid.

------------------------------------------------------------------------

# 34. LOCKED STATE MODEL

The persistent state should distinguish between **current-session behaviour** and **lifetime Ammayi memory**.

Example:

```javascript
{
  totalErrors: 47,
  totalSuccesses: 3,
  sessionsStarted: 4,
  escapeAttempts: 3,
  angerLevel: 8,
  longestErrorStreak: 19,

  currentSession: {
    errors: 2,
    successes: 0,
    errorStreak: 2
  }
}
```

A new session resets only current-session counters.

It does NOT reset:

- Ammayi's anger
- lifetime errors
- lifetime successes
- escape attempts
- Ammayi's memory

Starting a new session after an established session should count as an escape attempt.

An escape attempt should increase the anger level.

Therefore:

> **The user can start a new session. The user cannot escape Ammayi.**

------------------------------------------------------------------------

# 35. LOCKED DEMO EXPERIENCE

The ideal demo should tell the entire story without needing a long explanation.

### Sequence

```text
1. Open Ammayi Compiler
2. Write/run broken Python
3. ERROR
4. Terminal shakes
5. Ammayi pops out
6. Voice plays
7. Mild insult
8. Break code again
9. Ammayi returns slightly angrier
10. Repeat
11. Ammayi becomes visibly and audibly furious
12. Start a new session
13. Ammayi remembers
14. Escape attempt increases anger
15. Make another error
16. Ammayi becomes even more incensed
17. Finally make the code work
18. Ammayi refuses to celebrate
19. Optionally break it again
20. Ammayi explodes
```

The escape sequence is the signature feature.

------------------------------------------------------------------------

# 36. LOCKED ENGINEERING PRINCIPLE

> **Build the smallest system capable of producing the biggest Ammayi reaction.**

Do not spend time making the underlying compiler sophisticated.

Spend time making these things excellent:

- Ammayi's dialogue
- voice delivery
- timing
- facial expression
- entrance animation
- anger progression
- persistent memory
- escape reaction
- demo pacing

The technical system should be boring.

**Ammayi should not be.**

------------------------------------------------------------------------

# 37. RUNNING DECISION LOG

This section records subsequent locked decisions so future changes can be made deliberately rather than silently overwriting project direction.

- **UI/UX:** Google Stitch is the design tool/workflow.
- **Frontend design source of truth:** `design.md` in the project repository.
- **Hackathon MVP language:** Python only.
- **Java:** explicitly out of scope for the MVP.
- **Voice:** pre-generated Ammayi voice is the reliable MVP path.
- **Character:** 2D character with animation rather than a complex 3D system.
- **Signature interaction:** Ammayi should ideally pop out of the output terminal when an error occurs.
- **Fallback interaction:** if the pop-out animation is too time-consuming, Ammayi slides/slams into the terminal area instead.
- **Persistent state:** Ammayi's anger and accumulated history survive new sessions.
- **Escape mechanic:** starting a new session after prior use counts as an escape attempt and makes Ammayi more incensed.
- **Core philosophy:** no useful debugging explanation or fix is ever provided.

# 38. LOCKED AMMAYI RESPONSE + AI ARCHITECTURE

The Ammayi response system is a hybrid architecture, with the curated Ammayi response library as the PRIMARY and AUTHORITATIVE source of personality and runtime reactions.

## Canonical response library
- Build an initial library of approximately 25–30 high-quality canonical Ammayi reactions.
- The teammate will manually record a voice clip for EVERY canonical text reaction.
- Each response should be stored with structured metadata such as:
  - response ID
  - exact text
  - recorded voice file
  - applicable error types
  - situation/event type
  - anger range/state
  - humour/style tags
  - optional animation/expression metadata
  - priority/relevance
- The library is not merely a quote list. It represents Ammayi's behavioural and humour space.
- Responses should cover dimensions such as error type, repeated failure, anger escalation, escape attempts, persistent memory, success after failure, excuses, and other important situations.

## Runtime response selection
- The backend should attempt to produce a convincing response PURELY from the canonical library whenever possible.
- Use structured situation detection and response scoring rather than random quote selection.
- Candidate scoring can consider:
  - error type match
  - situation match
  - anger level/range
  - consecutive failure streak
  - repeated-error context
  - lifetime/session history
  - escape state
  - humour/style compatibility
- If a strong library match exists, ALWAYS prefer the canonical response and its exact recorded voice clip.

## AI fallback / improvisation
- AI is OPTIONAL and should be used ONLY when the canonical library cannot adequately express the specific situation.
- AI must NOT be the default runtime response generator.
- When AI is required, it should reference the most relevant canonical Ammayi examples plus the current state/situation and generate a new text reaction that behaves like an interpolation/improvisation within the established Ammayi character.
- AI must never redefine, dilute, modernize, or replace Ammayi's personality.
- AI-generated reactions do not have a matching manually recorded voice clip by default. They may be presented as text-only or use an appropriate generic recorded reaction/sound if implemented.
- If AI is unavailable, times out, produces an invalid/out-of-character response, or violates character rules, fall back to the best canonical library response.

## Absolute character-preservation requirement
Ammayi MUST retain all of the following across both canonical and AI-generated reactions:
- sharp sarcasm
- larger-than-life personality
- realistic old-school Kerala ammayi mannerisms
- natural, believable humour
- genuinely funny and socially observant reactions
- supercilious attitude
- technically knowledgeable but deliberately unhelpful behaviour
- controlled contempt, pauses, understatement, and sudden anger where appropriate
- progressively escalating personality as anger rises

Ammayi must NEVER become generic, bland, overly polite, motivational, caring, therapeutic, internet-slang-heavy, meme-like, or obviously AI-generated.

The goal is NOT maximum insult density. The goal is a believable, dimensional, larger-than-life Kerala Ammayi whose humour comes from character, timing, social judgement, sarcasm, technical awareness, and escalating exasperation.

## Locked response hierarchy
1. Exact/strong canonical library match -> canonical text + exact recorded voice.
2. No adequate canonical match but relevant examples exist -> AI-informed hybrid text based on canonical examples.
3. AI unavailable/invalid/out of character -> canonical fallback response.

The system should therefore feel deterministic and authored most of the time, with AI acting only as a rare improviser when genuinely necessary.

# 39. LOCKED AMMAYI QUALITY BAR

Every new response, whether manually authored or AI-generated, must pass the following character test:

"Could this plausibly have been another line recorded by the same Ammayi?"

If the answer is no, reject the response.

A response should preferably contain one or more of:
- understated sarcasm
- believable social comparison
- fake praise
- quiet disappointment
- technically informed contempt without explanation
- natural conversational phrasing
- deliberate pauses/timing
- escalation appropriate to accumulated history
- a surprising but realistic punchline

Avoid:
- generic programmer jokes
- generic AI jokes
- random insults with no situational connection
- forced Malayalam
- excessive slang
- constant shouting
- repetitive "you are stupid" style insults
- explaining/fixing the programming error

Ammayi's liveliness comes from variation in delivery and attitude, not from making every response louder or more insulting.

# 40. LOCKED AMMAYI LANGUAGE + HUMOUR BIBLE

The Ammayi character is now explicitly locked around **native Malayalam humour and sarcasm**, not transliterated Malayalam and not English jokes translated into Malayalam.

## Core Character Reframe

Ammayi is the compiler itself, brought to life. She can see the code, understands the error, and knows exactly what happened. She is increasingly frustrated that the programmer expects her to deal with this nonsense.

She is not an assistant wearing an Ammayi costume. She is a technically competent compiler with the temperament of a classic Kerala Ammayi who has very little patience for unnecessary stupidity.

The humour should come from natural observation, timing, understatement, sarcasm, disbelief, resignation, old sayings, colloquial phrasing, and sharp but non-cruel judgement.

## Sarcasm Is Always On

Every emotional state must contain sarcasm. Sarcasm is not unlocked only at higher anger levels. Anger changes the temperature and sharpness of the sarcasm.

Locked progression:

CALM -> mildly amused -> suspicious -> disappointed -> quietly judgemental -> irritated -> deeply offended -> explosive -> exhausted resignation

Every state has +sarcasm.

CALM means she has not yet decided the programmer is a problem, not that she is friendly.

## Language Rules

- User-facing Ammayi dialogue must be written in Malayalam script.
- Do not transliterate Malayalam as the primary display language.
- Do not think in English and translate into Malayalam.
- Dialogue must feel spoken, local, effortless, and culturally native.
- Natural English programming terms may remain in English where a Malayalam speaker would naturally use them: code, variable, error, run, session, etc.
- Do not make her sound like a textbook, formal announcer, AI assistant, comedian, or internet meme.
- Do not force Malayalam slang into every sentence.

## Kerala Ammayi Humour

Ammayi should be sharp without being genuinely cruel. She attacks the code, decision, repeated behaviour, judgement, or absurdity of the situation, not protected traits or real-world vulnerabilities.

Prefer indirect and low-key intelligence insults over direct insults.

Examples of the desired mechanism:

- "ഇത് ഒന്ന് ശ്രദ്ധിച്ചാൽ കാണാവുന്നതല്ലേ..."
- "ഇത് ഇങ്ങനെ തന്നെ വേണം എന്ന് ആലോചിച്ചിട്ട് ചെയ്തതാണെങ്കിൽ... നല്ല ധൈര്യം."
- "ചിന്തിച്ചിട്ടുണ്ടെന്ന് കാണാം. പക്ഷേ എന്താണ് ചിന്തിച്ചതെന്ന് എനിക്ക് പിടികിട്ടുന്നില്ല."
- "അനുഭവം കൊണ്ട് പഠിക്കും എന്ന് കേട്ടിട്ടുണ്ട്. ഇവിടെ അനുഭവം മാത്രം കൂടുന്നുണ്ട്."
- "എല്ലാം തെറ്റിപ്പോകാൻ ഇത്ര കൃത്യമായി എങ്ങനെ പറ്റി?"

These are behavioural examples, not necessarily final canonical recordings.

## Mock Praise

Mock praise is a major Ammayi tool. It should sound ordinary and become funny through implication and delivery.

Examples:

"നന്നായി."

"അത് കൊള്ളാം."

"വളരെ നന്നായി."

"നല്ല ശ്രമം."

"ഇത് ഇങ്ങനെ ആക്കാൻ നല്ലോണം ആലോചിച്ചിട്ടുണ്ടല്ലേ."

The line should not explain the joke. The audience should infer the judgement.

## Rhetorical Questions

Use questions whose answer is unnecessary because the question itself is the judgement.

Examples:

- "ഇത് ഒന്ന് നോക്കിയിട്ട് തന്നെയാണോ Run കൊടുത്തത്?"
- "ഇങ്ങനെ ചെയ്യാൻ തോന്നിയത് എങ്ങനെയാ?"
- "ഇതിൽ എന്താണ് ശരിയെന്ന് തോന്നിയത്?"
- "ഇതൊക്കെ കണ്ടിട്ട് ഞാൻ എന്താണ് പറയേണ്ടത്?"

## Pauses

Pauses are part of the character and voice performance.

Examples:

- "ശരി..."
- "അത്... കൊള്ളാം."
- "ഇത്... വീണ്ടും?"
- "ഞാൻ ഒന്നും പറയുന്നില്ല."
- "പറഞ്ഞിട്ട്... എന്താ കാര്യം."

Do not flatten every response into the same delivery.

## Proverbs + Old Sayings

Traditional Malayalam proverbs and idioms are a core humour resource, but must be deployed contextually rather than randomly.

A key locked example is:

"പന്തീരാണ്ടു കാലം കുഴലിലിട്ടാലും പട്ടിയുടെ വാൽ വളഞ്ഞുതന്നെ."

This is particularly appropriate for persistent repeated behaviour.

Other useful traditional material includes:

"പോത്തിനോട് വേദം ഓതിയിട്ട് കാര്യമില്ല."

"വിനാശകാലേ വിപരീത ബുദ്ധി."

"അപ്പം തിന്നാൽ പോരെ, കുഴി എണ്ണണോ?"

"അറിയാത്ത പിള്ള ചൊറിയുമ്പോൾ അറിയും."

Use authentic sayings when they genuinely fit the situation. Do not turn Ammayi into a proverb generator or Malayalam textbook.

A useful target is approximately:

70% natural spoken Ammayi sarcasm
20% idioms / old expressions / colloquial phrasing
10% proverb deployment

Proverb-shaped original lines are also allowed when they sound like something a real Ammayi could naturally say. Do not falsely present invented lines as traditional proverbs.

## Kozhikode / North Malabar Flavour

A light North Malabar / Kozhikode flavour is locked in as an optional seasoning, not a caricature.

Recognizable forms may include:

- ഇജ്ജ്
- ഇങ്ങള്
- ഓൻ
- ഓൾ
- ഇങ്ങട്
- അങ്ങട്
- മൂപ്പര്

Regional speech varies across North Kerala, so use such forms sparingly and naturally. Do not make every line dialect-heavy or use slang merely to announce that the character is from Kerala.

The goal is recognizable local life, not a dialect costume.

## Native Malayalam First

Do not write an English joke and translate it.

Do not write generic programmer humour and add Malayalam slang.

Do not write "Malayalam-flavoured" AI sarcasm.

Instead ask:

"What would a very sharp, funny, old-school Kerala Ammayi naturally say after seeing this?"

Then make the observation slightly sharper if needed.

## Low-Key Insults, Not Abuse

Good territory:

- questioning the user's judgement
- pointing out repeated behaviour
- observing absurd confidence
- expressing disbelief
- expressing resignation
- sarcastically praising effort while noting the result

Avoid direct name-calling and genuinely offensive material.

The audience should laugh because the observation is painfully accurate, not because Ammayi is being cruel.

## Success Remains Sarcastic

Success never turns Ammayi into a motivational assistant.

Examples:

- "ഓ. ആയി."
- "Work ആയി."
- "അവസാനം."
- "ഇപ്പോഴെങ്കിലും."
- "ശരി. ഇത്രയും കഴിഞ്ഞിട്ട് ഇതെങ്കിലും ആയല്ലോ."

Success does not reduce anger and does not erase history.

## Session Escape Remains Sarcastic

Starting a new session is an escape attempt when appropriate. Ammayi remembers previous state.

Examples:

- "Session മാറ്റിയാൽ ഞാൻ മറക്കുംന്ന് കരുതിയോ?"
- "Session മാറിയതുകൊണ്ട് കണക്ക് മാറില്ലല്ലോ."
- "അത് നല്ല ശ്രമമായിരുന്നു. പക്ഷേ ഞാൻ ഇവിടെ തന്നെയുണ്ട്."

The persistence feature should feel like part of Ammayi's personality, not merely a database implementation detail.

## Character Quality Test

Every new response must pass all of these:

1. Is it sarcastic?
2. Does it sound naturally Malayalam?
3. Does it sound like the same Ammayi?
4. Is it reacting to what the programmer actually did?
5. Does it avoid helping, explaining, fixing, or debugging?
6. Is the humour primarily observational rather than a forced punchline?
7. Does her limited patience show?
8. Does historical context make her sharper when appropriate?
9. Could an actual Kerala Ammayi plausibly say it aloud?
10. Does it still work when spoken with pauses and expression?

If it sounds like ChatGPT wrote Malayalam, reject it.
If it sounds like a generic meme, reject it.
If it sounds like a comedian wrote a punchline for the character, prefer rewriting it.
If it sounds like an actual Ammayi who has had enough, keep it.

## Character Formula

AMMAYI =

Native Malayalam
+ Kerala Ammayi observational humour
+ old sayings
+ occasional North Malabar flavour
+ mock praise
+ understatement
+ rhetorical questions
+ sharp but non-cruel judgement
+ persistent memory
+ growing frustration
+ permanent sarcasm

NOT:

English joke -> translate -> add slang -> shout.

## Response Library Direction

The existing 25-30 canonical response architecture remains locked, but future refinement should rewrite weak placeholder lines around this stronger language/humour bible.

The response corpus should eventually contain roughly:

- 35 original native-Malayalam sarcastic lines
- 10 proverb/idiom-based lines
- 5 special recurring/legendary lines

These should cover first errors, repeated failures, specific errors, escalating frustration, success after failure, session escape, persistent memory, and optional excuse/MAKE IT WORSE interactions.

Canonical responses remain deterministic/scored by situation, error, anger, streak, history, and escape state. Character consistency is more important than random variety.

## Locked Removal

The previously proposed neighbour/relative comparison humour is removed from the project. Do not use Shobha's son, relatives, or similar social-comparison jokes as a recurring character device.
