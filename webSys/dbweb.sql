/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50631
Source Host           : localhost:3306
Source Database       : dbweb

Target Server Type    : MYSQL
Target Server Version : 50631
File Encoding         : 65001

Date: 2016-11-23 20:13:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('ecb5cbcf4f99');

-- ----------------------------
-- Table structure for articles
-- ----------------------------
DROP TABLE IF EXISTS `articles`;
CREATE TABLE `articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL,
  `content` text NOT NULL,
  `visitNum` int(11) DEFAULT NULL,
  `updatedTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of articles
-- ----------------------------
INSERT INTO `articles` VALUES ('1', '证券模拟投资平台-需求文档', '## 概述\r\n本系统是一个用于帮助用户学习证券投资的虚拟交易平台，用户在该平台上进行模拟的\r\n证券投资。\r\n\r\n用户可进行的主要行为有：\r\n\r\n- 注册与登录证券投资账户\r\n- 查看证券市场信息，以及单个证券的详细情况（实时）\r\n- 选择交易某个证券，经过一段时间后可查看账户盈利状况\r\n- 查看资讯\r\n- 发布或评论主题贴\r\n\r\n## 功能模块设计\r\n\r\n### 用户管理\r\n\r\n- 用户使用个人邮箱注册账号，并经过邮箱验证\r\n- 用户登录\r\n- 用户通过个人邮箱找回密码\r\n- 用户的一些个人信息设置\r\n- 用户查询账户交易记录\r\n\r\n### 投资信息\r\n\r\n- 用户查看整体市场行情（如沪指、深指等反映股票市场的重要指标）\r\n- 用户查看具体某只证券的详细信息与实时走势\r\n- 用户买进某只证券，或卖出已有的某只证券\r\n- 用户查看某段时间的账户盈利情况\r\n\r\n### 用户社区', '20', '2016-11-05 15:09:55');
INSERT INTO `articles` VALUES ('2', 'Markdown 语法说明 (简体中文版)', '\r\n*   [概述](#overview)\r\n    *   [宗旨](#philosophy)\r\n    *   [兼容 HTML](#html)\r\n    *   [特殊字符自动转换](#autoescape)\r\n*   [区块元素](#block)\r\n    *   [段落和换行](#p)\r\n    *   [标题](#header)\r\n    *   [区块引用](#blockquote)\r\n    *   [列表](#list)\r\n    *   [代码区块](#precode)\r\n    *   [分隔线](#hr)\r\n*   [区段元素](#span)\r\n    *   [链接](#link)\r\n    *   [强调](#em)\r\n    *   [代码](#code)\r\n    *   [图片](#img)\r\n*   [其它](#misc)\r\n    *   [反斜杠](#backslash)\r\n    *   [自动链接](#autolink)\r\n*   [感谢](#acknowledgement)\r\n*	[Markdown 免费编辑器](#editor)\r\n\r\n* * *\r\n\r\n<h2 id=\"overview\">概述</h2>\r\n\r\n<h3 id=\"philosophy\">宗旨</h3>\r\n\r\nMarkdown 的目标是实现「易读易写」。\r\n\r\n可读性，无论如何，都是最重要的。一份使用 Markdown 格式撰写的文件应该可以直接以纯文本发布，并且看起来不会像是由许多标签或是格式指令所构成。Markdown 语法受到一些既有 text-to-HTML 格式的影响，包括 [Setext] [1]、[atx] [2]、[Textile] [3]、[reStructuredText] [4]、[Grutatext] [5] 和 [EtText] [6]，而最大灵感来源其实是纯文本电子邮件的格式。\r\n\r\n  [1]: http://docutils.sourceforge.net/mirror/setext.html\r\n  [2]: http://www.aaronsw.com/2002/atx/\r\n  [3]: http://textism.com/tools/textile/\r\n  [4]: http://docutils.sourceforge.net/rst.html\r\n  [5]: http://www.triptico.com/software/grutatxt.html\r\n  [6]: http://ettext.taint.org/doc/\r\n\r\n总之， Markdown 的语法全由一些符号所组成，这些符号经过精挑细选，其作用一目了然。比如：在文字两旁加上星号，看起来就像\\*强调\\*。Markdown 的列表看起来，嗯，就是列表。Markdown 的区块引用看起来就真的像是引用一段文字，就像你曾在电子邮件中见过的那样。\r\n\r\n<h3 id=\"html\">兼容 HTML</h3>\r\n\r\nMarkdown 语法的目标是：成为一种适用于网络的*书写*语言。\r\n\r\nMarkdown 不是想要取代 HTML，甚至也没有要和它相近，它的语法种类很少，只对应 HTML 标记的一小部分。Markdown 的构想*不是*要使得 HTML 文档更容易书写。在我看来， HTML 已经很容易写了。Markdown 的理念是，能让文档更容易读、写和随意改。HTML 是一种*发布*的格式，Markdown 是一种*书写*的格式。就这样，Markdown 的格式语法只涵盖纯文本可以涵盖的范围。\r\n\r\n不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。不需要额外标注这是 HTML 或是 Markdown；只要直接加标签就可以了。\r\n\r\n要制约的只有一些 HTML 区块元素――比如 `<div>`、`<table>`、`<pre>`、`<p>` 等标签，必须在前后加上空行与其它内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。Markdown 的生成器有足够智能，不会在 HTML 区块标签外加上不必要的 `<p>` 标签。\r\n\r\n例子如下，在 Markdown 文件里加上一段 HTML 表格：\r\n\r\n    这是一个普通段落。\r\n\r\n    <table>\r\n        <tr>\r\n            <td>Foo</td>\r\n        </tr>\r\n    </table>\r\n\r\n    这是另一个普通段落。\r\n\r\n请注意，在 HTML 区块标签间的 Markdown 格式语法将不会被处理。比如，你在 HTML 区块内使用 Markdown 样式的`*强调*`会没有效果。\r\n\r\nHTML 的区段（行内）标签如 `<span>`、`<cite>`、`<del>` 可以在 Markdown 的段落、列表或是标题里随意使用。依照个人习惯，甚至可以不用 Markdown 格式，而直接采用 HTML 标签来格式化。举例说明：如果比较喜欢 HTML 的 `<a>` 或 `<img>` 标签，可以直接使用这些标签，而不用 Markdown 提供的链接或是图像标签语法。\r\n\r\n和处在 HTML 区块标签间不同，Markdown 语法在 HTML 区段标签间是有效的。\r\n\r\n<h3 id=\"autoescape\">特殊字符自动转换</h3>\r\n\r\n在 HTML 文件中，有两个字符需要特殊处理： `<` 和 `&` 。 `<` 符号用于起始标签，`&` 符号则用于标记 HTML 实体，如果你只是想要显示这些字符的原型，你必须要使用实体的形式，像是 `&lt;` 和 `&amp;`。\r\n\r\n`&` 字符尤其让网络文档编写者受折磨，如果你要打「`AT&T`」 ，你必须要写成「`AT&amp;T`」。而网址中的 `&` 字符也要转换。比如你要链接到：\r\n\r\n    http://images.google.com/images?num=30&q=larry+bird\r\n\r\n你必须要把网址转换写为：\r\n\r\n    http://images.google.com/images?num=30&amp;q=larry+bird\r\n\r\n才能放到链接标签的 `href` 属性里。不用说也知道这很容易忽略，这也可能是 HTML 标准检验所检查到的错误中，数量最多的。\r\n\r\nMarkdown 让你可以自然地书写字符，需要转换的由它来处理好了。如果你使用的 `&` 字符是 HTML 字符实体的一部分，它会保留原状，否则它会被转换成 `&amp`;。\r\n\r\n所以你如果要在文档中插入一个版权符号 `©`，你可以这样写：\r\n\r\n    &copy;\r\n\r\nMarkdown 会保留它不动。而若你写：\r\n\r\n    AT&T\r\n\r\nMarkdown 就会将它转为：\r\n\r\n    AT&amp;T\r\n\r\n类似的状况也会发生在 `<` 符号上，因为 Markdown 允许 [兼容 HTML](#html) ，如果你是把 `<` 符号作为 HTML 标签的定界符使用，那 Markdown 也不会对它做任何转换，但是如果你写：\r\n\r\n    4 < 5\r\n\r\nMarkdown 将会把它转换为：\r\n\r\n    4 &lt; 5\r\n\r\n不过需要注意的是，code 范围内，不论是行内还是区块， `<` 和 `&` 两个符号都*一定*会被转换成 HTML 实体，这项特性让你可以很容易地用 Markdown 写 HTML code （和 HTML 相对而言， HTML 语法中，你要把所有的 `<` 和 `&` 都转换为 HTML 实体，才能在 HTML 文件里面写出 HTML code。）\r\n\r\n* * *\r\n\r\n<h2 id=\"block\">区块元素</h2>\r\n\r\n\r\n<h3 id=\"p\">段落和换行</h3>\r\n\r\n一个 Markdown 段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行（空行的定义是显示上看起来像是空的，便会被视为空行。比方说，若某一行只包含空格和制表符，则该行也会被视为空行）。普通段落不该用空格或制表符来缩进。\r\n\r\n「由一个或多个连续的文本行组成」这句话其实暗示了 Markdown 允许段落内的强迫换行（插入换行符），这个特性和其他大部分的 text-to-HTML 格式不一样（包括 Movable Type 的「Convert Line Breaks」选项），其它的格式会把每个换行符都转成 `<br />` 标签。\r\n\r\n如果你*确实*想要依赖 Markdown 来插入 `<br />` 标签的话，在插入处先按入两个以上的空格然后回车。\r\n\r\n的确，需要多费点事（多加空格）来产生 `<br />` ，但是简单地「每个换行都转换为 `<br />`」的方法在 Markdown 中并不适合， Markdown 中 email 式的 [区块引用][bq] 和多段落的 [列表][l] 在使用换行来排版的时候，不但更好用，还更方便阅读。\r\n\r\n  [bq]: #blockquote\r\n  [l]:  #list\r\n\r\n<h3 id=\"header\">标题</h3>\r\n\r\nMarkdown 支持两种标题的语法，类 [Setext] [1] 和类 [atx] [2] 形式。\r\n\r\n类 Setext 形式是用底线的形式，利用 `=` （最高阶标题）和 `-` （第二阶标题），例如：\r\n\r\n    This is an H1\r\n    =============\r\n\r\n    This is an H2\r\n    -------------\r\n\r\n任何数量的 `=` 和 `-` 都可以有效果。\r\n\r\n类 Atx 形式则是在行首插入 1 到 6 个 `#` ，对应到标题 1 到 6 阶，例如：\r\n\r\n    # 这是 H1\r\n\r\n    ## 这是 H2\r\n\r\n    ###### 这是 H6\r\n\r\n你可以选择性地「闭合」类 atx 样式的标题，这纯粹只是美观用的，若是觉得这样看起来比较舒适，你就可以在行尾加上 `#`，而行尾的 `#` 数量也不用和开头一样（行首的井字符数量决定标题的阶数）：\r\n\r\n    # 这是 H1 #\r\n\r\n    ## 这是 H2 ##\r\n\r\n    ### 这是 H3 ######\r\n\r\n\r\n<h3 id=\"blockquote\">区块引用 Blockquotes</h3>\r\n\r\nMarkdown 标记区块引用是使用类似 email 中用 `>` 的引用方式。如果你还熟悉在 email 信件中的引言部分，你就知道怎么在 Markdown 文件中建立一个区块引用，那会看起来像是你自己先断好行，然后在每行的最前面加上 `>` ：\r\n\r\n    > This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,\r\n    > consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.\r\n    > Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.\r\n    > \r\n    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse\r\n    > id sem consectetuer libero luctus adipiscing.\r\n效果就像：\r\n> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,\r\n> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.\r\n> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.\r\n> \r\n> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse\r\n> id sem consectetuer libero luctus adipiscing.\r\n\r\nMarkdown 也允许你偷懒只在整个段落的第一行最前面加上 `>` ：\r\n\r\n    > This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,\r\n    consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.\r\n    Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.\r\n\r\n    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse\r\n    id sem consectetuer libero luctus adipiscing.\r\n\r\n区块引用可以嵌套（例如：引用内的引用），只要根据层次加上不同数量的 `>` ：\r\n\r\n    > This is the first level of quoting.\r\n    >\r\n    > > This is nested blockquote.\r\n    >\r\n    > Back to the first level.\r\n\r\n引用的区块内也可以使用其他的 Markdown 语法，包括标题、列表、代码区块等：\r\n\r\n	> ## 这是一个标题。\r\n	> \r\n	> 1.   这是第一行列表项。\r\n	> 2.   这是第二行列表项。\r\n	> \r\n	> 给出一些例子代码：\r\n	> \r\n	>     return shell_exec(\"echo $input | $markdown_script\");\r\n\r\n任何像样的文本编辑器都能轻松地建立 email 型的引用。例如在 BBEdit 中，你可以选取文字后然后从选单中选择*增加引用阶层*。\r\n\r\n<h3 id=\"list\">列表</h3>\r\n\r\nMarkdown 支持有序列表和无序列表。\r\n\r\n无序列表使用星号、加号或是减号作为列表标记：\r\n\r\n    *   Red\r\n    *   Green\r\n    *   Blue\r\n\r\n等同于：\r\n\r\n    +   Red\r\n    +   Green\r\n    +   Blue\r\n\r\n也等同于：\r\n\r\n    -   Red\r\n    -   Green\r\n    -   Blue\r\n\r\n有序列表则使用数字接着一个英文句点：\r\n\r\n    1.  Bird\r\n    2.  McHale\r\n    3.  Parish\r\n\r\n很重要的一点是，你在列表标记上使用的数字并不会影响输出的 HTML 结果，上面的列表所产生的 HTML 标记为：\r\n\r\n    <ol>\r\n    <li>Bird</li>\r\n    <li>McHale</li>\r\n    <li>Parish</li>\r\n    </ol>\r\n\r\n如果你的列表标记写成：\r\n\r\n    1.  Bird\r\n    1.  McHale\r\n    1.  Parish\r\n\r\n或甚至是：\r\n\r\n    3. Bird\r\n    1. McHale\r\n    8. Parish\r\n\r\n你都会得到完全相同的 HTML 输出。重点在于，你可以让 Markdown 文件的列表数字和输出的结果相同，或是你懒一点，你可以完全不用在意数字的正确性。\r\n\r\n如果你使用懒惰的写法，建议第一个项目最好还是从 1. 开始，因为 Markdown 未来可能会支持有序列表的 start 属性。\r\n\r\n列表项目标记通常是放在最左边，但是其实也可以缩进，最多 3 个空格，项目标记后面则一定要接着至少一个空格或制表符。\r\n\r\n要让列表看起来更漂亮，你可以把内容用固定的缩进整理好：\r\n\r\n    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\r\n        Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,\r\n        viverra nec, fringilla in, laoreet vitae, risus.\r\n    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.\r\n        Suspendisse id sem consectetuer libero luctus adipiscing.\r\n\r\n但是如果你懒，那也行：\r\n\r\n    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\r\n    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,\r\n    viverra nec, fringilla in, laoreet vitae, risus.\r\n    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.\r\n    Suspendisse id sem consectetuer libero luctus adipiscing.\r\n\r\n如果列表项目间用空行分开，在输出 HTML 时 Markdown 就会将项目内容用 `<p>` \r\n标签包起来，举例来说：\r\n\r\n    *   Bird\r\n    *   Magic\r\n\r\n会被转换为：\r\n\r\n    <ul>\r\n    <li>Bird</li>\r\n    <li>Magic</li>\r\n    </ul>\r\n\r\n但是这个：\r\n\r\n    *   Bird\r\n\r\n    *   Magic\r\n\r\n会被转换为：\r\n\r\n    <ul>\r\n    <li><p>Bird</p></li>\r\n    <li><p>Magic</p></li>\r\n    </ul>\r\n\r\n列表项目可以包含多个段落，每个项目下的段落都必须缩进 4 个空格或是 1 个制表符：\r\n\r\n    1.  This is a list item with two paragraphs. Lorem ipsum dolor\r\n        sit amet, consectetuer adipiscing elit. Aliquam hendrerit\r\n        mi posuere lectus.\r\n\r\n        Vestibulum enim wisi, viverra nec, fringilla in, laoreet\r\n        vitae, risus. Donec sit amet nisl. Aliquam semper ipsum\r\n        sit amet velit.\r\n\r\n    2.  Suspendisse id sem consectetuer libero luctus adipiscing.\r\n\r\n如果你每行都有缩进，看起来会看好很多，当然，再次地，如果你很懒惰，Markdown 也允许：\r\n\r\n    *   This is a list item with two paragraphs.\r\n\r\n        This is the second paragraph in the list item. You\'re\r\n    only required to indent the first line. Lorem ipsum dolor\r\n    sit amet, consectetuer adipiscing elit.\r\n\r\n    *   Another item in the same list.\r\n\r\n如果要在列表项目内放进引用，那 `>` 就需要缩进：\r\n\r\n    *   A list item with a blockquote:\r\n\r\n        > This is a blockquote\r\n        > inside a list item.\r\n\r\n如果要放代码区块的话，该区块就需要缩进*两次*，也就是 8 个空格或是 2 个制表符：\r\n\r\n    *   一列表项包含一个列表区块：\r\n\r\n            <代码写在这>\r\n\r\n\r\n当然，项目列表很可能会不小心产生，像是下面这样的写法：\r\n\r\n    1986. What a great season.\r\n\r\n换句话说，也就是在行首出现*数字-句点-空白*，要避免这样的状况，你可以在句点前面加上反斜杠。\r\n\r\n    1986\\. What a great season.\r\n\r\n<h3 id=\"precode\">代码区块</h3>\r\n\r\n和程序相关的写作或是标签语言原始码通常会有已经排版好的代码区块，通常这些区块我们并不希望它以一般段落文件的方式去排版，而是照原来的样子显示，Markdown 会用 `<pre>` 和 `<code>` 标签来把代码区块包起来。\r\n\r\n要在 Markdown 中建立代码区块很简单，只要简单地缩进 4 个空格或是 1 个制表符就可以，例如，下面的输入：\r\n\r\n    这是一个普通段落：\r\n\r\n        这是一个代码区块。\r\n\r\nMarkdown 会转换成：\r\n\r\n    <p>这是一个普通段落：</p>\r\n\r\n    <pre><code>这是一个代码区块。\r\n    </code></pre>\r\n\r\n这个每行一阶的缩进（4 个空格或是 1 个制表符），都会被移除，例如：\r\n\r\n    Here is an example of AppleScript:\r\n\r\n        tell application \"Foo\"\r\n            beep\r\n        end tell\r\n\r\n会被转换为：\r\n\r\n    <p>Here is an example of AppleScript:</p>\r\n\r\n    <pre><code>tell application \"Foo\"\r\n        beep\r\n    end tell\r\n    </code></pre>\r\n\r\n一个代码区块会一直持续到没有缩进的那一行（或是文件结尾）。\r\n\r\n在代码区块里面， `&` 、 `<` 和 `>` 会自动转成 HTML 实体，这样的方式让你非常容易使用 Markdown 插入范例用的 HTML 原始码，只需要复制贴上，再加上缩进就可以了，剩下的 Markdown 都会帮你处理，例如：\r\n\r\n        <div class=\"footer\">\r\n            &copy; 2004 Foo Corporation\r\n        </div>\r\n\r\n会被转换为：\r\n\r\n    <pre><code>&lt;div class=\"footer\"&gt;\r\n        &amp;copy; 2004 Foo Corporation\r\n    &lt;/div&gt;\r\n    </code></pre>\r\n\r\n代码区块中，一般的 Markdown 语法不会被转换，像是星号便只是星号，这表示你可以很容易地以 Markdown 语法撰写 Markdown 语法相关的文件。\r\n\r\n<h3 id=\"hr\">分隔线</h3>\r\n\r\n你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：\r\n\r\n    * * *\r\n\r\n    ***\r\n\r\n    *****\r\n\r\n    - - -\r\n\r\n    ---------------------------------------\r\n\r\n\r\n* * *\r\n\r\n<h2 id=\"span\">区段元素</h2>\r\n\r\n<h3 id=\"link\">链接</h3>\r\n\r\nMarkdown 支持两种形式的链接语法： *行内式*和*参考式*两种形式。\r\n\r\n不管是哪一种，链接文字都是用 [方括号] 来标记。\r\n\r\n要建立一个*行内式*的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可，例如：\r\n\r\n    This is [an example](http://example.com/ \"Title\") inline link.\r\n\r\n    [This link](http://example.net/) has no title attribute.\r\n\r\n会产生：\r\n\r\n    <p>This is <a href=\"http://example.com/\" title=\"Title\">\r\n    an example</a> inline link.</p>\r\n\r\n    <p><a href=\"http://example.net/\">This link</a> has no\r\n    title attribute.</p>\r\n\r\n如果你是要链接到同样主机的资源，你可以使用相对路径：\r\n\r\n    See my [About](/about/) page for details.   \r\n\r\n*参考式*的链接是在链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记：\r\n\r\n    This is [an example][id] reference-style link.\r\n\r\n你也可以选择性地在两个方括号中间加上一个空格：\r\n\r\n    This is [an example] [id] reference-style link.\r\n\r\n接着，在文件的任意处，你可以把这个标记的链接内容定义出来：\r\n\r\n    [id]: http://example.com/  \"Optional Title Here\"\r\n\r\n链接内容定义的形式为：\r\n\r\n*   方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字\r\n*   接着一个冒号\r\n*   接着一个以上的空格或制表符\r\n*   接着链接的网址\r\n*   选择性地接着 title 内容，可以用单引号、双引号或是括弧包着\r\n\r\n下面这三种链接的定义都是相同：\r\n\r\n	[foo]: http://example.com/  \"Optional Title Here\"\r\n	[foo]: http://example.com/  \'Optional Title Here\'\r\n	[foo]: http://example.com/  (Optional Title Here)\r\n\r\n**请注意：**有一个已知的问题是 Markdown.pl 1.0.1 会忽略单引号包起来的链接 title。\r\n\r\n链接网址也可以用方括号包起来：\r\n\r\n    [id]: <http://example.com/>  \"Optional Title Here\"\r\n\r\n你也可以把 title 属性放到下一行，也可以加一些缩进，若网址太长的话，这样会比较好看：\r\n\r\n    [id]: http://example.com/longish/path/to/resource/here\r\n        \"Optional Title Here\"\r\n\r\n网址定义只有在产生链接的时候用到，并不会直接出现在文件之中。\r\n\r\n链接辨别标签可以有字母、数字、空白和标点符号，但是并*不*区分大小写，因此下面两个链接是一样的：\r\n\r\n	[link text][a]\r\n	[link text][A]\r\n\r\n*隐式链接标记*功能让你可以省略指定链接标记，这种情形下，链接标记会视为等同于链接文字，要用隐式链接标记只要在链接文字后面加上一个空的方括号，如果你要让 \"Google\" 链接到 google.com，你可以简化成：\r\n\r\n	[Google][]\r\n\r\n然后定义链接内容：\r\n\r\n	[Google]: http://google.com/\r\n\r\n由于链接文字可能包含空白，所以这种简化型的标记内也许包含多个单词：\r\n\r\n	Visit [Daring Fireball][] for more information.\r\n\r\n然后接着定义链接：\r\n\r\n	[Daring Fireball]: http://daringfireball.net/\r\n\r\n链接的定义可以放在文件中的任何一个地方，我比较偏好直接放在链接出现段落的后面，你也可以把它放在文件最后面，就像是注解一样。\r\n\r\n下面是一个参考式链接的范例：\r\n\r\n    I get 10 times more traffic from [Google] [1] than from\r\n    [Yahoo] [2] or [MSN] [3].\r\n\r\n      [1]: http://google.com/        \"Google\"\r\n      [2]: http://search.yahoo.com/  \"Yahoo Search\"\r\n      [3]: http://search.msn.com/    \"MSN Search\"\r\n\r\n如果改成用链接名称的方式写：\r\n\r\n    I get 10 times more traffic from [Google][] than from\r\n    [Yahoo][] or [MSN][].\r\n\r\n      [google]: http://google.com/        \"Google\"\r\n      [yahoo]:  http://search.yahoo.com/  \"Yahoo Search\"\r\n      [msn]:    http://search.msn.com/    \"MSN Search\"\r\n\r\n上面两种写法都会产生下面的 HTML。\r\n\r\n    <p>I get 10 times more traffic from <a href=\"http://google.com/\"\r\n    title=\"Google\">Google</a> than from\r\n    <a href=\"http://search.yahoo.com/\" title=\"Yahoo Search\">Yahoo</a>\r\n    or <a href=\"http://search.msn.com/\" title=\"MSN Search\">MSN</a>.</p>\r\n\r\n下面是用行内式写的同样一段内容的 Markdown 文件，提供作为比较之用：\r\n\r\n    I get 10 times more traffic from [Google](http://google.com/ \"Google\")\r\n    than from [Yahoo](http://search.yahoo.com/ \"Yahoo Search\") or\r\n    [MSN](http://search.msn.com/ \"MSN Search\").\r\n\r\n参考式的链接其实重点不在于它比较好写，而是它比较好读，比较一下上面的范例，使用参考式的文章本身只有 81 个字符，但是用行内形式的却会增加到 176 个字元，如果是用纯 HTML 格式来写，会有 234 个字元，在 HTML 格式中，标签比文本还要多。\r\n\r\n使用 Markdown 的参考式链接，可以让文件更像是浏览器最后产生的结果，让你可以把一些标记相关的元数据移到段落文字之外，你就可以增加链接而不让文章的阅读感觉被打断。\r\n\r\n<h3 id=\"em\">强调</h3>\r\n\r\nMarkdown 使用星号（`*`）和底线（`_`）作为标记强调字词的符号，被 `*` 或 `_` 包围的字词会被转成用 `<em>` 标签包围，用两个 `*` 或 `_` 包起来的话，则会被转成 `<strong>`，例如：\r\n\r\n    *single asterisks*\r\n\r\n    _single underscores_\r\n\r\n    **double asterisks**\r\n\r\n    __double underscores__\r\n\r\n会转成：\r\n\r\n    <em>single asterisks</em>\r\n\r\n    <em>single underscores</em>\r\n\r\n    <strong>double asterisks</strong>\r\n\r\n    <strong>double underscores</strong>\r\n\r\n你可以随便用你喜欢的样式，唯一的限制是，你用什么符号开启标签，就要用什么符号结束。\r\n\r\n强调也可以直接插在文字中间：\r\n\r\n    un*frigging*believable\r\n\r\n但是**如果你的 `*` 和 `_` 两边都有空白的话，它们就只会被当成普通的符号**。\r\n\r\n如果要在文字前后直接插入普通的星号或底线，你可以用反斜线：\r\n\r\n    \\*this text is surrounded by literal asterisks\\*\r\n\r\n<h3 id=\"code\">代码</h3>\r\n\r\n如果要标记一小段行内代码，你可以用反引号把它包起来（`` ` ``），例如：\r\n\r\n    Use the `printf()` function.\r\n\r\n会产生：\r\n\r\n    <p>Use the <code>printf()</code> function.</p>\r\n\r\n如果要在代码区段内插入反引号，你可以用多个反引号来开启和结束代码区段：\r\n\r\n    ``There is a literal backtick (`) here.``\r\n\r\n这段语法会产生：\r\n\r\n    <p><code>There is a literal backtick (`) here.</code></p>\r\n\r\n代码区段的起始和结束端都可以放入一个空白，起始端后面一个，结束端前面一个，这样你就可以在区段的一开始就插入反引号：\r\n\r\n	A single backtick in a code span: `` ` ``\r\n	\r\n	A backtick-delimited string in a code span: `` `foo` ``\r\n\r\n会产生：\r\n\r\n	<p>A single backtick in a code span: <code>`</code></p>\r\n	\r\n	<p>A backtick-delimited string in a code span: <code>`foo`</code></p>\r\n\r\n在代码区段内，`&` 和方括号**都**会被自动地转成 HTML 实体，这使得插入 HTML 原始码变得很容易，Markdown 会把下面这段：\r\n\r\n    Please don\'t use any `<blink>` tags.\r\n\r\n转为：\r\n\r\n    <p>Please don\'t use any <code>&lt;blink&gt;</code> tags.</p>\r\n\r\n你也可以这样写：\r\n\r\n    `&#8212;` is the decimal-encoded equivalent of `&mdash;`.\r\n\r\n以产生：\r\n\r\n    <p><code>&amp;#8212;</code> is the decimal-encoded\r\n    equivalent of <code>&amp;mdash;</code>.</p>\r\n\r\n\r\n\r\n<h3 id=\"img\">图片</h3>\r\n\r\n很明显地，要在纯文字应用中设计一个「自然」的语法来插入图片是有一定难度的。\r\n\r\nMarkdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式： *行内式*和*参考式*。\r\n\r\n行内式的图片语法看起来像是：\r\n\r\n    ![Alt text](/path/to/img.jpg)\r\n\r\n    ![Alt text](/path/to/img.jpg \"Optional title\")\r\n\r\n详细叙述如下：\r\n\r\n*   一个惊叹号 `!`\r\n*   接着一个方括号，里面放上图片的替代文字\r\n*   接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上\r\n    选择性的 \'title\' 文字。\r\n\r\n参考式的图片语法则长得像这样：\r\n\r\n    ![Alt text][id]\r\n\r\n「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：\r\n\r\n    [id]: url/to/image  \"Optional title attribute\"\r\n\r\n到目前为止， Markdown 还没有办法指定图片的宽高，如果你需要的话，你可以使用普通的 `<img>` 标签。\r\n\r\n* * *\r\n\r\n<h2 id=\"misc\">其它</h2>\r\n\r\n<h3 id=\"autolink\">自动链接</h3>\r\n\r\nMarkdown 支持以比较简短的自动链接形式来处理网址和电子邮件信箱，只要是用方括号包起来， Markdown 就会自动把它转成链接。一般网址的链接文字就和链接地址一样，例如：\r\n\r\n    <http://example.com/>\r\n\r\nMarkdown 会转为：\r\n\r\n    <a href=\"http://example.com/\">http://example.com/</a>\r\n\r\n邮址的自动链接也很类似，只是 Markdown 会先做一个编码转换的过程，把文字字符转成 16 进位码的 HTML 实体，这样的格式可以糊弄一些不好的邮址收集机器人，例如：\r\n\r\n    <address@example.com>\r\n\r\nMarkdown 会转成：\r\n\r\n    <a href=\"&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;\r\n    &#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;\r\n    &#109;\">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;\r\n    &#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;</a>\r\n\r\n在浏览器里面，这段字串（其实是 `<a href=\"mailto:address@example.com\">address@example.com</a>`）会变成一个可以点击的「address@example.com」链接。\r\n\r\n（这种作法虽然可以糊弄不少的机器人，但并不能全部挡下来，不过总比什么都不做好些。不管怎样，公开你的信箱终究会引来广告信件的。）\r\n\r\n<h3 id=\"backslash\">反斜杠</h3>\r\n\r\nMarkdown 可以利用反斜杠来插入一些在语法中有其它意义的符号，例如：如果你想要用星号加在文字旁边的方式来做出强调效果（但不用 `<em>` 标签），你可以在星号的前面加上反斜杠：\r\n\r\n    \\*literal asterisks\\*\r\n\r\nMarkdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：\r\n\r\n    \\   反斜线\r\n    `   反引号\r\n    *   星号\r\n    _   底线\r\n    {}  花括号\r\n    []  方括号\r\n    ()  括弧\r\n    #   井字号\r\n    +   加号\r\n    -   减号\r\n    .   英文句点\r\n    !   惊叹号\r\n\r\n<h2 id=\"acknowledgement\">感谢</h2>\r\n\r\n感谢 [leafy7382][] 协助翻译，[hlb][]、[Randylien][] 帮忙润稿，[ethantw][] 的[汉字标准格式・CSS Reset][]， [WM][] 回报文字错误。\r\n\r\n[leafy7382]:https://twitter.com/#!/leafy7382\r\n[hlb]:http://iamhlb.com/\r\n[Randylien]:http://twitter.com/randylien\r\n[ethantw]:https://twitter.com/#!/ethantw\r\n[汉字标准格式・CSS Reset]:http://ethantw.net/projects/han/\r\n[WM]:http://kidwm.net/\r\n\r\n感谢 [fenprace][]，[addv][]。\r\n\r\n[fenprace]:https://github.com/fenprace\r\n[addv]:https://github.com/addv\r\n\r\n----------\r\n<h2 id=\"editor\">Markdown 免费编辑器</h2>\r\n\r\nWindows 平台\r\n\r\n* [MarkdownPad](http://markdownpad.com/)\r\n* [MarkPad](http://code52.org/DownmarkerWPF/)\r\n\r\nLinux 平台\r\n\r\n* [ReText](http://sourceforge.net/p/retext/home/ReText/)\r\n\r\nMac 平台\r\n\r\n* [Mou](http://mouapp.com/)\r\n\r\n在线编辑器\r\n\r\n* [Markable.in](http://markable.in/)\r\n* [Dillinger.io](http://dillinger.io/)\r\n\r\n浏览器插件\r\n\r\n* [MaDe](https://chrome.google.com/webstore/detail/oknndfeeopgpibecfjljjfanledpbkog) (Chrome)\r\n\r\n高级应用\r\n\r\n* [Sublime Text 2](http://www.sublimetext.com/2) + [MarkdownEditing](http://ttscoff.github.com/MarkdownEditing/) / [教程](http://lucifr.com/2012/07/12/markdownediting-for-sublime-text-2/)', '4', '2016-11-05 07:13:19');
INSERT INTO `articles` VALUES ('3', '系统部署方法', '## 部署方法(Windows)：\r\n1. **使用virtualenv虚拟化环境**([virtualenv简易教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000))：根据项目下的requirements.txt把依赖包安装到虚拟环境中（有些依赖如MySQL-pyrhon、lxml安装不了的，去[windows下的python依赖包](http://www.lfd.uci.edu/~gohlke/pythonlibs/)下载安装）。以后启动项目前都需要先激活虚拟环境。\r\n\r\n2. **安装数据库**：在项目下的cogfig.py里把*SQLALCHEMY_DATABASE_URI*这项改为自己的mysql数据库用户名密码，之后再进入项目主目录进行数据迁移，即依次执行<pre><code>python manage.py db upgrade</code></pre>\r\n之后可以导入sql文件（建议使用navicat，一个可视化管理mysql的工具）\r\n\r\n3. **启动项目**：先激活虚拟环境，之后运行服务进程。<pre><code>venv/bin/activate\r\npython manage.py runserver</code></pre>', '6', '2016-11-05 07:15:54');

