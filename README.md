# codeforces-crawler

A crawler for problems, their tutorials and best solutions on [codeforces.com](http://codeforces.com)

You will need scrapy installed to use this crawler.

# usage

    git clone https://github.com/Nymphet/codeforces-crawler.git
    
    scrapy crawl SpiderName
    
e.g., to crawl problems
    
    scrapy crawl CodeforcesProblem

add `-o` argument to save the results to a file, e.g.

    scrapy crawl CodeforcesSolution -o solutions.jl
    
use `scrapy list` to show a list of available spiders.
    

# License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# Notice

Copyright of any material you crawled from codeforces.com belongs to its author, and your usage must comply with the Codeforces materials usage license. See http://codeforces.com/blog/entry/967 for more info.

**Codeforces materials usage license (v. 0.1)**

You may publish the texts of Codeforces problems in any open sources, but you must preserve a direct link to the site http://codeforces.ru (http://codeforces.com for English statements) and indicate Codeforces as the problem source. These data should be located in the close proximity to the statement, be easily noticeable and readable. It is forbidden to publish Codeforces problems in open sources supporting automatic testing (such as online judges or similar resources).

You must not use tests and other materials of the problems (generators, checkers, validators) to publish tasks in open sources supporting automatic testing (such as online judges or similar resources) even provided the original problem conditions has been changed.

You may use the provided material: tests, generators, checkers, validators and others for individual training or to organize short-term teaching and training activities with the participants present on-site. Task conditions should contain the data from paragraph 1 of this license. The secondary (subsequent) distribution of the tasks should contain this license and comply fully with the license’s rules.
