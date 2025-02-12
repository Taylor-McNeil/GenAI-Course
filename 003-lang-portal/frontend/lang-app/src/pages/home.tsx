import WordList from "../components/WordList"; // Import the WordList component
import { SidebarProvider,SidebarInset, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
import { Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator } from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
const Home = () => {
  return (
    <div>
    <SidebarInset>
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
      <SidebarTrigger className="-ml-1" />
      <Separator orientation="vertical" className="mr-2 h-4" />
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem className="hidden md:block">
            <BreadcrumbLink href="#">
              Home
            </BreadcrumbLink>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
      
    </header>
    <div>
    <p className="px-4">
    r breadcrumb is likely not expanding because its parent container (in this case, the header within the SidebarInset) is using a flex layout that only sizes itself to fit its content. By default, the Breadcrumb (and its inner BreadcrumbList) don’t have a full-width style, so they’re constrained


    </p>
</div>
    </SidebarInset>


  </div>
  );
};

export default Home;