-- ----------------------------
-- Table structure for groups
-- ----------------------------
DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL,
  `about` text NOT NULL,
  `logo` varchar(128) DEFAULT NULL,
  `topicNum` int(11) DEFAULT NULL,
  `createdTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of groups
-- ----------------------------
INSERT INTO `groups` VALUES ('1', '新手入门', '如果没有老司机带路，那就自己带自己吧', '/static/upload/group_logo/1.png?t=1477792474.18', '5', '2016-09-20 00:00:00');
INSERT INTO `groups` VALUES ('2', '策略-研究', '分享讨论策略', '/static/upload/group_logo/2.png?t=1477792507.31', '0', '2016-10-07 16:55:24');
INSERT INTO `groups` VALUES ('3', '讨论', '大家一起来讨论', '/static/upload/group_logo/3.png?t=1477792520.93', '1', '2016-10-14 16:56:03');

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(1024) NOT NULL,
  `topicID` int(11) DEFAULT NULL,
  `userID` int(11) DEFAULT NULL,
  `createdTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `topicID` (`topicID`),
  KEY `userID` (`userID`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`topicID`) REFERENCES `topics` (`id`),
  CONSTRAINT `post_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES ('4', '很好', '3', '1', '2016-10-29 17:01:08');
INSERT INTO `post` VALUES ('5', '板凳', '3', '1', '2016-10-29 17:01:19');
INSERT INTO `post` VALUES ('6', 'nice', '4', '1', '2016-10-29 17:03:29');
INSERT INTO `post` VALUES ('7', '地板', '3', '3', '2016-11-09 20:03:20');
INSERT INTO `post` VALUES ('8', '沙发', '5', '3', '2016-11-09 20:05:32');
INSERT INTO `post` VALUES ('9', '@<a href=\"/user/3/\" class=\"mention\">yinst</a> ', '5', '3', '2016-11-09 20:27:04');
INSERT INTO `post` VALUES ('10', '@<a href=\"/user/3/\" class=\"mention\">yinst</a> 自己回复自己，哈哈哈', '5', '3', '2016-11-09 20:27:19');
INSERT INTO `post` VALUES ('11', '加油？\r\n加油！', '6', '1', '2016-11-09 20:37:44');
INSERT INTO `post` VALUES ('12', '@<a href=\"/user/1/\" class=\"mention\">qiumy</a> 终于有人回复了，', '6', '3', '2016-11-09 20:39:13');
INSERT INTO `post` VALUES ('13', '居然不知道该写什么', '7', '3', '2016-11-09 22:11:12');
INSERT INTO `post` VALUES ('14', '66666', '6', '6', '2016-11-10 00:10:47');
INSERT INTO `post` VALUES ('15', '@<a href=\"/user/3/\" class=\"mention\">yinst</a> 8484', '5', '3', '2016-11-10 09:23:11');

-- ----------------------------
-- Table structure for stocks
-- ----------------------------
DROP TABLE IF EXISTS `stocks`;
CREATE TABLE `stocks` (
  `code` varchar(16) NOT NULL,
  `name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stocks
