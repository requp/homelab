## regex
### Flags
- i - case insensitive
- g - more than one entry
### Expression syntax
#### Uppercase letters
- [A-Z] - or any other range - [C-Y] and so on
#### Lowercase letters
- [a-z] - the same logic as for uppercase ones
#### Digits
- [0-9] - or any other range
- \d - all digits
#### Several character types
- \w - includes [A-Z], [a-z], [0-9] and '_'
#### Any space character (space, tab)
- \s
#### Any one character (actually every character - just it will be a new entry)
- .
#### Only one any character
- `/^.$/`
#### Not include characters from a range
- `/...[^<any-range>].../`
#### Find an entry which starts and ends with the given expression
- `/^<some-expression>$/`
#### Repeat the current part of the expression
- `/...<part-expression>+.../` - One time or more 
- `/...<part-expression>{start,end}.../` - With given amount of repeating from the start (empty means 0) to the end (empty means infinity)
#### Or statement
- `/^ba[t|d]$/` - an entry which ends on t or d letter (bad or bat)
#### Optional part of the expression
- `/...<part-expression>?.../`
#### Group one or several parts of the expression
- `/...(<part1><part2><part3>){2}.../` - repeat the group 2 times 
