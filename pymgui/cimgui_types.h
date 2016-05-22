
typedef unsigned int uint;

//these are copied from the D bindings for imgui (https://github.com/Extrawurst/DerelictImgui)

enum
{
	ImGuiKey_Tab,       // for tabbing through fields
	ImGuiKey_LeftArrow, // for text edit
	ImGuiKey_RightArrow,// for text edit
	ImGuiKey_UpArrow,   // for text edit
	ImGuiKey_DownArrow, // for text edit
	ImGuiKey_PageUp,
	ImGuiKey_PageDown,
	ImGuiKey_Home,      // for text edit
	ImGuiKey_End,       // for text edit
	ImGuiKey_Delete,    // for text edit
	ImGuiKey_Backspace, // for text edit
	ImGuiKey_Enter,     // for text edit
	ImGuiKey_Escape,    // for text edit
	ImGuiKey_A,         // for text edit CTRL+A: select all
	ImGuiKey_C,         // for text edit CTRL+C: copy
	ImGuiKey_V,         // for text edit CTRL+V: paste
	ImGuiKey_X,         // for text edit CTRL+X: cut
	ImGuiKey_Y,         // for text edit CTRL+Y: redo
	ImGuiKey_Z,         // for text edit CTRL+Z: undo
	ImGuiKey_COUNT
}ImGuiKey_;

enum
{
	// Default: 0
	ImGuiWindowFlags_NoTitleBar             = 1,   // Disable title-bar
	ImGuiWindowFlags_NoResize               = 2,   // Disable user resizing with the lower-right grip
	ImGuiWindowFlags_NoMove                 = 4,   // Disable user moving the window
	ImGuiWindowFlags_NoScrollbar            = 8,   // Disable scrollbar (window can still scroll with mouse or programatically)
	ImGuiWindowFlags_NoScrollWithMouse      = 16,   // Disable user scrolling with mouse wheel
	ImGuiWindowFlags_NoCollapse             = 32,   // Disable user collapsing window by double-clicking on it
	ImGuiWindowFlags_AlwaysAutoResize       = 64,   // Resize every window to its content every frame
	ImGuiWindowFlags_ShowBorders            = 128,   // Show borders around windows and items
	ImGuiWindowFlags_NoSavedSettings        = 256,   // Never load/save settings in .ini file
	ImGuiWindowFlags_NoInputs               = 512,   // Disable catching mouse or keyboard inputs
	ImGuiWindowFlags_MenuBar                = 1024,   // Has a menubar
	ImGuiWindowFlags_HorizontalScrollbar    = 2048,  // Enable horizontal scrollbar (off by default). You need to use SetNextWindowContentSize(ImVec2(width,0.0f)); prior to calling Begin() to specify width. Read code in imgui_demo in the "Horizontal Scrolling" section.
	ImGuiWindowFlags_NoFocusOnAppearing     = 4096,  // Disable taking focus when transitioning from hidden to visible state
	ImGuiWindowFlags_NoBringToFrontOnFocus  = 8192,  // Disable bringing window to front when taking focus (e.g. clicking on it or programatically giving it focus)
//	// [Internal]
//	ImGuiWindowFlags_ChildWindow            = 1048576,  // Don't use! For internal use by BeginChild()
//	ImGuiWindowFlags_ChildWindowAutoFitX    = 2097152,  // Don't use! For internal use by BeginChild()
//	ImGuiWindowFlags_ChildWindowAutoFitY    = 4194304,  // Don't use! For internal use by BeginChild()
//	ImGuiWindowFlags_ComboBox               = 8388608,  // Don't use! For internal use by ComboBox()
//	ImGuiWindowFlags_Tooltip                = 16777216,  // Don't use! For internal use by BeginTooltip()
//	ImGuiWindowFlags_Popup                  = 33554432,  // Don't use! For internal use by BeginPopup()
//	ImGuiWindowFlags_Modal                  = 67108864,  // Don't use! For internal use by BeginPopupModal()
//	ImGuiWindowFlags_ChildMenu              = 134217728   // Don't use! For internal use by BeginMenu()
}ImGuiWindowFlags_;


