# 🚀 Deep Execution Roadmap: Fluent Python Control Flow (Part IV) - Conservative Hourly Chunks

**Target Book:** Fluent Python, 2nd Edition by Luciano Ramalho
**Part IV Focus:** Control Flow (Chapters 17-21)
**Estimated Total Time:** Approx. 57-60 focused hours (adjust based on individual pace)

**Overarching Principles (Your Daily Mantra):**

1.  **"Who Controls the Flow?":** For every construct (loops, generators, `with`, `async`), be able to trace the transfer of execution control. Diagram it if necessary.
2.  **Master Transitions:** Understand the shift from eager to lazy (e.g., `for` loop to generator), sync to async (`yield` to `await`), imperative to declarative (`if/else` to `match`).
3.  **Build, Break, Debug, Document:** Every concept requires code. Every piece of code must be intentionally broken. Every break must be debugged. Every insight must be documented (even brief notes).
4.  **Explain the "Why Not":** For every pattern or feature, understand why alternative approaches are less suitable for a given problem. This builds design intuition.
5.  **Tooling is Non-Negotiable:** Profilers, debuggers, linters, and structured logging are part of the craft, not afterthoughts.

---

## Phase 0: Foundational Mindset & Setup (Approx. 2 Hours Total)

* **Chunk 0.1 (Focus: 45-60 mins): Deconstructing "Control Flow" & Personal Baseline**
    * **Learn:** Re-read the Introduction to Part IV in "Fluent Python" (p. 591 in 2nd Ed.). Contrast the book's definition/scope of "Control Flow" with traditional `if/else/for/while`.
    * **Task:** Document your *current* understanding of these terms from the book's Part IV TOC: Iterators, Generators, Context Managers, `match`, `else` (in loops/try), and the basic idea of Python concurrency (Threads, Processes, Asyncio, GIL). This is your diagnostic.
    * **Deliverable:** Your "current understanding" document. Share with your mentor.
    * **Mentor Action:** Review the baseline. Identify the 2-3 biggest conceptual gaps. This is where you'll apply the most pressure.
* **Chunk 0.2 (Focus: 30-45 mins): Environment Check & Basic Tooling**
    * **Task:** Verify your Python 3.10+ environment. Install: `pytest`, `pytest-asyncio`, `memory_profiler`, `tracemalloc`, `cProfile`, `httpx`, `tqdm`, `curio` (for later comparison).
    * **Task:** Write a "hello world" script. Run it with `python -m cProfile your_script.py`. Understand the basic output. Write a *minimal* script that uses `logging` (basic config, log one message) and another for `memory_profiler` (profile a function creating a small list).
    * **Deliverable:** Environment confirmed. Brief notes on `cProfile`, `logging`, and `memory_profiler` basic usage.

---

## Phase 1: Iteration Mastery & Contextual Power (Chapters 17 & 18) (Target: ~20 Chunks)

**Core Objective:** Master Python's iteration model not just as a way to loop, but as a foundation for data pipelines, lazy evaluation, and understanding how Python *actually* moves through your code.

### Chapter 17: Iterators, Generators, and Classic Coroutines

* **Chunk 1.1 (1 hr): The `for` Loop Deconstructed: The Iterator Protocol**
    * **Learn (FP Ch 17):** "A Sequence of Words," "Why Sequences Are Iterable: The iter Function."
    * **Task:** Manually iterate over `s = 'XYZ'` using `it = iter(s)` and a `while True` loop with `try/except StopIteration` around `val = next(it)`.
    * **Deliverable:** Working manual loop. Diagram the calls: `iter()` -> `s.__iter__()` -> `iterator_obj`, then `next(it)` -> `iterator_obj.__next__()`.
    * **Break-It:** What happens if `s` is empty? If `__iter__` is missing? If `__next__` doesn't raise `StopIteration`?
