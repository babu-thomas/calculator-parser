## TODO
[ ] Append newline to input string inside InputStream instead of caller passing a string ending with newline
[ ] Only expose Parser to caller and handle InputStream and TokenStream inside Parser
[ ] Fix bug where continuous operator tokens without space is lexed as a single token