/*
[0] = 1,
[1] = 2,
[2] = 4,
[3] = 8,
[4] = 16,
[5] = 32,
[6] = 64,
[7] = 128,
[8] = 256,
[9] = 512,
[10] = 1024,
[11] = 2048,
[12] = 4096,
[13] = 8192,
[14] = 16384,
[15] = 32768,
[16] = 65536,
[17] = 131072,
[18] = 262144,
[19] = 524288,
[20] = 1048576,
[21] = 2097152,
[22] = 4194304,
[23] = 8388608,
[24] = 16777216,
[25] = 33554432,
[26] = 67108864,
[27] = 134217728,

*/


enum
{
	// Default: 0
	ImGuiInputTextFlags_CharsDecimal        = 1,   // Allow 0123456789.+-*/
	ImGuiInputTextFlags_CharsHexadecimal    = 2,   // Allow 0123456789ABCDEFabcdef
	ImGuiInputTextFlags_CharsUppercase      = 4,   // Turn a..z into A..Z
	ImGuiInputTextFlags_CharsNoBlank        = 8,   // Filter out spaces, tabs
	ImGuiInputTextFlags_AutoSelectAll       = 16,   // Select entire text when first taking mouse focus
	ImGuiInputTextFlags_EnterReturnsTrue    = 32,   // Return 'true' when Enter is pressed (as opposed to when the value was modified)
	ImGuiInputTextFlags_CallbackCompletion  = 64,   // Call user function on pressing TAB (for completion handling)
	ImGuiInputTextFlags_CallbackHistory     = 128,   // Call user function on pressing Up/Down arrows (for history handling)
	ImGuiInputTextFlags_CallbackAlways      = 256,   // Call user function every time
	ImGuiInputTextFlags_CallbackCharFilter  = 512,   // Call user function to filter character. Modify data->EventChar to replace/filter input, or return 1 to discard character.
	ImGuiInputTextFlags_AllowTabInput       = 1024,  // Pressing TAB input a '\t' character into the text field
	ImGuiInputTextFlags_CtrlEnterForNewLine = 2048,  // In multi-line mode, allow exiting edition by pressing Enter. Ctrl+Enter to add new line (by default adds new lines with Enter).
	ImGuiInputTextFlags_NoHorizontalScroll  = 4096,  // Disable following the cursor horizontally
	ImGuiInputTextFlags_AlwaysInsertMode    = 8192,  // Insert mode
	ImGuiInputTextFlags_ReadOnly            = 16384,  // Read-only mode
	ImGuiInputTextFlags_Password            = 32768,  // Password mode, display all characters as '*'
	// [Internal]
	ImGuiInputTextFlags_Multiline           = 1048576   // For internal use by InputTextMultiline()
}ImGuiInputTextFlags_;

enum
{
	// Default: 0
	ImGuiSelectableFlags_DontClosePopups    = 1,   // Clicking this don't close parent popup window
	ImGuiSelectableFlags_SpanAllColumns     = 2,    // Selectable frame can span all columns (text will still fit in current column)
	ImGuiSelectableFlags_AllowDoubleClick   = 4    // Generate press events on double clicks too
}ImGuiSelectableFlags_;

typedef enum
{
	ImGuiSetCond_Always        = 1, // Set the variable
	ImGuiSetCond_Once          = 2, // Only set the variable on the first call per runtime session
	ImGuiSetCond_FirstUseEver  = 4, // Only set the variable if the window doesn't exist in the .ini file
	ImGuiSetCond_Appearing     = 8  // Only set the variable if the window is appearing after being inactive (or the first time)
}ImGuiSetCond_;