* **Chunk 1.2 (1 hr): Classic Iterator: `Sentence` & `SentenceIterator` - Part 1**
    * **Learn (FP Ch 17):** "Sentence Take #2: A Classic Iterator" (Ex 17-4). Focus on the `Sentence` class first.
    * **Project:** Implement *only* the `Sentence` class as in Ex 17-4. Its `__iter__` should `return SentenceIterator(self.words)`.
    * **Deliverable:** `Sentence` class code.
* **Chunk 1.3 (1 hr): Classic Iterator: `Sentence` & `SentenceIterator` - Part 2**
    * **Project:** Implement the `SentenceIterator` class (Ex 17-4) with `__init__`, `__next__`, and `__iter__` returning `self`. Test full iteration.
    * **Deliverable:** Complete, working `Sentence` and `SentenceIterator`.
    * **Break-It:** Modify `SentenceIterator.__iter__` to return a *new* `SentenceIterator(self.words)`. What happens? Why is returning `self` the correct iterator pattern?
* **Chunk 1.4 (1 hr): The Anti-Pattern: Iterable as Its Own Iterator**
    * **Learn (FP Ch 17):** "Don’t Make the Iterable an Iterator for Itself."
    * **Project:** Modify your `Sentence` class to include the `__next__` method directly and have `__iter__` return `self`.
    * **Task:** Try iterating over a `Sentence` instance *twice* in a row (two separate `for` loops). What happens?
    * **Deliverable:** Modified `Sentence` and a clear explanation of why this shared state is problematic for reusable iteration.
* **Chunk 1.5 (1 hr): Generators: `yield` and the Compiler's Magic**
    * **Learn (FP Ch 17):** "Sentence Take #3: A Generator Function" (Ex 17-5), "How a Generator Works" (Ex 17-6, 17-7).
    * **Project:** Implement `gen_123()` (Ex 17-6). Call it: what does it return? Call `next()` on the result. Refactor your `Sentence`'s `__iter__` method to be a generator function (like Ex 17-5).
    * **Deliverable:** Refactored `Sentence`. Notes: "How is a generator function call different from a regular function call?"
* **Chunk 1.6 (1 hr): Tracing Generator Execution**
    * **Learn (FP Ch 17):** Study `gen_AB()` (Ex 17-7) and its output meticulously.
    * **Task:** On paper or in comments, trace the exact sequence of `print`s and `yield`s for `for c in gen_AB(): print('-->', c)`. Where does control flow suspend and resume?
    * **Deliverable:** Your execution trace.
* **Chunk 1.7 (1 hr): Lazy Evaluation in Practice: `re.finditer`**
    * **Learn (FP Ch 17):** "Lazy Sentences," "Sentence Take #4: Lazy Generator" (Ex 17-8).
    * **Project:** Implement this "lazy" `Sentence`. If `self.text` was 10GB, why is this version superior to Ex 17-1 (which used `re.findall`)?
    * **Deliverable:** Lazy `Sentence`. Written explanation of the memory/performance benefit.
* **Chunk 1.8 (1 hr): Generator Expressions: Concise Laziness**
    * **Learn (FP Ch 17):** "Sentence Take #5: Lazy Generator Expression" (Ex 17-9, 17-10).
    * **Project:** Run Ex 17-9 (`res1` listcomp vs. `res2` genexp). Observe when prints from `gen_AB` occur. Refactor your `Sentence.__iter__` to use a generator expression (Ex 17-10).
    * **Deliverable:** Refactored `Sentence`. Notes on the critical difference in execution timing.
* **Chunk 1.9 (1 hr): `itertools` - Filtering Generators**
    * **Learn (FP Ch 17):** "Generator Functions in the Standard Library," Table 17-1 (Filtering), Ex 17-15.
    * **Project:** Take `range(20)`. Use `itertools.filterfalse` for even numbers. Use `itertools.takewhile` for numbers `< 10`. Use `itertools.compress` with a boolean selector.
    * **Deliverable:** Script demonstrating these three.
