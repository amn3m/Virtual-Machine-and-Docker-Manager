import os
import tkinter as tk
from tkinter import filedialog, messagebox

MAIN_BG_COLOR = "#7091E6"
MAIN_BTN_COLOR = "#ADBBDA"
SUB_BG_COLOR = "#233855"
SUB_BTN_COLOR = "#0FA4AF"

def create_vm(cpu, memory, disk_size, iso_path):
    try:
        disk_image = "disk_image.qcow2"
        os.system(f"qemu-img create -f qcow2 {disk_image} {disk_size}")
        qemu_command = f"qemu-system-x86_64 -cpu {cpu} -m {memory} -hda {disk_image} -cdrom {iso_path} -boot d -no-fd-bootchk"
        os.system(qemu_command)
        messagebox.showinfo("Success", "Virtual machine created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create virtual machine: {e}")

def create_vm_from_gui(cpu_var, memory_var, disk_var, iso_entry):
    cpu = cpu_var.get()
    memory = memory_var.get()
    disk_size = disk_var.get()
    iso_path = iso_entry.get()
    if not (cpu and memory and disk_size and iso_path):
        messagebox.showerror("Input Error", "All fields are required")
        return
    create_vm(cpu, memory, disk_size, iso_path)

def browse_iso(iso_entry):
    filename = filedialog.askopenfilename(title="Select ISO File", filetypes=[("ISO files", "*.iso")])
    if filename:
        iso_entry.delete(0, tk.END)
        iso_entry.insert(0, filename)

def create_dockerfile(path, contents):
    try:
        with open(path, 'w') as file:
            file.write(contents)
        messagebox.showinfo("Success", f"Dockerfile created at {path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create Dockerfile: {e}")

def create_dockerfile_from_gui(path_entry, contents_text):
    path = path_entry.get()
    contents = contents_text.get("1.0", tk.END)
    if not (path and contents.strip()):
        messagebox.showerror("Input Error", "Both fields are required")
        return
    create_dockerfile(path, contents)

def browse_save_path(path_entry):
    filename = filedialog.asksaveasfilename(title="Save Dockerfile As", defaultextension=".Dockerfile", filetypes=[("Dockerfile", "*.Dockerfile")])
    if filename:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, filename)

def build_docker_image(dockerfile_path, image_name):
    try:
        result = os.popen(f"docker build -t {image_name} -f {dockerfile_path} .").read()
        messagebox.showinfo("Success", f"Docker image {image_name} built successfully!\n\n{result}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to build Docker image: {e}")

def build_docker_image_from_gui(dockerfile_entry, image_entry):
    dockerfile_path = dockerfile_entry.get()
    image_name = image_entry.get()
    if not (dockerfile_path and image_name):
        messagebox.showerror("Input Error", "Both fields are required")
        return
    build_docker_image(dockerfile_path, image_name)

def browse_dockerfile(dockerfile_entry):
    filename = filedialog.askopenfilename(title="Select Dockerfile", filetypes=[("Dockerfile", "*.Dockerfile"), ("All Files", "*.*")])
    if filename:
        dockerfile_entry.delete(0, tk.END)
        dockerfile_entry.insert(0, filename)

def list_docker_images():
    try:
        result = os.popen("docker images").read()
        return result
    except Exception as e:
        return f"Error: {e}\nThis error may indicate that the Docker daemon is not running."

def list_running_containers():
    try:
        result = os.popen("docker ps").read()
        return result
    except Exception as e:
        return f"Error: {e}\nThis error may indicate that the Docker daemon is not running."

def stop_container(container_id):
    try:
        result = os.popen(f"docker stop {container_id}").read()
        if result:
            messagebox.showinfo("Success", f"Container {container_id} stopped successfully!\n\n{result}")
        else:
            messagebox.showinfo("Success", f"Container {container_id} stopped successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to stop container: {e}")

def stop_container_from_gui(container_id_entry):
    container_id = container_id_entry.get()
    if not container_id:
        messagebox.showerror("Input Error", "Container ID/Name is required")
        return
    stop_container(container_id)

def search_image(image_name):
    try:
        result = os.popen(f"docker images --filter=reference={image_name}").read()
        return result
    except Exception as e:
        return f"Error: {e}\nThis error may indicate that the Docker daemon is not running."