enum
{
	ImGuiCol_Text,
	ImGuiCol_TextDisabled,
	ImGuiCol_WindowBg,
	ImGuiCol_ChildWindowBg,
	ImGuiCol_PopupBg,
	ImGuiCol_Border,
	ImGuiCol_BorderShadow,
	ImGuiCol_FrameBg,               // Background of checkbox, radio button, plot, slider, text input
	ImGuiCol_FrameBgHovered,
	ImGuiCol_FrameBgActive,
	ImGuiCol_TitleBg,
	ImGuiCol_TitleBgCollapsed,
	ImGuiCol_TitleBgActive,
	ImGuiCol_MenuBarBg,
	ImGuiCol_ScrollbarBg,
	ImGuiCol_ScrollbarGrab,
	ImGuiCol_ScrollbarGrabHovered,
	ImGuiCol_ScrollbarGrabActive,
	ImGuiCol_ComboBg,
	ImGuiCol_CheckMark,
	ImGuiCol_SliderGrab,
	ImGuiCol_SliderGrabActive,
	ImGuiCol_Button,
	ImGuiCol_ButtonHovered,
	ImGuiCol_ButtonActive,
	ImGuiCol_Header,
	ImGuiCol_HeaderHovered,
	ImGuiCol_HeaderActive,
	ImGuiCol_Column,
	ImGuiCol_ColumnHovered,
	ImGuiCol_ColumnActive,
	ImGuiCol_ResizeGrip,
	ImGuiCol_ResizeGripHovered,
	ImGuiCol_ResizeGripActive,
	ImGuiCol_CloseButton,
	ImGuiCol_CloseButtonHovered,
	ImGuiCol_CloseButtonActive,
	ImGuiCol_PlotLines,
	ImGuiCol_PlotLinesHovered,
	ImGuiCol_PlotHistogram,
	ImGuiCol_PlotHistogramHovered,
	ImGuiCol_TextSelectedBg,
	ImGuiCol_ModalWindowDarkening,  // darken entire screen when a modal window is active
	ImGuiCol_COUNT
}ImGuiCol_;

typedef enum
{
	ImGuiStyleVar_Alpha,               // float
	ImGuiStyleVar_WindowPadding,       // ImVec2
	ImGuiStyleVar_WindowRounding,      // float
    ImGuiStyleVar_WindowMinSize,       // ImVec2
	ImGuiStyleVar_ChildWindowRounding, // float
	ImGuiStyleVar_FramePadding,        // ImVec2
	ImGuiStyleVar_FrameRounding,       // float
	ImGuiStyleVar_ItemSpacing,         // ImVec2
	ImGuiStyleVar_ItemInnerSpacing,    // ImVec2
	ImGuiStyleVar_IndentSpacing,       // float
	ImGuiStyleVar_GrabMinSize          // float
}ImGuiStyleVar_;

enum
{
	ImGuiAlign_Left     = 1,
	ImGuiAlign_Center   = 2,
	ImGuiAlign_Right    = 4,
	ImGuiAlign_Top      = 8,
	ImGuiAlign_VCenter  = 16,
	ImGuiAlign_Default  = 9,  //ImGuiAlign_Left | ImGuiAlign_Top,
}ImGuiAlign_;

enum
{
	ImGuiColorEditMode_UserSelect = -2,
	ImGuiColorEditMode_UserSelectShowButton = -1,
	ImGuiColorEditMode_RGB = 0,
	ImGuiColorEditMode_HSV = 1,
	ImGuiColorEditMode_HEX = 2
}ImGuiColorEditMode_;

enum
{
	ImGuiMouseCursor_Arrow = 0,
	ImGuiMouseCursor_TextInput,         // When hovering over InputText, etc.
	ImGuiMouseCursor_Move,              // Unused
	ImGuiMouseCursor_ResizeNS,          // Unused
	ImGuiMouseCursor_ResizeEW,          // When hovering over a column
	ImGuiMouseCursor_ResizeNESW,        // Unused
	ImGuiMouseCursor_ResizeNWSE,        // When hovering over the bottom-right corner of a window
	ImGuiMouseCursor_Count_
}ImGuiMouseCursor_;




