def addTimer( initialOffset, repeatOffset=0, callbackObj=None ):
	"""	
	功能说明：
	注册一个定时器，定时器由回调函数callbackObj触发，回调函数将在"initialOffset"秒后被执行第1次，而后将每间隔"repeatOffset"秒执行1次。
	
	例子:
	
	# 这里是使用addTimer的一个例子
	        import KBEngine
	 
	        # 增加一个定时器，5秒后执行第1次，而后每1秒执行1次，用户参数是9
	        KBEngine.addTimer( 5, 1, onTimer_Callbackfun )
	 
	        # 增加一个定时器，1秒后执行，用户参数缺省是0
	        KBEngine.addTimer( 1, onTimer_Callbackfun )
	 
	    def onTimer_Callbackfun( id ):
	        print "onTimer_Callbackfun called: id %i" % ( id )
	        # if 这是不断重复的定时器，当不再需要该定时器的时候，调用下面函数移除:
	        #     KBEngine.delTimer( id )
	
	
	
	参数：
	
	
	@initialOffset
	float，指定定时器从注册到第一次回调的时间间隔（秒）。
	
	
	@repeatOffset
	float，指定第一次回调执行后每次执行的时间间隔（秒）。必须用函数delTimer移除定时器，否则它会一直重复下去。值小于等于0将被忽略。
	
	
	@callbackObj
	function，指定的回调函数对象。
	
	
	
	
	
	返回:
	
	integer，该函数返回timer的内部id，这个id可用于delTimer移除定时器。
	
	
	
	
	
	

	"""
	pass

def delTimer( id ):
	"""	
	功能说明：
	函数delTimer用于移除一个注册的定时器，移除后的定时器不再执行。只执行1次的定时器在执行回调后自动移除，不必要使用delTimer移除。
	如果delTimer函数使用一个无效的id（例如已经移除），将会产生错误。
	
	到KBEngine.addTimer参考定时器的一个使用例子。
	
	
	参数：
	
	
	@id
	integer，它指定要移除的定时器id。
	
	
	
	
	
	

	"""
	pass

def executeRawDatabaseCommand( command, callback, threadID, dbInterfaceName ):
	"""	
	功能说明：
	这个脚本函数在数据库上执行原始数据库命令，该命令将直接由相关数据库进行解析。
	
	请注意使用该函数修改实体数据可能不生效，因为如果实体已经检出，被修改过的实体数据将仍会被实体存档而导致覆盖。
	强烈不推荐这个函数用于读取或修改实体数据。
	
	
	参数：
	
	
	@command
	这个数据库命令将会因为不同数据库配置方案而不同。对于方案为MySQL数据库它是一个SQL查询语句。
	
	
	@callback
	
	可选参数，带有命令执行结果的回调对象（比如说是一个函数）。这个回调带有4个参数：结果集合，影响的行数，自増长值，错误信息。
	
	声明样例：
	def 
	sqlcallback(result, rows, insertid, error):
	    print(result, rows, insertid, error)  
	
	如同上面的例子所示，result参数对应的就是&ldquo;结果集合&rdquo;，这个结果集合参数是一个行列表。
	每一行是一个包含字段值的字符串列表。
	命令执行没有返回结果集合（比如说是DELETE命令），
	或者
	命令执行有错误时这个结果集合为None。
	
	rows参数则是&ldquo;影响的行数&rdquo;，它是一个整数，表示命令执行受影响的行数。这个参数只和不返回结果结合的命令（如DELETE）相关。
	如果有结果集合返回或者命令执行有错误时这个参数为None。
	
	insertid对应的是&ldquo;自増长值&rdquo;，类似于实体的databaseID，当成功的向一张带有自増长类型字段的表中插入数据时，它返回该数据在插入时自増长字段所被赋于的值。
	更多的信息可以参阅mysql的mysql_insert_id()方法。另外，此参数仅在数据库类型为mysql时有意义。
	
	error则对应了&ldquo;错误信息&rdquo;，当命令执行有错误时，这个参数是一个描述错误的字符串。命令执行没有发生错误时这个参数为None。
	
	
	@threadID
	int32，可选参数，指定一个线程来处理本条命令。用户可以通过这个参数控制某一类命令的执行先后顺序（dbmgr是多线程处理的），默认是不指定，如果threadID是实体的ID，
	那么将加入到该实体的存档队列中由线程逐条写入。
	
	
	@dbInterfaceName
	string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
	
	
	
	
	
	

	"""
	pass

def urlopen( url, callback, postData, headers ):
	"""	
	功能说明：
	这个脚本函数在提供对外HTTP/HTTPS异步请求。
	
	
	参数：
	
	
	@url
	有效的HTTP/HTTPS网址，字符串类型。
	
	
	@callback
	
	可选参数，带有请求执行结果的回调对象（比如说是一个函数）。这个回调带有5个参数：HTTP请求返回码（如：200)，返回的内容，返回的HTTP协议头，是否成功，请求的网址。
	
	声明样例：
	def 
	onHttpCallback(httpcode, data, headers, success, url):
	    print(httpcode, data, headers, success, url)  
	
	如同上面的例子所示:
	httpcode:参数对应的就是&ldquo;HTTP请求返回码&rdquo;，这个结果集合参数是一个整形值。
	data:参数则是&ldquo;返回的内容&rdquo;，它是一个字符串。
	
	headers:参数是&ldquo;服务器返回的HTTP协议头&rdquo;，如：{"Content-Type": "application/x-www-form-urlencoded"}，它是一个字典。
	success:则对应了&ldquo;执行是否成功&rdquo;，当请求执行有错误时，为False，可以通过httpcode进一步判断错误信息。
	
	url:是&ldquo;请求所用的网址。
	
	
	
	@postData
	可选参数，默认是GET方式请求服务器，如果需要POST方式请提供需要POST的内容，引擎将自动使用POST方式请求服务器，它是一个bytes。
	
	
	@headers
	可选参数，请求时使用的HTTP头，如：{"Content-Type": "application/x-www-form-urlencoded"}，它是一个字典。
	
	
	
	
	
	
	

	"""
	pass

def onDBMgrReady(  ):
	"""	
	功能说明：
	当前进程已经准备好的时候回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	

	"""
	pass

def onDBMgrShutDown(  ):
	"""	
	功能说明：
	进程关闭会回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	

	"""
	pass

def onReadyForShutDown(  ):
	"""	
	功能说明：
	如果这个函数在脚本中有实现，当进程准备退出时，该回调函数被调用。
	
	可以通过该回调控制进程退出的时机。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	返回：
	
	
	bool，如果返回True，则允许进入进程退出流程，返回其它值则进程会过一段时间后再次询问。
	
	
	
	
	

	"""
	pass

def onSelectAccountDBInterface( accountName ):
	"""	
	功能说明：
	这个回调实现返回某个账号对应的数据库接口，选定接口后dbmgr针对这个账号的相关操作都由对应的数据库接口完成。
	数据库接口在kbengine_defaults.xml->dbmgr->databaseInterfaces定义。
	利用该接口可以根据accountName来决定账号应该存储在哪个数据库。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@accountName
	string，账号的名称。
	
	
	
	
	
	返回：
	
	
	string，数据库接口名（数据库接口在kbengine_defaults.xml->dbmgr->databaseInterfaces定义）。
	
	
	
	
	
	
	
	
	
	

	"""
	pass

