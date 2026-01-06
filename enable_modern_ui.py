#!/usr/bin/env python3
"""
Script to enable modern UI for the Travel website
This will backup original templates and replace them with modern versions
"""

import os
import shutil
from pathlib import Path

def enable_modern_ui():
    """Enable the modern UI by replacing templates"""
    
    # Get the project root directory
    project_root = Path(__file__).parent
    templates_dir = project_root / "templates"
    
    print("🎨 Enabling Modern UI for TravelTrip...")
    print(f"📁 Templates directory: {templates_dir}")
    
    # Create backup directory
    backup_dir = templates_dir / "backup_original"
    backup_dir.mkdir(exist_ok=True)
    
    # Template mappings: original -> modern -> backup
    template_mappings = {
        'index.html': 'modern-index.html',
        'dashboard.html': 'modern-dashboard.html', 
        'flights.html': 'modern-flights.html',
        'hotels.html': 'modern-hotels.html',
        'package.html': 'modern-package.html'
    }
    
    for original, modern in template_mappings.items():
        original_path = templates_dir / original
        modern_path = templates_dir / modern
        backup_path = backup_dir / f"original_{original}"
        
        # Backup original if it exists
        if original_path.exists():
            print(f"📋 Backing up {original} -> {backup_path.name}")
            shutil.copy2(original_path, backup_path)
        
        # Replace with modern version if it exists
        if modern_path.exists():
            print(f"✨ Replacing {original} with modern version")
            shutil.copy2(modern_path, original_path)
        else:
            print(f"⚠️  Modern template {modern} not found")
    
    print("\n🎉 Modern UI enabled successfully!")
    print("\n📋 What's new:")
    print("  ✨ Modern, clean design with professional aesthetics")
    print("  🎨 Consistent color scheme and typography")
    print("  📱 Fully responsive layout for all devices")
    print("  🚀 Smooth animations and transitions")
    print("  🎯 Improved user experience and navigation")
    print("  💳 Modern card-based layouts")
    print("  🔍 Enhanced search and booking interfaces")
    
    print(f"\n💾 Original templates backed up to: {backup_dir}")
    print("\n🌐 Visit your website to see the new modern design!")

def restore_original_ui():
    """Restore the original UI from backups"""
    
    project_root = Path(__file__).parent
    templates_dir = project_root / "templates"
    backup_dir = templates_dir / "backup_original"
    
    if not backup_dir.exists():
        print("❌ No backup directory found. Cannot restore original UI.")
        return
    
    print("🔄 Restoring original UI...")
    
    # Restore from backups
    for backup_file in backup_dir.glob("original_*.html"):
        original_name = backup_file.name.replace("original_", "")
        original_path = templates_dir / original_name
        
        print(f"📋 Restoring {original_name}")
        shutil.copy2(backup_file, original_path)
    
    print("✅ Original UI restored successfully!")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "restore":
        restore_original_ui()
    else:
        enable_modern_ui()