* **Chunk 1.10 (1 hr): `itertools` - Mapping & Merging**
    * **Learn (FP Ch 17):** Tables 17-2 (Mapping), 17-3 (Merging). Focus on `accumulate`, `starmap`, `chain`, `zip_longest`.
    * **Project:** Use `accumulate` for running totals of `[1,2,3,4,5]`. Use `starmap` with `operator.mul` and `enumerate(['a','b','c'], 1)`. Use `chain` for `'ABC'` and `range(3)`.
    * **Deliverable:** Script demonstrating these.
* **Chunk 1.11 (1 hr): `yield from`: Basic Delegation**
    * **Learn (FP Ch 17):** "Subgenerators with `yield from`" (up to Ex 17-25).
    * **Project:** Implement Ex 17-25 (simple `gen` and `sub_gen`). Explain how `yield from` changes the flow compared to a manual `for item in sub_gen: yield item`.
    * **Deliverable:** Code and explanation.
* **Chunk 1.12 (1 hr): Project - Log Processing Pipeline with `itertools` & `yield from`**
    * **Project:**
        * **Input:** Generator yielding log lines.
        * **Pipeline Steps (all lazy):**
            1.  `filter_errors(lines_gen)`: A generator function using `yield` to only pass lines with "ERROR".
            2.  `extract_messages(error_lines_gen)`: A generator function using `yield` to parse and return only the message part.
            3.  `main_pipeline(filename)`: Uses `yield from filter_errors(stream_log_lines(filename))` and then `yield from extract_messages(...)`.
        * Iterate through `main_pipeline` and print results.
    * **Deliverable:** Log pipeline script.
* **Chunk 1.13 (1 hr): Classic Coroutines - Conceptual Introduction**
    * **Learn (FP Ch 17):** "Classic Coroutines", "Example: Coroutine to Compute a Running Average" (Ex 17-37, 17-38). Focus on `.send()`, priming, and how state is maintained.
    * **Project:** Implement and step through `averager()` (Ex 17-37, 17-38).
    * **Deliverable:** Working `averager()`. Notes: "How is this different from a regular generator used for iteration?"
    * **Mentor Action (Phase 1 Review):** Review iterator/generator distinction, lazy evaluation benefits, `itertools` usage, `yield from` purpose. Provide a complex data transformation task and ask them to solve it with a clean `itertools` and/or generator pipeline. Stress test their Log Processor with diverse bad data. Ensure they understand the *state suspension/resumption* model of generators.

### Chapter 18: `with`, `match`, and `else` Blocks

* **Chunk 1.14 (1 hr): `with` Statement Mechanics: `__enter__` & `__exit__`**
    * **Learn (FP Ch 18):** "Context Managers and `with` Blocks" up to Ex 18-3 (`LookingGlass`).
    * **Project:** Implement `LookingGlass` (Ex 18-3). Add `print` statements at the start/end of `__enter__`, `__exit__`, and inside the `with` block body.
    * **Deliverable:** `LookingGlass` class. Trace output showing execution order.
* **Chunk 1.15 (1 hr): Context Manager - Exception Handling & `__exit__` Parameters**
    * **Learn (FP Ch 18):** How `__exit__` receives `exc_type, exc_value, traceback`. What does returning `True` from `__exit__` signify?
    * **Project:** Extend `LookingGlass` to handle `ZeroDivisionError` (latter part of Ex 18-3). Test: 1. Normal completion. 2. `ZeroDivisionError`. 3. A different error (e.g., `TypeError`).
    * **Deliverable:** Updated `LookingGlass`. Output from tests.
* **Chunk 1.16 (1 hr): `@contextmanager` Decorator**
    * **Learn (FP Ch 18):** "Using `@contextmanager`" (Ex 18-5). How `yield` splits the function.
    * **Project:** Rewrite `LookingGlass` as `looking_glass()` using `@contextmanager`.
    * **Deliverable:** `looking_glass()` function.
