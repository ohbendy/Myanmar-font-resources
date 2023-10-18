Current (18 October 2023) segmentation behaviour in different apps is extremely unpredictable. Here's what I found with the test string: အခြားတိုင်းပြည်မှလည်းကောင်း 

## Linebreaking ##
Linebreaks get added at each ! when the column width is set to a minimum

| App                   | Behaviour                                                                 |
|----------------|-------------------------------------------------|
| Firefox               | !အ!ခြား!တို!င်း!ပြ!ည်!မှ!လ!ည်း!ကော!င်း!                        |
| TextEdit/Pages | !အ!ခြား!တို!င်း!ပြ!ည်မှ!လ!ည်း!ကော!င်း!                          |
| Safari                | !အ!ခြ!ာ!း!တ!ို!င်း!ပြ!ည!်!မ!ှ!လ!ည!်း!ကေ!ာ!င်း! |
| Chrome            | !အ!ခြာ!း!တို!င်!း!ပြ!ည်!မှ!လ!ည်!း!ကေ!ာ!င်!း!        |

## Cursoring ##
Cursoring works differently in each app, ! shows valid positions the cursor can be clicked or moved with arrow keys:

| App                       | Behaviour                                                             |
|------------------|-----------------------------------------------|
| Firefox/TextEdit   | !အ!ခြား!တို!င်း!ပြ!ည်!မှ!လ!ည်း!ကော!င်း!                     |
| Safari/Pages        | !အ!ခြား!တို!င်း!ပြ!ည်မှ!လ!ည်း!ကော!င်း!                      |
| Chrome                | !အ!ခြ!ာ!း!တို!င်!း!ပြ!ည်!မှ!လ!ည်!း!ကေ!ာ!င်!း! |

## Backspacing ##
Firefox/TextEdit/Safari/Pages/Chrome: one backspace removes one character.

TextMate: one backspace removes a whole cluster !အ!ခြား!တို!င်း!ပြ!ည်!မှ!လ!ည်း!ကော!င်း! 

## Selecting text ##
When double clicking on text, how is it segmented into selectable parts?

| App                    | Behaviour                                      |
|-----------------|---------------------------------|
| Firefox/Chrome | !အခြား!တိုင်းပြည်!မှလည်းကောင်း!       |
| TextEdit             | !အခြား!တိုင်းပြ!ည်မှ!လည်းကောင်း!      |
| Safari/Pages      | !အခြား!တိုင်းပြည်မှ!လည်းကောင်း!      |