-- ----------------------------
INSERT INTO `stocks` VALUES ('600000', '浦发银行');
INSERT INTO `stocks` VALUES ('600005', '武钢股份');
INSERT INTO `stocks` VALUES ('600036', '招商银行');
INSERT INTO `stocks` VALUES ('601088', '中国神华');
INSERT INTO `stocks` VALUES ('601288', '中国农业银行');
INSERT INTO `stocks` VALUES ('601390', '中国中铁');
INSERT INTO `stocks` VALUES ('601628', '中国人寿');
INSERT INTO `stocks` VALUES ('601988', '中国银行');
INSERT INTO `stocks` VALUES ('601998', '中信银行');

-- ----------------------------
-- Table structure for topics
-- ----------------------------
DROP TABLE IF EXISTS `topics`;
CREATE TABLE `topics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL,
  `content` text NOT NULL,
  `visitNum` int(11) DEFAULT NULL,
  `postNum` int(11) DEFAULT NULL,
  `groupID` int(11) DEFAULT NULL,
  `userID` int(11) DEFAULT NULL,
  `createdTime` datetime DEFAULT NULL,
  `updatedTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `groupID` (`groupID`),
  KEY `userID` (`userID`),
  CONSTRAINT `topics_ibfk_1` FOREIGN KEY (`groupID`) REFERENCES `groups` (`id`),
  CONSTRAINT `topics_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of topics
-- ----------------------------
INSERT INTO `topics` VALUES ('3', '开启你的量化之旅！', '### 1. 什么是量化投资？\r\n---\r\n知乎上的一个热门Topic，关于如何从一个门外汉开始登堂入室，也许可以给你答案：\r\n学习量化交易如何入门？\r\n他山之石可以攻玉，先进市场的经验总是可以借鉴的。下面的书总结了一个合格的alpha交易系统的结构：\r\nInside the black box（中文版：打开量化投资的黑箱）\r\n\r\n### 2. 理论知识预备\r\n---\r\n金融市场的知识总是越多越好，下面的书单给出了一个比较全面的金融市场知识的覆盖：\r\n债券市场的分析入门： 固定收益证券\r\n如何学习金融工程学： 金融工程学\r\n研究市场的心理：行为金融\r\n时间序列和面板分析： 计量经济学\r\n当然如果你对公司基本面的研究感兴趣，财务会计知识总是需要的，下面的学习资料也许会帮到你：\r\n公司财务的权威： 公司财务原理\r\n期权市场方兴未艾，期货市场如火如荼。要想涉足衍生品市场，下面的书你不该错过：\r\n衍生品的圣经： 期权期货和其他衍生品', '5', '3', '1', '1', '2016-10-29 09:00:59', '2016-10-29 17:00:59');
INSERT INTO `topics` VALUES ('4', '量化分析师的Python日记【第1天：谁来给我讲讲Python？】', '### “谁来给我讲讲Python？”\r\n作为无基础的初学者，只想先大概了解一下Python，随便编个小程序，并能看懂一般的程序，那些什么JAVA啊、C啊、继承啊、异常啊通通不懂怎么办，于是我找了很多资料，写成下面这篇日记，希望以完全初学者的角度入手来认识Python这个在量化领域日益重要的语言\r\n\r\n### 一，熟悉基本\r\n在正式介绍python之前，了解下面两个基本操作对后面的学习是有好处的：\r\n1）基本的输入输出 可以在Python中使用+、-、*、/直接进行四则运算。\r\n\r\n```\r\n1+3*3\r\n```', '7', '2', '1', '2', '2016-10-29 09:03:10', '2016-10-29 17:03:23');
INSERT INTO `topics` VALUES ('5', '优矿社区导读——量化投资门派梳理', '在优矿社区混了这么久，虽然发帖不多，不过一直都在阅读各位大神的分享，希望从中学习量化知识。\r\n\r\n帖子数量比较多，为了方便阅读，特地建了一个目录。根据量化投资的种类，把社区的帖子分门别类的列出来。\r\n\r\n看了这么多帖子，是在是感叹，优矿是在太牛B了，有好多好多的精华沉淀啊。\r\n\r\n希望我也能在量化投资的路上走得更远，把我的更多心得和思考分享给大家。\r\n\r\n本帖涉猎股票、分级基金、固定收益、期权等方面的内容。\r\n\r\n当有新贴时，我会随时更新。\r\n\r\n本帖最后更新时间：2016年1月8日。\r\n\r\n另外，jiang.wei写了一个精华帖推荐，很值得一读。\r\n[https://uqer.io/community/share/567ba9c3228e5b344568822c](https://uqer.io/community/share/567ba9c3228e5b344568822c)', '4', '4', '3', '3', '2016-11-05 07:19:11', '2016-11-05 15:19:11');
INSERT INTO `topics` VALUES ('6', '咸鱼证券上线感言', '\r\n### 测试还是很揪心的，更揪心的是展示时再出BUG，Goodbye my friend!\r\n\r\n放女神镇楼！\r\n\r\n![放女神镇楼](http://www.wudage.com/uploads/allimg/150731/10-150I1153I0.jpg \"插入图片标题\")\r\n\r\n[中山大学](http://www.sysu.edu.cn)\r\n[数据学院](http://sdcs.sysu.edu.cn)', '26', '3', '1', '3', '2016-11-09 12:04:33', '2016-11-09 20:40:11');
INSERT INTO `topics` VALUES ('7', '大盘指数开盘公告', '略', '5', '1', '1', '3', '2016-11-09 14:06:05', '2016-11-09 22:10:52');
INSERT INTO `topics` VALUES ('8', '当一个老司机是一种什么样的体验？', '#老司机\r\n###秋名山上行人稀\r\n###常有车手较高低\r\n###如今车道依旧在\r\n###不见当年老司机', '3', '0', '1', '6', '2016-11-09 16:12:47', '2016-11-10 00:12:47');
INSERT INTO `topics` VALUES ('9', 'deee', 'ghyyu\r\n\r\n\r\n1465151456', '3', '0', null, '3', '2016-11-10 01:22:05', '2016-11-10 09:22:29');

-- ----------------------------
-- Table structure for trades
-- ----------------------------
DROP TABLE IF EXISTS `trades`;
CREATE TABLE `trades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `stock_id` varchar(16) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `is_buy` tinyint(1) DEFAULT NULL,
  `tradeTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_id` (`stock_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `trades_ibfk_1` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`code`),
  CONSTRAINT `trades_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of trades
-- ----------------------------
INSERT INTO `trades` VALUES ('1', '2', '601628', '3', '21.75', '1', '2016-11-09 03:29:09');
INSERT INTO `trades` VALUES ('2', '2', '601088', '4', '17.2', '1', '2016-11-09 03:31:41');
INSERT INTO `trades` VALUES ('3', '3', '601988', '8', '3.36', '1', '2016-11-09 12:06:18');
INSERT INTO `trades` VALUES ('4', '3', '601988', '4', '3.36', '0', '2016-11-09 12:06:36');
INSERT INTO `trades` VALUES ('5', '3', '601088', '10000', '17.7', '1', '2016-11-09 12:11:43');
INSERT INTO `trades` VALUES ('6', '3', '601628', '100', '21.8', '1', '2016-11-09 12:12:34');
INSERT INTO `trades` VALUES ('7', '3', '601088', '500', '17.7', '0', '2016-11-09 12:13:07');
INSERT INTO `trades` VALUES ('8', '1', '601998', '5', '6.13', '1', '2016-11-09 12:13:21');
INSERT INTO `trades` VALUES ('9', '1', '601998', '4', '6.13', '0', '2016-11-09 12:13:45');
INSERT INTO `trades` VALUES ('10', '3', '601088', '9500', '17.7', '0', '2016-11-09 12:29:48');
INSERT INTO `trades` VALUES ('11', '3', '601390', '1000', '8.61', '1', '2016-11-09 12:47:54');
INSERT INTO `trades` VALUES ('12', '4', '601288', '1000', '3.15', '1', '2016-11-09 13:46:09');
INSERT INTO `trades` VALUES ('13', '4', '601288', '500', '3.15', '0', '2016-11-09 13:46:19');
INSERT INTO `trades` VALUES ('14', '4', '601288', '500', '3.15', '0', '2016-11-09 13:50:27');
INSERT INTO `trades` VALUES ('15', '6', '600000', '1000', '16.46', '1', '2016-11-09 16:16:14');
INSERT INTO `trades` VALUES ('16', '6', '600000', '400', '16.46', '0', '2016-11-09 16:16:27');
INSERT INTO `trades` VALUES ('17', '6', '600005', '400', '3.1', '1', '2016-11-09 16:17:27');
INSERT INTO `trades` VALUES ('18', '6', '600005', '100', '3.1', '0', '2016-11-09 16:17:46');
INSERT INTO `trades` VALUES ('19', '6', '600005', '700', '3.1', '1', '2016-11-09 23:54:51');
INSERT INTO `trades` VALUES ('20', '7', '601988', '1000', '3.36', '1', '2016-11-10 01:14:53');
INSERT INTO `trades` VALUES ('21', '7', '601988', '500', '3.36', '0', '2016-11-10 01:15:04');
INSERT INTO `trades` VALUES ('22', '7', '600000', '560', '16.46', '1', '2016-11-10 01:16:04');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `is_valid_registered` tinyint(1) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `date_joined` datetime DEFAULT NULL,
  `permissions` int(11) NOT NULL,
  `avatar_url` varchar(64) DEFAULT NULL,
  `telephone` varchar(32) DEFAULT NULL,
  `personal_id` varchar(32) DEFAULT NULL,
  `personal_profile` text,
  `topicNum` int(11) NOT NULL,
  `postNum` int(11) NOT NULL,
  `is_password_reset_link_valid` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'qiumy', 'pbkdf2:sha1:1000$pLs7Yykq$1de03c236f9093ad14699577c62d773f7baebf80', '1415456511@qq.com', '199994', '1', '2016-11-09 13:13:41', '2016-11-09 03:24:02', '1', '/static/upload/1.png?t=1478674388.62', null, null, 'hello', '0', '1', '1');
