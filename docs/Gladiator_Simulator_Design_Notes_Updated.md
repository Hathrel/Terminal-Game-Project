# **Gladiator Simulator — Prospective Feature Design Notes**

**Status note (updated November 18, 2026):** The original notes below preserve the design discussion as it stood after baseline armor balancing. Sections 11–15 document later decisions, revisions, and additional proposals. The original sections are retained for context; where they conflict with the update, the later sections take precedence. Do not interpret proposed mechanics as implemented.

## **1. Core design principles**

- Player and NPC gladiators operate under identical mechanics.
- No plot armor, artificial player advantages, or scripted outcomes.
- Gladiators are persistent characters who can develop, acquire equipment, retire, or permanently die.
- NPC behavior is autonomous and driven by personality.
- The world continues progressing while the player fights, shops, trains, rests, or spectates.
- Equipment objects own their behaviors; the combat system coordinates interactions between objects.

## **2. Combat and equipment**

### **Weapons**

Existing weapon characteristics include attack bonus, damage bonus, damage dice, and blunt-weapon knockout behavior.

**Prospective changes:**

- Introduce material/quality tiers, potentially wood, iron, and steel.
- Weapon type and material independently influence effectiveness.
- A high-quality dagger may outperform a low-quality greatsword.
- Material quality may affect attack, damage, and durability.
- Rebalance weapons against existing armor defense and damage reduction.
- Preserve distinct weapon behaviors across material tiers.

### **Blunt weapons and knockouts**

- Maces have a proposed 8% knockout chance on a successful hit.
- Knockouts immediately end combat or initiate a victory decision.
- The victor may accept victory and spare the opponent or execute them.
- Execution permanently kills the opponent.
- NPC personality influences the decision to spare or execute.
- Whether zero-damage hits can trigger knockouts remains undecided.

Because knockout bypasses remaining HP, blunt weapons require particularly careful balancing.

### **Helmets**

Introduce specialized knockout protection for helmets.

| Helmet  | Illustrative knockout negation |
| ------- | ------------------------------ |
| None    | 0%                             |
| Leather | 10%                            |
| Iron    | 40%                            |
| Steel   | 70%                            |

These values are **examples, not finalized statistics**.

- Helmets retain their existing armor/defense functionality.
- Helmet type determines knockout resistance.
- A successful knockout roll can be negated by the defender's helmet.
- Helmet resistance is independent of ordinary damage reduction.

### **Equipment breakage**

Successful defensive actions can trigger equipment breakage.

- **Shields:** Successful blocks can break the shield.
- **Helmets:** Successfully preventing a knockout can break the helmet.
- **Other armor:** Durability/breakage remains a possible future extension.
- Higher-quality materials may have lower break probabilities.
- Equipment that breaks while defending still successfully prevents that particular attack or knockout.
- Broken equipment loses its protective functionality.
- Replacement equipment introduces recurring expenses.

Equipment objects manage their own breakage rolls and state.

## **3. Experience, leveling, and personalities**

### **Character progression**

- Gladiators potentially begin with every attribute at 1.
- All gladiators initially receive a dagger, no armor, and no gold.
- Fighting awards experience, with victories awarding more than defeats.
- Leveling grants attribute progression.
- Personality influences how NPCs allocate attributes.

An alternative discussed was deriving personality from starting attributes, but having personality influence subsequent attribute development may be more suitable.

### **Personality-driven NPCs**

Personality affects:

- Aggression and defensive decisions.
- Willingness to yield.
- Decisions to execute or spare defeated opponents.
- Equipment purchases.
- Training and resting priorities.
- Attribute specialization.
- Financial priorities and retirement decisions.

Examples:

| Personality | Behavioral tendency                                   |
| ----------- | ----------------------------------------------------- |
| Berserker   | Aggressive, prioritizes weapons, takes risks          |
| Coward      | Defensive, yields early, prioritizes survival         |
| Opportunist | Exploits favorable fights and financial opportunities |
| Balanced    | Mixes offense, defense, and long-term planning        |