* **Chunk 1.17 (1 hr): `@contextmanager` - Exception Handling & Resource Safety**
    * **Learn (FP Ch 18):** Study Ex 18-7 (`mirror_gen_exc.py`). Why is `try/finally` around `yield` critical?
    * **Project:** Implement exception-handling `looking_glass()` (Ex 18-7).
    * **Deliverable:** Robust `looking_glass()`.
    * **Break-It:** Remove `finally`. What happens if an unhandled error occurs in `with`? Is `sys.stdout.write` restored?
    * **Mentor Action:** Ask for a context manager for a mock database connection (open on enter, log commit/rollback based on exception, close on exit).
* **Chunk 1.18 (1 hr): `match/case` - Introduction & Basic Patterns**
    * **Learn (FP Ch 18):** "Pattern Matching in lis.py" (skim Scheme, focus on Python `match/case` syntax for literals, sequences, and basic captures).
    * **Project (Command Parser v1):** Function `parse_cmd(cmd: list)` (e.g., `["DRAW", "CIRCLE", 10, 20, 5]` or `["COLOR", "RED"]`). Use `match/case` to print command type and basic args.
    * **Deliverable:** `parse_cmd` function.
* **Chunk 1.19 (1 hr): `match/case` - Mapping Patterns, Guards, Wildcard `_`**
    * **Learn (FP Ch 18):** More `match/case`. Focus on dict patterns, `if` guards, `_`.
    * **Project (Command Parser v2):** `parse_cmd(cmd: dict)` (e.g., `{"type": "DRAW", "shape": "CIRCLE", "params": [10,20,5]}`). Use mapping patterns. Add guards (e.g., `params` length).
    * **Deliverable:** Enhanced parser.
* **Chunk 1.20 (1 hr): `else` in `for` and `try` Statements**
    * **Learn (FP Ch 18):** "Do This, Then That: `else` Blocks Beyond `if`."
    * **Project:** 1. `for/break/else` to find an item. 2. `try/except/else` for a risky operation where `else` runs on success.
    * **Deliverable:** Scripts. Explain precisely when `else` runs.
    * **Mentor Action (Phase 1 End):** Provide a moderately complex, nested data structure (list of dicts of lists). Require `match/case` to extract and transform specific data elements, using captures and guards. Review all Phase 1 deliverables for conceptual clarity.

---

## Phase 2: Taming Concurrency & The GIL (Chapters 19 & 20) (Target: ~15 Chunks)

**Core Objective:** Understand Python's concurrency models, the GIL's true impact, and how to use `threading` and `multiprocessing` effectively via `concurrent.futures`.

### Chapter 19: Concurrency Models in Python

* **Chunk 2.1 (1 hr): Concurrency vs. Parallelism & Core Terminology**
    * **Learn (FP Ch 19):** "The Big Picture," "A Bit of Jargon."
    * **Task:** Write down your own definitions for: Concurrency, Parallelism, Process, Thread, Coroutine, GIL, Queue, Lock.
    * **Deliverable:** Your definitions.
* **Chunk 2.2 (1 hr): The Global Interpreter Lock (GIL) - Demystified**
    * **Learn (FP Ch 19):** "Processes, Threads, and Python’s Infamous GIL."
    * **Task:** In simple terms: What is the GIL? Why does CPython have it? How does it affect CPU-bound threaded code? When is the GIL released?
    * **Deliverable:** Q&A notes.
* **Chunk 2.3 (1 hr): `spinner_thread.py` - Code Analysis**
    * **Learn (FP Ch 19):** "Spinner with Threads" (Ex 19-1, 19-2).
    * **Project:** Implement and run `spinner_thread.py`.
    * **Task:** Annotate the code, explaining the role of `Thread`, `target`, `args`, `.start()`, `Event`, `.set()`, `.wait()`, `.join()`.
    * **Deliverable:** Annotated script.
* **Chunk 2.4 (1 hr): `spinner_proc.py` - Code Analysis & Comparison**
    * **Learn (FP Ch 19):** "Spinner with Processes" (Ex 19-3).
    * **Project:** Implement and run `spinner_proc.py`.
    * **Task:** List the key API differences and similarities to the threaded version. Why are processes better for CPU-bound parallelism in Python?
    * **Deliverable:** Comparison notes.
