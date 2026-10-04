using System;
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
namespace MD3Catalog;
public sealed partial class MainWindow : Window {
    public MainWindow(){InitializeComponent();}
    private async void ShowDialog(object sender, RoutedEventArgs e){var d=new ContentDialog{Title="Confirm action",Content="Basic Dialog example",PrimaryButtonText="Confirm",CloseButtonText="Cancel",XamlRoot=Content.XamlRoot};await d.ShowAsync();}
    private async void ShowSheet(object sender, RoutedEventArgs e){var d=new ContentDialog{Title="Bottom sheet",Content="Supporting content and actions",PrimaryButtonText="Done",XamlRoot=Content.XamlRoot};await d.ShowAsync();}
}