These are tendencies, not absolute restrictions.

## **4. Training dummy and population replenishment**

New gladiators may eventually be generated to replace deaths and retirements.

To prevent newcomers from being immediately overwhelmed by experienced gladiators:

- Introduce a safe training dummy.
- Training awards a modest, predictable amount of XP.
- Training awards **no gold**.
- NPC newcomers observe the average level of living gladiators.
- They train toward that level before entering combat.
- Personality can influence when they consider themselves sufficiently trained.
- Training consumes world time.

A newly trained gladiator may have competitive attributes but still possess only starting equipment.

Population replenishment and the training system remain prospective.

## **5. Persistent world simulation and calendar**

### **Global clock**

The simulation uses one shared world clock.

Previously discussed pacing:

- One combat round consists of actions by both combatants.
- While the player fights, NPC fights advance one round per player combat round.
- NPCs outside combat act approximately once per five combat rounds.
- Outside player combat, NPC fights can advance approximately 3–5 rounds per player action.
- All characters experience the same global passage of time.

### **Seasons and years**

Introduce a configurable season length, \\(n\\), measured in out-of-combat action equivalents.

- One out-of-combat action equivalent = 5 combat rounds.
- One season = \\(n\\) out-of-combat equivalents.
- Four seasons = one year.
- Tentative \\(n\\): **8–10**, subject to playtesting.

| Calendar interval | n = 8             | n = 10            |
| ----------------- | ----------------- | ----------------- |
| Season            | 40 combat rounds  | 50 combat rounds  |
| Year              | 160 combat rounds | 200 combat rounds |

These values are not final. Combat duration must be measured before choosing a season length.

## **6. Aging, retirement, and freedom**

### **Aging**

- Gladiators age as the global calendar progresses.
- Physical deterioration may occur with age.
- Old age may eventually introduce a risk of natural death.
- Endurance and other characteristics may influence aging effects.
- Retirement becomes available at age **50**.

The exact aging penalties and mortality mechanics are undecided.

### **Purchasing freedom**

Gladiators may also purchase their freedom and retire before age 50.

**Buyout cost decreases as age increases.**

- Younger gladiators must pay more for freedom.
- Older gladiators can purchase freedom more cheaply.
- At age 50, retirement is available without purchasing freedom.
- The buyout price may be set just above the cost of the most expensive steel armor item.

This deliberately creates an economic dilemma:

**Buy expensive armor to improve survival, or save that money toward freedom and risk another fight.**

NPC personalities influence their decisions to save, purchase equipment, continue fighting, or retire.

### **Retirement records**

Both age-based retirement and purchased freedom end the gladiator's active career.

The proposed archived career snapshot includes:

- Name and age.
- Final attributes and level.
- Controller/personality.
- Equipment.
- Wins, losses, and kills.
- Career earnings and final wealth.
- Career duration.
- Retirement reason.

Permanent death is another possible career outcome.

## **7. Annual fight quota and historical eligibility**

A gladiator must remain active throughout their career to qualify for the permanent career archive.

**Rule: At least 10 fights per year.**

Each gladiator has:

- An annual fight counter.
- A permanent archive-eligibility flag.
- Their stable entry season.

At the end of each calendar year:

1. Determine the required fight quota.
2. Compare the gladiator's completed fights against that quota.
3. If the quota is missed, permanently set archive eligibility to `False`.
4. Reset the annual fight counter.

Once disqualified, a gladiator can never regain eligibility, regardless of subsequent accomplishments.

### **First-year proration**

The first year's quota depends on the season the gladiator enters the stable.

A gladiator entering in **Winter requires only 5 fights**.

The precise quotas for other entry seasons remain to be finalized.

### **Consequences**

- A gladiator who fights 100 times one year but misses the next year's quota is permanently disqualified.
- A gladiator who consistently fights 10 times per year remains eligible.
- Cowardly gladiators may survive to retirement without qualifying for historical recognition.
- Retirement is possible regardless of archive eligibility.

**The event log and permanent career archive are separate systems.** All important events remain recorded even for characters who fail to qualify for the archive.