def search_image_dockerhub(image_name):
    try:
        result = os.popen(f"docker search {image_name}").read()
        return result
    except Exception as e:
        return f"Error: {e}\nThis error may indicate that the Docker daemon is not running."

def pull_image(image_name):
    try:
        result = os.popen(f"docker pull {image_name}").read()
        return result
    except Exception as e:
        return f"Error: {e}\nThis error may indicate that the Docker daemon is not running."

def search_image_from_gui(image_name_entry, result_text):
    image_name = image_name_entry.get()
    if not image_name:
        messagebox.showerror("Input Error", "Image name/tag is required")
        return
    result = search_image(image_name)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

def search_image_dockerhub_from_gui(image_name_entry, result_text):
    image_name = image_name_entry.get()
    if not image_name:
        messagebox.showerror("Input Error", "Image name/tag is required")
        return
    result = search_image_dockerhub(image_name)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

def pull_image_from_gui(image_name_entry):
    image_name = image_name_entry.get()
    if not image_name:
        messagebox.showerror("Input Error", "Image name/tag is required")
        return
    result = pull_image(image_name)
    messagebox.showinfo("Result", result)

def open_create_vm_window():
    create_vm_window = tk.Toplevel(root)
    create_vm_window.title("Create Virtual Machine")
    create_vm_window.geometry("960x540")
    create_vm_window.resizable(False, False)
    create_vm_window.configure(bg=SUB_BG_COLOR)
    cpu_options = ["qemu64", "kvm64", "host"]
    memory_options = ["512", "1024", "2048", "4096", "8192"]
    disk_options = ["10G", "20G", "50G", "100G"]
    tk.Label(create_vm_window, text="CPU:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    cpu_var = tk.StringVar(create_vm_window)
    cpu_var.set(cpu_options[0])
    cpu_menu = tk.OptionMenu(create_vm_window, cpu_var, *cpu_options)
    cpu_menu.grid(row=0, column=1, padx=10, pady=5)
    cpu_menu.configure(bg=SUB_BTN_COLOR)
    tk.Label(create_vm_window, text="Memory (MB):", bg=SUB_BG_COLOR, fg="white").grid(row=1, column=0, padx=10, pady=5)
    memory_var = tk.StringVar(create_vm_window)
    memory_var.set(memory_options[0])
    memory_menu = tk.OptionMenu(create_vm_window, memory_var, *memory_options)
    memory_menu.grid(row=1, column=1, padx=10, pady=5)
    memory_menu.configure(bg=SUB_BTN_COLOR)
    tk.Label(create_vm_window, text="Disk Size (e.g., 10G):", bg=SUB_BG_COLOR, fg="white").grid(row=2, column=0, padx=10, pady=5)
    disk_var = tk.StringVar(create_vm_window)
    disk_var.set(disk_options[0])
    disk_menu = tk.OptionMenu(create_vm_window, disk_var, *disk_options)
    disk_menu.grid(row=2, column=1, padx=10, pady=5)
    disk_menu.configure(bg=SUB_BTN_COLOR)
    tk.Label(create_vm_window, text="ISO Path:", bg=SUB_BG_COLOR, fg="white").grid(row=3, column=0, padx=10, pady=5)
    iso_entry = tk.Entry(create_vm_window)
    iso_entry.grid(row=3, column=1, padx=10, pady=5)
    browse_button = tk.Button(create_vm_window, text="Browse", bg=SUB_BTN_COLOR, command=lambda: browse_iso(iso_entry))
    browse_button.grid(row=3, column=2, padx=10, pady=5)
    create_button = tk.Button(create_vm_window, text="Create VM", bg=SUB_BTN_COLOR, command=lambda: create_vm_from_gui(cpu_var, memory_var, disk_var, iso_entry))
    create_button.grid(row=4, column=0, columnspan=3, pady=10)

def open_create_dockerfile_window():
    create_dockerfile_window = tk.Toplevel(root)
    create_dockerfile_window.title("Create Dockerfile")
    create_dockerfile_window.geometry("960x540")
    create_dockerfile_window.resizable(False, False)
    create_dockerfile_window.configure(bg=SUB_BG_COLOR)
    tk.Label(create_dockerfile_window, text="Save Path:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    path_entry = tk.Entry(create_dockerfile_window)
    path_entry.grid(row=0, column=1, padx=10, pady=5)
    browse_button = tk.Button(create_dockerfile_window, text="Browse", bg=SUB_BTN_COLOR, command=lambda: browse_save_path(path_entry))
    browse_button.grid(row=0, column=2, padx=10, pady=5)
    tk.Label(create_dockerfile_window, text="Dockerfile Contents:", bg=SUB_BG_COLOR, fg="white").grid(row=1, column=0, padx=10, pady=5)
    contents_text = tk.Text(create_dockerfile_window, height=10, width=40)
    contents_text.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
    create_button = tk.Button(create_dockerfile_window, text="Create Dockerfile", bg=SUB_BTN_COLOR, command=lambda: create_dockerfile_from_gui(path_entry, contents_text))
    create_button.grid(row=3, column=0, columnspan=3, pady=10)

def open_build_docker_image_window():
    build_docker_image_window = tk.Toplevel(root)
    build_docker_image_window.title("Build Docker Image")
    build_docker_image_window.geometry("960x540")
    build_docker_image_window.resizable(False, False)
    build_docker_image_window.configure(bg=SUB_BG_COLOR)
    tk.Label(build_docker_image_window, text="Dockerfile Path:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    dockerfile_entry = tk.Entry(build_docker_image_window)
    dockerfile_entry.grid(row=0, column=1, padx=10, pady=5)
    browse_button = tk.Button(build_docker_image_window, text="Browse", bg=SUB_BTN_COLOR, command=lambda: browse_dockerfile(dockerfile_entry))
    browse_button.grid(row=0, column=2, padx=10, pady=5)
    tk.Label(build_docker_image_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=1, column=0, padx=10, pady=5)
    image_entry = tk.Entry(build_docker_image_window)
    image_entry.grid(row=1, column=1, padx=10, pady=5)
    build_button = tk.Button(build_docker_image_window, text="Build Docker Image", bg=SUB_BTN_COLOR, command=lambda: build_docker_image_from_gui(dockerfile_entry, image_entry))
    build_button.grid(row=2, column=0, columnspan=3, pady=10)

def open_list_docker_images_window():
    list_docker_images_window = tk.Toplevel(root)
    list_docker_images_window.title("List Docker Images")
    list_docker_images_window.geometry("960x540")
    list_docker_images_window.resizable(False, False)
    list_docker_images_window.configure(bg=SUB_BG_COLOR)
    images_text = tk.Text(list_docker_images_window, wrap=tk.WORD)
    images_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    images = list_docker_images()
    images_text.insert(tk.END, images)

def open_list_running_containers_window():
    list_running_containers_window = tk.Toplevel(root)
    list_running_containers_window.title("List Running Containers")
    list_running_containers_window.geometry("960x540")
    list_running_containers_window.resizable(False, False)
    list_running_containers_window.configure(bg=SUB_BG_COLOR)
    containers_text = tk.Text(list_running_containers_window, wrap=tk.WORD)
    containers_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    containers = list_running_containers()
    containers_text.insert(tk.END, containers)

def open_stop_container_window():
    stop_container_window = tk.Toplevel(root)
    stop_container_window.title("Stop Docker Container")
    stop_container_window.geometry("960x540")
    stop_container_window.resizable(False, False)
    stop_container_window.configure(bg=SUB_BG_COLOR)
    tk.Label(stop_container_window, text="Container ID/Name:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    container_id_entry = tk.Entry(stop_container_window)
    container_id_entry.grid(row=0, column=1, padx=10, pady=5)
    stop_button = tk.Button(stop_container_window, text="Stop Container", bg=SUB_BTN_COLOR, command=lambda: stop_container_from_gui(container_id_entry))
    stop_button.grid(row=1, column=0, columnspan=2, pady=10)

def open_search_image_window():
    search_image_window = tk.Toplevel(root)
    search_image_window.title("Search Docker Image")
    search_image_window.geometry("960x540")
    search_image_window.resizable(False, False)
    search_image_window.configure(bg=SUB_BG_COLOR)
    tk.Label(search_image_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    image_name_entry = tk.Entry(search_image_window)
    image_name_entry.grid(row=0, column=1, padx=10, pady=5)
    result_text = tk.Text(search_image_window, wrap=tk.WORD)
    result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    search_button = tk.Button(search_image_window, text="Search Image", bg=SUB_BTN_COLOR, command=lambda: search_image_from_gui(image_name_entry, result_text))
    search_button.grid(row=2, column=0, columnspan=2, pady=10)

def open_search_image_dockerhub_window():
    search_image_dockerhub_window = tk.Toplevel(root)
    search_image_dockerhub_window.title("Search DockerHub Image")
    search_image_dockerhub_window.geometry("960x540")
    search_image_dockerhub_window.resizable(False, False)
    search_image_dockerhub_window.configure(bg=SUB_BG_COLOR)
    tk.Label(search_image_dockerhub_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    image_name_entry = tk.Entry(search_image_dockerhub_window)
    image_name_entry.grid(row=0, column=1, padx=10, pady=5)
    result_text = tk.Text(search_image_dockerhub_window, wrap=tk.WORD)
    result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    search_button = tk.Button(search_image_dockerhub_window, text="Search DockerHub", bg=SUB_BTN_COLOR, command=lambda: search_image_dockerhub_from_gui(image_name_entry, result_text))
    search_button.grid(row=2, column=0, columnspan=2, pady=10)

def open_pull_image_window():
    pull_image_window = tk.Toplevel(root)
    pull_image_window.title("Pull Docker Image")
    pull_image_window.geometry("960x540")
    pull_image_window.resizable(False, False)
    pull_image_window.configure(bg=SUB_BG_COLOR)
    tk.Label(pull_image_window, text="Image Name/Tag:", bg=SUB_BG_COLOR, fg="white").grid(row=0, column=0, padx=10, pady=5)
    image_name_entry = tk.Entry(pull_image_window)
    image_name_entry.grid(row=0, column=1, padx=10, pady=5)
    pull_button = tk.Button(pull_image_window, text="Pull Image", bg=SUB_BTN_COLOR, command=lambda: pull_image_from_gui(image_name_entry))
    pull_button.grid(row=1, column=0, columnspan=2, pady=10)

root = tk.Tk()
root.title("QEMU VM Manager")
root.geometry("1440x810")
root.resizable(False, False)
root.configure(bg=MAIN_BG_COLOR)

main_button_vm = tk.Button(root, text="Create Virtual Machine", bg=MAIN_BTN_COLOR, command=open_create_vm_window)
main_button_vm.pack(padx=20, pady=10)

main_button_dockerfile = tk.Button(root, text="Create Dockerfile", bg=MAIN_BTN_COLOR, command=open_create_dockerfile_window)
main_button_dockerfile.pack(padx=20, pady=10)

"""
FROM python:3.9-slim
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
"""

"myapp:v1.0"

main_button_build_image = tk.Button(root, text="Build Docker Image", bg=MAIN_BTN_COLOR, command=open_build_docker_image_window)
main_button_build_image.pack(padx=20, pady=10)

main_button_list_images = tk.Button(root, text="List Docker Images", bg=MAIN_BTN_COLOR, command=open_list_docker_images_window)
main_button_list_images.pack(padx=20, pady=10)

main_button_list_running_containers = tk.Button(root, text="List Running Containers", bg=MAIN_BTN_COLOR, command=open_list_running_containers_window)
main_button_list_running_containers.pack(padx=20, pady=10)

main_button_stop_container = tk.Button(root, text="Stop Docker Container", bg=MAIN_BTN_COLOR, command=open_stop_container_window)
main_button_stop_container.pack(padx=20, pady=10)

main_button_search_image = tk.Button(root, text="Search Docker Image", bg=MAIN_BTN_COLOR, command=open_search_image_window)
main_button_search_image.pack(padx=20, pady=10)

main_button_search_image_dockerhub = tk.Button(root, text="Search DockerHub Image", bg=MAIN_BTN_COLOR, command=open_search_image_dockerhub_window)
main_button_search_image_dockerhub.pack(padx=20, pady=10)

main_button_pull_image = tk.Button(root, text="Pull Docker Image", bg=MAIN_BTN_COLOR, command=open_pull_image_window)
main_button_pull_image.pack(padx=20, pady=10)

root.mainloop()
