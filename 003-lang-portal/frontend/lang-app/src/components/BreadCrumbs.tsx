import { useLocation, Link } from "react-router-dom";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";
import { Separator } from "@/components/ui/separator";
import { SidebarTrigger } from "@/components/ui/sidebar";

// Define route mappings for better names
const routeMappings: { [key: string]: string } = {
  "": "Home",
  "dashboard": "Dashboard",
  "study-activities": "Study Activities",
  "words": "Words",
  "groups": "Word Groups",
  "sessions": "Study Sessions",
  "settings": "Settings",
  "launch": "Launch",
};

export default function Breadcrumbs() {
  const location = useLocation();
  const pathnames = location.pathname.split("/").filter((x) => x);

  // If at root, show "Home"
  if (pathnames.length === 0) {
    pathnames.push("");
  }

  const breadcrumbItems = pathnames
    .map((name, index) => {
      let displayName = routeMappings[name] || name; // Default to mapped name or raw path

      const isLast = index === pathnames.length - 1;
      const fullPath = `/${pathnames.slice(0, index + 1).join("/")}`;

      const items = [];

      items.push(
        <BreadcrumbItem key={`item-${name || "home"}`}>
          {isLast ? (
            <BreadcrumbPage>{displayName}</BreadcrumbPage>
          ) : (
            <BreadcrumbLink asChild>
              <Link to={fullPath}>{displayName}</Link>
            </BreadcrumbLink>
          )}
        </BreadcrumbItem>
      );

      if (!isLast) {
        items.push(<BreadcrumbSeparator key={`separator-${name || "home"}`} />);
      }

      return items;
    })
    .flat();

  return (
    <header className="flex h-16 items-center gap-2 border-b px-4">
       <SidebarTrigger />
      <Separator orientation="vertical" className="mr-2 h-4" />
      <Breadcrumb>
        <BreadcrumbList>{breadcrumbItems}</BreadcrumbList>
      </Breadcrumb>
    </header>
  );
}