## **8. Event logging and career history**

Introduce a persistent, queryable world event log.

Potential recorded events:

- Match victories and defeats.
- Yields and knockouts.
- Executions and deaths.
- Equipment purchases and breakage.
- Level-ups.
- Retirement and freedom purchases.
- Other important character developments.

Gladiator names are already unique, consisting of given name and surname.

Potential terminal commands:

```
log recent
log deaths
log matches
history Marcus Varro
inspect Marcus Varro
```

Historical records should remain accessible after a gladiator dies or retires.

Detailed combat events may be stored separately from concise world-history events.

## **9. Combat telemetry and automated balancing**

Use the actual combat engine to simulate matches without requiring player interaction.

### **Initial benchmark**

Simulate approximately **100 fights** to establish combat-duration statistics.

Measure:

- Mean and median combat rounds.
- Minimum and maximum rounds.
- Death and yield rates.
- Outcome distribution across different equipment and character levels.

Use the results to determine a suitable value for \\(n\\), the season length.

### **Detailed combat telemetry**

Capture complete attack and defense data for deeper balancing.

| Category   | Data                                        |
| ---------- | ------------------------------------------- |
| Combatants | Attributes, level, personality              |
| Equipment  | Weapon type/material, armor, shield         |
| Attack     | Raw roll, modifiers, defense target         |
| Defense    | Hit/miss, shield block, helmet protection   |
| Damage     | Raw damage, armor absorbed, final HP damage |
| Knockout   | Attempt, success, negation                  |
| Durability | Defensive successes, equipment breakage     |
| Outcome    | Winner, loser, yield, death, execution      |
| Duration   | Number of rounds                            |

### **Balancing applications**

Use collected data to determine:

- Weapon effectiveness by material and type.
- Armor effectiveness against different weapons.
- Whether maces produce excessive knockout victories.
- Whether helmets negate too many knockouts.
- How frequently equipment breaks.
- Average equipment lifespan.
- Whether certain equipment combinations are disproportionately powerful.
- Which NPC personalities have the highest survival and victory rates.
- How equipment replacement costs affect the ability to purchase freedom.

Record random seeds to reproduce unusual fights.

Python and pandas can be used to aggregate and analyze the results.

## **10. Implementation order to consider**

This is a suggested sequence, not an established development commitment.

1. Finish weapon and combat interactions using the existing armor statistics.
2. Implement autonomous NPC combat controllers.
3. Add structured combat telemetry and automated fight simulations.
4. Establish initial combat-duration and equipment-balance baselines.
5. Introduce helmets, knockout resistance, and equipment breakage.
6. Introduce weapon material/quality tiers and rebalance.
7. Implement persistent NPC progression, shopping, recovery, and training.
8. Implement the global calendar, seasons, and aging.
9. Introduce retirement, purchased freedom, and declining buyout prices.
10. Implement annual archive eligibility and permanent career records.

**Overall design direction:** A persistent, autonomous gladiator simulation in which combat ability, equipment quality, personality, economic decisions, aging, and mortality interact to produce unscripted careers. Gladiators may become champions, die unexpectedly, purchase freedom, retire through old age, or survive without ever earning historical recognition.

---

## **11. Updated attribute system (later discussion)**

The original discussion expanded beyond the earlier Strength/Defense model. The **current preferred four-attribute design** is:

| Attribute | Intended mechanical role |
| --- | --- |
| **Strength** | Raw damage modifier; **no longer contributes to attack accuracy** if Dexterity is adopted |
| **Dexterity** | Offensive accuracy / attack modifier |
| **Agility** | Defensive combat skill (defense bonus) **and** dodge chance |
| **Fortitude** | Maximum health, independent of armor |

**Health formula (changed):** `max_health = 90 + (Fortitude * 10)`.

Examples: Fortitude 1 → 100 HP; 5 → 140 HP; 10 → 190 HP; 20 → 290 HP.

