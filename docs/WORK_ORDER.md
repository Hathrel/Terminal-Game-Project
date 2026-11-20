# Gladiator Simulator Work Order

## 1. Project boilerplate and shared utilities

- [x] Organize Python source into entity, equipment, utility, dialogue, and debugging modules.
- [x] Define player and AI controller identifiers.
- [x] Define head, shoulders, chest, hands, legs, feet, and shield equipment slots.
- [x] Provide a shared dice roller with inclusive results from 1 through the specified die size.
- [x] Route terminal text through a shared output function.
- [x] Provide toggleable debug output and automatic success, failure, and generic dialogue placeholders that identify the caller’s file, class when available, and method. Accept a descriptive category for generic placeholders, such as `generic_message_auto("Shopping List")`.
- [ ] Keep remaining dialogue placeholders recognizable during playtesting so each missing line of flavor text can be located while functional development continues.
- [ ] Establish a consistent package import strategy for standalone launch and tests. Resolve relative imports beyond the package root, sibling imports, and the inventory/dialogue import cycle.
- [ ] Provide a terminal entry point, document the launch command, and verify that it can construct a character and open the game loop.

## 2. Gladiator model and starting state

- [x] Model a human with name, age, controller, individual inventory, level 1, and zero XP.
- [x] Initialize Strength, Dexterity, Agility, Fortitude, and Luck at 1.
- [x] Initialize HP from `90 + Fortitude × 10`, yielding 100 HP at Fortitude 1.
- [x] Expose candidate modifiers of Strength divided by 2 and Dexterity, Agility, and Fortitude divided by 3, rounded down.
- [x] Expose Luck-based stat and XP bonuses. Apply a 65% ceiling to the trigger chance and award Luck or Luck × 10 when the respective roll succeeds.
- [x] Expose Dexterity-based second-attack, Agility-based instinctive-block, and Fortitude-based recovery rolls scaled by Luck and capped at 65%. Return Fortitude HP on a successful recovery roll.
- [x] Track consciousness, determine life from positive HP, and allow conscious living gladiators to enter a defending stance.
- [x] Generate given-name/surname combinations, track names used in the running process, and bound retries.
- [ ] Allocate and persist unique gladiator identities and names across restarts and after death or retirement. Handle exhausted name pools explicitly.
- [x] Initialize inventories with zero coins and no equipped armor.
- [ ] Equip newly admitted gladiators with a starting dagger.
- [ ] Track maximum and current HP separately, cap healing, and define how Fortitude gains affect both.
- [ ] Decide which Luck effects and candidate modifiers participate in the shared rules. Decide how armor mitigation and any proposed Fortitude mitigation bonus should interact.

## 3. Equipment, inventory, and shop

- [x] Define item names, values, and equipment types, with separate armor defense and mitigation ratings and shield defense and block chance.
- [x] Catalog leather, iron, and steel armor for all six body slots and shields for the shield slot.
- [x] Define one equipped slot per armor location and one equipped weapon.
- [x] Supply fists when the weapon slot is empty, with a +3 attack bonus, base damage 4, and a 4% knockout roll on a hit.
- [x] Sum equipped defense across body armor and shield, and sum mitigation across body armor.
- [x] Define equip handlers for head, shoulders, chest, and hands with checks for missing items, wrong slots, occupied slots, and re-equipping the same object.
- [x] Define unequip handlers for all seven slots and return the removed item to inventory through the inventory action.
- [ ] Equip leg armor into the leg slot and add equip handling for boots and shields.
- [ ] Validate item ownership and transfer items between storage and equipped slots without duplication or item loss. Reject broken gear before equipping it.
- [x] Format footchest contents for empty, single-item, two-item, and longer lists, with a coin balance when positive.
- [x] Format slot-aware equipment feedback with singular/plural grammar and varied equip and unequip verbs.
- [x] Support purchases with an affordability check, coin deduction, and a copy of the purchased item. Support discarding owned items.
- [x] Match sale candidates by item name and reject empty candidate lists before reading the first item.
- [x] Guard against a `None` sale selection before changing inventory or money.
- [x] Calculate resale from half the base value, subtract durability wear, and apply a further tenfold divisor to broken items.
- [ ] Present equipment choices in the text interface with distinct entries and condition details for items of the same type. Resolve the player’s choice to the exact existing object instance. Use UUIDs only if a concrete persistence or identity requirement calls for them.
- [ ] Let text selection return `None` on cancellation, such as when the player enters `0`. Handle cancellation before changing inventory or money.
- [ ] Verify that selling removes the selected instance and uses its condition to calculate proceeds. Exercise cancellation through terminal input and a deliberately injected `None` in debug mode.
- [ ] Set catalog prices, settle resale rounding and minimum proceeds, and supply player-facing shop feedback for browsing, purchases, sales, discards, and cancellation.
- [x] Define item-owned breakable armor and shield primitives with durability counters, depletion checks, and a probabilistic defensive-break mode.
- [ ] Preserve independent condition for each owned item through purchase, equip, unequip, sale, and any repair. Verify that items of the same type can have different durability and that changing one item leaves its peers untouched.
- [ ] Make catalog items eligible for their intended durability and breakage rules.
- [ ] Disable protection from broken gear on later actions, preserve the defense that caused it to break, and support replacement through the shop.
- [ ] Decide whether non-helmet body armor should wear or break and how material quality affects durability.
- [ ] Evaluate repairs for damaged armor and shields before they break. Decide whether to offer repairs, where they are available, and how to price and balance them.
- [ ] If repairs are adopted, apply them to the selected damaged item and reject completely broken equipment without charging the gladiator. Balance recurring repair costs so they compete with savings for early retirement.