typedef struct ImVec2
{
	float x;
	float y;
}ImVec2;

typedef struct ImVec4
{
	float x;
	float y;
	float z;
	float w;
}ImVec4;



//struct ImFont{}
//struct ImFontAtlas{}
//struct ImDrawList{}
//struct ImGuiStorage{}

typedef unsigned int ImU32;
typedef unsigned short ImWchar;     // character for display
typedef void* ImTextureID;          // user data to refer to a texture (e.g. store your texture handle/id)
typedef ImU32 ImGuiID;              // unique ID used by widgets (typically hashed from a stack of string)
typedef int ImGuiCol;               // enum ImGuiCol_
typedef int ImGuiStyleVar;          // enum ImGuiStyleVar_
typedef int ImGuiKey;               // enum ImGuiKey_
typedef int ImGuiAlign;             // enum ImGuiAlign_
typedef int ImGuiColorEditMode;     // enum ImGuiColorEditMode_
typedef int ImGuiMouseCursor;       // enum ImGuiMouseCursor_
typedef int ImGuiWindowFlags;       // enum ImGuiWindowFlags_
typedef int ImGuiSetCond;           // enum ImGuiSetCond_
typedef int ImGuiInputTextFlags;    // enum ImGuiInputTextFlags_
typedef int ImGuiSelectableFlags;   // enum ImGuiSelectableFlags_

typedef struct ImGuiTextEditCallbackData ImGuiTextEditCallbackData;
typedef int (*ImGuiTextEditCallback)(ImGuiTextEditCallbackData *data);



typedef struct ImFont ImFont;
typedef struct ImFontAtlas ImFontAtlas;
typedef struct ImDrawList ImDrawList;
typedef struct ImGuiStorage ImGuiStorage;



typedef unsigned short ImDrawIdx;
typedef struct ImDrawData_
{
    bool            Valid;
    ImDrawList**    CmdLists;
    int             CmdListsCount;
    int             TotalVtxCount;          // For convenience, sum of all cmd_lists vtx_buffer.Size
    int             TotalIdxCount;          // For convenience, sum of all cmd_lists idx_buffer.Size
}ImDrawData;


// backend function pointers
typedef void (*RenderDrawListFunc)(ImDrawData* data);
typedef const char* (*GetClipboardTextFunc)();
typedef void (*SetClipboardTextFunc )(const char *);
typedef void* (*MemAllocFunc )(size_t);
typedef void (*MemFreeFunc )(void*);
typedef void (*ImeSetInputScreenPosFunc )(int,int);


struct ImGuiTextEditCallbackData
{
    ImGuiInputTextFlags EventFlag;      // One of ImGuiInputTextFlags_Callback* // Read-only
    ImGuiInputTextFlags Flags;          // What user passed to InputText()      // Read-only
    void*               UserData;       // What user passed to InputText()      // Read-only

    // CharFilter event:
    ImWchar             EventChar;      // Character input                      // Read-write (replace character or set to zero)

    // Completion,History,Always events:
    ImGuiKey            EventKey;       // Key pressed (Up/Down/TAB)            // Read-only
    char*               Buf;            // Current text                         // Read-write (pointed data only)
    size_t              BufSize;        //                                      // Read-only
    bool                BufDirty;       // Set if you modify Buf directly       // Write
    int                 CursorPos;      //                                      // Read-write
    int                 SelectionStart; //                                      // Read-write (== to SelectionEnd when no selection)
    int                 SelectionEnd;   //                                      // Read-write

    // NB: calling those function loses selection.
    //void DeleteChars(int pos, int bytes_count);
    //void InsertChars(int pos, const char* text, const char* text_end = NULL);
};