* **Chunk 2.5 (1 hr): GIL Impact Experiment - CPU-Bound Work**
    * **Learn (FP Ch 19):** "The Real Impact of the GIL," "Quick Quiz."
    * **Project:** Modify your `spinner_thread.py` and `spinner_proc.py`. Replace `time.sleep(3)` in `slow()` with a call to `is_prime(VERY_LARGE_NUMBER)` (from Ex 19-10).
    * **Task:** Observe spinner behavior and total execution time for both. Does it match the book's explanation for the GIL's time-slicing vs. true process parallelism?
    * **Deliverable:** Modified scripts & observations.
    * **Mentor Action:** Discuss GIL results. If the threaded CPU-bound spinner *still* spins a bit, why? (Hint: GIL release interval).

### Chapter 20: Concurrent Executors

* **Chunk 2.6 (1 hr): `concurrent.futures` Intro & Sequential Baseline (`flags.py`)**
    * **Learn (FP Ch 20):** "Concurrent Web Downloads," "A Sequential Download Script" (Ex 20-2 `flags.py`).
    * **Project:** Ensure `flags.py` runs and downloads flags correctly (set up a local server or use a small, safe list of public image URLs if needed).
    * **Deliverable:** Working `flags.py`.
* **Chunk 2.7 (1 hr): `ThreadPoolExecutor.map()` for I/O-Bound Tasks**
    * **Learn (FP Ch 20):** "Downloading with `concurrent.futures`" (Ex 20-3 `flags_threadpool.py`).
    * **Project:** Implement `flags_threadpool.py` using `executor.map()`.
    * **Deliverable:** Working script. Benchmark against `flags.py`.
* **Chunk 2.8 (1 hr): `Future` Objects - The What and Why**
    * **Learn (FP Ch 20):** "Where Are the Futures?".
    * **Task:** What is a `Future`? Who creates it? Key methods: `.done()`, `.result()`, `.add_done_callback()`. How does `.result()` behave if the future isn't done?
    * **Deliverable:** Notes.
* **Chunk 2.9 (1 hr): `executor.submit()` & `futures.as_completed()`**
    * **Learn (FP Ch 20):** Study Ex 20-4 (`flags_threadpool_futures.py`).
    * **Project:** Implement Ex 20-4. Why is `as_completed` useful here for progress display or immediate result processing? How is `to_do_map` used?
    * **Deliverable:** Working script.
* **Chunk 2.10 (1 hr): `ProcessPoolExecutor` for CPU-Bound Tasks**
    * **Learn (FP Ch 20):** "Launching Processes with `concurrent.futures`," "Multicore Prime Checker Redux" (Ex 20-6 `proc_pool.py`).
    * **Project:** Implement `proc_pool.py`. Compare its code to `procs.py` (Ch 19).
    * **Deliverable:** Working script.
* **Chunk 2.11 (1 hr): Performance & Output Order: `map` vs. `as_completed`**
    * **Project:** Run `proc_pool.py` (uses `map`). Note the output order. If `numbers` is sorted descending, the largest primes (slowest) will block the output of faster ones.
    * **Task:** Refactor `proc_pool.py` to use `executor.submit()` and `futures.as_completed()`. Run again. Does the output order change? Why?
    * **Deliverable:** Refactored script and explanation of output order differences.
* **Chunk 2.12 (1 hr): Error Handling with Executors - Setup (`flags2`)**
    * **Learn (FP Ch 20):** "Downloads with Progress Display and Error Handling." Understand `flags2_common.py` and error handling in `flags2_sequential.py` (Ex 20-14, 20-15).
    * **Project:** Set up local test servers (LOCAL, DELAY, ERROR). Run `flags2_sequential.py` against ERROR server.
    * **Deliverable:** Working setup.