The attribute split is a **current design direction**, not a claim that all four attributes and formulas have been implemented. Initially, Fortitude was considered as the defense-bonus stat; the subsequent preference shifted the defense bonus to Agility and kept Fortitude as raw health. The user specifically rejected treating defense as damage mitigation.

**Mechanics must remain distinct:**

- **Defense** is the chance/ability to prevent a hit through parrying, positioning, glancing deflections, or effectively presenting armor geometry. It does **not** reduce damage after a successful hit.
- **Agility** improves defense and is intended to influence a separate dodge check.
- **Armor** provides **raw damage mitigation** after a hit connects, regardless of the gladiator's defensive skill.
- **Fortitude** provides health, allowing a fighter to withstand more damage even if attacks connect.
- **Dexterity** governs whether attacks connect; **Strength** governs how much damage successful attacks inflict.

A heavily armored novice may be hit more often than a veteran but survive more landed blows. A lightly armored, skilled veteran may deflect/dodge more often yet be vulnerable when hit. An unarmored gladiator can still have high defense because defense reflects combat skill, not armor thickness.

### **Dodge and encumbrance — proposed, not balanced**

- Add a separate dodge mechanic, affected positively by Agility and negatively by armor burden.
- Earlier wording suggested an inverse relationship with “defense,” but the later conceptual clarification is that **heavy armor/encumbrance**, not defensive skill itself, should be what impedes dodging.
- No dodge probability formula, cap, armor-weight model, or resolution order is finalized. A sample formula discussed by the assistant was illustrative **only**, not an adopted design.
- The sequence of attack/defense, dodge, shield block, and armor mitigation still needs to be chosen and tested.

### **Why four attributes?**

- More attributes create more meaningful build diversity and avoid every high-level gladiator converging on the same three statistics.
- Intelligence and Wisdom were considered inappropriate to the simulator's current scope.
- Endurance/fatigue and Perception were floated as possible additional systems, **not accepted attributes**.
- Slowing attribute awards (e.g. one point every other level) was considered as an alternative but does not itself produce more build diversity.
- The exact attribute gain rate, caps, scaling functions, and level progression remain undecided.

## **12. Offensive styles and matchups**

Splitting Strength from Dexterity should enable qualitatively different fighters:

- **Powerful berserker:** Heavy blows and large weapons, generally light armor; fewer hits may be needed to win, but accuracy may suffer.
- **Fast, dexterous fighter:** Lands many precise attacks, often with smaller individual damage; may struggle to penetrate heavy armor.
- **Balanced/hybrid builds:** Combine attributes to mitigate weaknesses without necessarily matching specialists at their strengths.

Armor creates matchup-dependent outcomes: low-damage, frequent hits can be ineffective against high flat damage mitigation, while less accurate heavy strikes may penetrate it. No archetype should be guaranteed victory. Weapon choice, quality, defensive skill, HP, dodge, knockout chance, and randomness all contribute.

### **Weapon attack bonuses — confirmed range from the later discussion**

| Weapon | Base attack bonus |
| --- | ---: |
| Knife | +3 |
| Dagger | +4 |
| Mace | +5 |
| Longsword | +6 |
| Greatsword | +8 |

The **weapon-only range is +3 to +8**. An earlier configuration added Strength `strength // 3` for a +0 to +6 attribute bonus, yielding +3 to +14 combined. **That combined range is now historical**, because the later four-attribute plan transfers accuracy scaling from Strength to Dexterity. The replacement Dexterity formula and final combined attack range have **not** been decided. The earlier weapon bonus values are recorded here without assuming they have been rebalanced for the new attribute split.

## **13. NPC learning through combat experience**

NPCs should be **believable, personality-driven, and imperfect**, not hyper-optimized agents.

### **Short-term combat memory**

- Each gladiator remembers a recent window of their own combat performances.
- Relevant signals may include attack attempts, successful hits, hit rate, damage inflicted, damage suffered, opponent armor, defenses, victories, and defeats.
- NPCs evaluate persistent weaknesses and adjust future attribute spending, training, and possibly equipment purchases.
- This can be implemented with simple rules and weighted preferences; no neural network or full reinforcement-learning framework is required.

