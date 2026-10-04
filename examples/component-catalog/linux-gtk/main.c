#include <gtk/gtk.h>

static gboolean quit_app(gpointer data) {
  g_application_quit(G_APPLICATION(data));
  return G_SOURCE_REMOVE;
}
#include <string.h>

typedef struct { GtkWidget *window; gboolean smoke; } AppState;
static GtkWidget* row(void){ GtkWidget *b=gtk_box_new(GTK_ORIENTATION_HORIZONTAL,10); gtk_widget_set_hexpand(b,TRUE); return b; }
static GtkWidget* section(GtkWidget *parent,const char *id,const char *title){
  GtkWidget *frame=gtk_frame_new(NULL),*box=gtk_box_new(GTK_ORIENTATION_VERTICAL,10),*head=gtk_box_new(GTK_ORIENTATION_HORIZONTAL,8);
  GtkWidget *t=gtk_label_new(title),*code=gtk_label_new(id);
  gtk_widget_add_css_class(t,"title-3"); gtk_widget_set_halign(t,GTK_ALIGN_START); gtk_widget_set_halign(code,GTK_ALIGN_END); gtk_widget_set_hexpand(t,TRUE);
  gtk_box_append(GTK_BOX(head),t); gtk_box_append(GTK_BOX(head),code); gtk_box_append(GTK_BOX(box),head); gtk_frame_set_child(GTK_FRAME(frame),box); gtk_box_append(GTK_BOX(parent),frame); return box;
}
static void add_button(GtkWidget *r,const char *s){gtk_box_append(GTK_BOX(r),gtk_button_new_with_label(s));}
static void activate(GtkApplication *app,gpointer data){
  gboolean smoke=GPOINTER_TO_INT(data); GtkWidget *win=gtk_application_window_new(app); gtk_window_set_title(GTK_WINDOW(win),"MD3 Component Catalog"); gtk_window_set_default_size(GTK_WINDOW(win),980,820);
  GtkWidget *scroll=gtk_scrolled_window_new(),*root=gtk_box_new(GTK_ORIENTATION_VERTICAL,14); gtk_widget_set_margin_start(root,24);gtk_widget_set_margin_end(root,24);gtk_widget_set_margin_top(root,24);gtk_widget_set_margin_bottom(root,24);
  gtk_scrolled_window_set_child(GTK_SCROLLED_WINDOW(scroll),root); gtk_window_set_child(GTK_WINDOW(win),scroll);
  GtkWidget *s,*r,*w;
  s=section(root,"component-buttons","Buttons"); r=row();add_button(r,"Filled");add_button(r,"Tonal");add_button(r,"Outlined");add_button(r,"Text");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-floating-action-button","Floating action button");r=row();add_button(r,"+");add_button(r,"＋ New");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-icon-buttons","Icon buttons");r=row();add_button(r,"☆");add_button(r,"★");add_button(r,"⋯");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-segmented-buttons","Segmented buttons");r=row();w=gtk_toggle_button_new_with_label("List");gtk_toggle_button_set_active(GTK_TOGGLE_BUTTON(w),TRUE);gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(r),gtk_toggle_button_new_with_label("Grid"));gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-badges","Badges");r=row();w=gtk_label_new("12");gtk_widget_add_css_class(w,"badge");gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-progress-indicators","Progress indicators");r=row();w=gtk_progress_bar_new();gtk_progress_bar_set_fraction(GTK_PROGRESS_BAR(w),.62);gtk_widget_set_size_request(w,220,-1);gtk_box_append(GTK_BOX(r),w);w=gtk_spinner_new();gtk_spinner_start(GTK_SPINNER(w));gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-snackbars","Snackbar");r=row();w=gtk_label_new("Settings saved   Undo");gtk_widget_add_css_class(w,"snackbar");gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-tooltips","Tooltips");r=row();w=gtk_button_new_with_label("Help");gtk_widget_set_tooltip_text(w,"Help information");gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-bottom-sheets","Bottom sheet");r=row();add_button(r,"Open sheet");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-cards","Cards");r=row();add_button(r,"Filled card");add_button(r,"Outlined card");add_button(r,"Elevated card");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-carousel","Carousel");r=row();for(int i=1;i<=4;i++){char x[8];g_snprintf(x,sizeof x,"%02d",i);add_button(r,x);}gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-dialogs","Dialogs");r=row();add_button(r,"Open dialog");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-divider","Divider");gtk_box_append(GTK_BOX(s),gtk_separator_new(GTK_ORIENTATION_HORIZONTAL));
  s=section(root,"component-lists","List");w=gtk_list_box_new();gtk_list_box_append(GTK_LIST_BOX(w),gtk_label_new("Single-line list"));gtk_list_box_append(GTK_LIST_BOX(w),gtk_label_new("Two-line list · Supporting text"));gtk_box_append(GTK_BOX(s),w);
  s=section(root,"component-side-sheets","Side sheet");gtk_box_append(GTK_BOX(s),gtk_label_new("Side sheet · Supporting information"));
  s=section(root,"component-bottom-app-bar","Bottom app bar");r=row();add_button(r,"Menu");add_button(r,"Search");add_button(r,"+");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-top-app-bar","Top app bar");r=row();add_button(r,"←");gtk_box_append(GTK_BOX(r),gtk_label_new("Page title"));add_button(r,"⋯");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-navigation-bar","Navigation bar");r=row();add_button(r,"Home");add_button(r,"Saved");add_button(r,"Settings");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-navigation-drawer","Navigation drawer");r=row();add_button(r,"Inbox");add_button(r,"Drafts");add_button(r,"Archive");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-navigation-rail","Navigation rail");r=row();add_button(r,"Home");add_button(r,"Saved");add_button(r,"Settings");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-search","Search");w=gtk_search_entry_new();gtk_entry_set_placeholder_text(GTK_ENTRY(w),"Search");gtk_box_append(GTK_BOX(s),w);
  s=section(root,"component-tabs","Tabs");r=row();add_button(r,"Overview");add_button(r,"Activity");add_button(r,"Settings");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-checkbox","Checkbox");r=row();gtk_box_append(GTK_BOX(r),gtk_check_button_new_with_label("Not selected"));w=gtk_check_button_new_with_label("Selected");gtk_check_button_set_active(GTK_CHECK_BUTTON(w),TRUE);gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-chips","Chips");r=row();add_button(r,"Assist");add_button(r,"Filter");add_button(r,"Input ×");add_button(r,"Suggestion");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-date-pickers","Date picker");r=row();gtk_box_append(GTK_BOX(r),gtk_entry_new());add_button(r,"Choose date");gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-menus","Menu");r=row();w=gtk_menu_button_new();gtk_menu_button_set_label(GTK_MENU_BUTTON(w),"Menu");gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-radio-button","Radio button");r=row();GtkWidget *a=gtk_check_button_new_with_label("System"),*b=gtk_check_button_new_with_label("Light"),*c=gtk_check_button_new_with_label("Dark");gtk_check_button_set_group(GTK_CHECK_BUTTON(b),GTK_CHECK_BUTTON(a));gtk_check_button_set_group(GTK_CHECK_BUTTON(c),GTK_CHECK_BUTTON(a));gtk_check_button_set_active(GTK_CHECK_BUTTON(a),TRUE);gtk_box_append(GTK_BOX(r),a);gtk_box_append(GTK_BOX(r),b);gtk_box_append(GTK_BOX(r),c);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-sliders","Slider");r=row();w=gtk_scale_new_with_range(GTK_ORIENTATION_HORIZONTAL,0,100,1);gtk_range_set_value(GTK_RANGE(w),42);gtk_widget_set_size_request(w,240,-1);gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-switch","Switch");r=row();w=gtk_switch_new();gtk_switch_set_active(GTK_SWITCH(w),TRUE);gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(r),gtk_label_new("Notifications"));gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-time-pickers","Time picker");r=row();w=gtk_entry_new();gtk_editable_set_text(GTK_EDITABLE(w),"09:30");gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  s=section(root,"component-text-fields","Text fields");r=row();w=gtk_entry_new();gtk_entry_set_placeholder_text(GTK_ENTRY(w),"Filled");gtk_box_append(GTK_BOX(r),w);w=gtk_entry_new();gtk_entry_set_placeholder_text(GTK_ENTRY(w),"Outlined");gtk_box_append(GTK_BOX(r),w);gtk_box_append(GTK_BOX(s),r);
  GtkCssProvider *css=gtk_css_provider_new();gtk_css_provider_load_from_data(css,"frame{padding:18px;border-radius:20px;background:#f3edf7;} .badge{background:#b3261e;color:white;padding:3px 8px;border-radius:12px;} .snackbar{background:#322f35;color:white;padding:12px;border-radius:4px;}",-1);gtk_style_context_add_provider_for_display(gdk_display_get_default(),GTK_STYLE_PROVIDER(css),GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);g_object_unref(css);
  gtk_window_present(GTK_WINDOW(win)); if(smoke) g_timeout_add(700, quit_app, app);
}
int main(int argc,char **argv){gboolean smoke=argc>1 && strcmp(argv[1],"--smoke")==0;GtkApplication *app=gtk_application_new("org.example.md3gtk",G_APPLICATION_DEFAULT_FLAGS);g_signal_connect(app,"activate",G_CALLBACK(activate),GINT_TO_POINTER(smoke));int status=g_application_run(G_APPLICATION(app),smoke?1:argc,smoke?argv:argv);g_object_unref(app);return status;}
