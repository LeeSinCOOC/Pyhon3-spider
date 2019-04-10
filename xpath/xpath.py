text = '''
<li class="">
                                <div class="job-primary">
                                    <div class="info-primary">
                                        <h3 class="name">
                                            <a href="/job_detail/895a038ca04715c01HZ729W6FFI~.html" data-jid="895a038ca04715c01HZ729W6FFI~" data-itemid="1" data-lid="1qO3ruFu4Qb.search" data-jobid="32108740" data-index="0" ka="search_list_1" target="_blank" class="">
                                                <div class="job-title">初级数据分析师</div>
                                                <span class="red">5k-8k</span>
                                                <div class="info-detail" style="top: 0px;"><div class="info-detail-top">
            <div class="detail-top-title">初级数据分析师</div>
            <div class="detail-top-text">嘉捷信诚 · HR： 许凯琼</div>
            <div class="detail-top-right">
                <span href="javascript:;" ka="popjob_interest_895a038ca04715c01HZ729W6FFI~" data-url="/geek/tag/jobtagupdate.json?jobId=895a038ca04715c01HZ729W6FFI~&amp;expectId=&amp;tag=4&amp;lid=1qO3ruFu4Qb.search" class="link-like " job-id="af6407f9f54025941HZ639y_E1U~">感兴趣</span>
                <span ka="popjob_greet_895a038ca04715c01HZ729W6FFI~" href="javascript:;" data-url="/gchat/addRelation.json?jobId=895a038ca04715c01HZ729W6FFI~&amp;lid=1qO3ruFu4Qb.search" redirect-url="/geek/new/index/chat?id=af6407f9f54025941HZ639y_E1U~" target="_blank" class="btn btn-startchat">立即沟通</span>
            </div>
        </div>
        <div class="detail-bottom"> <div class="detail-bottom-title">职位描述</div>
            <div class="detail-bottom-text">
                职位描述：<br>1. 我们对候选人的期望：<br>l 热爱数据挖掘、建模分析行业，对数据行业的发展和未来抱有坚定的信心，能够脚踏实地的在每一项具体工作中实践个人价值——有创造梦想的意愿，也有务实干活的能力；<br>l 工作中，从业务理解入手，形成从业务到数据的映射，通过数据挖掘、分析等手段，在业主的生产和商业环境中所产生的数据里，带领项目组找到为企业提升价值的机会点，实现数据价值的最终呈现；<br>2. 岗位描述<br>l 面向客户服务的岗位职责，与销售、客户服务、产品运营等其他团队协作，为中大型企业提供数据挖掘、建模分析服务；<br>l 服务职责覆盖数据链全流程，包括从源头的各类型数据收集整理，到基于业主需求的数据预处理、建模，以及为确保数据价值呈现的模型落地应用；<br>3 职责描述：<br>1.遵守部门业务流程/规范并认真执行；<br>2.根据业务需求，对数据进行提取、整合、分析、建模、通过数据为产品、业务优化提供效果评估，为客户提供数据决策支持。<br>3.依据业务需求，对文献进行制作、归类、整理、制作主题报告；<br>5.理解大数据平台数据产品, 融汇应用并且指导业务方使用<br>6.根据任务目标制定个人月工作计划，接受绩效考核；<br>7.记录工作中发现及解决的问题到问题总结表，做知识共享；<br>8.遵守公司管理制度，认同公司企业文化；<br>9.承接上级领导交办的临时任务；<br>4.任职要求：<br>1.数学、统计、信息管理、心理学、计算机或项目所需专业，本科及以上学历，，专业知识扎实者优先；<br>2..熟练使用Excel软件，包括公式、图表基础操作；<br>3.熟练使用搜索引擎进行检索、扩检，查准、查全所需数据；<br>4、对于Spark/Hadoop/HBase/Hive等大数据处理平台具备一定了解，有系统实际操作经验者优先；<br>5、对数据敏感，有较强的分析问题和解决问题的能力。<br>6.在校期间担任过班干部或者学生会干部者优先；<br>7.有组织、协调、管理方面经验者优先。
            </div>
        </div></div>
                                            </a>
                                        </h3>
                                        <p>成都  <em class="vline"></em>1-3年<em class="vline"></em>本科</p>
                                    </div>
                                    <div class="info-company">
                                        <div class="company-text">
                                            <h3 class="name"><a href="/gongsi/675cc5acdecaf3c51n152tm0Fw~~.html" ka="search_list_company_1_custompage" target="_blank">嘉捷信诚</a></h3>
                                            <p>计算机软件<em class="vline"></em>未融资<em class="vline"></em>20-99人</p>
                                        </div>
                                    </div>
                                    <div class="info-publis">
                                        <h3 class="name"><img src="https://img.bosszhipin.com/beijin/mcs/useravatar/20180703/f14b26507b47aad9e27331e30ff7ee69cfcd208495d565ef66e7dff9f98764da_s.jpg?x-oss-process=image/resize,w_40,limit_0">许凯琼<em class="vline"></em>HR</h3>
                                        <p>发布于01月02日</p>
                                    </div>
                                    <a href="javascript:;" data-url="/gchat/addRelation.json?jobId=895a038ca04715c01HZ729W6FFI~&amp;lid=1qO3ruFu4Qb.search" redirect-url="/geek/new/index/chat?id=af6407f9f54025941HZ639y_E1U~" target="_blank" class="btn btn-startchat">立即沟通
                                    </a>
                                </div>
                            </li>
'''

from lxml import etree

html = etree.HTML(text)

result = etree.tostring(html) 
print(result.decode('utf-8'))

#tostring()方法可输出修正后的代码，但是结果是bytes格式的





















                        