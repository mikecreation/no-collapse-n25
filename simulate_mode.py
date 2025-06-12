from mirror_bore import solve, mem

def simulate_mode(puzzle_name, sample_fn, grade_fn, tag_prefix, rounds=10):
    results = []

    for i in range(rounds):
        tag = f"{tag_prefix}:{i}"
        inst, prompt = sample_fn()

        # Get memory traces
        prev = mem.get(tag)
        full_prompt = f"{prev}\n\n{prompt}" if prev else prompt

        # Run inference
        reply, toks = solve(tag, full_prompt)
        ok = grade_fn(inst, reply)

        print(f"[{i+1}/{rounds}] {puzzle_name}: {'✓' if ok else '✗'} | tokens: {toks}")
        results.append((i, ok, toks))

        # If stuck on same failure twice in a row, initiate correction loop
        if not ok and i > 0 and not results[i - 1][1]:
            print("  ❗Stagnation detected — injecting failure correction sequence.")
            correction_tag = f"{tag_prefix}:correction:{i}"
            fail_trace = "\n".join(mem.store.get(tag, []))
            corrected_prompt = (
                f"You previously tried solving this but failed.\n\n"
                f"Here are your prior attempts:\n{fail_trace}\n\n"
                f"Before solving again, explain briefly (in one line) what you think went wrong.\n"
                f"Then, try again. Remember:\n{prompt}"
            )
            solve(correction_tag, corrected_prompt)

    return results