"""
SYSTEM INFORMATION SCRIPT - Mac System Details
===============================================
Get your Mac's OS, Processor, RAM, Storage, and other system information
"""

import platform
import os
import sys
import subprocess
from datetime import datetime

# Try to import psutil (external module for detailed system info)
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    print("Note: psutil not installed. Install it for detailed RAM/Storage info:")
    print("      pip install psutil\n")


def format_bytes(bytes_size):
    """Convert bytes to human-readable format (GB, MB, etc.)"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"


def get_os_info():
    """Get Operating System Information"""
    print("=" * 60)
    print("OPERATING SYSTEM INFORMATION")
    print("=" * 60)
    
    print(f"System:          {platform.system()}")
    print(f"Release:         {platform.release()}")
    print(f"Version:         {platform.version()}")
    print(f"Platform:        {platform.platform()}")
    print(f"Architecture:    {platform.architecture()[0]}")
    
    # Mac-specific info
    if platform.system() == 'Darwin':
        try:
            # Get macOS version
            result = subprocess.run(['sw_vers'], capture_output=True, text=True)
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    if 'ProductName:' in line:
                        print(f"macOS Name:      {line.split(':', 1)[1].strip()}")
                    elif 'ProductVersion:' in line:
                        print(f"macOS Version:   {line.split(':', 1)[1].strip()}")
                    elif 'BuildVersion:' in line:
                        print(f"macOS Build:     {line.split(':', 1)[1].strip()}")
        except:
            pass
    
    print()


def get_processor_info():
    """Get Processor/CPU Information"""
    print("=" * 60)
    print("PROCESSOR INFORMATION")
    print("=" * 60)
    
    print(f"Processor:       {platform.processor()}")
    print(f"Machine Type:    {platform.machine()}")
    
    # Get detailed CPU info on Mac
    if platform.system() == 'Darwin':
        try:
            # Get CPU brand/model
            result = subprocess.run(['sysctl', '-n', 'machdep.cpu.brand_string'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"CPU Model:       {result.stdout.strip()}")
            
            # Get number of CPU cores
            result = subprocess.run(['sysctl', '-n', 'hw.ncpu'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                cores = result.stdout.strip()
                print(f"CPU Cores:       {cores}")
            
            # Get physical CPU cores
            result = subprocess.run(['sysctl', '-n', 'hw.physicalcpu'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Physical Cores:  {result.stdout.strip()}")
            
            # Get logical CPU cores
            result = subprocess.run(['sysctl', '-n', 'hw.logicalcpu'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Logical Cores:   {result.stdout.strip()}")
                
        except:
            pass
    
    # CPU usage if psutil available
    if PSUTIL_AVAILABLE:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        print(f"CPU Usage:       {cpu_percent}%")
        print(f"CPU Count:       {cpu_count} cores")
    
    print()


def get_ram_info():
    """Get RAM/Memory Information"""
    print("=" * 60)
    print("RAM/MEMORY INFORMATION")
    print("=" * 60)
    
    if PSUTIL_AVAILABLE:
        memory = psutil.virtual_memory()
        print(f"Total RAM:       {format_bytes(memory.total)}")
        print(f"Available RAM:   {format_bytes(memory.available)}")
        print(f"Used RAM:        {format_bytes(memory.used)}")
        print(f"Free RAM:        {format_bytes(memory.free)}")
        print(f"RAM Usage:       {memory.percent}%")
    else:
        # Try to get RAM info using system commands
        if platform.system() == 'Darwin':
            try:
                result = subprocess.run(['sysctl', '-n', 'hw.memsize'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    total_ram = int(result.stdout.strip())
                    print(f"Total RAM:       {format_bytes(total_ram)}")
                    print("(Install psutil for detailed RAM usage: pip install psutil)")
            except:
                print("RAM info not available (install psutil for details)")
    
    print()


def get_storage_info():
    """Get Storage/Disk Information"""
    print("=" * 60)
    print("STORAGE INFORMATION")
    print("=" * 60)
    
    if PSUTIL_AVAILABLE:
        # Get disk usage for root partition
        disk = psutil.disk_usage('/')
        print(f"Total Storage:   {format_bytes(disk.total)}")
        print(f"Used Storage:    {format_bytes(disk.used)}")
        print(f"Free Storage:    {format_bytes(disk.free)}")
        print(f"Storage Usage:   {disk.percent}%")
        print()
        
        # Get all disk partitions
        print("Disk Partitions:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                print(f"  {partition.device}")
                print(f"    Mountpoint:   {partition.mountpoint}")
                print(f"    File System:  {partition.fstype}")
                print(f"    Total:        {format_bytes(usage.total)}")
                print(f"    Used:         {format_bytes(usage.used)} ({usage.percent}%)")
                print(f"    Free:         {format_bytes(usage.free)}")
                print()
            except PermissionError:
                pass
    else:
        # Try to get disk info using system commands
        if platform.system() == 'Darwin':
            try:
                result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    if len(lines) > 1:
                        parts = lines[1].split()
                        if len(parts) >= 4:
                            print(f"Total Storage:   {parts[1]}")
                            print(f"Used Storage:    {parts[2]}")
                            print(f"Free Storage:    {parts[3]}")
                            print("(Install psutil for detailed storage info: pip install psutil)")
            except:
                print("Storage info not available (install psutil for details)")
    
    print()


def get_python_info():
    """Get Python Information"""
    print("=" * 60)
    print("PYTHON INFORMATION")
    print("=" * 60)
    
    print(f"Python Version:  {sys.version.split()[0]}")
    print(f"Python Build:    {platform.python_build()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Python Location: {sys.executable}")
    print(f"Platform:        {platform.python_implementation()}")
    print()


def get_user_info():
    """Get User Information"""
    print("=" * 60)
    print("USER INFORMATION")
    print("=" * 60)
    
    print(f"Username:        {os.getenv('USER', 'N/A')}")
    print(f"Home Directory:  {os.path.expanduser('~')}")
    print(f"Current Directory: {os.getcwd()}")
    
    if platform.system() == 'Darwin':
        try:
            result = subprocess.run(['whoami'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"System User:     {result.stdout.strip()}")
        except:
            pass
    
    print()


def get_network_info():
    """Get Network Information"""
    print("=" * 60)
    print("NETWORK INFORMATION")
    print("=" * 60)
    
    if PSUTIL_AVAILABLE:
        # Get network interfaces
        interfaces = psutil.net_if_addrs()
        print("Network Interfaces:")
        for interface_name, interface_addresses in interfaces.items():
            print(f"  {interface_name}:")
            for addr in interface_addresses:
                if addr.family == 2:  # IPv4
                    print(f"    IPv4:        {addr.address}")
                    if addr.netmask:
                        print(f"    Netmask:     {addr.netmask}")
                elif addr.family == 10:  # IPv6
                    print(f"    IPv6:        {addr.address}")
            print()
    else:
        print("(Install psutil for network info: pip install psutil)")
    
    print()


def get_general_info():
    """Get General System Information"""
    print("=" * 60)
    print("GENERAL INFORMATION")
    print("=" * 60)
    
    print(f"Hostname:        {platform.node()}")
    print(f"System Time:     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if platform.system() == 'Darwin':
        try:
            # Get Mac model
            result = subprocess.run(['sysctl', '-n', 'hw.model'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Mac Model:       {result.stdout.strip()}")
        except:
            pass
    
    print()


def main():
    """Main function to display all system information"""
    print("\n" + "=" * 60)
    print("SYSTEM INFORMATION REPORT")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Display all information
    get_os_info()
    get_processor_info()
    get_ram_info()
    get_storage_info()
    get_python_info()
    get_user_info()
    get_network_info()
    get_general_info()
    
    print("=" * 60)
    print("END OF REPORT")
    print("=" * 60)


if __name__ == "__main__":
    main()