INSERT INTO `users` VALUES ('2', 'root', 'pbkdf2:sha1:1000$VssUHFpd$6f210466e23ba857603289614a2fe531659efd76', 'minyi_qiu@163.com', '199866', '1', '2016-11-09 22:01:35', '2016-11-09 03:26:06', '0', '/static/images/default_avatar.jpg', null, null, null, '0', '0', '1');
INSERT INTO `users` VALUES ('3', 'yinst', 'pbkdf2:sha1:1000$2ZJUE8nT$4d866b9c2763ddad847a8b580a0883e70ee88f77', '876184917@qq.com', '189196', '1', '2016-11-10 09:18:55', '2016-11-09 04:19:33', '0', '/static/upload/3.png?t=1478739141.66', null, null, '我有1元钱，求带飞', '3', '7', '1');
INSERT INTO `users` VALUES ('4', 'Zouzhp', 'pbkdf2:sha1:1000$B18Nevlw$2c2b01cc2a8220e6e2ed9d872477e45e04a55b53', '5034@qq.com', '200000', '1', '2016-11-09 21:50:12', '2016-11-09 13:22:24', '1', '/static/upload/4.png?t=1478698985.68', null, null, '愿逐月华流照君', '0', '0', '0');
INSERT INTO `users` VALUES ('5', 'Zouzhp_233', 'pbkdf2:sha1:1000$fBrEEd59$2787bc9abab79ac2a88289a7d9d8d3f9f5f556fd', 'Zouzhp3@mail2.sysu.edu.cn', '200000', '0', '2016-11-09 15:43:51', '2016-11-09 15:43:51', '1', '/static/images/default_avatar.jpg', null, null, null, '0', '0', '0');
INSERT INTO `users` VALUES ('6', 'kongming', 'pbkdf2:sha1:1000$EVhGqhk4$690d57b19a9fd7d4ae54a14bf9d211fda9d7ea2e', '954943776@qq.com', '187024', '1', '2016-11-10 07:53:08', '2016-11-09 16:03:58', '1', '/static/upload/6.png?t=1478735621.54', null, null, '愿逐月华流照君', '1', '1', '0');
INSERT INTO `users` VALUES ('7', 'Zouzhp3', 'pbkdf2:sha1:1000$QOm30rBM$7f893809d48c39e4fc5bfccbd4aada9d50b010b3', '503951764@qq.com', '189102', '1', '2016-11-10 09:36:42', '2016-11-10 01:08:05', '1', '/static/upload/7.png?t=1478740630.97', null, null, '春江潮水连海平', '0', '0', '1');

