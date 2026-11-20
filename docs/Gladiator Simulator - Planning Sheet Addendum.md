# Gladiator Simulator — Planning Sheet Addendum

This addendum records decisions visible in the referenced chat. Merge it into the original planning sheet when that file is available. Keep the original exhibition payout rules.

## Confirmed design decisions

| Topic | Decision |
| --- | --- |
| Sacred arena sands | Only one fight can take place on the sands at a time. A group battle occupies the sands as one fight. |
| Organizer events | The arena organizer schedules obligatory events for a specific in-game day and time. These events pay more than voluntary exhibitions. |
| Selection and start | Alert the player when selected for an organizer ticket. At the scheduled day and time, force a selected player into combat mode. An ongoing bout must finish before a new fight begins on the sands. |
| Voluntary exhibitions | Use the established rules for determining fight payouts. Add a fight ticket to the roster once the challenge is accepted. |
| Changes before a bout is called | Either fighter may cancel or choose another opponent before the bout is called. Remove the original ticket from the roster. If the fighter chooses a new opponent, add the replacement ticket when the new challenge is accepted. |
| Exhibition forfeits | When the player's ticket is called, start an action-based grace period for reaching the sands. If the player misses the deadline, record a loss, award no XP, and deduct a small monetary fine. |
| Organizer priority | When an organizer ticket takes precedence, let the fight already in progress finish, then clear the queued voluntary roster. Clearing carries no penalty. Cleared tickets stay off the roster after the organizer event ends. |

## Tentative ideas and open details

| Topic | Current idea or open decision |
| --- | --- |
| Organizer identity | The stable owner or colosseum director could organize events. Whether to build a storyteller AI for the role remains open. |
| Event formats | Group battles and special ticket fights are candidate formats. |
| Exhibition grace period | Try three actions from the call. The final limit is open. |
| Payout and fine amounts | The organizer payout premium and the exhibition forfeit fine are open. |
| Scheduling overlap | The one-fight limit and the right of an ongoing bout to finish are established. The exact timing of the forced combat transition if the sands are occupied at the scheduled time remains open. |

## Implementation note from the chat

During normal gameplay, the equipment list contains valid equipment instances. Keep the empty-list check before reading the first item. Debug sessions can deliberately inject a None selection to exercise the cancellation path and verify that it leaves inventory and money intact.