## 4. Shared combat engine

- [x] Define weapon-owned d30 attack checks against defense and damage-die rolls with a damage bonus and flat armor subtraction.
- [x] Define shield-owned percentage block checks while actively blocking and blunt-weapon knockout checks gated on a successful hit.
- [ ] Add knife (+3), dagger (+4), mace (+5), longsword (+6), and greatsword (+8) weapon entries.
- [ ] Use a single combat resolver for players and NPCs, with shared eligibility, actions, rolls, and outcomes.
- [ ] Apply Dexterity to attack accuracy, Strength to damage, Agility to hit prevention, and armor to post-hit mitigation. Set scaling and derive the resulting attack and defense ranges.
- [ ] Decide whether equipment defense ratings contribute to avoiding hits alongside Agility, and keep avoidance distinct from flat damage mitigation.
- [ ] Define a separate dodge check with Agility scaling, armor burden, a probability cap, and a resolution order for attack, dodge, shield, damage, and knockout.
- [ ] Determine minimum damage after mitigation and whether a zero-damage hit can cause a knockout.
- [ ] Resolve attack, defend, yield, and any extra attacks or instinctive blocks. Clear transient stance flags at the chosen action or round boundary.
- [ ] Define a round in terms of fighter actions and resolve bout completion, unconsciousness, death, and permanent removal from active play.
- [ ] Trigger a spare-or-execute decision on knockout as designed. Use NPC personality for mercy decisions and record executions as permanent deaths.
- [ ] Introduce helmet-specific knockout negation independent of ordinary mitigation. Balance material odds, using 10% leather, 40% iron, and 70% steel as illustrative candidates.
- [ ] Roll shield breakage after a successful block and helmet breakage after a successful knockout negation.
- [ ] Playtest the proposed 8% mace knockout chance and the effect of bypassing remaining HP.
- [ ] Introduce weapon material/quality tiers such as wood, iron, and steel. Balance type and quality independently across accuracy, damage, and durability while preserving weapon-specific behavior and allowing a high-quality smaller weapon to outperform a low-quality larger weapon.

## 5. NPC controllers, telemetry, and balance

- [ ] Implement autonomous combat controllers with weighted tendencies for aggression, defense, risk, yielding, and mercy. Support berserker, cowardly, opportunistic, and balanced personalities.
- [ ] Run unattended fights through the shared combat engine and capture random seeds for reproduction.
- [ ] Capture attributes, level, personality, equipment type and material, raw rolls, modifiers, defense targets, dodge/block/helmet outcomes, raw and absorbed damage, HP loss, knockout attempts and negations, breakage, result, and round count.
- [ ] Run roughly 100 baseline fights and report mean, median, minimum, and maximum round counts, deaths, yields, and outcomes by level and loadout.
- [ ] Compare weapon and armor effectiveness, knockout and helmet rates, equipment lifespan, dominant combinations, personality survival and victory rates, and the impact of replacement costs on freedom savings.
- [ ] Playtest power, precision, and hybrid builds against different armor and skill levels. Quantify Agility’s combined defense and dodge, Fortitude’s effect on duration, and attribute convergence at high levels.

## 6. Progression, autonomous routines, and calendar

- [ ] Award fight XP with a victory premium. Choose thresholds, attribute award frequency and caps, and player and NPC attribute allocation rules.
- [ ] Let NPC personality influence spending, gear preferences, training, rest, fight selection, attribute investment, and retirement.
- [ ] Add an out-of-combat recovery action, define its time cost, and apply the chosen Fortitude and Luck recovery rules.
- [ ] Add safe training dummy sessions that consume world time and award modest, predictable XP and zero gold.
- [ ] Decide when to replenish the stable after retirements and deaths. Generate newcomers and let their training target reflect living gladiators’ average level and individual risk tolerance.
- [ ] Maintain a small personal rolling summary of attempts, hit rates, damage, defenses, opponent armor, and outcomes. Choose the window size and evidence thresholds.
- [ ] Apply personality-weighted adaptation to attribute spending, training, and purchases. Let a berserker temporarily address repeated misses with Dexterity before returning to Strength. Decide whether adaptability varies by personality.
- [ ] Advance one shared deterministic clock while the player fights, shops, trains, rests, or spectates. Give NPCs meaningful out-of-combat turns and advance any active NPC bout during player downtime.
- [ ] Define the relationship between rounds, action equivalents, days, and times. Playtest five rounds per action equivalent, roughly one out-of-combat NPC action per five rounds, and roughly three to five NPC rounds per out-of-combat player action.
- [ ] Configure four seasons per year and choose season length from measured bout duration, using 8–10 action equivalents per season as candidates.
- [ ] Age gladiators using the calendar. Decide the timing, severity, and modifiers for physical decline and natural mortality.

