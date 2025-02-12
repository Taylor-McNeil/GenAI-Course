import { BookOpenText, Home, Settings, Hourglass, WholeWord, Group } from "lucide-react"
import {
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarRail
  } from "@/components/ui/sidebar"
import { url } from "inspector"
import { title } from "process"
  
  // Menu Items
  const items = [
    {
        title: "Dashboard",
        url:"/",
        icon: Home,
    },
    {
        title: "Study Activities",
        url:"/#",
        icon: BookOpenText,
    },
    {
        title: "Words",
        url:"/words",
        icon: WholeWord,
    },
    {
        title:"Word Groups",
        url:"/#",
        icon: Group

    },
    {
        title: "Sessions",
        url:"/#",
        icon: Hourglass,

    },
    {
        title: "Settings",
        url:"/#",
        icon: Settings,
    }
  ]

  export function AppSidebar() {
    return (
      <Sidebar>
        <SidebarContent>
            <SidebarGroup>
                <SidebarGroupContent>
                    <SidebarMenu>
                        {items.map((item) => (
                            <SidebarMenuItem key={item.title}>
                                <SidebarMenuButton asChild>
                                    <a href={item.url}>
                                        <item.icon />
                                        <span>{item.title}</span>
                                        </a>
                                </SidebarMenuButton>
                            </SidebarMenuItem> 
                        ))}
                    </SidebarMenu>
                </SidebarGroupContent>
            </SidebarGroup>
        </SidebarContent>
      </Sidebar>
      
)
  }
  