typedef struct ImGuiIO_ {
	ImVec2        DisplaySize;              // <unset>              // Display size, in pixels. For clamping windows positions.
	float         DeltaTime;                // = 1.0f/60.0f         // Time elapsed since last frame, in seconds.
	float         IniSavingRate;            // = 5.0f               // Maximum time between saving positions/sizes to .ini file, in seconds.
	const char*   IniFilename;              // = "imgui.ini"        // Path to .ini file. NULL to disable .ini saving.
	const char*   LogFilename;              // = "imgui_log.txt"    // Path to .log file (default parameter to ImGui::LogToFile when no file is specified).
	float         MouseDoubleClickTime;     // = 0.30f              // Time for a double-click, in seconds.
	float         MouseDoubleClickMaxDist;  // = 6.0f               // Distance threshold to stay in to validate a double-click, in pixels.
	float         MouseDragThreshold;       // = 6.0f               // Distance threshold before considering we are dragging
	int           KeyMap[ImGuiKey_COUNT];   // <unset>              // Map of indices into the KeysDown[512] entries array
    float         KeyRepeatDelay;           // = 0.250f             // When holding a key/button, time before it starts repeating, in seconds. (for actions where 'repeat' is active)
    float         KeyRepeatRate;            // = 0.020f             // When holding a key/button, rate at which it repeats, in seconds.
	void*         UserData;                 // = NULL               // Store your own data for retrieval by callbacks.

	ImFontAtlas*  Fonts;                    // <auto>               // Load and assemble one or more fonts into a single tightly packed texture. Output to Fonts array.
	float         FontGlobalScale;          // = 1.0f               // Global scale all fonts
	bool          FontAllowUserScaling;     // = false              // Allow user scaling text of individual window with CTRL+Wheel.
    ImVec2        DisplayFramebufferScale;  // = (1.0f,1.0f)        // For retina display or other situations where window coordinates are different from framebuffer coordinates. User storage only, presently not used by ImGui.
	ImVec2        DisplayVisibleMin;        // <unset> (0.0f,0.0f)  // If you use DisplaySize as a virtual space larger than your screen, set DisplayVisibleMin/Max to the visible area.
	ImVec2        DisplayVisibleMax;        // <unset> (0.0f,0.0f)  // If the values are the same, we defaults to Min=(0.0f) and Max=DisplaySize

	// Advanced/subtle behaviors
	bool          WordMovementUsesAltKey;   // = defined(__APPLE__) // OS X style: Text editing cursor movement using Alt instead of Ctrl
	bool          ShortcutsUseSuperKey;     // = defined(__APPLE__) // OS X style: Shortcuts using Cmd/Super instead of Ctrl
	bool          DoubleClickSelectsWord;   // = defined(__APPLE__) // OS X style: Double click selects by word instead of selecting whole text
	bool          MultiSelectUsesSuperKey;  // = defined(__APPLE__) // OS X style: Multi-selection in lists uses Cmd/Super instead of Ctrl [unused yet]

	//------------------------------------------------------------------
	// User Functions
	//------------------------------------------------------------------

	// REQUIRED: rendering function.
	// See example code if you are unsure of how to implement this.
    RenderDrawListFunc RenderDrawListsFn;

	// Optional: access OS clipboard
	// (default to use native Win32 clipboard on Windows, otherwise uses a private clipboard. Override to access OS clipboard on other architectures)
    GetClipboardTextFunc GetClipboardTextFn;
    SetClipboardTextFunc SetClipboardTextFn;

	// Optional: override memory allocations. MemFreeFn() may be called with a NULL pointer.
	// (default to posix malloc/free)
	MemAllocFunc MemAllocFn;
    MemFreeFunc MemFreeFn;

	// Optional: notify OS Input Method Editor of the screen position of your cursor for text input position (e.g. when using Japanese/Chinese IME in Windows)
	// (default to use native imm32 api on Windows)
    ImeSetInputScreenPosFunc ImeSetInputScreenPosFn;
	void*       ImeWindowHandle;            // (Windows) Set this to your HWND to get automatic IME cursor positioning.

	//------------------------------------------------------------------
	// Input - Fill before calling NewFrame()
	//------------------------------------------------------------------

	ImVec2      	MousePos;                   // Mouse position, in pixels (set to -1,-1 if no mouse / on another screen, etc.)
	bool        	MouseDown[5];        		    // Mouse buttons. ImGui itself only uses button 0 (left button). Others buttons allows to track if mouse is being used by your application + available to user as a convenience via IsMouse** API.
	float       	MouseWheel;                 // Mouse wheel: 1 unit scrolls about 5 lines text.
	bool        	MouseDrawCursor;            // Request ImGui to draw a mouse cursor for you (if you are on a platform without a mouse cursor).
	bool        	KeyCtrl;                    // Keyboard modifier pressed: Control
	bool        	KeyShift;                   // Keyboard modifier pressed: Shift
	bool        	KeyAlt;                     // Keyboard modifier pressed: Alt
	bool        	KeysDown[512];              // Keyboard keys that are pressed (in whatever storage order you naturally have access to keyboard data)
	ImWchar     	InputCharacters[17];      // List of characters input (translated by user from keypress+keyboard state). Fill using AddInputCharacter() helper.

	//------------------------------------------------------------------
	// Output - Retrieve after calling NewFrame(), you can use them to discard inputs or hide them from the rest of your application
	//------------------------------------------------------------------

	bool        WantCaptureMouse;           // Mouse is hovering a window or widget is active (= ImGui will use your mouse input)
	bool        WantCaptureKeyboard;        // Widget is active (= ImGui will use your keyboard input)
    bool        WantTextInput;              // Some text input widget is active, which will read input characters from the InputCharacters array.
	float       Framerate;                  // Framerate estimation, in frame per second. Rolling average estimation based on IO.DeltaTime over 120 frames
    int         MetricsAllocs;              // Number of active memory allocations
    int         MetricsRenderVertices;      // Vertices processed during last call to Render()
    int         MetricsRenderIndices;       //
    int         MetricsActiveWindows;       // Number of visible windows (exclude child windows)

	//------------------------------------------------------------------
	// [Internal] ImGui will maintain those fields for you
	//------------------------------------------------------------------

	ImVec2      MousePosPrev;               // Previous mouse position
	ImVec2      MouseDelta;                 // Mouse delta. Note that this is zero if either current or previous position are negative to allow mouse enabling/disabling.
	bool        MouseClicked[5];            // Mouse button went from !Down to Down
	ImVec2      MouseClickedPos[5];         // Position at time of clicking
	float       MouseClickedTime[5];        // Time of last click (used to figure out double-click)
	bool        MouseDoubleClicked[5];      // Has mouse button been double-clicked?
    bool        MouseReleased[5];           // Mouse button went from Down to !Down
	bool        MouseDownOwned[5];          // Track if button was clicked inside a window. We don't request mouse capture from the application if click started outside ImGui bounds.
    float       MouseDownDuration[5];       // Duration the mouse button has been down (0.0f == just clicked)
    float       MouseDownDurationPrev[5];   // Previous time the mouse button has been down
	float       MouseDragMaxDistanceSqr[5]; // Squared maximum distance of how much mouse has traveled from the click point
    float       KeysDownDuration[512];      // Duration the keyboard key has been down (0.0f == just pressed)
    float       KeysDownDurationPrev[512];  // Previous duration the key has been down
} ImGuiIO;



