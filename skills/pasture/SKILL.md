---
name: pasture
description: Work well inside pasture, a macOS setup that runs several coding agents (Claude Code, Codex, Grok, Antigravity) side by side under herdr. Use when HERDR_ENV=1 or pasture-* commands exist, or when the user mentions pasture, herdr, the collie, parallel agents, pasture-task, pasture-duo, worktrees, Sapling stacks, agent-browser or agent-desktop; it maps each kind of task to the pasture tool and states the shared rules.
metadata:
  tags: ["pasture", "herdr", "multi-agent", "worktree", "sapling", "agent-browser", "workflow"]
---

# Pasture

pasture (https://github.com/kinhluan/pasture) is a dotfiles setup where several
coding agents work at once: herdr hosts the panes and agents, Ghostty draws
them, and small `pasture-*` scripts tie the workflow together. You are one of
those agents. Use the tools below instead of improvising, and follow the shared
rules: other agents and the user are working in the same machine and often the
same repository.

## Detect It First

Run these read-only checks before relying on anything here:

```bash
echo "${HERDR_ENV:-}" "${HERDR_PANE_ID:-}"   # 1 and a pane id inside herdr
command -v herdr pasture-task wt sl agent-browser agent-desktop
```

- A missing command means that part of pasture is not installed: say so and
  fall back to plain git or the user's instructions. Do not install tools
  unless the user asks.
- herdr commands also work outside a herdr pane (for example from an IDE
  terminal) as long as the herdr server runs.

## Use pasture's Commands Before Writing a Script

pasture ships tested scripts for the local CLIs. Before writing a shell script
to drive herdr, git, Sapling, glab or a browser, run:

```bash
pasture help            # or: pasture list --json
pasture help <group> <command>
```

Use a matching command instead of writing your own. Respect its safety label:

- `read`: run it.
- `write`: run it; use `--dry-run` first when unsure.
- `external`: run it without `--yes` to get the plan (exit code 3), show the
  plan to the user, and add `--yes` only after they approve.

Exit codes are shared: 0 ok, 1 failed, 2 usage, 3 needs the user, 4 timed
out, 5 missing tool or wrong place. If no command fits and the task recurs,
suggest adding one under `~/.config/pasture/cmds.local/<group>/<command>`
rather than repeating an ad-hoc script.

## Pick the Tool for the Task

| Task | Use | Not |
| ---- | --- | --- |
| Start a second task in parallel with the current one | Suggest `pasture-task <branch> [agent]` to the user: a git worktree (Worktrunk), a herdr workspace and an agent in it | editing a second task in the same working copy |
| Split one task into small reviewable commits | Sapling: `sl commit`, `sl prev`/`sl next`, `sl amend`, `sl absorb`, `sl stack` | `git rebase -i` |
| Get the change reviewed by other agents | `pasture-duo` (the user runs it; you act as writer or reviewer) | prompting other agents ad hoc |
| See what another pane or agent is doing | `pasture pane tail <pane>`, `herdr agent list`, `herdr agent read <name>` | asking the user to paste output |
| Wait for a dev server, build or test in another pane | `pasture pane tail <pane> --wait "<regex>"` | polling with sleep |
| Ask another agent one question | `pasture agent ask <name> "<prompt>"` (refuses when it is blocked) | raw `herdr agent prompt` plus guessing when it finished |
| Read a web page | your fetch tool, or `pasture web read <url>` (fetch, then a browser when needed) | a browser for static pages |
| Click, fill or navigate a page | `agent-browser` (`open`, `snapshot -i`, `click @e1`) | retrying fetch |
| Inspect a ticket's merge requests | `pasture mr stack <ticket>` | hand-rolled `glab api` + `git rev-list` |
| Publish a Sapling stack as branches / MRs | `pasture stack push <prefix> [--mr]` (external) | pushing each step by hand |
| Make stacked branches independent (trunk-based) | `pasture mr fanout <branch>…` (external) | manual `rebase --onto` + force-push |
| Operate a native macOS app | `agent-desktop`, only if `agent-desktop status` shows the permission granted | asking for the permission yourself |
| Build or test a Bazel repo | `bazel` (bazelisk runs the repo's `.bazelversion`) | a globally pinned Bazel |
| Python / JavaScript | `uv`; `pnpm` or `bun`, matching the repo's lockfile | `pip install` into the system, a different package manager than the lockfile |

Before using agent-browser or agent-desktop for the first time in a session,
read their version-matched guides: `agent-browser skills get core` and
`agent-desktop skills get desktop`.

## Worktrees (Worktrunk)

- One task, one worktree. Worktrees live in `<repo>/.worktrees/<branch>`;
  `wt list` shows them with status, `wt switch <branch>` moves between them.
- Stay inside the worktree you were started in. Never edit files in another
  agent's worktree.
- `wt merge` merges locally into the default branch. In repositories that use
  merge requests, push the branch and open the MR instead; the user runs
  `pasture-task --done <branch>` after it lands.
- Build caches are per repo (for example a Bazel `--disk_cache` in the repo's
  `.bazelrc`); do not delete them to "clean up".

## Stacks (Sapling)

- `sl` works directly in git repos and worktrees. It leaves git's HEAD
  detached. Once a stack is managed with `sl`, commit with `sl commit`: a
  `git commit` on a detached HEAD moves no branch and the work is easy to lose.
- Publish a step with `sl push --to <branch>`. `sl pr` is GitHub only; on
  GitLab push each step to its own branch and open the merge requests with
  `glab`.
- Confirm with `sl stack` (the current stack only) before and after rewriting.

## Working With Other Agents (herdr)

- Address agents by name or pane id from `herdr agent list`. Check
  `agent_status` first: `idle` or `done` can take input; `working` cannot;
  `blocked` is waiting for a human.
- `herdr agent prompt <name> "<text>" --wait --timeout <ms>` sends one prompt
  and waits for a settled state; then read the answer with
  `herdr agent read <name> --source recent-unwrapped --lines 200`.
- If a command returns `agent_blocked`, `agent_prompt_stalled` or a timeout,
  inspect with `herdr agent get` and `herdr agent read` before resending.
- As a reviewer in `pasture-duo`: you were started read-only. Report findings
  as `file:line`, problem, why; do not edit files.
- As the writer in `pasture-duo`: follow the review-loop prompt the user
  pasted: ask all reviewers at once, merge findings, fix safety issues raised
  by anyone, let the majority decide the rest, ask the user on a tie.

## Shared Rules

1. **Never answer another agent's approval or question dialog.** A `blocked`
   agent waits for the user. Report it; the collie (🐕 in the sidebar,
   `⌃⌥A` to jump) already alerts them.
2. **Do not close, quit or restart other agents or panes** (`pane close`,
   `workspace close`, `--sweep`, quit commands) unless the user asked for that
   exact action.
3. **Do not type into panes you do not own** (`pane run`, `send-keys`,
   `send-text`) except to run the command the user asked for.
4. **Keep secrets out of output.** Pane reads, browser snapshots and desktop
   snapshots can contain tokens or private content from other apps; quote only
   what the task needs.
5. **Leave pasture's config alone.** Files under `~/.config/herdr`,
   `~/.config/worktrunk`, `~/.config/pasture` and similar are symlinks into the
   pasture repository; change them only when the task is about pasture itself.

## Completion

Before reporting a task done in pasture, confirm:

- the change is in the intended worktree and branch (`git status -sb` or
  `sl stack`);
- builds and tests ran in that worktree, or say they did not;
- no other agent's pane, worktree or dialog was touched;
- anything the user must do next (open the MR, run `pasture-task --done`,
  grant a permission) is stated explicitly.
