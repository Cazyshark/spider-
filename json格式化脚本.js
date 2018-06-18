/**
 * 解决json传输数据时存在 同时存在单引号和双引号的问题
 *
 * 思路：
 *
 * 1 首选将 双引号转义
 *
 * 2 将 单双引号用不容易在字符串中出现的字符分别替换
 *   在后台 分别用过单双引号替换掉即可
 *
 * 注：可以传入字符串 也可以传入字符串数组
 * author: 明明如月 QQ 605283073
 * time:2015年5月19日15:33:44
 */

function JsonQuotesUtil()
{

    var defualtSingleQuotePlaceholder="s%0";//默认单引号占位符
    var defualtDoubleQuotePlaceholder="d%1";//默认双引号占位符

    var singleQuotePlaceholder=defualtSingleQuotePlaceholder;//单引号占位符
    var doubleQuotePlaceholder=defualtDoubleQuotePlaceholder;//双引号占位符

    //设置单引号占位符(建议起不容易出现的字符)
    this.setSingleQuotePlaceholder = function(single)
    {
        singleQuotePlaceholder=single;
        return this;
    }

    //设置双引号占位符(建议起不容易出现的字符)
    this.setDoubleQuotePlaceholder = function(double)
    {
        doubleQuotePlaceholder=double;

        return this;
    }

    //恢复默认单引号和双引号占位符
    this.restoreDefaults = function()
    {
        singleQuotePlaceholder=defualtSingleQuotePlaceholder;
        doubleQuotePlaceholder=defualtDoubleQuotePlaceholder;
        return this;
    }

    //用单引号占位符替换单引号 并返回替换后的字符串
    this.replaceSingleQuote=function (str)
    {

        if(str instanceof  Array)//如果是数组分别替换
        {
            for(var i=0;i<str.length;i++)
            {
                str[i]= str[i].replace(/'/g, singleQuotePlaceholder);

            }
        }else
        {
            str= str[i].replace(/'/g, singleQuotePlaceholder);
        }
        return str;
    }

    //用双引号替换符替换双引号 并返回替换后的字符串
    this.replaceDoubleQuote = function (str)
    {
        // return str.replace(/"/g, doubleQuotePlaceholder);

        if(str instanceof  Array)//如果是数组分别替换
        {
            for(var i=0;i<str.length;i++)
            {
                str[i]= str[i].replace(/'/g, doubleQuotePlaceholder);

            }
        }else
        {
            str= str[i].replace(/'/g, doubleQuotePlaceholder);
        }
        return str;

    }




    this.replaceSingleAndDoubleQuote = function(str)
    {
        // return str.replace(/'/g,singleQuotePlaceholder).replace(/"/g, doubleQuotePlaceholder);
        if(str instanceof  Array)//如果是数组分别替换
        {
            alert("1");
            for(var i=0;i<str.length;i++)
            {
                alert(str[i]);
                str[i]= str[i].replace(/'/g,singleQuotePlaceholder).replace(/"/g, doubleQuotePlaceholder);

            }
        }else
        {
            str= str.replace(/'/g,singleQuotePlaceholder).replace(/"/g, doubleQuotePlaceholder);
        }
        return str;
    }


    //双引号转义
    this.escapeDoubleQuote = function(str)
    {


        if(str instanceof  Array)//如果是数组分别替换
        {
            alert("1");
            for(var i=0;i<str.length;i++)
            {
                alert(str[i]);
                str[i]= str[i].replace(/"/g,"\\\"");

            }
        }else
        {
            str= str.replace(/"/g,"\\\"");;
        }
        return str;
    }
}
/**
 * 解决json传输数据时存在 同时存在单引号和双引号的问题
 *
 * 思路：
 *
 * 1 首选将 双引号转义
 *
 * 2 将 单双引号用不容易在字符串中出现的字符分别替换
 *   在后台 分别用过单双引号替换掉即可
 *
 * 注：可以传入字符串 也可以传入字符串数组
 * author: 明明如月 QQ 605283073
 * time:2015年5月19日15:33:44
 */

function JsonQuotesUtil()
{

    var defualtSingleQuotePlaceholder="s%0";//默认单引号占位符
    var defualtDoubleQuotePlaceholder="d%1";//默认双引号占位符

    var singleQuotePlaceholder=defualtSingleQuotePlaceholder;//单引号占位符
    var doubleQuotePlaceholder=defualtDoubleQuotePlaceholder;//双引号占位符

    //设置单引号占位符(建议起不容易出现的字符)
    this.setSingleQuotePlaceholder = function(single)
    {
        singleQuotePlaceholder=single;
        return this;
    }

    //设置双引号占位符(建议起不容易出现的字符)
    this.setDoubleQuotePlaceholder = function(double)
    {
        doubleQuotePlaceholder=double;

        return this;
    }

    //恢复默认单引号和双引号占位符
    this.restoreDefaults = function()
    {
        singleQuotePlaceholder=defualtSingleQuotePlaceholder;
        doubleQuotePlaceholder=defualtDoubleQuotePlaceholder;
        return this;
    }

    //用单引号占位符替换单引号 并返回替换后的字符串
    this.replaceSingleQuote=function (str)
    {

        if(str instanceof  Array)//如果是数组分别替换
        {
            for(var i=0;i<str.length;i++)
            {
                str[i]= str[i].replace(/'/g, singleQuotePlaceholder);

            }
        }else
        {
            str= str[i].replace(/'/g, singleQuotePlaceholder);
        }
        return str;
    }

    //用双引号替换符替换双引号 并返回替换后的字符串
    this.replaceDoubleQuote = function (str)
    {
        // return str.replace(/"/g, doubleQuotePlaceholder);

        if(str instanceof  Array)//如果是数组分别替换
        {
            for(var i=0;i<str.length;i++)
            {
                str[i]= str[i].replace(/'/g, doubleQuotePlaceholder);

            }
        }else
        {
            str= str[i].replace(/'/g, doubleQuotePlaceholder);
        }
        return str;

    }




    this.replaceSingleAndDoubleQuote = function(str)
    {
        // return str.replace(/'/g,singleQuotePlaceholder).replace(/"/g, doubleQuotePlaceholder);
        if(str instanceof  Array)//如果是数组分别替换
        {
            alert("1");
            for(var i=0;i<str.length;i++)
            {
                alert(str[i]);
                str[i]= str[i].replace(/'/g,singleQuotePlaceholder).replace(/"/g, doubleQuotePlaceholder);

            }
        }else
        {
            str= str.replace(/'/g,singleQuotePlaceholder).replace(/"/g, doubleQuotePlaceholder);
        }
        return str;
    }


    //双引号转义
    this.escapeDoubleQuote = function(str)
    {


        if(str instanceof  Array)//如果是数组分别替换
        {
            alert("1");
            for(var i=0;i<str.length;i++)
            {
                alert(str[i]);
                str[i]= str[i].replace(/"/g,"\\\"");

            }
        }else
        {
            str= str.replace(/"/g,"\\\"");;
        }
        return str;
    }
}