typedef struct ImGuiStyle_
{
    float       Alpha;                      // Global alpha applies to everything in ImGui
    ImVec2      WindowPadding;              // Padding within a window
    ImVec2      WindowMinSize;              // Minimum window size
    float       WindowRounding;             // Radius of window corners rounding. Set to 0.0f to have rectangular windows
    ImGuiAlign  WindowTitleAlign;           // Alignment for title bar text
    float       ChildWindowRounding;        // Radius of child window corners rounding. Set to 0.0f to have rectangular windows
    ImVec2      FramePadding;               // Padding within a framed rectangle (used by most widgets)
    float       FrameRounding;              // Radius of frame corners rounding. Set to 0.0f to have rectangular frame (used by most widgets).
    ImVec2      ItemSpacing;                // Horizontal and vertical spacing between widgets/lines
    ImVec2      ItemInnerSpacing;           // Horizontal and vertical spacing between within elements of a composed widget (e.g. a slider and its label)
    ImVec2      TouchExtraPadding;          // Expand reactive bounding box for touch-based system where touch position is not accurate enough. Unfortunately we don't sort widgets so priority on overlap will always be given to the first widget. So don't grow this too much!
    float       IndentSpacing;              // Horizontal indentation when e.g. entering a tree node
    float       ColumnsMinSpacing;          // Minimum horizontal spacing between two columns
    float       ScrollbarSize;             // Width of the vertical scrollbar
    float       ScrollbarRounding;          // Radius of grab corners for scrollbar
    float       GrabMinSize;                // Minimum width/height of a grab box for slider/scrollbar
    float       GrabRounding;               // Radius of grabs corners rounding. Set to 0.0f to have rectangular slider grabs.
    ImVec2      DisplayWindowPadding;       // Window positions are clamped to be visible within the display area by at least this amount. Only covers regular windows.
    ImVec2      DisplaySafeAreaPadding;     // If you cannot see the edge of your screen (e.g. on a TV) increase the safe area padding. Covers popups/tooltips as well regular windows.
    bool        AntiAliasedLines;           // Enable anti-aliasing on lines/borders. Disable if you are really tight on CPU/GPU.
    bool        AntiAliasedShapes;          // Enable anti-aliasing on filled shapes (rounded rectangles, circles, etc.)
    float       CurveTessellationTol;       // Tessellation tolerance. Decrease for highly tessellated curves (higher quality, more polygons), increase to reduce quality.
    ImVec4      Colors[ImGuiCol_COUNT];
}ImGuiStyle;



