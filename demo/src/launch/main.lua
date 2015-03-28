require 'ui.controls'
require 'utils.platform'

root_scene_node = nil

function main()
    math.randomseed( os.time() )
    collectgarbage( 'setpause', 100 )
    collectgarbage( 'setstepmul', 5000 )

    CCLuaLog("started" .. tostring(GetSdkType()))

    MCLoader:sharedMCLoader():loadIndexFile( 'mc/anim.index', 'mc/frames.index' )

    AssetsManager:sharedAssetsManager():addSearchPath( '' )
    AssetsManager:sharedAssetsManager():addSearchPath( 'images/' )

    -- 富文本
    TLFontTex:setFontOriginSize( 22 )
    TLFontTex:setFontName( 'FZCuYuan-M03S' )
    TLFontTex:setEdgeSize( 3 )
    -- TLFontTex:setParseRichTextHandler( parseRichTextMark )

    TLFontTex:sharedTLFontTex():initFontTexture( 'Ncolor.png', 8, 8, 'position_texture_color_rich_string_color' )

    root_scene_node = TLRunningScene:create()

    layer_ui = TLWindowManager:SharedTLWindowManager()
    root_scene_node:addChild(layer_ui)

    CCDirector:sharedDirector():runWithScene( root_scene_node )

    g_platform = PlatformBase.new()
    init()
end

function init()
    -- whole screen
    local winSize = CCDirector:sharedDirector():getWinSize()

    local spriteLogin = MCLoader:sharedMCLoader():loadSprite('10000_11_1.png')
    spriteLogin:setPosition(100, winSize.height/2)
    local win = TLWindow:createWindow( spriteLogin, win_flags or TL_WINDOW_UNIVARSAL )
    init_simple_button(win, function()
        g_platform:login()
    end)
    layer_ui:AddModuleWindow(win)

    local spritePay = MCLoader:sharedMCLoader():loadSprite('10000_10_4.png')
    spritePay:setPosition(300, winSize.height/2)
    win = TLWindow:createWindow( spritePay, win_flags or TL_WINDOW_UNIVARSAL )
    init_simple_button(win, function()
        g_platform:pay("test good id", "test good name", 10.0, {
            id = 0,
            name = 'test',
            faction = '',
            vip = 1,
            level = 2,
            serverID = 100,
        })
    end)
    layer_ui:AddModuleWindow(win)

    local spritePay = MCLoader:sharedMCLoader():loadSprite('10000_11_3.png')
    spritePay:setPosition(600, winSize.height/2)
    win = TLWindow:createWindow( spritePay, win_flags or TL_WINDOW_UNIVARSAL )
    init_simple_button(win, function()
        g_platform:logout()
    end)
    layer_ui:AddModuleWindow(win)

end

function __G__TRACKBACK__( msg )
    CCLuaLog(msg)
    CCLuaLog(debug.traceback())
end

xpcall( main,  __G__TRACKBACK__ )