* **Chunk 2.13 (1 hr): Error Handling with `ThreadPoolExecutor` & `as_completed`**
    * **Learn (FP Ch 20):** Study `flags2_threadpool.py` (Ex 20-16). How are exceptions from `future.result()` handled?
    * **Project:** Implement and test `flags2_threadpool.py` against ERROR and DELAY servers.
    * **Deliverable:** Working script.
    * **Break-It:** In `download_one` (from `flags2_sequential`), make it sometimes raise `ValueError` instead of an `httpx` error. How does `flags2_threadpool.py` react?
    * **Mentor Action (Phase 2 End):** Review all Phase 2 projects. Discuss pickling issues with `ProcessPoolExecutor`. Give a problem that requires choosing between `ThreadPoolExecutor` and `ProcessPoolExecutor` and justify the choice.

---

## Phase 3: The World of `async/await` (Chapter 21) (Target: ~20 Chunks)

**Core Objective:** Internalize `asyncio`'s event loop model, native coroutines, and how `await` enables cooperative multitasking for high-throughput I/O.

* **Chunk 3.1 (1 hr): `asyncio` - Definitions & First Example (`blogdom.py`)**
    * **Learn (FP Ch 21):** "A Few Definitions," "An `asyncio` Example: Probing Domains" (Ex 21-1).
    * **Project:** Implement and run `blogdom.py`.
    * **Deliverable:** Working script. Define: native coroutine, `await`, event loop, `asyncio.run()`.
* **Chunk 3.2 (1 hr): Awaitables & Reading Async Code**
    * **Learn (FP Ch 21):** "Guido’s Trick to Read Asynchronous Code," "New Concept: Awaitable."
    * **Deliverable:** Notes explaining awaitables.
* **Chunk 3.3 (1 hr): `flags_asyncio.py` - Structure & Supervisor**
    * **Learn (FP Ch 21):** "Downloading with `asyncio` and HTTPX" (Ex 21-2: `download_many`, `supervisor`).
    * **Deliverable:** Implement these two functions.
* **Chunk 3.4 (1 hr): `flags_asyncio.py` - Core Coroutines**
    * **Project (FP Ch 21):** Implement `download_one`, `get_flag` (Ex 21-3). Complete `flags_asyncio.py`.
    * **Deliverable:** Working script. Speed compare with threaded version.
* **Chunk 3.5 (1 hr): `await` Control Flow & The "All-or-Nothing" Trap**
    * **Learn (FP Ch 21):** "The Secret of Native Coroutines," "The All-or-Nothing Problem."
    * **Break-It:** In `flags_asyncio.py`'s `get_flag`, temporarily replace `await client.get(...)` with synchronous `httpx.get(...)`. Observe the "freezing." Explain why. Change it back.
    * **Deliverable:** Observation notes.
* **Chunk 3.6 (1 hr): Asynchronous Context Managers (`async with`)**
    * **Learn (FP Ch 21):** "Asynchronous Context Managers." Why is `async with` needed?
    * **Task:** Review `flags_asyncio.py` (Ex 21-2) usage of `async with AsyncClient()`.
    * **Deliverable:** Notes.
* **Chunk 3.7 (1 hr): `flags2_asyncio.py` - Error Handling & `asyncio.to_thread`**
    * **Learn (FP Ch 21):** Study `flags2_asyncio.py` (Ex 21-6: `get_flag`, `download_one`).
    * **Deliverable:** Implement these coroutines.
* **Chunk 3.8 (1 hr): `asyncio.Semaphore` for Throttling**
    * **Learn (FP Ch 21):** "Throttling Requests with a Semaphore," "Python’s Semaphores."
    * **Project:** Implement `supervisor`, `download_many` (Ex 21-7). Complete `flags2_asyncio.py`.
    * **Deliverable:** Working script.
* **Chunk 3.9 (1 hr): Testing `flags2_asyncio.py` - Focus on Errors & Concurrency**
    * **Project:** Test `flags2_asyncio.py` against DELAY and ERROR servers. Vary `-m` concurrency.
    * **Deliverable:** Test observations. How does the semaphore affect behavior?
