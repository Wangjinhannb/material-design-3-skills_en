using Microsoft.UI.Xaml;
namespace MD3Catalog;
public partial class App : Application { public App(){InitializeComponent();} protected override void OnLaunched(LaunchActivatedEventArgs args){var w=new MainWindow();w.Activate();} }