typedef struct ImDrawVert_
{
	ImVec2  pos;
	ImVec2  uv;
	ImU32   col;
}ImDrawVert;


typedef struct ImDrawCmd ImDrawCmd;

typedef void (*ImDrawCallback )(const ImDrawList* parent_list, const ImDrawCmd* cmd);

struct ImDrawCmd
{
    uint            ElemCount;              // Number of indices (multiple of 3) to be rendered as triangles. Vertices are stored in the callee ImDrawList's vtx_buffer[] array, indices in idx_buffer[].
    ImVec4          ClipRect;               // Clipping rectangle (x1, y1, x2, y2)
    ImTextureID     TextureId;              // User-provided texture ID. Set by user in ImfontAtlas::SetTexID() for fonts or passed to Image*() functions. Ignore if never using images or multiple fonts atlas.
    ImDrawCallback  UserCallback;           // If != NULL, call the function instead of rendering the vertices. clip_rect and texture_id will be set normally.
    void*           UserCallbackData;       // The draw callback code can access this.
};



// Todo: move initialization to the python init functions
typedef struct ImFontConfig_
{
    void*           FontData;
    int             FontDataSize;
    bool            FontDataOwnedByAtlas; //=true;
    int             FontNo; //=0;
    float           SizePixels; //=0.0f;
    int             OversampleH; //=3;
    int             OversampleV; //=1;
    bool            PixelSnapH;// =false;
    ImVec2          GlyphExtraSpacing;
    const ImWchar*  GlyphRanges;
    bool            MergeMode; //=false;
    bool            MergeGlyphCenterV;// =false;

    // [Internal]
    char            Name[32];
    ImFont*         DstFont;
}ImFontConfig;


typedef struct ImColor
{
	ImVec4 value;
}ImColor;