* **Chunk 3.10 (1 hr): Sequential `await` for Multi-Step Async Logic**
    * **Learn (FP Ch 21):** "Making Multiple Requests for Each Download" (Ex 21-8, 21-9, `flags3_asyncio.py`).
    * **Project:** Implement `flags3_asyncio.py`.
    * **Deliverable:** Working script. Explain why `await get_country` after `await get_flag` is fine.
* **Chunk 3.11 (1 hr): Asynchronous Iteration: `async for`, `__aiter__`, `__anext__`**
    * **Learn (FP Ch 21):** "Asynchronous Iteration and Asynchronous Iterables."
    * **Deliverable:** Notes on differences between sync/async iteration protocols.
* **Chunk 3.12 (1 hr): Asynchronous Generator Functions (`async def` with `yield`)**
    * **Learn (FP Ch 21):** "Asynchronous Generator Functions," "Experimenting with Python’s async console."
    * **Project:** In `python -m asyncio` console, work through Ex 21-16, 21-17 using `probe` and `multi_probe` from `domainlib.py` (Ex 21-18).
    * **Deliverable:** Successful console session.
* **Chunk 3.13 (1 hr): Using an Async Generator (`domaincheck.py`)**
    * **Project (FP Ch 21):** Implement and run `domaincheck.py` (Ex 21-19).
    * **Deliverable:** Working script.
* **Chunk 3.14 (1 hr): Async Comprehensions & Async Generator Expressions**
    * **Learn (FP Ch 21):** "Async Comprehensions and Async Generator Expressions."
    * **Project:** In async console, try the examples: async genexp, async list comp, async dict comp.
    * **Deliverable:** Successful execution.
* **Chunk 3.15 (1 hr): Delegating Blocking Code: `asyncio.to_thread` vs. `run_in_executor`**
    * **Learn (FP Ch 21):** "Delegating Tasks to Executors."
    * **Task:** When would you use `loop.run_in_executor(process_pool_executor, ...)` instead of `asyncio.to_thread()`?
    * **Deliverable:** Notes.
* **Chunk 3.16 (1 hr): `asyncio` TCP Server - Part 1 (Supervisor/Main - Ex 21-12)**
    * **Learn (FP Ch 21):** "Writing `asyncio` Servers," "An `asyncio` TCP Server." Study `supervisor` and `main` in `tcp_mojifinder.py` (Ex 21-12).
    * **Deliverable:** Implement these parts.
* **Chunk 3.17 (1 hr): `asyncio` TCP Server - Part 2 (Handler Coroutines - Ex 21-14, 21-15)**
    * **Project:** Implement `finder` and `search` coroutines. Complete and test `tcp_mojifinder.py` with `telnet`.
    * **Deliverable:** Working TCP server.
* **Chunk 3.18 (1 hr): `async` Beyond `asyncio`: Curio (Conceptual Overview)**
    * **Learn (FP Ch 21):** "async Beyond `asyncio`: Curio" (Ex 21-21).
    * **Task:** What are the key API differences you notice in Curio for starting tasks and handling results compared to `asyncio`? (Conceptual, no Curio install needed if short on time).
    * **Deliverable:** Notes.
* **Chunk 3.19 (1 hr): Realities of Async - "I/O-Bound Myth" & CPU Traps**
    * **Learn (FP Ch 21):** "How Async Works and How It Doesn’t."
    * **Task:** Why is "I/O-bound system" a misleading simplification for async? What are strategies for CPU-bound work in an async app?
    * **Deliverable:** Written answers.
* **Chunk 3.20 (1 hr): Phase 3 Review & Mentor Gauntlet**
    * **Task:** Review all your Phase 3 notes and code. Prepare questions.
    * **Mentor Action:**
        * Scenario: An `asyncio` service handles incoming requests. Some requests are quick (DB lookup), some are slow (call external flaky API), some are CPU-bound (report generation). How do you structure this to keep the service responsive? What specific `asyncio` tools or patterns for each?
        * Discuss the "What Color Is Your Function?" problem in the context of Python.

---

This expanded, conservative roadmap should provide a more sustainable path. Remember to adjust based on your actual progress and energy. The key is consistent, focused learning and immediate application.