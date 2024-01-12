Current (18 October 2023) segmentation behaviour in different apps is extremely unpredictable. The test string is အခြားတိုင်းပြည်မှလည်းကောင်း and the recommended breakpoints are ·အခြား·တိုင်း·ပြည်·မှ·လည်းကောင်း· 

## Linebreaking ##
Linebreaks get added at each · when the column width is set to a minimum

| App            | Behaviour                                       | Notes |
|----------------|-------------------------------------------------|-------|
| Chrome         | ·အ·ခြာ·း·တို·င်·း·ပြ·ည်·မှ·လ·ည်·း·ကေ·ာ·င်·း·     |       |
| Firefox        | ·အ·ခြား·တို·င်း·ပြ·ည်·မှ·လ·ည်း·ကော·င်း·                |       |
| Pages          | ·အ·ခြား·တို·င်း·ပြ·ည်မှ·လ·ည်း·ကော·င်း·                 |       |
| Safari         | ·အ·ခြ·ာ·း·တ·ို·င်း·ပြ·ည·်·မ·ှ·လ·ည·်း·ကေ·ာ·င်း· |       |
| TextEdit       | ·အ·ခြား·တို·င်း·ပြ·ည်မှ·လ·ည်း·ကော·င်း·                 |       |
| TextMate       | Burmese text doesn't wrap                       |       |

## Cursoring ##
Cursoring works differently in each app, · shows valid positions the cursor can be clicked or moved with arrow keys:

| App              | Behaviour                                     | Notes |
|------------------|-----------------------------------------------|-------|
| Chrome           | ·အ·ခြ·ာ·း·တို·င်·း·ပြ·ည်·မှ·လ·ည်·း·ကေ·ာ·င်·း· | Cursor can be placed between spacing characters except medials and 1031|
| Firefox          | ·အ·ခြား·တို·င်း·ပြ·ည်·မှ·လ·ည်း·ကော·င်း·             | Cursor can be placed between grapheme clusters |
| Pages            | ·အ·ခြား·တို·င်း·ပြ·ည်မှ·လ·ည်း·ကော·င်း·              | Cursor can be placed between grapheme clusters except after asat |
| Safari           | ·အ·ခြား·တို·င်း·ပြ·ည်မှ·လ·ည်း·ကော·င်း·              | Cursor can be placed between grapheme clusters except after asat |
| TextEdit         | ·အ·ခြား·တို·င်း·ပြ·ည်·မှ·လ·ည်း·ကော·င်း·             | Cursor can be placed between grapheme clusters |
| TextMate         | ·အ·ခြား·တို·င်း·ပြ·ည်·မှ·လ·ည်း·ကော·င်း·             | Cursor can be placed between grapheme clusters |


## Backspacing ##

| App              | Behaviour                                                         | Notes                                 |
|------------------|-----------------------------------------------------------------  |---------------------------------------|
| Chrome           | ·အ·ခ·ြ·ာ·း·တ·ိ·ု·င·်·း·ပ·ြ·ည·်·မ·ှ·လ·ည·်·း·က·ေ·ာ·င·်·း· | One backspace removes one character   |
| Firefox          | ·အ·ခ·ြ·ာ·း·တ·ိ·ု·င·်·း·ပ·ြ·ည·်·မ·ှ·လ·ည·်·း·က·ေ·ာ·င·်·း· | One backspace removes one character   |
| Pages            | ·အ·ခ·ြ·ာ·း·တ·ိ·ု·င·်·း·ပ·ြ·ည·်·မ·ှ·လ·ည·်·း·က·ေ·ာ·င·်·း· | One backspace removes one character   |
| Safari           | ·အ·ခ·ြ·ာ·း·တ·ိ·ု·င·်·း·ပ·ြ·ည·်·မ·ှ·လ·ည·်·း·က·ေ·ာ·င·်·း· | One backspace removes one character   |
| TextEdit         | ·အ·ခ·ြ·ာ·း·တ·ိ·ု·င·်·း·ပ·ြ·ည·်·မ·ှ·လ·ည·်·း·က·ေ·ာ·င·်·း· | One backspace removes one character   |
| TextMate         | ·အ·ခြား·တို·င်း·ပြ·ည်·မှ·လ·ည်း·ကော·င်း·                                  | One backspace removes a whole cluster |

## Selecting text ##
When double clicking on text, how is it segmented into selectable parts?

| App              | Behaviour                  | Notes |
|------------------|----------------------------|-------|
| Chrome           | ·အခြား·တိုင်းပြည်·မှလည်းကောင်း·  |       |
| Firefox          | ·အခြား·တိုင်းပြည်·မှလည်းကောင်း·  |       |
| Pages            | ·အခြား·တိုင်းပြည်မှ·လည်းကောင်း·  |       |
| Safari           | ·အခြား·တိုင်းပြည်မှ·လည်းကောင်း·  |       |
| TextEdit         | ·အခြား·တိုင်းပြ·ည်မှ·လည်းကောင်း· |       |
| TextMate         | ·အခြားတိုင်းပြည်မှလည်းကောင်း·    |       |


