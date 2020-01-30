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

def onLoggerAppReady(  ):
	"""	
	功能说明：
	当前进程已经准备好的时候回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	

	"""
	pass

def onLoggerAppShutDown(  ):
	"""	
	功能说明：
	进程关闭会回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	

	"""
	pass

def onLogWrote( datas ):
	"""	
	功能说明：
	如果这个函数在脚本中有实现，logger进程获得了一条新日志，该回调函数被调用。
	数据库接口在kbengine_defaults.xml->dbmgr->databaseInterfaces定义。
	
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@datas
	bytes，日志数据。
	
	
	
	
	
	

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

