# Puzzling Python

This repo contains a series of examples of strange Python behaviors. These are based on my remembrance of posts that I made while working at Meta that I thought would be fun to share.

Each folder (except experiments) corresponds to a post on [lonfarr.com](https://www.lonfarr.com). A README.md contains a link to the blog post. Each of these folders is also referenced below in the table of contents with links.

The `experiments` folder contains some smaller files that are little tests. Feel free to browse and view the README, but these files will not be as well maintained.

I'd highly recommend looking at the post on the website since it has additional information beyond what is in the code. This repo mainly serves as a place for the code to live and others to find it.

# Environment Setup
Since a fair number of the puzzles are exploring the realm of typing in Python, here is my setup for testing the code. I am using [Pyright](https://github.com/microsoft/pyright) through the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) module in [VSCode](https://code.visualstudio.com), but there are others such as [Mypy](https://mypy-lang.org) and [Pyre](https://pyre-check.org), which may yield different results. I personally find that the Pyright setup with VSCode is the easiest way to get started with type checking since it can all be installed easily in the IDE, so I opted for that configuration. To setup VSCode for strict type checking (which is my recommendation for any new code) you can add the following into the `settings.json` for VSCode:
```
    "python.analysis.typeCheckingMode": "strict",
```

I use black as my linter because it has no configuration, so it removes all of the minor lint debates (like spaces before and after equality operators). It is also easy to setup in VSCode. After installing the [black extension], I add the following to my `settings.json` file so that it uses the formatter automatically on save:
```
    "[python]": {
      "editor.defaultFormatter": "ms-python.black-formatter",
      "editor.formatOnSave": true
    },
    "black-formatter.showNotifications": "onWarning"
```

# Acknowledgements and Inspirations
I'd like to call out several locations where I learned about these quirks. While I do try to recognize them in the individual posts, I want to have a full list here along side the code to direct people to these interesting resources.
* [wtfpython GitHub](https://github.com/satwikkansal/wtfpython)
  * A great GitHub (much greater than this one) with many examples. The readme is heavily detailed and you don't really even need to look at the code in the repo. A lot of my more detailed puzzles/examples were inspired by these relatively simple examples.
* [mCoding YouTube Channel](https://www.youtube.com/@mCoding)
  * mCoding has a variety of videos on C++, Python, and Math. The Python videos do go into some depth of the inner workings of Python and led to some of the ideas for my posts.
  
# Table of Contents

* Iterable Membership Check
  * [Blog Post](https://www.lonfarr.com/posts/2025-05-18-iterable_membership_check/)
  * [Code](https://github.com/lonfarr/puzzling_python/blob/main/iterable_membership_check)
  * Published 2025-05-18
  * Updated 2025-05-23
* Iterators as Function Inputs
  * [Blog Post](https://www.lonfarr.com/posts/2025-05-26-iterators_as_function_inputs/)
  * [Code](https://github.com/lonfarr/puzzling_python/blob/main/iterators_as_function_inputs)
  * Published 2025-05-25
* How do you make a tuple?
  * [Blog Post](https://www.lonfarr.com/posts/2025-06-03-how_do_you_make_a_tuple/)
  * [Code](https://github.com/lonfarr/puzzling_python/blob/main/how_do_you_make_a_tuple)
  * Published 2025-06-03