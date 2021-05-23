1) [Anon Club site](https://youthful-minsky-60409b.netlify.app/):<br>
For this challenge inspect the _source code_ you'll get a part of the flag in index page and other parts in _css_ and _javascript_ comments.

2) [Agent](https://web-challenges-anonctf.000webhostapp.com/agent/):<br>
Change the user agent of your browser to _evilbrowser_ either [manually](https://www.howtogeek.com/113439/how-to-change-your-browsers-user-agent-without-installing-any-extensions/) or by using add-ons to your browser.

3) [Login](https://web-challenges-anonctf.000webhostapp.com/login/):<br>
If you try to login you'll notice the error message that you are not the admin. Open the developer tools check the cookies. Change the value of _admin cookie_ to _true_ and login again.

4) [Under Construction](https://web-challenges-anonctf.000webhostapp.com/underConstruction/):<br>
It's always good to check for _robots.txt_ file to see which path or file is not allowed to crawl by the search engines.

5) [Egallery](https://web-challenges-anonctf.000webhostapp.com/Egallery/):<br>
If you try to login to this site you get an error message saying Invalid Credentials. There must be some kind of check for credentials. Try sql injection.<br>
Use `' or true -- ` for the username. Which will always evaluate the condition to always true and the first entry of the sql table is returned.<br>
```MySQL
SELECT * FROM users WHERE username = 'admin' AND password = 'adminpassword'; -- This is a sql query
SELECT * FROM users WHERE username = '' or true -- AND password = '1234'; SQL injection, here everything after -- will considered a comment
```
6) [Protected Portal](https://protectedportal-anonctf.herokuapp.com/):<br>
Looking at the source code, there is obfuscated javascript. Using [JS Nice](http://jsnice.org/)
```Javascript
'use strict';
/** @type {!Array} */
var _0x575c = ["2-4", "substring", "4-7", "getItem", "deleteItem", "12-14", "0-2", "setItem", "9-12", "^7M", "updateItem", "bb=", "7-9", "14-16", "localStorage"];
(function(data, i) {
  /**
   * @param {number} isLE
   * @return {undefined}
   */
  var write = function(isLE) {
    for (; --isLE;) {
      data["push"](data["shift"]());
    }
  };
  write(++i);
})(_0x575c, 120);
/**
 * @param {string} level
 * @param {?} ai_test
 * @return {?}
 */
var _0x51ee = function(level, ai_test) {
  /** @type {number} */
  level = level - 0;
  var rowsOfColumns = _0x575c[level];
  return rowsOfColumns;
};
/**
 * @param {!Object} results
 * @return {?}
 */
function CheckPassword(results) {
  /** @type {!Array} */
  var easing = [_0x51ee("0xe"), _0x51ee("0x3"), _0x51ee("0x7"), _0x51ee("0x4"), _0x51ee("0xa")];
  window[easing[0]][easing[2]]("9-12", "BE*");
  window[easing[0]][easing[2]](_0x51ee("0x2"), _0x51ee("0xb"));
  window[easing[0]][easing[2]](_0x51ee("0x6"), "5W");
  window[easing[0]][easing[2]]("16", _0x51ee("0x9"));
  window[easing[0]][easing[2]](_0x51ee("0x5"), "pg");
  window[easing[0]][easing[2]]("7-9", "+n");
  window[easing[0]][easing[2]](_0x51ee("0xd"), "4t");
  window[easing[0]][easing[2]](_0x51ee("0x0"), "$F");
  if (window[easing[0]][easing[1]](_0x51ee("0x8")) === results[_0x51ee("0x1")](9, 12)) {
    if (window[easing[0]][easing[1]](_0x51ee("0x2")) === results["substring"](4, 7)) {
      if (window[easing[0]][easing[1]](_0x51ee("0x6")) === results[_0x51ee("0x1")](0, 2)) {
        if (window[easing[0]][easing[1]]("16") === results[_0x51ee("0x1")](16)) {
          if (window[easing[0]][easing[1]](_0x51ee("0x5")) === results[_0x51ee("0x1")](12, 14)) {
            if (window[easing[0]][easing[1]](_0x51ee("0xc")) === results[_0x51ee("0x1")](7, 9)) {
              if (window[easing[0]][easing[1]](_0x51ee("0xd")) === results[_0x51ee("0x1")](14, 16)) {
                if (window[easing[0]][easing[1]](_0x51ee("0x0")) === results[_0x51ee("0x1")](2, 4)) {
                  return !![];
                }
              }
            }
          }
        }
      }
    }
  }
  return ![];
}
;
```
Analyse the functions and understand what they do to find the flag.<br><br>

7) [Fuzzy Brother](https://oreo-anonctf.herokuapp.com/):<br>
Checking the cookies, there is a cookie called flavour. The value of this cookie is base64 encoded.<br>
In the challenge _chocolate_ flavour is mentioned. Base64 encode it and change the value of the flavour cookie to get the flag.