### **Personality remains the anchor**

- A **berserker** normally prioritizes Strength, heavy weapons, powerful blows, and lighter armor.
- If the berserker repeatedly misses attacks, it can temporarily invest a few attribute points in **Dexterity** to address accuracy, then return to its preferred Strength focus.
- Other personalities may react differently to the same evidence: a defensive fighter might address inadequate damage, while a fragile evasive fighter might increase Fortitude.
- Personality biases **how** an NPC responds to a problem; identical outcomes need not lead to identical decisions.
- A proposed additional nuance is different willingness or speed to adapt (e.g. stubborn vs. flexible personalities). This is **an idea**, not a finalized mechanic.

This is **learning-like adaptive behavior**: outcomes influence future choices. More precisely, the initial proposal is **rule-based adaptation informed by experience**, rather than a formally trained machine-learning policy.

### **Telemetry versus memory**

The simulator's detailed combat telemetry (section 9) can support balancing and reproducibility. Each NPC needs only a **small, personal rolling summary** for decisions. Keep full-world analytical records separate from the information that an individual gladiator is allowed to “know.”

## **14. Dialogue grounded in lived experience**

Dialogue is intended to reflect **actual simulated events, struggles, plans, and memories**, not just generic personality templates.

Possible topics:

- Complaints about repeated misses and plans to practice accuracy.
- Satisfaction with a weapon or armor piece that has proven reliable.
- Recollections of particular opponents, defeats, victories, knockouts, or broken equipment.
- Saving money for better armor versus saving to purchase freedom.
- Plans to train, fight, rest, retire, or change fighting style.
- Boasting, apprehension, frustration, grudges, rivalries, and hopes informed by personal history.

Example *illustrative* lines (not canonical script):

> “Couldn't land a proper blow in my last three fights. I'm working on my accuracy.”
>
> “Another couple of good purses and I might finally buy my freedom.”

An NPC's **beliefs and intentions need not guarantee their actions or outcomes**. A gladiator can make a plan, fail to follow it, or die before completing it. Dialogue should communicate character and recent experience while preserving the simulator's autonomy and unpredictability.

Potential implementation: generate dialogue from structured character state, recent performance summaries, personal event history, current goals, and personality. This is a **design concept**, not a completed dialogue engine.

## **15. Player career endings and continuation options (undecided)**

It has **not** been decided whether player death or retirement ends the simulation. Two ideas were discussed:

1. **New Game+** — potentially uncapped levels and a **4× freedom buyout cost**. Whether age-based retirement and other rules would change remains undecided.
2. **Fresh gladiator in a mature stable** — create a new level-one character in the **same developed simulation**, with existing veterans, history, equipment disparities, and world events still in place.

These may coexist as separate choices; neither has been committed to. The established training-dummy proposal (section 4) could help newcomers survive in an advanced stable. Persisting the world between player characters could make archived careers, reputations, and rivalries more meaningful.

## **16. Updated open questions / balancing checklist**

- Decide Dexterity-to-attack and Agility-to-defense scaling; recalculate combined attack/defense ranges.
- Decide dodge formula, armor encumbrance effects, dodge cap, and combat resolution order.
- Confirm how flat armor mitigation interacts with very weak attacks and knockout attempts.
- Determine whether Agility's **defense plus dodge** produces disproportionate survivability.
- Test Fortitude's HP scaling against fight duration, especially with uncapped levels.
- Determine attribute point frequency, any caps, and whether advanced characters become too similar.
- Define the size of an NPC's recent-fight memory and the thresholds for changing investment priorities.
- Define which events and goals NPC dialogue may reference, and how personal knowledge differs from omniscient event logs.
- Decide how player death/retirement transitions into New Game+, a new gladiator, or a final ending.

**Updated overall direction:** A persistent gladiator simulator in which four differentiated attributes, equipment, personality, adaptive decision-making, real combat histories, and dialogue grounded in actual events produce unscripted individual careers. The goal is **credible, diverse behavior**, not mathematically optimal NPCs.