-- ----------------------------
-- Table structure for user_stock
-- ----------------------------
DROP TABLE IF EXISTS `user_stock`;
CREATE TABLE `user_stock` (
  `user_id` int(11) NOT NULL,
  `stock_id` varchar(16) NOT NULL,
  `average_price` float DEFAULT NULL,
  `own_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`stock_id`),
  KEY `stock_id` (`stock_id`),
  CONSTRAINT `user_stock_ibfk_1` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`code`),
  CONSTRAINT `user_stock_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_stock
-- ----------------------------
INSERT INTO `user_stock` VALUES ('1', '601998', '6.13', '1');
INSERT INTO `user_stock` VALUES ('2', '601088', '17.2', '4');
INSERT INTO `user_stock` VALUES ('2', '601628', '21.75', '3');
INSERT INTO `user_stock` VALUES ('3', '601390', '8.61', '1000');
INSERT INTO `user_stock` VALUES ('3', '601628', '21.8', '100');
INSERT INTO `user_stock` VALUES ('3', '601988', '3.36', '4');
INSERT INTO `user_stock` VALUES ('6', '600000', '16.46', '600');
INSERT INTO `user_stock` VALUES ('6', '600005', '3.1', '1000');
INSERT INTO `user_stock` VALUES ('7', '600000', '16.46', '560');
INSERT INTO `user_stock` VALUES ('7', '601988', '3.36', '500');