## 7. Arena scheduling and fight economy

- [ ] Enforce exclusive use of the sacred arena sands. Treat group combat as a single occupying bout and allow active bouts to finish before starting another.
- [ ] Resolve the organizer role and supported formats, including group battles and special tickets. Decide whether to add a storyteller controller.
- [ ] Schedule obligatory organizer tickets by in-game day and time, notify the player when selected, and require selected gladiators to enter combat at the scheduled time subject to arena occupancy.
- [ ] Define when the player transitions into combat if the sands are occupied at the scheduled time.
- [ ] Award organizer payouts above voluntary exhibition payouts and settle the size of the premium.
- [ ] Apply the original planning-sheet payout rules to voluntary exhibitions. Recover the payout specifications before setting values.
- [ ] Create a roster ticket when an exhibition challenge is accepted. Permit either fighter to withdraw or switch opponents before the call, remove the old ticket, and create a replacement only after acceptance.
- [ ] Start an action-based grace period on the exhibition call. Test the proposed three-action limit for reporting to the sands and choose the final deadline and small fine. On expiry, record a loss, award zero XP, and deduct the fine.
- [ ] Give organizer tickets precedence after the active bout. Cancel queued exhibition tickets without penalty and require a new accepted challenge to put an exhibition back on the roster after the event.

## 8. Retirement, historical records, and dialogue

- [ ] Offer retirement without a buyout from age 50 and purchasable freedom before age 50.
- [ ] Set a buyout curve that declines with age and balance it against steel armor prices, earnings, replacement expenses, and prospective repair costs.
- [ ] End active careers on retirement, buyout, or death. Apply the rules consistently to player and NPC gladiators.
- [ ] Track annual completed fights, stable entry season, and permanent archive eligibility. Require 10 fights in a full year and five for a winter entrant’s first year. Set the remaining prorated quotas.
- [ ] Check quota at year-end, permanently disqualify careers that miss it, and reset annual counters without banking surplus fights. Allow retirement regardless of eligibility.
- [ ] Archive eligible careers with name, age, final attributes and level, controller and personality, equipment, wins, losses and kills, career earnings and final wealth, duration, and career-ending reason. Decide how eligibility applies to death or retirement during a partial year.
- [ ] Persist queryable world events for matches, yields, knockouts, deaths and executions, purchases and breakage, level-ups, and freedom and retirement. Preserve world events for every gladiator independently of archive eligibility.
- [ ] Provide recent, deaths, and match log views and named gladiator history and inspection commands that work after death or retirement. Keep concise world events distinct from detailed combat telemetry.
- [ ] Generate dialogue from personality, personal memories, simulated events, beliefs, and goals. Cover combat struggles, reliable or broken gear, rivalries, and plans to train, fight, rest, save, or retire.
- [ ] Set boundaries on personal knowledge so NPC memory and dialogue use information the gladiator could know. Allow intentions to change or go unfulfilled.

## 9. Player loop, persistence, and verification

- [ ] Connect character creation, inventory, shopping, challenge and ticket handling, arena combat, spectating, training, rest, and retirement through terminal controls.
- [ ] Persist fighters, equipment state, money, clock, tickets, history, and career eligibility across sessions. Preserve pending scheduling and avoid reapplying payouts or year-end checks on reload.
- [ ] Decide which player death or retirement outcomes end the run. Evaluate a new level-one gladiator in the same mature stable and New Game+ with candidate uncapped levels and a fourfold freedom buyout. Decide how age-based retirement carries over.
- [ ] Verify a complete career through the terminal, including starter equipment, combat rewards, equipment purchases, training, annual quotas, retirement, and historical lookup.
- [ ] Verify edge cases for occupied sands at organizer time, group fights, ticket cancellation and forfeits, duplicate sale items, defensive breakage, permanent death, and save/reload boundaries.

## 10. Development workflow

- [ ] Commit frequently in units of one coherent change, using concise, descriptive commit messages.
- [ ] Preserve the original 2023 project on `master` and develop the refactor on `update`.
- [ ] If the project becomes a release candidate, decide whether to create a separate repository.
